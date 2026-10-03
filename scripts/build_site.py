#!/usr/bin/env python3
"""Build the catalog page from data/benchmarks.json and scripts/site_template.html.

Korean text for each entry comes from data/benchmarks.ko.json, keyed by id.
Writes docs/index.html (a standalone page; images are read from docs/images/).
With --fragment PATH it also writes the same page without the document skeleton,
which is the form the Claude artifact publisher expects.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.json"
DATA_KO = ROOT / "data" / "benchmarks.ko.json"
FOCUS = ROOT / "data" / "focus.json"
ANNOTATIONS = ROOT / "data" / "annotations.json"
TEMPLATE = ROOT / "scripts" / "site_template.html"
OUT = ROOT / "docs" / "index.html"

SKELETON_HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>img{max-width:100%}[hidden]{display:none!important}</style>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment", help="also write a skeleton-free copy to this path")
    args = ap.parse_args()

    entries = json.loads(DATA.read_text())
    korean = json.loads(DATA_KO.read_text()) if DATA_KO.exists() else {}
    focus = json.loads(FOCUS.read_text()) if FOCUS.exists() else {}
    notes = json.loads(ANNOTATIONS.read_text()) if ANNOTATIONS.exists() else {}
    for e in entries:
        e.pop("pass2", None)
        lenses = [k for k in ("dexterity", "dynamism") if e["id"] in focus.get(k, []) or k in e.get("focus", [])]
        e.pop("focus", None)
        if lenses:
            e["focus"] = lenses
        for key in [k for k, v in e.items() if v == ""]:
            if key not in ("improves", "agreement", "image", "image_source"):
                del e[key]
        if e["id"] in korean:
            e["ko"] = dict(korean[e["id"]])
        for field in ("policies", "timing"):
            extra = notes.get(field, {}).get(e["id"])
            if extra:
                ko = e.setdefault("ko", {})
                e[field] = "; ".join(x for x in (e.get(field), extra["en"]) if x)
                ko[field] = ". ".join(x for x in (ko.get(field), extra["ko"]) if x)
    payload = json.dumps(entries, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = TEMPLATE.read_text().replace("/*__DATA__*/[]", payload)
    head, body = page.split("<!--BODY-->", 1)

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(SKELETON_HEAD + head + "</head>\n<body>" + body + "</body>\n</html>\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(entries)} entries)")
    if args.fragment:
        Path(args.fragment).write_text(head + body)
        print(f"wrote {args.fragment}")


if __name__ == "__main__":
    main()
