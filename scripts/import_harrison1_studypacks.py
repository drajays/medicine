#!/usr/bin/env python3
"""Import Harrison1 studypack JSON files into data/ as h1-NNN chapters.

Skips folders that already have a matching data/h1-NNN_*.json file.
Transforms studypack ids (h22-NNN) to catalog ids (h1-NNN).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDYPACK_ROOT = ROOT / "noupload/harrison/Harrison1_studypacks"
DATA_DIR = ROOT / "data"
INDEX_PATH = ROOT / "data/index.json"


def replace_ids(obj, old_prefix: str, new_prefix: str):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("id", "_generatedFrom") and isinstance(v, str):
                obj[k] = v.replace(old_prefix, new_prefix)
            else:
                replace_ids(v, old_prefix, new_prefix)
    elif isinstance(obj, list):
        for item in obj:
            replace_ids(item, old_prefix, new_prefix)
    elif isinstance(obj, str):
        pass


def chapter_section_map(index: dict) -> dict[str, tuple[dict, str]]:
    out: dict[str, tuple[dict, str]] = {}
    for sec in index.get("sections", []):
        sec_name = sec.get("name", "")
        for ch in sec.get("chapters", []):
            cid = ch.get("id", "")
            if cid.startswith("h1-"):
                out[cid] = (ch, sec_name)
    return out


def main() -> int:
    index = json.loads(INDEX_PATH.read_text())
    ch_map = chapter_section_map(index)

    imported: list[str] = []
    skipped_existing: list[str] = []
    skipped_no_index: list[str] = []
    skipped_no_json: list[str] = []

    for folder in sorted(STUDYPACK_ROOT.iterdir()):
        if not folder.is_dir():
            continue
        m = re.match(r"^(\d{3})_", folder.name)
        if not m:
            continue
        n = int(m.group(1))
        ch_id = f"h1-{n:03d}"
        old_prefix = f"h22-{n:03d}"

        if list(DATA_DIR.glob(f"h1-{n:03d}_*.json")):
            skipped_existing.append(ch_id)
            continue

        json_files = sorted(folder.glob("h22-*.json"))
        if not json_files:
            skipped_no_json.append(folder.name)
            continue

        if ch_id not in ch_map:
            skipped_no_index.append(ch_id)
            continue

        ch_entry, section_name = ch_map[ch_id]
        src_path = json_files[0]
        data = json.loads(src_path.read_text())

        replace_ids(data, old_prefix, ch_id)
        data["id"] = ch_id
        data["volume"] = data.get("volume") or 1
        if section_name:
            data["section"] = section_name
        data["sourceFile"] = f"noupload/harrison/Harrison1_studypacks/{folder.name}/{src_path.name}"

        out_name = src_path.name.replace("h22-", "h1-")
        out_path = DATA_DIR / out_name
        out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

        ch_entry["file"] = out_name
        ch_entry["status"] = "ready"
        if data.get("chapterNo") and not ch_entry.get("no"):
            ch_entry["no"] = str(data["chapterNo"])
        if data.get("title"):
            ch_entry["title"] = data["title"]
        if data.get("authors"):
            ch_entry.setdefault("authors", data["authors"])

        imported.append(ch_id)

    INDEX_PATH.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")

    print(f"Imported: {len(imported)}")
    print(f"Skipped (already in data/): {len(skipped_existing)}")
    print(f"Skipped (no index entry): {len(skipped_no_index)}")
    print(f"Skipped (no studypack json): {len(skipped_no_json)}")
    if skipped_no_index:
        print("No index entry:", ", ".join(skipped_no_index))
    if skipped_no_json:
        print("No json:", ", ".join(skipped_no_json[:10]), "..." if len(skipped_no_json) > 10 else "")
    if imported:
        print("First:", imported[0], "| Last:", imported[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
