#!/usr/bin/env python3
"""Merge the second-pass survey files into data/benchmarks.json.

Reads the *.entries.json files in research_notes/simulation-benchmarks-for-vla-evaluation/
and (re)creates every catalog entry that came from them. Entries from the first
survey are left untouched. Safe to re-run: second-pass entries are replaced, and
image fields are refilled by select_images.py.

Usage: merge_survey.py [source ...]   e.g. merge_survey.py new_sim_suites diagnostic_sim_benchmarks
With no arguments every *.entries.json source is merged.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.json"
NOTES = ROOT / "research_notes" / "simulation-benchmarks-for-vla-evaluation"

# Display-name fixes for names that carry a long parenthetical.
RENAME = {
    "DOM (Dynamic Object Manipulation benchmark, DynamicVLA)": "DOM (DynamicVLA)",
    "Isaac Lab-Arena (Lightwheel RoboCasa and LIBERO task suites)": "Isaac Lab-Arena task suites",
    "PerAct2 bimanual benchmark (RLBench2)": "PerAct2 / RLBench2",
    "GenManip (GenManip-Bench)": "GenManip-Bench",
    "LBM Eval (lbm_eval)": "LBM Eval",
    "HumanoidGen (HGen-Bench)": "HumanoidGen",
    "BEHAVIOR Challenge (2025, 2026)": "BEHAVIOR Challenge",
    "RoboTwin (1.0)": "RoboTwin 1.0",
    "RoboDojo (simulation suite)": "RoboDojo simulation suite",
}
# Names that duplicate an entry already merged under another name.
SAME_AS = {"ALOHA sim (Transfer Cube, Bimanual Insertion)": "aloha-simulation-tasks"}
# Diagnostic benchmarks are filed under the axis named by their first tag.
AXIS = {
    "Dynamic": "Dynamic scenes",
    "Robustness": "Robustness",
    "Generalization": "Generalization",
    "Memory": "Memory and long horizon",
    "Long-horizon": "Memory and long horizon",
    "Language": "Language and reasoning",
    "Reasoning": "Language and reasoning",
    "Safety": "Safety",
}
PHYSICAL_SUB = "VLA-era benchmarks"
# Released tools for scoring or resetting real-robot trials; filed with the physical group.
TOOLING = {"Eval-Actions", "RoboReward", "FailBench", "PRM-as-a-Judge 1.5"}
REAL_SUBS = {"hosted": "Platforms", "competition": "Competitions"}
PROXY_SUBS = {"World model": "Video world models", "Gaussian splatting": "Reconstruction-based"}


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def sentence(text):
    """Tidy a survey field: drop process boilerplate, capitalize, no trailing period on fragments."""
    text = re.sub(r"Details taken from an automated extraction of the arXiv HTML opened in this session\.\s*", "", text)
    text = re.sub(r"\s+in this session", "", text)
    text = re.sub(r"[;,]? included because the brief names it", "", text)
    text = text.replace(", which belongs to the newer slice", " (see BEHAVIOR Challenge)")
    text = text.replace("pi0.5", "π0.5").replace("pi0-FAST", "π0-FAST").replace("pi0", "π0")
    text = re.sub(r"Paper opened \([^)]*\)[.;]\s*", "", text)
    text = text.strip()
    return text[:1].upper() + text[1:] if text[:1].isascii() else text


def fragment(text):
    return sentence(text).rstrip(".")


def load(name):
    path = NOTES / f"{name}.entries.json"
    wanted = not sys.argv[1:] or name in sys.argv[1:]
    return json.loads(path.read_text()) if wanted and path.exists() else []


def main():
    existing = json.loads(DATA.read_text())
    first_pass = [e for e in existing if not e.get("pass2")]
    taken_ids = {e["id"] for e in first_pass}
    taken_names = {e["name"].lower() for e in first_pass}
    out = []

    def add(raw, group, sub, focus=None):
        name = RENAME.get(raw["name"], raw["name"])
        if name.lower() in taken_names or name in SAME_AS:
            return
        ident = slug(name.split("(")[0]) or slug(name)
        if ident in taken_ids:
            ident = slug(name) if slug(name) not in taken_ids else slug(name) + "-" + group
        taken_ids.add(ident)
        taken_names.add(name.lower())
        out.append(dict(
            id=ident, name=name, group=group, sub=sub, year=raw["year"], venue=raw["venue"],
            evaluates=fragment(raw["evaluates"]), improves=fragment(raw.get("improves", "")),
            setup=sentence(raw.get("setup", "")), scale=fragment(raw.get("scale", "")),
            agreement=fragment(raw.get("agreement", "")),
            real_check=sentence(raw.get("real_validation", "")),
            policies=fragment(raw.get("vla_results", "")),
            status=fragment(raw.get("status", "")),
            note=sentence(raw.get("note", "")),
            tags=raw["tags"], links=raw["links"], image="", image_source="", pass2=True,
            **({"focus": [focus]} if focus else {}),
        ))

    def real_sub(raw):
        group = raw["group"]
        if raw["name"] in TOOLING:
            return "Evaluation tooling"
        if group == "physical":
            return PHYSICAL_SUB if "Generalist / VLA" in raw["tags"] else "Domain and task-specific benchmarks"
        if group == "proxy":
            return next((PROXY_SUBS[t] for t in raw["tags"] if t in PROXY_SUBS), "Simulator twins")
        return REAL_SUBS[group]

    for raw in load("established_sim_benchmarks"):
        add(raw, "simulation", "Established benchmarks")
    for raw in load("new_sim_suites"):
        add(raw, "simulation", "Broad suites")
    for raw in load("diagnostic_sim_benchmarks"):
        add(raw, "simulation", AXIS.get(raw["tags"][0], "Generalization"))
    for source, focus, sim_sub in (("focus_dexterity", "dexterity", "Precision and dexterity"),
                                   ("focus_dynamism", "dynamism", "Dynamic scenes")):
        for raw in load(source):
            sim = raw["group"] == "simulation"
            add(raw, raw["group"], sim_sub if sim else real_sub(raw), focus)
    for raw in load("real_world_gap_check"):
        add(raw, raw["group"], real_sub(raw))

    DATA.write_text(json.dumps(first_pass + out, ensure_ascii=False, indent=2) + "\n")
    counts = {}
    for e in out:
        counts[(e["group"], e["sub"])] = counts.get((e["group"], e["sub"]), 0) + 1
    print(f"{len(first_pass)} first-pass + {len(out)} second-pass entries")
    for key, n in sorted(counts.items()):
        print(f"  {key[0]:12s} {key[1]:26s} {n}")


if __name__ == "__main__":
    main()
