import type { ItemMark } from '@/lib/types'
import type { ItemEngagementRecord } from '@/lib/studyProgress'
import type { RevisionStudyItem, ReviewRecord } from '@/lib/revision-math'
import type { DailyStats, SessionHistoryEntry } from '@/stores/revisionStore'

/**
 * Backup/restore for the user's local-only study data (the h22-ui-store). The
 * whole point is portability + safety: localStorage can be cleared by the
 * browser at any time, and there is no server, so this is the only way to move
 * progress between devices or recover from a wipe.
 */
export const STUDY_EXPORT_VERSION = 2
export const STUDY_STORE_KEY = 'h22-ui-store'

/**
 * The persisted slice of the revision engine (h22-revision-engine-v2). Bundled
 * into the backup so a restore preserves FSRS intervals, review history, streaks
 * and daily stats — none of which can be reconstructed from study marks alone.
 */
export interface RevisionBackup {
  items?: Record<string, RevisionStudyItem>
  reviews?: ReviewRecord[]
  streak?: number
  lastStudyDate?: string | null
  dailyStats?: Record<string, DailyStats>
  sessionHistory?: SessionHistoryEntry[]
  showTimeAfterReveal?: boolean
}

/** Every per-item map the user can generate. All optional so old/partial
 * backups still import cleanly. */
export interface StudyDataPayload {
  marks?: Record<string, ItemMark>
  ratings?: Record<string, number>
  flags?: Record<string, string>
  feedbackCtx?: Record<string, unknown>
  bookmarks?: Record<string, boolean>
  mcqSelections?: Record<string, number | null>
  revealed?: Record<string, boolean>
  readItems?: Record<string, boolean>
  itemEngagement?: Record<string, ItemEngagementRecord>
  chapterTotals?: Record<string, number>
  chapterEngagedMs?: Record<string, number>
  totalEngagementMs?: number
  revision?: RevisionBackup
}

export interface StudyExport {
  app: 'harrison_app'
  kind: 'study-data'
  version: number
  exportedAt: string
  data: StudyDataPayload
}

const PAYLOAD_KEYS: (keyof StudyDataPayload)[] = [
  'marks',
  'ratings',
  'flags',
  'feedbackCtx',
  'bookmarks',
  'mcqSelections',
  'revealed',
  'readItems',
  'itemEngagement',
  'chapterTotals',
  'chapterEngagedMs',
]

export function buildStudyExport(data: StudyDataPayload): StudyExport {
  return {
    app: 'harrison_app',
    kind: 'study-data',
    version: STUDY_EXPORT_VERSION,
    exportedAt: new Date().toISOString(),
    data,
  }
}

export function studyDataCounts(d: StudyDataPayload) {
  return {
    marks: Object.keys(d.marks ?? {}).length,
    ratings: Object.keys(d.ratings ?? {}).length,
    flags: Object.keys(d.flags ?? {}).length,
    bookmarks: Object.keys(d.bookmarks ?? {}).length,
    revisionCards: Object.keys(d.revision?.items ?? {}).length,
    reviews: (d.revision?.reviews ?? []).length,
  }
}

export function isStudyDataEmpty(d: StudyDataPayload): boolean {
  const mapsEmpty = PAYLOAD_KEYS.every((k) => Object.keys(d[k] ?? {}).length === 0)
  const revisionEmpty = Object.keys(d.revision?.items ?? {}).length === 0
  return mapsEmpty && revisionEmpty
}

/** Parse + lightly validate an uploaded backup file. */
export function parseStudyExport(
  text: string,
): { ok: true; value: StudyExport } | { ok: false; error: string } {
  let raw: unknown
  try {
    raw = JSON.parse(text)
  } catch {
    return { ok: false, error: 'Not a valid JSON file.' }
  }
  if (!raw || typeof raw !== 'object') {
    return { ok: false, error: 'File does not contain a study-data object.' }
  }
  const obj = raw as Record<string, unknown>
  if (obj.kind !== 'study-data' || obj.app !== 'harrison_app') {
    return { ok: false, error: 'This file is not a Harrison study-data backup.' }
  }
  const data = obj.data
  if (!data || typeof data !== 'object') {
    return { ok: false, error: 'Backup is missing its data section.' }
  }
  // Keep only the maps we recognise; ignore anything else.
  const clean: StudyDataPayload = {}
  for (const key of PAYLOAD_KEYS) {
    const v = (data as Record<string, unknown>)[key]
    if (v && typeof v === 'object') {
      ;(clean as Record<string, unknown>)[key] = v
    }
  }
  const revision = (data as Record<string, unknown>).revision
  if (revision && typeof revision === 'object') {
    clean.revision = revision as RevisionBackup
  }
  if (isStudyDataEmpty(clean)) {
    return { ok: false, error: 'Backup contains no study data.' }
  }
  return {
    ok: true,
    value: {
      app: 'harrison_app',
      kind: 'study-data',
      version: typeof obj.version === 'number' ? obj.version : STUDY_EXPORT_VERSION,
      exportedAt: typeof obj.exportedAt === 'string' ? obj.exportedAt : '',
      data: clean,
    },
  }
}

/** Generic per-id merge: incoming entries win on a key conflict. */
export function mergeRecord<T>(
  base: Record<string, T> = {},
  incoming: Record<string, T> = {},
): Record<string, T> {
  return { ...base, ...incoming }
}

/**
 * Marks merge that respects history: on a conflict keep whichever entry was
 * touched most recently (lastSeenAt), so importing an older backup never
 * silently rewinds newer progress.
 */
export function mergeMarks(
  base: Record<string, ItemMark> = {},
  incoming: Record<string, ItemMark> = {},
): Record<string, ItemMark> {
  const out: Record<string, ItemMark> = { ...base }
  for (const [id, inc] of Object.entries(incoming)) {
    const cur = out[id]
    if (!cur) {
      out[id] = inc
      continue
    }
    out[id] = (inc.lastSeenAt ?? 0) >= (cur.lastSeenAt ?? 0) ? inc : cur
  }
  return out
}

/** Trigger a client-side download of a JSON object. */
export function downloadJSON(filename: string, obj: unknown) {
  const blob = new Blob([JSON.stringify(obj, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  a.remove()
  URL.revokeObjectURL(url)
}

export function exportFilename(): string {
  const d = new Date()
  const pad = (n: number) => String(n).padStart(2, '0')
  return `harrison-study-${d.getFullYear()}${pad(d.getMonth() + 1)}${pad(d.getDate())}.json`
}

// ── Revision engine merge helpers ────────────────────────────────────────────

/** Per-card merge: keep whichever was reviewed (or created) most recently. */
export function mergeRevisionItems(
  base: Record<string, RevisionStudyItem> = {},
  incoming: Record<string, RevisionStudyItem> = {},
): Record<string, RevisionStudyItem> {
  const out: Record<string, RevisionStudyItem> = { ...base }
  for (const [id, inc] of Object.entries(incoming)) {
    const cur = out[id]
    if (!cur) {
      out[id] = inc
      continue
    }
    const incT = inc.lastReviewedAt ?? inc.createdAt ?? 0
    const curT = cur.lastReviewedAt ?? cur.createdAt ?? 0
    out[id] = incT >= curT ? inc : cur
  }
  return out
}

/** Union review log, de-duplicated by (itemId, reviewedAt), chronological. */
export function mergeReviews(
  base: ReviewRecord[] = [],
  incoming: ReviewRecord[] = [],
): ReviewRecord[] {
  const seen = new Set<string>()
  const out: ReviewRecord[] = []
  for (const r of [...base, ...incoming]) {
    const key = `${r.itemId}@${r.reviewedAt}`
    if (seen.has(key)) continue
    seen.add(key)
    out.push(r)
  }
  return out.sort((a, b) => a.reviewedAt - b.reviewedAt)
}

/** Per-day stats: keep the busier record to avoid double-counting overlap. */
export function mergeDailyStats(
  base: Record<string, DailyStats> = {},
  incoming: Record<string, DailyStats> = {},
): Record<string, DailyStats> {
  const out: Record<string, DailyStats> = { ...base }
  for (const [date, inc] of Object.entries(incoming)) {
    const cur = out[date]
    out[date] = !cur || inc.reviewed > cur.reviewed ? inc : cur
  }
  return out
}

export function mergeSessionHistory(
  base: SessionHistoryEntry[] = [],
  incoming: SessionHistoryEntry[] = [],
): SessionHistoryEntry[] {
  const seen = new Set<string>()
  const out: SessionHistoryEntry[] = []
  for (const e of [...base, ...incoming]) {
    if (seen.has(e.id)) continue
    seen.add(e.id)
    out.push(e)
  }
  return out.sort((a, b) => a.startedAt - b.startedAt).slice(-50)
}

function laterDate(a?: string | null, b?: string | null): string | null {
  if (!a) return b ?? null
  if (!b) return a
  return a >= b ? a : b // ISO YYYY-MM-DD compares lexicographically
}

/**
 * Combine the current revision slice with an incoming backup. 'replace' takes
 * the incoming wholesale (per-field, falling back to current when absent);
 * 'merge' folds the two together without losing review history or streaks.
 */
export function mergeRevisionBackup(
  current: RevisionBackup,
  incoming: RevisionBackup,
  mode: 'merge' | 'replace',
): Required<RevisionBackup> {
  if (mode === 'replace') {
    return {
      items: incoming.items ?? current.items ?? {},
      reviews: incoming.reviews ?? current.reviews ?? [],
      streak: incoming.streak ?? current.streak ?? 0,
      lastStudyDate: incoming.lastStudyDate ?? current.lastStudyDate ?? null,
      dailyStats: incoming.dailyStats ?? current.dailyStats ?? {},
      sessionHistory: incoming.sessionHistory ?? current.sessionHistory ?? [],
      showTimeAfterReveal: incoming.showTimeAfterReveal ?? current.showTimeAfterReveal ?? true,
    }
  }
  return {
    items: mergeRevisionItems(current.items, incoming.items),
    reviews: mergeReviews(current.reviews, incoming.reviews),
    streak: Math.max(current.streak ?? 0, incoming.streak ?? 0),
    lastStudyDate: laterDate(current.lastStudyDate, incoming.lastStudyDate),
    dailyStats: mergeDailyStats(current.dailyStats, incoming.dailyStats),
    sessionHistory: mergeSessionHistory(current.sessionHistory, incoming.sessionHistory),
    showTimeAfterReveal: incoming.showTimeAfterReveal ?? current.showTimeAfterReveal ?? true,
  }
}
