import type { HeaderKind } from '@/lib/types'

export type ContentKind =
  | 'harrison'
  | 'hot_topic'
  | 'case_report'
  | 'pediatric_endo'
  | 'story'
  | 'trial'
  | 'calculator'
  | 'imaging'
  | 'catalog'
  | 'other'

export type ContentAction = 'added' | 'updated' | 'expanded' | 'fixed' | 'removed'

export interface ContentLogItem {
  id: string
  kind: ContentKind
  title: string
  subtitle?: string
  action: ContentAction
  stats?: string
  file?: string
}

export interface ContentLogEntry {
  date: string
  commit: string
  summary: string
  items: ContentLogItem[]
}

export interface ContentLog {
  title: string
  description: string
  generatedAt: string
  totalCommits: number
  totalModules: number
  entries: ContentLogEntry[]
}

export type LogViewMode = 'daily' | 'weekly' | 'monthly'

export interface LogPeriod {
  key: string
  label: string
  startDate: string
  endDate: string
  entries: ContentLogEntry[]
  itemCount: number
  commitCount: number
}

export const KIND_META: Record<
  ContentKind,
  { label: string; icon: string; kind: HeaderKind | null }
> = {
  harrison: { label: 'Harrison', icon: '📖', kind: 'harrison_banner' },
  hot_topic: { label: 'Hot Topics', icon: '🔥', kind: 'hot_topics' },
  case_report: { label: 'Case Reports', icon: '📋', kind: 'case_reports' },
  pediatric_endo: { label: 'Pediatric Endo', icon: '🧒', kind: 'pediatric_endo' },
  story: { label: 'Stories', icon: '💬', kind: 'stories' },
  trial: { label: 'Trials', icon: '📊', kind: 'trials' },
  calculator: { label: 'Calculators', icon: '🧮', kind: 'calculators' },
  imaging: { label: 'Imaging & Atlases', icon: '🩻', kind: 'imaging_resources' },
  catalog: { label: 'Catalog', icon: '🗂️', kind: null },
  other: { label: 'Other', icon: '📄', kind: null },
}

export const ACTION_META: Record<ContentAction, { label: string; className: string }> = {
  added: {
    label: 'New',
    className:
      'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-300',
  },
  expanded: {
    label: 'Expanded',
    className: 'bg-blue-100 text-blue-800 dark:bg-blue-950/50 dark:text-blue-300',
  },
  updated: {
    label: 'Updated',
    className: 'bg-slate-100 text-slate-700 dark:bg-zinc-800 dark:text-zinc-300',
  },
  fixed: {
    label: 'Fixed',
    className: 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-300',
  },
  removed: {
    label: 'Removed',
    className: 'bg-red-100 text-red-800 dark:bg-red-950/50 dark:text-red-300',
  },
}

function parseDate(iso: string): Date {
  const [y, m, d] = iso.split('-').map(Number)
  return new Date(y, m - 1, d)
}

function formatDay(iso: string): string {
  return parseDate(iso).toLocaleDateString(undefined, {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  })
}

function formatMonth(iso: string): string {
  const [y, m] = iso.split('-').map(Number)
  return new Date(y, m - 1, 1).toLocaleDateString(undefined, { month: 'long', year: 'numeric' })
}

function weekStart(iso: string): Date {
  const d = parseDate(iso)
  const day = d.getDay()
  const diff = day === 0 ? -6 : 1 - day
  const start = new Date(d)
  start.setDate(d.getDate() + diff)
  return start
}

function toIso(d: Date): string {
  const y = d.getFullYear()
  const m = String(d.getMonth() + 1).padStart(2, '0')
  const day = String(d.getDate()).padStart(2, '0')
  return `${y}-${m}-${day}`
}

export function groupLogEntries(entries: ContentLogEntry[], mode: LogViewMode): LogPeriod[] {
  const map = new Map<string, LogPeriod>()

  for (const entry of entries) {
    let key: string
    let label: string
    let startDate: string
    let endDate: string

    if (mode === 'daily') {
      key = entry.date
      label = formatDay(entry.date)
      startDate = entry.date
      endDate = entry.date
    } else if (mode === 'weekly') {
      const start = weekStart(entry.date)
      const end = new Date(start)
      end.setDate(start.getDate() + 6)
      key = toIso(start)
      label = `Week of ${start.toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' })}`
      startDate = toIso(start)
      endDate = toIso(end)
    } else {
      key = entry.date.slice(0, 7)
      label = formatMonth(entry.date)
      const [y, m] = key.split('-').map(Number)
      const last = new Date(y, m, 0)
      startDate = `${key}-01`
      endDate = toIso(last)
    }

    const existing = map.get(key)
    if (existing) {
      existing.entries.push(entry)
      existing.itemCount += entry.items.length
      existing.commitCount += 1
    } else {
      map.set(key, {
        key,
        label,
        startDate,
        endDate,
        entries: [entry],
        itemCount: entry.items.length,
        commitCount: 1,
      })
    }
  }

  return [...map.values()]
}

export function filterEntries(
  entries: ContentLogEntry[],
  kind: ContentKind | 'all',
  query: string,
): ContentLogEntry[] {
  const q = query.trim().toLowerCase()
  return entries
    .map((entry) => {
      const items = entry.items.filter((item) => {
        if (kind !== 'all' && item.kind !== kind) return false
        if (!q) return true
        return (
          item.title.toLowerCase().includes(q) ||
          item.id.toLowerCase().includes(q) ||
          entry.summary.toLowerCase().includes(q)
        )
      })
      if (items.length === 0 && q && !entry.summary.toLowerCase().includes(q)) return null
      if (kind !== 'all' && items.length === 0) return null
      return { ...entry, items: items.length ? items : entry.items }
    })
    .filter((e): e is ContentLogEntry => e !== null)
}

export function countRecent(entries: ContentLogEntry[], days: number): number {
  const cutoff = new Date()
  cutoff.setDate(cutoff.getDate() - days)
  return entries.filter((e) => parseDate(e.date) >= cutoff).length
}
