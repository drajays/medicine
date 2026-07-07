#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-16 and e21-21 through e21-27 (Pituitary/NET batch)."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_16_21 import build_chapter_16, build_chapter_21  # noqa: E402
from build_endo_esap_22_24 import build_chapter_22, build_chapter_23, build_chapter_24  # noqa: E402
from build_endo_esap_25_27 import build_chapter_25, build_chapter_26, build_chapter_27  # noqa: E402

PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")

MODULES = {
    "endo2021_chapter_16_Modern_Manager_Patient_With_Pac.json": build_chapter_16,
    "endo2021_chapter_21_Pseudoacromegaly_Syndromes.json": build_chapter_21,
    "endo2021_chapter_22_Prevention_and_Management_of_Carcinoid_Crisis.json": build_chapter_22,
    "endo2021_chapter_23_Management_complications.json": build_chapter_23,
    "endo2021_chapter_24_Risks_Adverse_Effects_Surveillance_and_Intervention.json": build_chapter_24,
    "endo2021_chapter_25_Treatment_of_Functioning_Gonadotroph_Pituitary_Adenomas.json": build_chapter_25,
    "endo2021_chapter_26_Management_of_Pituitary_Hormone_Replacement_Through_Transition_From_Adolescence_to_Young_Adulthood.json": build_chapter_26,
    "endo2021_chapter_27_When_to_Worry_and_What_to_Do.json": build_chapter_27,
}


def write_module(filename: str, data: dict) -> tuple[Path, Path]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    MASTER_DATA.mkdir(parents=True, exist_ok=True)
    master_path = MASTER_DATA / filename
    shutil.copy2(portal_path, master_path)
    return portal_path, master_path


def main() -> None:
    for filename, builder in MODULES.items():
        data = builder()
        portal_path, master_path = write_module(filename, data)
        counts: dict[str, int] = {}
        for item in data["items"]:
            counts[item["type"]] = counts.get(item["type"], 0) + 1
        notes = counts.get("note", 0)
        wh = sum(
            1
            for i in data["items"]
            if i["type"] == "note" and i.get("title", "").startswith(("Why", "How"))
        )
        pct = 100 * wh // notes if notes else 0
        print(
            f"Wrote {portal_path.name} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes} = {pct}%)"
        )
        print(f"  Copied to {master_path}")


if __name__ == "__main__":
    main()
