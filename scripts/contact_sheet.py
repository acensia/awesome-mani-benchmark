#!/usr/bin/env python3
"""Draw contact sheets of candidate images so a person can choose among them.

  contact_sheet.py first [--pass2]     first candidate of every entry (30 per sheet)
  contact_sheet.py alts id1,id2,... NAME   every candidate of the given entries

Sheets are written to .cache/sheets/. Record choices in data/image_picks.json.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "image_candidates"
OUT = ROOT / ".cache" / "sheets"
W, H, LAB = 300, 190, 22


def sheet(items, cols, out):
    rows = (len(items) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * W, rows * (H + LAB)), (40, 40, 40))
    draw = ImageDraw.Draw(canvas)
    for i, (label, path) in enumerate(items):
        x, y = (i % cols) * W, (i // cols) * (H + LAB)
        if path.exists():
            im = Image.open(path).convert("RGB")
            im.thumbnail((W - 6, H - 6))
            bg = Image.new("RGB", (W - 6, H - 6), (255, 255, 255))
            bg.paste(im, ((W - 6 - im.width) // 2, (H - 6 - im.height) // 2))
            canvas.paste(bg, (x + 3, y + 3))
        draw.text((x + 5, y + H + 4), label[:44], fill=(255, 255, 120))
    canvas.save(out, quality=80)


def count(ident):
    meta = CACHE / ident / "meta.json"
    return len(json.loads(meta.read_text())) if meta.exists() else 0


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "data" / "benchmarks.json").read_text())
    if sys.argv[1] == "first":
        if "--pass2" in sys.argv:
            data = [e for e in data if e.get("pass2")]
        items = [(f"{e['id']} [{count(e['id'])}]", CACHE / e["id"] / "0.webp") for e in data]
        for k in range(0, len(items), 30):
            sheet(items[k:k + 30], 5, OUT / f"first_{k // 30}.jpg")
        print("sheets:", (len(items) + 29) // 30)
    else:
        items = [(f"{i} #{k}", CACHE / i / f"{k}.webp") for i in sys.argv[2].split(",") for k in range(count(i))]
        sheet(items, 5, OUT / f"alts_{sys.argv[3]}.jpg")
        print(len(items), "candidates")


if __name__ == "__main__":
    main()
