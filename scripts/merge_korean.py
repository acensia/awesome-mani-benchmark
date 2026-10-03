#!/usr/bin/env python3
"""Fold translated batches (.cache/ko/out_*.json) into data/benchmarks.ko.json.

Each batch is {id: {field: korean text}}. Fragment fields lose a trailing period,
sentence fields gain one, and a few recurring phrases are made consistent.
Usage: merge_korean.py 4 5   (batch numbers; default: every out_*.json)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KO = ROOT / "data" / "benchmarks.ko.json"
DATA = ROOT / "data" / "benchmarks.json"
BATCHES = ROOT / ".cache" / "ko"
FRAGMENTS = ("evaluates", "improves", "scale", "policies", "status", "agreement")
SENTENCES = ("setup", "real_check", "note")
PHRASES = (
    ("method 전이이며", "방법을 실로봇으로 옮겨 본 것이며"),
    ("method 전이뿐이며", "방법을 실로봇으로 옮겨 본 것뿐이며"),
    ("방법의 전이를 본 것이며", "방법을 실로봇으로 옮겨 본 것이며"),
    ("code, 데이터셋", "코드, 데이터셋"),
)


def tidy(field, text):
    text = text.strip()
    for old, new in PHRASES:
        text = text.replace(old, new)
    text = re.sub(r"상관은 없다\.", "상관은 보고되지 않았다.", text)
    text = re.sub(r"(\d) h\b", r"\1시간", text)
    if field in FRAGMENTS:
        text = text.rstrip(".")
    elif field in SENTENCES and text and text[-1] not in ".)":
        text += "."
    return text


def main():
    korean = json.loads(KO.read_text())
    paths = [BATCHES / f"out_{n}.json" for n in sys.argv[1:]] or sorted(BATCHES.glob("out_*.json"))
    for path in paths:
        for ident, fields in json.loads(path.read_text()).items():
            korean[ident] = {f: tidy(f, v) for f, v in fields.items()}
    entries = json.loads(DATA.read_text())
    ordered = {e["id"]: korean[e["id"]] for e in entries if e["id"] in korean}
    KO.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n")
    missing = [e["id"] for e in entries if e["id"] not in korean]
    print(f"{len(ordered)} of {len(entries)} entries have Korean text")
    if missing:
        print("missing:", ", ".join(missing))


if __name__ == "__main__":
    main()
