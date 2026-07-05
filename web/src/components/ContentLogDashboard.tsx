import { useEffect, useMemo, useState } from 'react'
import {
  Calendar,
  CalendarDays,
  CalendarRange,
  ChevronDown,
  ChevronRight,
  Clock,
  GitCommit,
  Loader2,
  Search,
} from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { fetchJSON } from '@/lib/data'
import {
  ACTION_META,
  countRecent,
  filterEntries,
  groupLogEntries,
  KIND_META,
  type ContentKind,
  type ContentLog,
  type ContentLogEntry,
  type ContentLogItem,
  type LogViewMode,
} from '@/lib/contentLog'
import { cn } from '@/lib/utils'

const BASE = import.meta.env.BASE_URL

const VIEW_OPTIONS: { mode: LogViewMode; label: string; icon: typeof Calendar }[] = [
  { mode: 'daily', label: 'Daily', icon: CalendarDays },
  { mode: 'weekly', label: 'Weekly', icon: CalendarRange },
  { mode: 'monthly', label: 'Monthly', icon: Calendar },
]

const KIND_FILTERS: Array<{ value: ContentKind | 'all'; label: string }> = [
  { value: 'all', label: 'All sections' },
  { value: 'harrison', label: 'Harrison' },
  { value: 'case_report', label: 'Case Reports' },
  { value: 'hot_topic', label: 'Hot Topics' },
  { value: 'pediatric_endo', label: 'Pediatric Endo' },
  { value: 'story', label: 'Stories' },
  { value: 'trial', label: 'Trials' },
  { value: 'calculator', label: 'Calculators' },
]

function StatTile({ label, value, sub }: { label: string; value: string; sub?: string }) {
  return (
    <div className="clinical-card p-4">
      <p className="text-[10px] font-bold uppercase tracking-wider text-teal-700 dark:text-teal-300">
        {label}
      </p>
      <p className="mt-2 text-2xl font-bold tabular-nums">{value}</p>
      {sub && <p className="mt-0.5 text-xs clinical-muted">{sub}</p>}
    </div>
  )
}

function LogItemRow({
  item,
  onOpen,
}: {
  item: ContentLogItem
  onOpen: (item: ContentLogItem) => void
}) {
  const meta = KIND_META[item.kind] ?? KIND_META.other
  const action = ACTION_META[item.action] ?? ACTION_META.updated
  const clickable = item.kind !== 'catalog' && item.action !== 'removed'

  return (
    <button
      type="button"
      disabled={!clickable}
      onClick={() => clickable && onOpen(item)}
      className={cn(
        'flex w-full items-start gap-3 rounded-lg border clinical-border p-3 text-left transition-colors',
        clickable && 'hover:bg-slate-50 dark:hover:bg-zinc-900/60',
        !clickable && 'cursor-default opacity-80',
      )}
    >
      <span className="mt-0.5 text-lg leading-none" aria-hidden>
        {meta.icon}
      </span>
      <div className="min-w-0 flex-1">
        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-[10px] font-bold uppercase tracking-wide clinical-muted">
            {item.id}
          </span>
          <span className={cn('rounded-full px-2 py-0.5 text-[10px] font-bold', action.className)}>
            {action.label}
          </span>
          {item.stats && (
            <span className="text-[10px] clinical-muted">{item.stats}</span>
          )}
        </div>
        <p className="mt-1 text-sm font-semibold leading-snug">{item.title}</p>
        {item.subtitle && (
          <p className="mt-0.5 line-clamp-2 text-xs clinical-muted">{item.subtitle}</p>
        )}
      </div>
      {clickable && (
        <ChevronRight className="mt-1 h-4 w-4 shrink-0 clinical-muted" />
      )}
    </button>
  )
}

function CommitBlock({
  entry,
  defaultOpen,
  onOpenItem,
}: {
  entry: ContentLogEntry
  defaultOpen: boolean
  onOpenItem: (item: ContentLogItem) => void
}) {
  const [open, setOpen] = useState(defaultOpen)

  return (
    <div className="rounded-xl border clinical-border bg-white/50 dark:bg-zinc-950/30">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="flex w-full items-start gap-3 p-4 text-left"
      >
        {open ? (
          <ChevronDown className="mt-0.5 h-4 w-4 shrink-0 clinical-muted" />
        ) : (
          <ChevronRight className="mt-0.5 h-4 w-4 shrink-0 clinical-muted" />
        )}
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2 text-xs clinical-muted">
            <span className="inline-flex items-center gap-1 font-mono">
              <GitCommit className="h-3 w-3" />
              {entry.commit}
            </span>
            <span>{entry.date}</span>
            {entry.items.length > 0 && (
              <span>
                {entry.items.length} module{entry.items.length === 1 ? '' : 's'}
              </span>
            )}
          </div>
          <p className="mt-1 text-sm leading-relaxed">{entry.summary}</p>
        </div>
      </button>
      {open && entry.items.length > 0 && (
        <div className="space-y-2 border-t clinical-border px-4 pb-4 pt-3">
          {entry.items.map((item) => (
            <LogItemRow key={`${entry.commit}-${item.id}`} item={item} onOpen={onOpenItem} />
          ))}
        </div>
      )}
    </div>
  )
}

function PeriodSection({
  period,
  defaultOpen,
  onOpenItem,
}: {
  period: ReturnType<typeof groupLogEntries>[number]
  defaultOpen: boolean
  onOpenItem: (item: ContentLogItem) => void
}) {
  const [open, setOpen] = useState(defaultOpen)

  return (
    <section className="clinical-card overflow-hidden">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="flex w-full items-center justify-between gap-4 p-5 text-left md:p-6"
      >
        <div>
          <p className="text-lg font-semibold">{period.label}</p>
          <p className="mt-1 text-xs clinical-muted">
            {period.startDate === period.endDate
              ? period.startDate
              : `${period.startDate} → ${period.endDate}`}
            {' · '}
            {period.commitCount} commit{period.commitCount === 1 ? '' : 's'}
            {' · '}
            {period.itemCount} module change{period.itemCount === 1 ? '' : 's'}
          </p>
        </div>
        {open ? (
          <ChevronDown className="h-5 w-5 shrink-0 clinical-muted" />
        ) : (
          <ChevronRight className="h-5 w-5 shrink-0 clinical-muted" />
        )}
      </button>
      {open && (
        <div className="space-y-3 border-t clinical-border px-4 pb-5 pt-4 md:px-6 md:pb-6">
          {period.entries.map((entry, i) => (
            <CommitBlock
              key={`${period.key}-${entry.commit}`}
              entry={entry}
              defaultOpen={i === 0 && period.entries.length <= 3}
              onOpenItem={onOpenItem}
            />
          ))}
        </div>
      )}
    </section>
  )
}

export function ContentLogDashboard() {
  const selectChapter = useAppStore((s) => s.selectChapter)
  const [log, setLog] = useState<ContentLog | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [view, setView] = useState<LogViewMode>('daily')
  const [kindFilter, setKindFilter] = useState<ContentKind | 'all'>('all')
  const [query, setQuery] = useState('')

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    fetchJSON<ContentLog>('content_log.json')
      .then((data) => {
        if (!cancelled) {
          setLog(data)
          setError(null)
        }
      })
      .catch(() => {
        if (!cancelled) setError('Could not load the content update log.')
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [])

  const filtered = useMemo(
    () => (log ? filterEntries(log.entries, kindFilter, query) : []),
    [log, kindFilter, query],
  )

  const periods = useMemo(() => groupLogEntries(filtered, view), [filtered, view])

  const generatedLabel = log
    ? new Date(log.generatedAt).toLocaleString(undefined, {
        dateStyle: 'medium',
        timeStyle: 'short',
      })
    : ''

  const openItem = (item: ContentLogItem) => {
    if (item.kind === 'calculator' && item.file) {
      window.open(`${BASE}${item.file}`, '_blank', 'noopener,noreferrer')
      return
    }
    if (item.id && item.kind !== 'catalog') {
      void selectChapter(item.id)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center gap-2 py-20 clinical-muted">
        <Loader2 className="h-5 w-5 animate-spin" />
        <span className="text-sm">Loading content log…</span>
      </div>
    )
  }

  if (error || !log) {
    return (
      <div className="clinical-card p-8 text-center">
        <p className="text-sm clinical-muted">{error ?? 'Log unavailable.'}</p>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="clinical-card border-l-4 border-l-teal-500 p-5 md:p-6">
        <div className="flex items-center gap-2 text-teal-700 dark:text-teal-300">
          <Clock className="h-4 w-4" />
          <p className="text-xs font-bold uppercase tracking-wider">Content update log</p>
        </div>
        <p className="mt-2 text-sm leading-relaxed clinical-muted">{log.description}</p>
        <p className="mt-2 text-xs clinical-muted">
          Last generated {generatedLabel} · {log.totalCommits} commits · {log.totalModules} unique
          modules tracked
        </p>
      </div>

      <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
        <StatTile label="This week" value={String(countRecent(log.entries, 7))} sub="commits" />
        <StatTile label="This month" value={String(countRecent(log.entries, 30))} sub="commits" />
        <StatTile label="Total commits" value={String(log.totalCommits)} />
        <StatTile label="Unique modules" value={String(log.totalModules)} />
      </div>

      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex flex-wrap gap-1.5">
          {VIEW_OPTIONS.map(({ mode, label, icon: Icon }) => (
            <button
              key={mode}
              type="button"
              onClick={() => setView(mode)}
              className={cn(
                'inline-flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-semibold transition-colors',
                view === mode
                  ? 'bg-teal-600 text-white shadow-sm'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
              )}
            >
              <Icon className="h-4 w-4" />
              {label}
            </button>
          ))}
        </div>

        <div className="relative min-w-[200px] flex-1 sm:max-w-xs">
          <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 clinical-muted" />
          <input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search modules or commits…"
            className="w-full rounded-lg border clinical-border bg-transparent py-2 pl-9 pr-3 text-sm outline-none focus:ring-2 focus:ring-teal-500/40"
          />
        </div>
      </div>

      <div className="flex flex-wrap gap-1.5">
        {KIND_FILTERS.map(({ value, label }) => (
          <button
            key={value}
            type="button"
            onClick={() => setKindFilter(value)}
            className={cn(
              'rounded-full px-3 py-1 text-xs font-semibold transition-colors',
              kindFilter === value
                ? 'bg-teal-600 text-white'
                : 'bg-slate-100 text-slate-600 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-300 dark:hover:bg-zinc-700',
            )}
          >
            {label}
          </button>
        ))}
      </div>

      {periods.length === 0 ? (
        <div className="clinical-card p-8 text-center text-sm clinical-muted">
          No updates match your filters.
        </div>
      ) : (
        <div className="space-y-4">
          {periods.map((period, i) => (
            <PeriodSection
              key={period.key}
              period={period}
              defaultOpen={i < 3}
              onOpenItem={openItem}
            />
          ))}
        </div>
      )}
    </div>
  )
}
