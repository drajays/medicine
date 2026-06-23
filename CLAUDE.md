# harrison_app

Harrison's Principles of Internal Medicine (22nd ed.) — a clinical Q-bank &
notes study portal. A **React + Vite + TypeScript** single-page app reads a
static tree of JSON content files. No backend; deployed on GitHub Pages.

## Architecture

Two layers: a React UI that is built and a static JSON data layer that is not.

### UI — `web/` (React 19 + Vite 8 + TypeScript + Tailwind CSS v4)

- Source lives in `web/src/`. State is Zustand (`web/src/store/useAppStore.ts`,
  persists theme/progress/bookmarks). Sidebar list is virtualized
  (`@tanstack/react-virtual`); `⌘K` command palette via `cmdk`; transitions
  via Framer Motion.
- **Build & deploy to the live site:**
  ```bash
  cd web
  npm install      # first time
  npm run dev      # local dev at http://localhost:5173/medicine/
  npm run deploy   # build + copy web/dist → repo root (index.html + assets/)
  ```
  `npm run deploy` runs `scripts/deploy-pages.mjs`, which writes the built
  `index.html` and hashed `assets/` into the repo root (what GitHub Pages
  serves). Commit the regenerated root `index.html` + `assets/` along with
  your `web/src` changes.
- The original vanilla-JS app is archived in `legacy/` (`app.js`, `styles.css`)
  and is no longer served.
- Design system: scholarly parchment-editorial — Fraunces (serif display) +
  Hanken Grotesk (UI), amber accent, per-section colour coding. Tokens live in
  `web/src/index.css` (`@theme`). See `web/README.md`.

### Data — `data/` (static JSON, served at `/medicine/data/`, no build)

- `data/index.json` — the catalog. Content trees:
  - `sections[]` — Harrison chapters (also hosts `pe-cr-*` pediatric-endocrine
    case reports, registered as chapters)
  - `hotTopics.topics[]` — standalone hot topics
  - `caseReports.reports[]` — clinical case vignettes
  - `stories.entries[]` — narrative ethics / management / patient-interaction
    vignettes (`kind: story`, rose accent)
  - `calculators.entries[]` — standalone interactive HTML tools in
    `calculators/` (opened in a new tab, not fetched as item JSON)
  - `trials.entries[]` — clinical trials; `subsection`: `nejm` | `general`
- `data/*.json` — one file per chapter/topic/report/trial/story. Item types:
  `note` | `mcq` | `true_false` | `assertion_reason` | `why` | `how` |
  `shortanswer` (the why/how/shortanswer types are used mainly by trials/NEJM
  and stories).
- File naming: `h{vol}-{NNN}_*` (Harrison chapters, vol 1|2) ·
  `pe-cr-{NNN}_*` (pediatric-endocrine case reports under `sections`) ·
  `ht-{NNN}_*` (hot topics; header carries `topicType: "hot_topic"` +
  `category`) · `cr-{NNN}_*` (case reports) · `story-{NNN}_*` (stories;
  `topicType: "story"`, `section: "Stories"`) · `tr-{NNN}` / `tr-nejm-{NNN}`
  (trials).
- The deployed app fetches `data/` at runtime (`DATA_BASE` in
  `web/src/lib/constants.ts`). **Adding/editing content = write the data file,
  register it in `data/index.json`, commit & push — no React rebuild needed.**
  Only UI/component changes require `npm run deploy`.

## Forking for another subject

See `.claude/skills/bootstrap_subject_app/` — workflow + agent prompt for
creating a similar Q-bank app for a different textbook/subject.

## Authoring workflows (skills)

These skills encode the full author → validate → register → commit → push
pipeline (UI rebuild not required — content is fetched at runtime):

- **`.claude/skills/mcq_skill/`** — Harrison chapters. Source is a specific
  chapter's `content.md` under `~/harrison/Harrison{1,2}_chapters/`. Use
  when a chapter is `"pending"` in `index.json`.
- **`.claude/skills/hot_topics_skill/`** — hot topics.
- **`.claude/skills/nejm_trials_skill/`** — NEJM trials subsection
  (reference-linked Q&A from `noupload/NEJM`).
- **`.claude/skills/story_skill/`** — Stories: narrative case-study teaching
  modules (ethics, communication, practice management, patient education,
  clinical reasoning). Registered under `stories.entries[]`. Unlike the others,
  Story content is original (no verbatim `reference` quotes), and **every story
  must end with a `story-{NNN}-appraisal` note giving the module's strength,
  limitation, and the assumptions it makes.**

Shared rules:
- The item types and validation rules above (note/mcq/true_false/
  assertion_reason — see either skill's SKILL.md for exact JSON shapes).
- `reference` must always be a verbatim quote from the source, prefixed
  with the section heading it came from — never paraphrased, never invented.
- Notes: ≥50% must have a `title` starting with "Why" or "How" (deep
  reasoning), not just factual recall.
- MCQs: vignette-style stems on diagnosis/management/treatment, not trivia.
- A node validation script (parses JSON, no duplicate ids, every reference
  has a quote, every mcq has 4 options with `correctOption` 0-3, every
  assertion_reason has `correctOption` 0-4, every true_false has a boolean
  `correctAnswer`, Why/How % ≥50).
- Register the new/updated entry in `data/index.json`, then commit and push
  to `drajays/medicine` `main`, staging only the specific changed files
  (never `git add -A` — `.DS_Store` must stay untracked).

`AR_OPTIONS` (assertion-reason answer choices, fixed in
`web/src/lib/constants.ts`, never paraphrase):
```
0: Both A and R are true, and R is the correct explanation of A
1: Both A and R are true, but R is NOT the correct explanation of A
2: A is true, but R is false
3: A is false, but R is true
4: Both A and R are false
```

## Conventions

- Do one chapter/topic fully through the pipeline before reporting back —
  don't batch multiple in one pass.
- Commit messages: one-line summary (item counts, % Why/How) + a short
  paragraph on major topics covered, ending with
  `Co-Authored-By: Claude <model> <noreply@anthropic.com>` (the model that
  authored it).
- Live site: https://drajays.github.io/medicine/ (GitHub Pages, served
  straight from `main`).
