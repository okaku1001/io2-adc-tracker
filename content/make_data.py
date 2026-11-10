#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from e_ivo1 import ENTRIES as A
from e_ivo2 import ENTRIES as B
from e_ivo3 import ENTRIES as C
from e_cado import ENTRIES as D
from e_partner import ENTRIES as E
from e_comp import ENTRIES as F
from daily import all_days

DATA = ROOT.parent / "data"


def grades_in(entry):
    found = []
    for ev in entry.get("timeline", []):
        for g in ev.get("grades", []):
            if g not in found:
                found.append(g)
        for s in ev.get("sources", []):
            g = s.get("grade")
            if g and g not in found:
                found.append(g)
    return found


def main():
    entries = A + B + C + D + E + F
    slugs = [e["slug"] for e in entries]
    if len(slugs) != len(set(slugs)):
        raise SystemExit("duplicate slugs")
    for e in entries:
        e["grades_present"] = grades_in(e)
        e.setdefault("aliases", [])

    DATA.mkdir(parents=True, exist_ok=True)
    daily_dir = DATA / "daily"
    daily_dir.mkdir(exist_ok=True)
    for old in daily_dir.glob("*.json"):
        old.unlink()

    (DATA / "entries.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    days = all_days()
    missing = []
    for day in days:
        for it in day.get("items", []):
            slug = it.get("entry")
            if slug and slug not in slugs:
                missing.append((day["date"], slug))
        (daily_dir / f"{day['date']}.json").write_text(
            json.dumps(day, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if missing:
        raise SystemExit(f"daily items point to unknown entries: {missing}")
    print(f"wrote {len(entries)} entries, {len(days)} daily files")


if __name__ == "__main__":
    main()
