#!/bin/bash
# Double-click in Finder, or run: open "Open Medicine Local.command"
# Starts the Vite dev server and opens the study portal in your browser.

set -e
cd "$(dirname "$0")"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm not found. Install Node.js first (https://nodejs.org/), then try again."
  read -r -p "Press Enter to close…"
  exit 1
fi

if [ ! -d web/node_modules ]; then
  echo "Installing dependencies (first run)…"
  (cd web && npm install)
fi

URL="http://localhost:5173/medicine/"
echo "Starting local server → $URL"
echo "Leave this window open. Press Ctrl+C to stop."
echo

# Open the browser once Vite is listening (or after a short wait).
(
  for _ in $(seq 1 60); do
    if curl -sf -o /dev/null "$URL" 2>/dev/null; then
      open "$URL"
      exit 0
    fi
    sleep 0.5
  done
  open "$URL"
) &

cd web
exec npm run dev
