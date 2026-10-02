#!/usr/bin/env python3
"""Find a representative image for each benchmark in data/benchmarks.json.

For every entry the script collects candidate images from, in order:
  1. the og:image / twitter:image of its project pages,
  2. the first figures of its arXiv HTML page,
  3. teaser-like <img> tags and video posters on its project pages,
  4. images in its GitHub README,
  5. (fallback) raster images embedded in the first pages of its arXiv PDF.
Accepted candidates are saved as WebP under .cache/image_candidates/<id>/ with a
meta.json listing where each one came from. select_images.py then copies the
chosen candidate into docs/images/ and records it in the data file.

Usage: python3 scripts/fetch_images.py [--only id1,id2] [--force]
"""
import argparse
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path

from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.json"
CACHE = ROOT / ".cache" / "image_candidates"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
MAX_KEEP = 5          # accepted candidates kept per entry
MAX_TRIES = 28        # image downloads attempted per entry
MAX_SIDE = 960

SKIP_WORDS = ("logo", "icon", "favicon", "badge", "shields.io", "avatar", "sprite", "spinner",
              "smileybones", "arxiv-logo", "funders", "social/", "orcid", "license", "qrcode",
              "github-mark", "twitter", "youtube", "play_button", "placeholder", "your_banner")
BOOST_WORDS = ("teaser", "overview", "pipeline", "setup", "hero", "cover", "banner", "main",
               "fig1", "figure1", "fig_1", "intro", "task", "bench", "system", "framework", "splash")
NO_OG_HOSTS = ("github.com", "arxiv.org", "semanticscholar.org", "core.ac.uk", "zenodo.org",
               "openaccess.thecvf.com", "openreview.net", "link.springer.com", "tandfonline.com",
               "frontiersin.org", "nist.gov", "huggingface.co")


def get(url, timeout=25, limit=12_000_000):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.geturl(), r.read(limit), r.headers.get("Content-Type", "")


def get_text(url):
    final, body, ctype = get(url, limit=4_000_000)
    if "html" not in ctype and "text" not in ctype and "json" not in ctype:
        return final, ""
    return final, body.decode("utf-8", "ignore")


def arxiv_id(url):
    m = re.search(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})", url)
    return m.group(1) if m else None


def attr(tag, name):
    m = re.search(r'\b%s\s*=\s*"([^"]*)"' % name, tag, re.I) or re.search(r"\b%s\s*=\s*'([^']*)'" % name, tag, re.I)
    return unescape(m.group(1)).strip() if m else None


def page_candidates(url):
    """Return (og_images, body_images) found on a web page."""
    try:
        final, html = get_text(url)
    except Exception:
        return [], []
    if not html:
        return [], []
    base = final
    b = re.search(r"<base[^>]+>", html, re.I)
    if b and attr(b.group(0), "href"):
        base = urllib.parse.urljoin(final, attr(b.group(0), "href"))
    og = []
    if not any(h in urllib.parse.urlparse(final).netloc for h in NO_OG_HOSTS):
        for tag in re.findall(r"<meta[^>]+>", html, re.I):
            key = (attr(tag, "property") or attr(tag, "name") or "").lower()
            if key in ("og:image", "og:image:url", "og:image:secure_url", "twitter:image", "twitter:image:src"):
                c = attr(tag, "content")
                if c:
                    og.append(urllib.parse.urljoin(base, c))
    body = []
    for tag in re.findall(r"<(?:img|video|source)[^>]+>", html, re.I):
        src = None
        if tag.lower().startswith("<img"):
            src = attr(tag, "src") or attr(tag, "data-src")
            if not src and attr(tag, "srcset"):
                src = attr(tag, "srcset").split(",")[0].split()[0]
        elif tag.lower().startswith("<video"):
            src = attr(tag, "poster")
        if src and not src.startswith("data:"):
            body.append(urllib.parse.urljoin(base, src))
    seen, uniq = set(), []
    for u in body:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    boosted = [u for u in uniq if any(w in u.lower() for w in BOOST_WORDS)]
    rest = [u for u in uniq if u not in boosted]
    return og, boosted + rest[:14]


def arxiv_html_candidates(aid):
    try:
        final, html = get_text("https://arxiv.org/html/" + aid)
    except Exception:
        return []
    if "/html/" not in final:
        return []
    out = []
    for tag in re.findall(r"<img[^>]+>", html, re.I):
        if "ltx_graphics" not in tag:
            continue
        src = attr(tag, "src")
        if src and not src.startswith("data:"):
            out.append(urllib.parse.urljoin(final, src))
    return out[:6]


def github_candidates(url):
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        return []
    owner, repo = m.group(1), m.group(2)
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/"
    md = ""
    for name in ("README.md", "readme.md", "README.rst"):
        try:
            _, md = get_text(raw_base + name)
            if md:
                break
        except Exception:
            continue
    out = []
    for u in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", md) + re.findall(r'<img[^>]+src="([^"]+)"', md, re.I):
        u = u.strip()
        if u.startswith("http"):
            u = re.sub(r"https://github\.com/([^/]+)/([^/]+)/blob/", r"https://raw.githubusercontent.com/\1/\2/", u)
        else:
            u = urllib.parse.urljoin(raw_base, u.lstrip("./"))
        out.append(u)
    return out[:10]


def load_image(raw):
    im = Image.open(io.BytesIO(raw))
    im.seek(0)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    return im


def acceptable(im):
    w, h = im.size
    if w < 360 or h < 180:
        return False
    if not 0.45 <= w / h <= 4.2:
        return False
    stat = ImageStat.Stat(im.convert("L").resize((64, 64)))
    return stat.stddev[0] >= 10


def save(im, path):
    im = im.copy()
    im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    im.save(path, "WEBP", quality=82, method=6)


def pdf_candidates(aid):
    """Largest raster images embedded in the first pages of the arXiv PDF, else a render of page 1."""
    try:
        import fitz
        _, raw, _ = get("https://arxiv.org/pdf/" + aid, limit=40_000_000)
        doc = fitz.open(stream=raw, filetype="pdf")
    except Exception:
        return []
    ims = []
    for page in list(doc)[:4]:
        for info in page.get_images(full=True):
            try:
                pix = fitz.Pixmap(doc, info[0])
                if pix.n - pix.alpha >= 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                ims.append(load_image(pix.tobytes("png")))
            except Exception:
                continue
    ims = [im for im in ims if acceptable(im)]
    ims.sort(key=lambda im: -im.size[0] * im.size[1])
    if not ims:
        try:
            pix = doc[0].get_pixmap(dpi=110)
            ims = [load_image(pix.tobytes("png"))]
        except Exception:
            pass
    return ims[:3]


def process(entry, force=False):
    out_dir = CACHE / entry["id"]
    meta_path = out_dir / "meta.json"
    if meta_path.exists() and not force:
        return entry["id"], len(json.loads(meta_path.read_text()))
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.webp"):
        old.unlink()

    urls = [l["url"] for l in entry["links"]]
    aids = [a for a in (arxiv_id(u) for u in urls) if a]
    pages = [u for u in urls if not arxiv_id(u) and not u.lower().endswith(".pdf")]

    queue = []  # (image_url, source_page)
    body_later = []
    for p in pages:
        if "github.com" in p:
            body_later += [(u, p) for u in github_candidates(p)]
            continue
        og, body = page_candidates(p)
        queue += [(u, p) for u in og]
        body_later += [(u, p) for u in body]
    for a in aids:
        queue += [(u, "https://arxiv.org/abs/" + a) for u in arxiv_html_candidates(a)]
    queue += body_later

    kept, tried, seen = [], 0, set()
    for img_url, src in queue:
        if len(kept) >= MAX_KEEP or tried >= MAX_TRIES:
            break
        low = img_url.lower()
        if img_url in seen or low.split("?")[0].endswith(".svg") or any(w in low for w in SKIP_WORDS):
            continue
        seen.add(img_url)
        tried += 1
        try:
            _, raw, _ = get(img_url)
            im = load_image(raw)
        except Exception:
            continue
        if not acceptable(im):
            continue
        save(im, out_dir / f"{len(kept)}.webp")
        kept.append(dict(image_url=img_url, source=src, size=list(im.size)))

    if not kept:
        for a in aids:
            for im in pdf_candidates(a):
                save(im, out_dir / f"{len(kept)}.webp")
                kept.append(dict(image_url="https://arxiv.org/pdf/" + a, source="https://arxiv.org/abs/" + a, size=list(im.size)))
            if kept:
                break
    meta_path.write_text(json.dumps(kept, indent=2))
    return entry["id"], len(kept)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    entries = json.loads(DATA.read_text())
    if args.only:
        want = set(args.only.split(","))
        entries = [e for e in entries if e["id"] in want]
    with ThreadPoolExecutor(8) as pool:
        results = list(pool.map(lambda e: process(e, args.force), entries))
    empty = [i for i, n in results if n == 0]
    print(f"{len(results) - len(empty)}/{len(results)} entries have candidates")
    if empty:
        print("no image:", ", ".join(empty))


if __name__ == "__main__":
    sys.exit(main())
