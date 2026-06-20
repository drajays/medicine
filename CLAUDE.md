# harrison_app

Harrison's Principles of Internal Medicine (22nd ed.) — a static, vanilla-JS
clinical Q-bank & notes web app. No build step, no framework, no backend.

## Architecture

- `index.html` / `app.js` / `styles.css` — the entire app. `app.js` loads
  `data/index.json` (the catalog), then lazy-loads each chapter/topic JSON
  file on demand.
- `data/index.json` — the catalog. Content trees:
  - `sections[]` — Harrison chapters
  - `hotTopics.topics[]` — standalone hot topics
  - `caseReports.reports[]` — clinical case vignettes
  - `trials.entries[]` — clinical trials; `subsection`: `nejm` | `general`
- `data/*.json` — one file per chapter/topic/trial. Item types: `note` | `mcq` |
  `true_false` | `assertion_reason` | `why` | `how` | `shortanswer` (trials/NEJM).
- `data/h{vol}-{NNN}_*.json` — Harrison chapters (`vol` 1 or 2).
- `data/ht-{NNN}_*.json` — hot topics. Header includes `topicType:
  "hot_topic"` and `category` (must match its `index.json` entry) instead of
  a chapter `section`/`chapterNo`.
- `scripts/build_nejm_trials.js` — splits `noupload/NEJM` OCR markdown, maps
  bibliography numbers to one question each, emits `data/tr-nejm-*.json`.

## Forking for another subject

See `.claude/skills/bootstrap_subject_app/` — scaffold workflow + copy-paste agent prompt for creating a similar Q-bank app for a different textbook/subject.

## Authoring workflows (skills)

Two skills encode the full author → validate → register → commit → push
pipeline:

- **`.claude/skills/mcq_skill/`** — Harrison chapters. Source is a specific
  chapter's `content.md` under `~/harrison/Harrison{1,2}_chapters/`. Use
  when a chapter is `"pending"` in `index.json`.
- **`.claude/skills/hot_topics_skill/`** — hot topics.
- **`.claude/skills/nejm_trials_skill/`** — NEJM trials subsection (reference-linked Q&A from `noupload/NEJM`).

Both skills share:
- The same four item types and validation rules (note/mcq/true_false/
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

`AR_OPTIONS` (assertion-reason answer choices, fixed in `app.js`, never
paraphrase):
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
  `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` (or whichever
  model authored it).
- Live site: https://drajays.github.io/medicine/ (GitHub Pages, served
  straight from `main`).
