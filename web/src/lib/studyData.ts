import type { ItemMark } from '@/lib/types'
import type { ItemEngagementRecord } from '@/lib/studyProgress'

/**
 * Backup/restore for the user's local-only study data (the h22-ui-store). The
 * whole point is portability + safety: localStorage can be cleared by the
 * browser at any time, and there is no server, so this is the only way to move
 * progress between devices or recover from a wipe.
 */
export const STUDY_EXPORT_VERSION = 2
export const STUDY_STORE_KEY = 'h22-ui-store'

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
  }
}

export function isStudyDataEmpty(d: StudyDataPayload): boolean {
  return PAYLOAD_KEYS.every((k) => Object.keys(d[k] ?? {}).length === 0)
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
