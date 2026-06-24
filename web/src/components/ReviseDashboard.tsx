import { type ReactNode, useEffect } from 'react'
import { Brain, Clock, Flame, Target, TrendingUp } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { RevisionMode } from '@/components/RevisionMode'
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

/** Revise landing: Revision Mode + session stats + subject health. */
export function ReviseDashboard() {
  const marks = useAppStore((s) => s.marks)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const getDueCount = useRevisionStore((s) => s.getDueCount)
  const getSubjectSummary = useRevisionStore((s) => s.getSubjectSummary)
  const getTodayStats = useRevisionStore((s) => s.getTodayStats)

  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  const dueCount = getDueCount()
  const today = getTodayStats()
  const subjects = getSubjectSummary()

  return (
    <div className="space-y-6">
      <RevisionMode />

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
