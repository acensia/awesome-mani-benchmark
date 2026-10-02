#!/usr/bin/env python3
"""Copy the chosen candidate image for each benchmark into docs/images/ and record it in the data file.

Choices live in data/image_picks.json (see its _comment). Run after fetch_images.py.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.json"
PICKS = ROOT / "data" / "image_picks.json"
CACHE = ROOT / ".cache" / "image_candidates"
OUT = ROOT / "docs" / "images"


def main():
    entries = json.loads(DATA.read_text())
    picks = json.loads(PICKS.read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    used = 0
    for e in entries:
        pick = picks.get(e["id"], 0)
        src_id, idx = e["id"], pick
        if isinstance(pick, dict):
            src_id, idx = pick["from"], pick["index"]
        meta_path = CACHE / src_id / "meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else []
        target = OUT / f"{e['id']}.webp"
        if idx is None or idx >= len(meta):
            e["image"], e["image_source"] = "", ""
            target.unlink(missing_ok=True)
            continue
        shutil.copyfile(CACHE / src_id / f"{idx}.webp", target)
        e["image"] = f"images/{e['id']}.webp"
        e["image_source"] = meta[idx]["source"] or meta[idx]["image_url"]
        used += 1
    DATA.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    missing = [e["id"] for e in entries if not e["image"]]
    print(f"{used}/{len(entries)} entries have an image")
    if missing:
        print("no image:", ", ".join(missing))


if __name__ == "__main__":
    main()
