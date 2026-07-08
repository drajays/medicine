#!/usr/bin/env bash
# Sync validated endo content from authoring workspace → Medicine portal sub-app.
set -euo pipefail

SRC="${1:-/Users/dr.ajayshukla/endo_masterapp/data}"
DEST="$(cd "$(dirname "$0")/.." && pwd)/endo/data"

echo "Validating source JSON..."
python3 "$(dirname "$0")/validate_endo_json.py" "$SRC"/*.json 2>/dev/null || {
  # validate only non-index files in src
  for f in "$SRC"/endo2021_*.json "$SRC"/w15-*.json "$SRC"/endo2015_*.json "$SRC"/endo2024_*.json; do
    [ -f "$f" ] || continue
    python3 "$(dirname "$0")/validate_endo_json.py" "$f" || exit 1
  done
}

echo "Syncing $SRC → $DEST"
mkdir -p "$DEST"
rsync -av --include='*.json' --exclude='*' "$SRC/" "$DEST/"
cp "$SRC/index.json" "$DEST/index.json"
echo "Done. $(ls "$DEST"/*.json 2>/dev/null | wc -l | tr -d ' ') JSON files in portal endo/data/"
