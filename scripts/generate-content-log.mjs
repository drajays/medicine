#!/usr/bin/env node
/**
 * Build data/content_log.json from git history of data/.
 * Run after content commits: node scripts/generate-content-log.mjs
 */
import { execSync } from 'node:child_process'
import { readFileSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const INDEX_PATH = join(ROOT, 'data/index.json')
const OUT_PATH = join(ROOT, 'data/content_log.json')

const ID_FROM_FILE = [
  [/^(h[12]-\d{3})_/i, 'harrison'],
  [/^(pe-cr-\d{3})_/i, 'pediatric_endo'],
  [/^(ht-\d{3})_/i, 'hot_topic'],
  [/^(cr-\d{3})_/i, 'case_report'],
  [/^(story-\d{3})_/i, 'story'],
  [/^(tr-nejm-\d{3})/i, 'trial'],
  [/^(tr-\d{3})/i, 'trial'],
  [/^(calc-\d{3})/i, 'calculator'],
]

function parseIdAndKind(filename) {
  const base = filename.replace(/^data\//, '').replace(/\.json$/, '')
  for (const [re, kind] of ID_FROM_FILE) {
    const m = base.match(re)
    if (m) return { id: m[1].toLowerCase(), kind }
  }
  if (filename.endsWith('index.json')) return { id: 'catalog', kind: 'catalog' }
  return null
}

function buildCatalogMap(index) {
  const map = new Map()
  const trees = [
    ['harrison', index.sections?.flatMap((s) => s.chapters ?? []) ?? []],
    ['hot_topic', index.hotTopics?.topics ?? []],
    ['case_report', index.caseReports?.reports ?? []],
    ['pediatric_endo', index.pediatricEndo?.chapters ?? []],
    ['story', index.stories?.entries ?? []],
    ['calculator', index.calculators?.entries ?? []],
    ['trial', index.trials?.entries ?? []],
  ]
  for (const [kind, entries] of trees) {
    for (const e of entries) {
      if (e?.id) {
        map.set(e.id, {
          title: e.title ?? e.id,
          subtitle: e.subtitle ?? '',
          kind,
          file: e.file ?? null,
        })
      }
    }
  }
  return map
}

function inferAction(status, summary, itemId) {
  if (status === 'A') return 'added'
  if (status === 'D') return 'removed'
  const s = summary.toLowerCase()
  const id = itemId.toLowerCase()
  if (s.includes('fix') || s.includes('correct')) return 'fixed'
  if (s.includes('expand') && (s.includes(id) || s.includes('module'))) return 'expanded'
  if (s.includes('author') || /\badd\b/.test(s)) return 'added'
  return 'updated'
}

function extractStats(summary, itemId) {
  if (!summary.toLowerCase().includes(itemId.toLowerCase())) {
    const range = summary.match(/(\d+)\s*items?(?:,\s*(\d+)%?\s*why\/how)?(?:,\s*(\d+)\s*mcqs?)?/i)
    if (!range || summary.split(',').length > 3) return undefined
  }
  const m = summary.match(/(\d+)\s*items?(?:,\s*(\d+)%?\s*why\/how)?(?:,\s*(\d+)\s*mcqs?)?/i)
  if (m) {
    const parts = [`${m[1]} items`]
    if (m[2]) parts.push(`${m[2]}% Why/How`)
    if (m[3]) parts.push(`${m[3]} MCQs`)
    return parts.join(', ')
  }
  const mcq = summary.match(/(\d+)\s*MCQs?/i)
  if (mcq) return `${mcq[1]} MCQs`
  return undefined
}

function gitLines(cmd) {
  return execSync(cmd, { cwd: ROOT, encoding: 'utf8' })
    .trim()
    .split('\n')
    .filter(Boolean)
}

function main() {
  const index = JSON.parse(readFileSync(INDEX_PATH, 'utf8'))
  const catalog = buildCatalogMap(index)

  const commits = gitLines(
    'git log --reverse --format="%H|%ad|%s" --date=short -- data/',
  )

  const entries = []

  for (const line of commits) {
    const [hash, date, ...rest] = line.split('|')
    const summary = rest.join('|')
    const short = hash.slice(0, 7)

    let files
    try {
      files = gitLines(`git show --name-status --format="" ${hash} -- data/`)
    } catch {
      continue
    }

    const itemMap = new Map()

    for (const row of files) {
      const parts = row.split('\t')
      if (parts.length < 2) continue
      const status = parts[0].charAt(0)
      const file = parts[parts.length - 1]
      if (!file.startsWith('data/')) continue

      const parsed = parseIdAndKind(file)
      if (!parsed) continue

      const { id, kind: fileKind } = parsed
      if (id === 'catalog') continue

      const meta = catalog.get(id)
      const kind = meta?.kind ?? fileKind
      const action = inferAction(status, summary, id)
      const stats = extractStats(summary, id)

      const existing = itemMap.get(id)
      if (existing) {
        if (action === 'added' || existing.action === 'updated') existing.action = action
        continue
      }

      itemMap.set(id, {
        id,
        kind,
        title: meta?.title ?? id,
        subtitle: meta?.subtitle || undefined,
        action,
        stats: stats || undefined,
        file: meta?.file ?? file.replace(/^data\//, ''),
      })
    }

    const items = [...itemMap.values()]
    if (items.length === 0 && !summary.toLowerCase().includes('catalog')) {
      const bulk = summary.match(/\((h[12]-\d{3})\s+to\s+(h[12]-\d{3})\)/i)
      if (bulk) {
        entries.push({ date, commit: short, summary, items: [] })
      }
      continue
    }

    entries.push({ date, commit: short, summary, items })
  }

  entries.reverse()

  const totalItems = new Set(entries.flatMap((e) => e.items.map((i) => i.id))).size

  const log = {
    title: "Content Update Log",
    description:
      "Chronological record of study modules added or updated in this portal — generated from git history.",
    generatedAt: new Date().toISOString(),
    totalCommits: entries.length,
    totalModules: totalItems,
    entries,
  }

  writeFileSync(OUT_PATH, `${JSON.stringify(log, null, 2)}\n`)
  console.log(`Wrote ${OUT_PATH} — ${entries.length} commits, ${totalItems} unique modules`)
}

main()
