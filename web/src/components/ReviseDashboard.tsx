import { type ReactNode, useEffect } from 'react'
import { Brain, CalendarClock, Clock, Flame, Target, Timer, TrendingUp } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { RevisionMode } from '@/components/RevisionMode'
import { formatTimeToReveal } from '@/lib/timeToReveal'
import { cn } from '@/lib/utils'

function formatDuration(ms: number): string {
  if (ms < 60_000) return `${Math.round(ms / 1000)}s`
  const mins = Math.floor(ms / 60_000)
  const secs = Math.round((ms % 60_000) / 1000)
  return secs > 0 ? `${mins}m ${secs}s` : `${mins}m`
}

function StatCard({
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
      <div className="flex items-center gap-2 text-amber-700 dark:text-amber-300">
        {icon}
        <span className="text-[10px] font-bold uppercase tracking-wider">{label}</span>
      </div>
      <p className="mt-2 text-2xl font-bold tabular-nums">{value}</p>
      {sub && <p className="mt-0.5 text-xs clinical-muted">{sub}</p>}
    </div>
  )
}

function HealthBar({ percent, label }: { percent: number; label: string }) {
  const color =
    percent >= 70 ? 'bg-emerald-500' : percent >= 40 ? 'bg-amber-500' : 'bg-red-500'
  return (
    <div>
      <div className="mb-1 flex items-center justify-between text-xs">
        <span className="truncate font-medium">{label}</span>
        <span className="shrink-0 tabular-nums clinical-muted">{percent}%</span>
      </div>
      <div className="h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-zinc-800">
        <div
          className={cn('h-full rounded-full transition-all duration-300', color)}
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  )
}

function BucketBar({
  label,
  count,
  total,
  color,
}: {
  label: string
  count: number
  total: number
  color: string
}) {
  const pct = total > 0 ? Math.round((count / total) * 100) : 0
  return (
    <div>
      <div className="mb-1 flex items-center justify-between text-xs">
        <span className="font-medium">{label}</span>
        <span className="tabular-nums clinical-muted">
          {count} {total > 0 ? `(${pct}%)` : ''}
        </span>
      </div>
      <div className="h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-zinc-800">
        <div
          className={cn('h-full rounded-full transition-all duration-300', color)}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  )
}

/** Seven-day view of upcoming review load (overdue rolls into Today). */
function ForecastStrip() {
  const getForecast = useRevisionStore((s) => s.getForecast)
  const days = getForecast(7)
  const max = Math.max(1, ...days.map((d) => d.count))
  const totalUpcoming = days.reduce((n, d) => n + d.count, 0)

  if (totalUpcoming === 0) return null

  return (
    <section className="clinical-card p-5 md:p-6">
      <div className="flex items-center gap-2">
        <CalendarClock className="h-4 w-4 text-amber-600" />
        <h3 className="text-sm font-bold">7-day forecast</h3>
      </div>
      <p className="mt-1 text-xs clinical-muted">
        Scheduled reviews per day — overdue cards count toward Today.
      </p>
      <div className="mt-4 flex items-end justify-between gap-2">
        {days.map((d, i) => {
          const heightPct = d.count > 0 ? Math.max(8, Math.round((d.count / max) * 100)) : 0
          const isToday = i === 0
          return (
            <div key={d.date} className="flex min-w-0 flex-1 flex-col items-center gap-1">
              <span className="text-[11px] font-bold tabular-nums">
                {d.count > 0 ? d.count : ''}
              </span>
              <div className="flex h-20 w-full items-end">
                <div
                  className={cn(
                    'w-full rounded-t-md transition-all',
                    d.count === 0
                      ? 'bg-slate-100 dark:bg-zinc-800'
                      : isToday
                        ? 'bg-amber-500'
                        : 'bg-amber-300 dark:bg-amber-500/50',
                  )}
                  style={{ height: d.count === 0 ? '3px' : `${heightPct}%` }}
                  title={`${d.count} due ${d.label}${d.overdue ? ` · ${d.overdue} overdue` : ''}`}
                />
              </div>
              <span
                className={cn(
                  'truncate text-[10px]',
                  isToday ? 'font-bold text-amber-700 dark:text-amber-300' : 'clinical-muted',
                )}
              >
                {d.label}
              </span>
            </div>
          )
        })}
      </div>
    </section>
  )
}

/** Revise landing: Revision Mode + session stats + subject health. */
export function ReviseDashboard() {
  const marks = useAppStore((s) => s.marks)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const getDueCount = useRevisionStore((s) => s.getDueCount)
  const getSubjectSummary = useRevisionStore((s) => s.getSubjectSummary)
  const getTodayStats = useRevisionStore((s) => s.getTodayStats)
  const getTodayTimeToRevealStats = useRevisionStore((s) => s.getTodayTimeToRevealStats)

  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  const dueCount = getDueCount()
  const today = getTodayStats()
  const revealToday = getTodayTimeToRevealStats()
  const subjects = getSubjectSummary()

  return (
    <div className="space-y-6">
      <RevisionMode />

      <ForecastStrip />

      <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
        <StatCard
          icon={<Target className="h-4 w-4" />}
          label="Reviewed today"
          value={String(today.reviewed)}
        />
        <StatCard
          icon={<TrendingUp className="h-4 w-4" />}
          label="Avg rating"
          value={today.avgRating > 0 ? today.avgRating.toFixed(1) : '—'}
          sub="0 blackout · 5 perfect"
        />
        <StatCard
          icon={<Clock className="h-4 w-4" />}
          label="Session time"
          value={today.sessionMs > 0 ? formatDuration(today.sessionMs) : '—'}
        />
        <StatCard
          icon={<Flame className="h-4 w-4" />}
          label="Streak"
          value={`${today.streak}d`}
          sub={dueCount > 0 ? `${dueCount} due now` : 'All caught up'}
        />
      </div>

      {revealToday.count > 0 && (
        <section className="clinical-card p-5 md:p-6">
          <div className="flex items-center gap-2">
            <Timer className="h-4 w-4 text-amber-600" />
            <h3 className="text-sm font-bold">Time to reveal today</h3>
          </div>
          <p className="mt-1 text-xs clinical-muted">
            Pre-answer fluency — stats only, does not affect scheduling.
          </p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            <div>
              <p className="text-[10px] font-bold uppercase tracking-wider clinical-muted">
                Average
              </p>
              <p className="mt-1 text-2xl font-bold tabular-nums">
                {formatTimeToReveal(revealToday.avgMs)}
              </p>
              <p className="text-xs clinical-muted">{revealToday.count} reveals</p>
            </div>
            <div className="space-y-3">
              <BucketBar
                label="< 10s"
                count={revealToday.buckets.under10s}
                total={revealToday.count}
                color="bg-emerald-500"
              />
              <BucketBar
                label="10–30s"
                count={revealToday.buckets.s10to30}
                total={revealToday.count}
                color="bg-amber-500"
              />
              <BucketBar
                label="30–120s"
                count={revealToday.buckets.s30to120}
                total={revealToday.count}
                color="bg-orange-500"
              />
            </div>
          </div>
        </section>
      )}

      {subjects.length > 0 && (
        <section className="clinical-card p-5 md:p-6">
          <div className="flex items-center gap-2">
            <Brain className="h-4 w-4 text-amber-600" />
            <h3 className="text-sm font-bold">Subject health</h3>
          </div>
          <p className="mt-1 text-xs clinical-muted">
            Average RPS by chapter group — lower is healthier.
          </p>
          <div className="mt-4 space-y-4">
            {subjects.map((s) => (
              <div key={s.subject}>
                <HealthBar percent={s.healthPercent} label={s.subject} />
                <p className="mt-1 text-[10px] clinical-muted">
                  {s.itemCount} items · avg RPS {s.avgRps}
                  {s.criticalCount > 0 && ` · ${s.criticalCount} critical`}
                </p>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
