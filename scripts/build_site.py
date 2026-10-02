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
    for e in entries:
        if e["id"] in korean:
            e["ko"] = korean[e["id"]]
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
