# Harrison's 22e — Modern UI (React + Vite)

A blisteringly fast, clinical-minimalist study interface for the Harrison Q-Bank. Lives alongside the legacy vanilla-JS app in the repo root.

## Quick start

```bash
cd web
npm install
npm run dev
```

Open the URL Vite prints (typically `http://localhost:5173`).

## Stack

| Layer | Choice |
|-------|--------|
| Framework | React 19 + Vite 8 + TypeScript |
| State | Zustand (persisted progress, theme, bookmarks) |
| Styling | Tailwind CSS v4 + custom clinical design tokens |
| Virtualization | `@tanstack/react-virtual` (sidebar chapter list) |
| Command palette | `cmdk` — `⌘K` / `Ctrl+K` |
| Motion | Framer Motion (≤150ms, non-blocking) |

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| `⌘K` / `Ctrl+K` | Command palette |
| `Space` | Toggle reveal answer |
| `←` / `→` | Previous / next question |
| `1`–`4` | Select MCQ option |

On mobile: swipe left/right on the question card; bottom nav for navigation.

## Mock data

Three chapters, five items total — wired in `src/data/`:

- **Heart Failure** — 2 MCQs
- **Hyperthyroidism** — 1 note + 1 MCQ
- **Acute Kidney Injury** — 1 note

Replace mock imports in `src/store/useAppStore.ts` with fetches to `../data/index.json` when ready to connect the live catalog.

## Architecture

```
src/
├── store/useAppStore.ts     # Glassbox state (no UI logic)
├── components/
│   ├── layout/              # Shell, sidebar, utility bar, mobile nav
│   ├── question/            # MCQ, notes, answer reveal
│   └── ui/                  # Button, skeleton, command palette
├── hooks/                   # Keyboard shortcuts, swipe gestures
└── data/                    # Mock catalog + chapter JSON
```

## Production build

```bash
npm run build   # outputs to web/dist/
npm run preview
```
