import { useMemo, type ReactNode } from 'react'
import { Activity, BarChart3, BookOpen, Bug, Clock, Layers, LineChart, Target } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { formatStudyDuration } from '@/lib/studyProgress'
import {
  accuracyTrend,
  findLeeches,
  retentionByInterval,
  summarize,
} from '@/lib/revisionAnalytics'
import { StudyAccountPanel } from '@/components/StudyAccountPanel'
import { cn } from '@/lib/utils'
import type { HeaderKind } from '@/lib/types'

function retentionColor(percent: number): string {
  return percent >= 80 ? 'bg-emerald-500' : percent >= 50 ? 'bg-amber-500' : 'bg-red-500'
}

const SECTION_ICON: Partial<Record<HeaderKind, string>> = {
  hot_topics: '🔥',
  case_reports: '📋',
  pediatric_endo: '🧒',
  stories: '💬',
  calculators: '🧮',
  imaging_resources: '🩻',
  trials: '📊',
  harrison_banner: '📖',
}

function ProgressBar({ percent, className }: { percent: number; className?: string }) {
  const color =
    percent >= 80 ? 'bg-emerald-500' : percent >= 40 ? 'bg-amber-500' : 'bg-slate-400'
  return (
    <div className={cn('h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-zinc-800', className)}>
      <div
        className={cn('h-full rounded-full transition-all duration-300', color)}
        style={{ width: `${Math.min(100, percent)}%` }}
      />
    </div>
  )
}

function StatTile({
  icon,
  label,
  value,
  sub,
}: {
  icon: ReactNode
  label: string
  value: string
  sub?: string
}) {
  return (
    <div className="clinical-card p-4">
      <div className="flex items-center gap-2 text-indigo-700 dark:text-indigo-300">
        {icon}
        <span className="text-[10px] font-bold uppercase tracking-wider">{label}</span>
      </div>
      <p className="mt-2 text-2xl font-bold tabular-nums">{value}</p>
      {sub && <p className="mt-0.5 text-xs clinical-muted">{sub}</p>}
    </div>
  )
}

/** Spaced-repetition analytics: retention, accuracy trend, and leeches. */
function RevisionAnalytics() {
  const reviews = useRevisionStore((s) => s.reviews)
  const items = useRevisionStore((s) => s.items)
  const selectChapter = useAppStore((s) => s.selectChapter)

  const { summary, trend, curve, leeches } = useMemo(
    () => ({
      summary: summarize(reviews),
      trend: accuracyTrend(reviews, 14),
      curve: retentionByInterval(reviews),
      leeches: findLeeches(items),
    }),
    [reviews, items],
  )

  if (summary.total === 0) return null

  const trendMax = Math.max(1, ...trend.map((d) => d.total))

  return (
    <section className="space-y-4">
      <div className="clinical-card border-l-4 border-l-indigo-500 p-5 md:p-6">
        <div className="flex items-center gap-2 text-indigo-700 dark:text-indigo-300">
          <Activity className="h-4 w-4" />
          <p className="text-xs font-bold uppercase tracking-wider">Revision analytics</p>
        </div>
        <p className="mt-1 text-xs clinical-muted">
          Recall performance from your triage reviews. A “pass” is rating ≥ 3.
        </p>

        <div className="mt-4 grid grid-cols-3 gap-3">
          <StatTile
            icon={<Target className="h-4 w-4" />}
            label="Retention"
            value={`${summary.percent}%`}
            sub={`${summary.correct}/${summary.total} passed`}
          />
          <StatTile
            icon={<LineChart className="h-4 w-4" />}
            label="Reviews"
            value={String(summary.total)}
          />
          <StatTile
            icon={<Bug className="h-4 w-4" />}
            label="Leeches"
            value={String(leeches.length)}
            sub="≥4 lapses"
          />
        </div>
      </div>

      {/* Accuracy over time */}
      <div className="clinical-card p-5 md:p-6">
        <h4 className="text-sm font-bold">Accuracy — last 14 days</h4>
        <p className="mt-1 text-xs clinical-muted">Daily pass rate; bar height scales with review volume.</p>
        <div className="mt-4 flex items-end justify-between gap-1">
          {trend.map((d) => {
            const h = d.total > 0 ? Math.max(10, Math.round((d.total / trendMax) * 100)) : 0
            return (
              <div key={d.date} className="flex min-w-0 flex-1 flex-col items-center gap-1">
                <div className="flex h-20 w-full items-end">
                  <div
                    className={cn(
                      'w-full rounded-t-md transition-all',
                      d.total === 0 ? 'bg-slate-100 dark:bg-zinc-800' : retentionColor(d.percent),
                    )}
                    style={{ height: d.total === 0 ? '3px' : `${h}%` }}
                    title={
                      d.total === 0
                        ? `${d.date}: no reviews`
                        : `${d.date}: ${d.correct}/${d.total} passed (${d.percent}%)`
                    }
                  />
                </div>
                <span
                  className={cn(
                    'truncate text-[9px]',
                    d.label === 'Today'
                      ? 'font-bold text-indigo-700 dark:text-indigo-300'
                      : 'clinical-muted',
                  )}
                >
                  {d.label}
                </span>
              </div>
            )
          })}
        </div>
      </div>

      {/* Retention curve by interval */}
      <div className="clinical-card p-5 md:p-6">
        <h4 className="text-sm font-bold">Retention by interval</h4>
        <p className="mt-1 text-xs clinical-muted">
          How well recall holds as scheduled gaps grow — your forgetting curve.
        </p>
        <div className="mt-4 space-y-3">
          {curve.map((b) => (
            <div key={b.band}>
              <div className="mb-1 flex items-center justify-between text-xs">
                <span className="font-medium tabular-nums">{b.band}</span>
                <span className="tabular-nums clinical-muted">
                  {b.total > 0 ? `${b.percent}% · ${b.correct}/${b.total}` : 'no reviews'}
                </span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-zinc-800">
                <div
                  className={cn('h-full rounded-full transition-all', retentionColor(b.percent))}
                  style={{ width: `${b.total > 0 ? b.percent : 0}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Leeches */}
      {leeches.length > 0 && (
        <div className="clinical-card p-5 md:p-6">
          <div className="flex items-center gap-2">
            <Bug className="h-4 w-4 text-red-600 dark:text-red-400" />
            <h4 className="text-sm font-bold">Leeches</h4>
          </div>
          <p className="mt-1 text-xs clinical-muted">
            Chronically failed cards (≥4 lapses) — consider reformulating or simplifying these.
          </p>
          <div className="mt-4 space-y-2">
            {leeches.slice(0, 15).map((item) => (
              <button
                key={item.id}
                type="button"
                onClick={() => selectChapter(item.chapterId)}
                className="flex w-full items-center gap-3 rounded-lg border border-red-200/60 bg-red-50/40 px-3 py-2 text-left transition-colors hover:bg-red-50 dark:border-red-500/25 dark:bg-red-500/10 dark:hover:bg-red-500/15"
              >
                <span className="shrink-0 rounded-full bg-red-100 px-2 py-0.5 text-[10px] font-bold tabular-nums text-red-700 dark:bg-red-950/50 dark:text-red-300">
                  {item.lapseCount}× lapsed
                </span>
                <div className="min-w-0 flex-1">
                  <p className="truncate text-sm font-medium">{item.title}</p>
                  <p className="truncate text-[11px] clinical-muted">{item.subject}</p>
                </div>
                <span className="shrink-0 text-[10px] tabular-nums clinical-muted">
                  {item.reviewCount} reviews
                </span>
              </button>
            ))}
            {leeches.length > 15 && (
              <p className="px-2 text-[10px] clinical-muted">+{leeches.length - 15} more</p>
            )}
          </div>
        </div>
      )}
    </section>
  )
}

export function StudyProgressDashboard() {
  const getStudyProgress = useAppStore((s) => s.getStudyProgress)
  const selectChapter = useAppStore((s) => s.selectChapter)

  const { overall, sections } = useMemo(() => getStudyProgress(), [getStudyProgress])

  const hasAny =
    overall.completed > 0 || overall.engagedMs > 0 || sections.some((s) => s.completed > 0)

  if (!hasAny) {
    return (
      <div className="space-y-6">
        <StudyAccountPanel />
        <div className="clinical-card p-8 text-center">
          <BarChart3 className="mx-auto h-10 w-10 text-indigo-600 dark:text-indigo-400" />
          <h2 className="mt-4 text-lg font-semibold">No study progress yet</h2>
          <p className="clinical-serif mx-auto mt-2 max-w-md text-[15px] leading-relaxed clinical-muted">
            Progress counts when you <strong>reveal an answer</strong>, <strong>solve a question</strong>,{' '}
            <strong>mark an item</strong>, or tap <strong>Mark as read</strong> on notes — not from scrolling
            alone. Register a study account above to keep stats after reinstall.
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <StudyAccountPanel />
      <div className="clinical-card border-l-4 border-l-indigo-500 p-5 md:p-6">
        <p className="text-xs font-bold uppercase tracking-wider text-indigo-700 dark:text-indigo-300">
          Overall
        </p>
        <div className="mt-3 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="text-3xl font-bold tabular-nums">{overall.percent}%</p>
            <p className="mt-1 text-sm clinical-muted">
              {overall.completed} of {overall.total} items engaged
            </p>
            <p className="text-xs clinical-muted">
              {overall.chaptersComplete} chapters complete · {overall.chaptersStarted} started
            </p>
          </div>
          <div className="md:min-w-[240px] md:flex-1">
            <ProgressBar percent={overall.percent} />
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 md:grid-cols-3">
        <StatTile
          icon={<BookOpen className="h-4 w-4" />}
          label="Items engaged"
          value={`${overall.completed}/${overall.total}`}
        />
        <StatTile
          icon={<Layers className="h-4 w-4" />}
          label="Sections active"
          value={String(sections.filter((s) => s.completed > 0).length)}
          sub={`of ${sections.length} with loaded totals`}
        />
        <StatTile
          icon={<Clock className="h-4 w-4" />}
          label="Engaged time"
          value={formatStudyDuration(overall.engagedMs)}
          sub="Actions + bounded read dwell"
        />
      </div>

      <section className="space-y-4">
        <h3 className="px-1 text-sm font-bold">By section</h3>
        {sections.map((section) => (
          <div key={section.key} className="clinical-card p-4 md:p-5">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <span aria-hidden>{SECTION_ICON[section.kind] ?? '📚'}</span>
                <h4 className="font-semibold">{section.title}</h4>
              </div>
              <span className="text-sm tabular-nums clinical-muted">
                {section.completed}/{section.total} · {section.percent}% ·{' '}
                {formatStudyDuration(section.engagedMs)}
              </span>
            </div>
            <ProgressBar percent={section.percent} className="mt-3" />

            {section.chapters.filter((c) => c.total > 0 || c.completed > 0).length > 0 && (
              <div className="mt-4 space-y-2 border-t clinical-border pt-3">
                {section.chapters
                  .filter((c) => c.total > 0 || c.completed > 0)
                  .slice(0, 12)
                  .map((ch) => (
                    <button
                      key={ch.id}
                      type="button"
                      onClick={() => selectChapter(ch.id)}
                      className="flex w-full items-center gap-3 rounded-lg px-2 py-1.5 text-left transition-colors hover:bg-slate-50 dark:hover:bg-zinc-800/60"
                    >
                      <div className="min-w-0 flex-1">
                        <p className="truncate text-sm">{ch.title}</p>
                        <ProgressBar percent={ch.percent} className="mt-1.5" />
                      </div>
                      <span className="shrink-0 text-xs tabular-nums clinical-muted">
                        {ch.completed}/{ch.total}
                      </span>
                    </button>
                  ))}
                {section.chapters.filter((c) => c.total > 0).length > 12 && (
                  <p className="px-2 text-[10px] clinical-muted">
                    +{section.chapters.filter((c) => c.total > 0).length - 12} more chapters
                  </p>
                )}
              </div>
            )}
          </div>
        ))}
      </section>

      <p className="px-1 text-[11px] leading-relaxed clinical-muted">
        Engaged time = base credit per action (reveal 45s, answer 60s, mark 30s, read 75s) plus up to
        90s dwell per item while it stays in view after you engage. Scrolling without engaging awards
        nothing.
      </p>

      <RevisionAnalytics />
    </div>
  )
}
