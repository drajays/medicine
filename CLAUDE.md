# harrison_app

Harrison's Principles of Internal Medicine (22nd ed.) — a static, vanilla-JS
clinical Q-bank & notes web app. No build step, no framework, no backend.

## Architecture

- `index.html` / `app.js` / `styles.css` — the entire app. `app.js` loads
  `data/index.json` (the catalog), then lazy-loads each chapter/topic JSON
  file on demand.
- `data/index.json` — the catalog. Two content trees:
  - `sections[]` — Harrison chapters, grouped by body-system section. Each
    chapter entry: `{id, no, title, file, status}`. `status` is `"pending"`
    (not yet authored, `file: null`) or `"ready"`.
  - `hotTopics.topics[]` — standalone topics beyond Harrison chapters
    (landmark trials, mechanisms, focused clinical-pearl deep dives). Each
    entry: `{id, title, subtitle, category, file, status}`.
- `data/*.json` — one file per chapter/topic. Shared item schema across both
  trees: every item has `id`, `type` (`note` | `mcq` | `true_false` |
  `assertion_reason`), `subtopic`, `reference`. See the two skills below for
  the full per-type shape.
- `data/h{vol}-{NNN}_*.json` — Harrison chapters (`vol` 1 or 2).
- `data/ht-{NNN}_*.json` — hot topics. Header includes `topicType:
  "hot_topic"` and `category` (must match its `index.json` entry) instead of
  a chapter `section`/`chapterNo`.
- `scripts/` — one-off Node scripts used to bulk-generate specific hot-topic
  files from external source markdown (e.g. `build_semaglutide.js` parsed a
  downloaded PubMed Q&A file). Not a general pipeline — most hot topics are
  authored directly as JSON, not via a script.

## Authoring workflows (skills)

Two skills encode the full author → validate → register → commit → push
pipeline:

- **`.claude/skills/mcq_skill/`** — Harrison chapters. Source is a specific
  chapter's `content.md` under `~/harrison/Harrison{1,2}_chapters/`. Use
  when a chapter is `"pending"` in `index.json`.
- **`.claude/skills/hot_topics_skill/`** — hot topics. Source is whatever
  the user pastes/provides in-conversation (no fixed source file), or
  external reference material the user points to. Use when the user names
  a topic for "Hot Topics" that isn't a Harrison chapter.

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
