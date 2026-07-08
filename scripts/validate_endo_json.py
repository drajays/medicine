#!/usr/bin/env python3
"""Validate Endocrinology Master JSON modules (Harrison-compatible schema)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "endo" / "data"


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"JSON parse error: {e}"]

    items = data.get("items", [])
    if not items:
        errors.append("no items")

    ids: set[str] = set()
    notes = why_how = 0
    legacy_why = legacy_how = 0

    for it in items:
        iid = it.get("id", "?")
        if iid in ids:
            errors.append(f"duplicate id: {iid}")
        ids.add(iid)

        ref = it.get("reference", "")
        if not ref or '"' not in ref:
            errors.append(f"{iid}: missing verbatim reference quote")

        t = it.get("type")
        if t == "note":
            notes += 1
            if it.get("title", "").startswith(("Why", "How")):
                why_how += 1
        elif t == "why":
            legacy_why += 1
            errors.append(f"{iid}: legacy type 'why' — convert to note with Why title")
        elif t == "how":
            legacy_how += 1
            errors.append(f"{iid}: legacy type 'how' — convert to note with How title")
        elif t == "mcq":
            opts = it.get("options", [])
            mod_id = str(data.get("id", ""))
            allow_five = (
                mod_id.startswith("e15-")
                or mod_id.startswith("e24-")
                or path.name.startswith("endo2015_")
                or path.name.startswith("endo2024_")
            )
            if allow_five:
                if len(opts) not in (4, 5):
                    errors.append(f"{iid}: mcq needs 4 or 5 options, has {len(opts)}")
                co = it.get("correctOption")
                if co not in (0, 1, 2, 3, 4):
                    errors.append(f"{iid}: mcq correctOption must be 0-4")
            else:
                if len(opts) != 4:
                    errors.append(f"{iid}: mcq needs 4 options, has {len(opts)}")
                co = it.get("correctOption")
                if co not in (0, 1, 2, 3):
                    errors.append(f"{iid}: mcq correctOption must be 0-3")
            if not (it.get("question") or it.get("stem")):
                errors.append(f"{iid}: mcq missing question/stem")
        elif t == "true_false":
            if not isinstance(it.get("correctAnswer"), bool):
                errors.append(f"{iid}: true_false needs boolean correctAnswer")
        elif t == "assertion_reason":
            co = it.get("correctOption")
            if co not in (0, 1, 2, 3, 4):
                errors.append(f"{iid}: ar correctOption must be 0-4")
        else:
            errors.append(f"{iid}: unknown type {t}")

    if notes and why_how / notes < 0.5:
        errors.append(f"Why/How notes {why_how}/{notes} ({100*why_how/notes:.0f}%) — need ≥50%")

    if legacy_why or legacy_how:
        pass  # already flagged

    return errors


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else sorted(DATA.glob("*.json"))
    paths = [p for p in paths if p.name != "index.json"]

    failed = 0
    for path in paths:
        errs = validate_file(path)
        if errs:
            failed += 1
            print(f"FAIL {path.name}:")
            for e in errs:
                print(f"  - {e}")
        else:
            data = json.loads(path.read_text())
            items = data["items"]
            counts: dict[str, int] = {}
            notes = [i for i in items if i["type"] == "note"]
            wh = sum(1 for n in notes if n.get("title", "").startswith(("Why", "How")))
            for i in items:
                counts[i["type"]] = counts.get(i["type"], 0) + 1
            print(f"PASS {path.name}: {len(items)} items {counts} Why/How {wh}/{len(notes)}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
