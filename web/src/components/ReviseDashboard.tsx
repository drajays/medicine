import { type ReactNode, useEffect, useState } from 'react'
import {
  Brain,
  Clock,
  Flame,
  Play,
  Target,
  TrendingUp,
  Zap,
} from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { SmartTriageModal } from '@/components/SmartTriageModal'
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
    percent >= 70
      ? 'bg-emerald-500'
      : percent >= 40
        ? 'bg-amber-500'
        : 'bg-red-500'

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

export function ReviseDashboard() {
  const marks = useAppStore((s) => s.marks)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const startTriage = useRevisionStore((s) => s.startTriage)
  const getCriticalCount = useRevisionStore((s) => s.getCriticalCount)
  const getDueCount = useRevisionStore((s) => s.getDueCount)
  const getSubjectSummary = useRevisionStore((s) => s.getSubjectSummary)
  const getTodayStats = useRevisionStore((s) => s.getTodayStats)
  const getPrioritized = useRevisionStore((s) => s.getPrioritized)
  const items = useRevisionStore((s) => s.items)

  const [triageOpen, setTriageOpen] = useState(false)

  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  const criticalCount = getCriticalCount()
  const dueCount = getDueCount()
  const today = getTodayStats()
  const subjects = getSubjectSummary()
  const itemCount = Object.keys(items).length
  const topItems = getPrioritized(5)

  const handleStartTriage = () => {
    startTriage()
    setTriageOpen(true)
  }

  if (itemCount === 0) {
    return (
      <div className="clinical-card p-8 text-center">
        <Brain className="mx-auto h-10 w-10 text-amber-600 dark:text-amber-400" />
        <h2 className="mt-4 text-lg font-semibold">Revision Engine ready</h2>
        <p className="clinical-serif mx-auto mt-2 max-w-md text-[15px] leading-relaxed clinical-muted">
          Open any chapter and mark items <strong>Revise</strong> or <strong>Doubt</strong> using the
          marks bar under each item. The engine will score them with RPS and surface the highest-priority
          items in Smart Triage.
        </p>
      </div>
    )
  }

  return (
    <>
      <div className="space-y-6">
        {/* Hero CTA */}
        <div className="clinical-card relative overflow-hidden border-l-4 border-l-amber-500 p-6 md:p-8">
          <div className="relative z-10 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-amber-700 dark:text-amber-300">
                Glassbox Revision Engine v2
              </p>
              <h2 className="mt-1 text-xl font-semibold md:text-2xl">Smart Triage</h2>
              <p className="clinical-serif mt-2 max-w-lg text-sm leading-relaxed clinical-muted">
                FSRS-inspired scheduling ranks your flagged items by Revision Priority Score — time
                pressure, stability, difficulty, lapses, and hazard clusters.
              </p>
            </div>
            <button
              type="button"
              onClick={handleStartTriage}
              className="inline-flex shrink-0 items-center justify-center gap-2 rounded-xl bg-amber-600 px-6 py-3.5 text-sm font-bold text-white shadow-md transition-all hover:bg-amber-700 hover:shadow-lg active:scale-[0.98]"
            >
              <Play className="h-4 w-4 fill-current" />
              Start triage
              {criticalCount > 0 && (
                <span className="rounded-full bg-white/25 px-2 py-0.5 text-xs font-bold tabular-nums">
                  {criticalCount} critical
                </span>
              )}
            </button>
          </div>
          <Zap
            className="pointer-events-none absolute -right-4 -top-4 h-32 w-32 text-amber-500/10"
            aria-hidden
          />
        </div>

        {/* Today stats */}
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

        {/* Subject health */}
        {subjects.length > 0 && (
          <section className="clinical-card p-5 md:p-6">
            <h3 className="text-sm font-bold">Subject health</h3>
            <p className="mt-1 text-xs clinical-muted">
              Lower average RPS and fewer critical items → higher health bar.
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

        {/* Priority queue preview */}
        {topItems.length > 0 && (
          <section className="clinical-card p-5 md:p-6">
            <h3 className="text-sm font-bold">Top priority queue</h3>
            <div className="mt-3 space-y-2">
              {topItems.map(({ item, breakdown }, i) => (
                <div
                  key={item.id}
                  className="flex items-center gap-3 rounded-lg border clinical-border px-3 py-2.5"
                >
                  <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-bold text-amber-800 dark:bg-amber-950/50 dark:text-amber-200">
                    {i + 1}
                  </span>
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{item.title}</p>
                    <p className="truncate text-[10px] clinical-muted">{item.subject}</p>
                  </div>
                  <div className="shrink-0 text-right">
                    <p className="text-sm font-bold tabular-nums text-amber-700 dark:text-amber-300">
                      {breakdown.rps}
                    </p>
                    <p className="text-[9px] uppercase clinical-muted">RPS</p>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}
      </div>

      <SmartTriageModal open={triageOpen} onClose={() => setTriageOpen(false)} />
    </>
  )
}
