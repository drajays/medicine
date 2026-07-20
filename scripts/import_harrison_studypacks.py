#!/usr/bin/env python3
"""Import Harrison1/Harrison2 studypack JSON into data/ under h1-/h2- chapters.

- Skips section-header folders (no index entry).
- Skips chapters whose content already matches the studypack (same fingerprints).
- For chapters with no data file yet: write the studypack (ids remapped).
- For chapters that already exist with different content: append only
  studypack items whose content is not already present (new unique ids).
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INDEX_PATH = ROOT / "data/index.json"

VOLUMES = [
    {
        "vol": 1,
        "prefix": "h1",
        "studypack_root": ROOT / "noupload/harrison/Harrison1_studypacks",
        "source_label": "Harrison1_studypacks",
    },
    {
        "vol": 2,
        "prefix": "h2",
        "studypack_root": ROOT / "noupload/harrison/Harrison2_studypacks",
        "source_label": "Harrison2_studypacks",
    },
]


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


def content_fp(it: dict) -> tuple:
    t = it.get("type")
    if t == "note":
        return ("note", (it.get("title") or "").strip(), (it.get("content") or "").strip()[:200])
    if t == "mcq":
        return ("mcq", (it.get("question") or "").strip()[:200])
    if t == "true_false":
        return ("tf", (it.get("statement") or "").strip()[:200])
    if t == "assertion_reason":
        return (
            "ar",
            (it.get("assertion") or "").strip()[:150],
            (it.get("reason") or "").strip()[:150],
        )
    return (t, it.get("id"))


def chapter_section_map(index: dict, prefix: str) -> dict[str, tuple[dict, str]]:
    out: dict[str, tuple[dict, str]] = {}
    for sec in index.get("sections", []):
        sec_name = sec.get("name", "")
        for ch in sec.get("chapters", []):
            cid = ch.get("id", "")
            if cid.startswith(f"{prefix}-"):
                out[cid] = (ch, sec_name)
    return out


def remap_item_id(item: dict, ch_id: str, used: set[str], tag: str = "sp") -> None:
    """Give item a unique id under ch_id, preferring {ch_id}-{tag}-{suffix}."""
    old = item.get("id", "")
    # h22-063-n12 → n12; also handle already-remapped h1-063-n12
    m = re.search(r"-(?:sp-)?([a-z]+\d+(?:-[a-z0-9]+)*)$", old)
    suffix = m.group(1) if m else re.sub(r"[^a-z0-9]+", "", old)[-12:] or "x"
    base = f"{ch_id}-{tag}-{suffix}"
    new_id = base
    n = 2
    while new_id in used:
        new_id = f"{base}-{n}"
        n += 1
    item["id"] = new_id
    used.add(new_id)
    if isinstance(item.get("_generatedFrom"), str):
        item["_generatedFrom"] = item["_generatedFrom"].replace(old, new_id)


def prepare_studypack(
    data: dict,
    *,
    ch_id: str,
    old_prefix: str,
    vol: int,
    section_name: str,
    source_rel: str,
) -> dict:
    data = copy.deepcopy(data)
    replace_ids(data, old_prefix, ch_id)
    data["id"] = ch_id
    data["volume"] = data.get("volume") or vol
    if section_name:
        data["section"] = section_name
    data["sourceFile"] = source_rel
    return data


def update_index_entry(ch_entry: dict, data: dict, out_name: str) -> None:
    ch_entry["file"] = out_name
    ch_entry["status"] = "ready"
    if data.get("chapterNo") and not ch_entry.get("no"):
        ch_entry["no"] = str(data["chapterNo"])
    if data.get("title"):
        ch_entry["title"] = data["title"]
    if data.get("authors"):
        ch_entry.setdefault("authors", data["authors"])


def import_volume(index: dict, cfg: dict) -> dict:
    prefix = cfg["prefix"]
    vol = cfg["vol"]
    root: Path = cfg["studypack_root"]
    ch_map = chapter_section_map(index, prefix)

    stats = {
        "imported_new": [],
        "merged": [],
        "skipped_identical": [],
        "skipped_no_index": [],
        "skipped_no_json": [],
        "merged_items": 0,
    }

    if not root.is_dir():
        print(f"WARN: missing {root}", file=sys.stderr)
        return stats

    for folder in sorted(root.iterdir()):
        if not folder.is_dir():
            continue
        m = re.match(r"^(\d{3})_", folder.name)
        if not m:
            continue
        n = int(m.group(1))
        ch_id = f"{prefix}-{n:03d}"
        old_prefix = f"h22-{n:03d}"

        json_files = sorted(folder.glob("h22-*.json"))
        if not json_files:
            stats["skipped_no_json"].append(folder.name)
            continue

        if ch_id not in ch_map:
            stats["skipped_no_index"].append(ch_id)
            continue

        ch_entry, section_name = ch_map[ch_id]
        src_path = json_files[0]
        source_rel = f"noupload/harrison/{cfg['source_label']}/{folder.name}/{src_path.name}"
        raw = json.loads(src_path.read_text())
        prepared = prepare_studypack(
            raw,
            ch_id=ch_id,
            old_prefix=old_prefix,
            vol=vol,
            section_name=section_name,
            source_rel=source_rel,
        )

        existing_paths = sorted(DATA_DIR.glob(f"{prefix}-{n:03d}_*.json"))
        out_name = src_path.name.replace("h22-", f"{prefix}-")
        out_path = DATA_DIR / out_name

        if not existing_paths:
            out_path.write_text(json.dumps(prepared, indent=2, ensure_ascii=False) + "\n")
            update_index_entry(ch_entry, prepared, out_name)
            stats["imported_new"].append(ch_id)
            continue

        # Chapter already loaded — compare content, maybe merge new items
        existing_path = existing_paths[0]
        existing = json.loads(existing_path.read_text())
        existing_fps = {content_fp(it) for it in existing.get("items", [])}
        prepared_fps = {content_fp(it) for it in prepared.get("items", [])}

        if prepared_fps and prepared_fps <= existing_fps:
            stats["skipped_identical"].append(ch_id)
            # Ensure index points at the existing file
            if ch_entry.get("status") != "ready" or not ch_entry.get("file"):
                update_index_entry(ch_entry, existing, existing_path.name)
            continue

        new_items = [it for it in prepared.get("items", []) if content_fp(it) not in existing_fps]
        if not new_items:
            stats["skipped_identical"].append(ch_id)
            continue

        used_ids = {it["id"] for it in existing.get("items", []) if it.get("id")}
        appended = []
        for it in new_items:
            # Remap again in case prepare already used colliding ids
            remap_item_id(it, ch_id, used_ids, tag="sp")
            appended.append(it)

        existing.setdefault("items", []).extend(appended)
        # Keep original sourceFile; note studypack merge
        note = existing.get("_studypackMergedFrom")
        paths = list(note) if isinstance(note, list) else ([] if not note else [note])
        if source_rel not in paths:
            paths.append(source_rel)
        existing["_studypackMergedFrom"] = paths
        existing_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n")
        update_index_entry(ch_entry, existing, existing_path.name)
        stats["merged"].append(f"{ch_id}(+{len(appended)})")
        stats["merged_items"] += len(appended)

    return stats


def main() -> int:
    index = json.loads(INDEX_PATH.read_text())
    all_stats = {}
    for cfg in VOLUMES:
        print(f"\n=== Volume {cfg['vol']} ({cfg['prefix']}) ===")
        stats = import_volume(index, cfg)
        all_stats[cfg["prefix"]] = stats
        print(f"Imported new: {len(stats['imported_new'])}")
        print(f"Merged into existing: {len(stats['merged'])} chapters, {stats['merged_items']} items")
        print(f"Skipped identical: {len(stats['skipped_identical'])}")
        print(f"Skipped (no index / section): {len(stats['skipped_no_index'])}")
        print(f"Skipped (no json): {len(stats['skipped_no_json'])}")
        if stats["imported_new"]:
            print(f"  First new: {stats['imported_new'][0]} | Last: {stats['imported_new'][-1]}")
        if stats["merged"][:10]:
            print(f"  Merged sample: {', '.join(stats['merged'][:10])}")
        if stats["skipped_no_index"]:
            print(f"  No index: {', '.join(stats['skipped_no_index'])}")

    INDEX_PATH.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")

    # Summary counts
    ready = pending = 0
    for sec in index.get("sections", []):
        for ch in sec.get("chapters", []):
            if ch.get("status") == "ready":
                ready += 1
            elif ch.get("status") == "pending":
                pending += 1
    print(f"\nIndex chapters: ready={ready} pending={pending}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
