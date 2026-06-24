import { useEffect, useMemo, useState } from 'react'
import { Play, Sparkles } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { SmartTriageModal } from '@/components/SmartTriageModal'
import {
  REVISION_MODES,
  buildRevisionQueue,
  computeSmartScore,
  countForPreset,
  type RevisionModePreset,
} from '@/lib/revisionQueue'
import { cn } from '@/lib/utils'

const SESSION_SIZES = [15, 25, 40] as const

export function RevisionMode() {
  const marks = useAppStore((s) => s.marks)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const getPrioritized = useRevisionStore((s) => s.getPrioritized)
  const startRevisionMode = useRevisionStore((s) => s.startRevisionMode)
  const items = useRevisionStore((s) => s.items)

  const [preset, setPreset] = useState<RevisionModePreset>('smart')
  const [limit, setLimit] = useState<number>(25)
  const [sessionOpen, setSessionOpen] = useState(false)

  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  const allEntries = useMemo(() => getPrioritized(), [getPrioritized, items])
  const queue = useMemo(
    () => buildRevisionQueue(allEntries, { preset, limit }),
    [allEntries, preset, limit],
  )

  const itemCount = Object.keys(items).length
  const selectedMeta = REVISION_MODES.find((m) => m.preset === preset)!

  const handleStart = () => {
    if (!queue.length) return
    startRevisionMode({ preset, limit })
    setSessionOpen(true)
  }

  if (itemCount === 0) {
    return (
      <div className="clinical-card p-8 text-center">
        <Sparkles className="mx-auto h-10 w-10 text-amber-600 dark:text-amber-400" />
        <h2 className="mt-4 text-lg font-semibold">Revision Mode</h2>
        <p className="clinical-serif mx-auto mt-2 max-w-md text-[15px] leading-relaxed clinical-muted">
          Mark items while studying — <strong>Revise</strong>, <strong>Doubt</strong>,{' '}
          <strong>Tough</strong>, <strong>Guessed</strong>, <strong>Concept gap</strong>, or{' '}
          <strong>Important</strong>. The engine turns your tags into a ranked revision queue.
        </p>
      </div>
    )
  }

  return (
    <>
      <div className="space-y-5">
        <div className="clinical-card border-l-4 border-l-amber-500 p-5 md:p-6">
          <p className="text-xs font-bold uppercase tracking-wider text-amber-700 dark:text-amber-300">
            Revision Mode
          </p>
          <h2 className="mt-1 text-xl font-semibold">Build your best session</h2>
          <p className="clinical-serif mt-2 max-w-2xl text-sm leading-relaxed clinical-muted">
            Combines your study marks with the RPS auto-scheduler to pick what to review next.
            Choose a strategy, preview the queue, then start.
          </p>
        </div>

        {/* Mode picker */}
        <div className="grid grid-cols-1 gap-2 sm:grid-cols-2 lg:grid-cols-3">
          {REVISION_MODES.map((mode) => {
            const count = countForPreset(allEntries, mode.preset)
            const active = preset === mode.preset
            return (
              <button
                key={mode.preset}
                type="button"
                onClick={() => setPreset(mode.preset)}
                className={cn(
                  'clinical-card p-4 text-left transition-all',
                  active
                    ? 'ring-2 ring-amber-500 ring-offset-2 ring-offset-[var(--color-clinical-bg-light)] dark:ring-offset-[var(--color-clinical-bg-dark)]'
                    : 'hover:-translate-y-0.5 hover:shadow-md',
                )}
              >
                <div className="flex items-start justify-between gap-2">
                  <span className="text-xl" aria-hidden>
                    {mode.emoji}
                  </span>
                  <span
                    className={cn(
                      'rounded-full px-2 py-0.5 text-[10px] font-bold tabular-nums',
                      active
                        ? 'bg-amber-500 text-white'
                        : 'bg-slate-100 text-slate-600 dark:bg-zinc-800 dark:text-zinc-300',
                    )}
                  >
                    {count}
                  </span>
                </div>
                <p className="mt-2 text-sm font-semibold">{mode.title}</p>
                <p className="mt-1 text-xs leading-relaxed clinical-muted">{mode.description}</p>
              </button>
            )
          })}
        </div>

        {/* Session size */}
        <div className="flex flex-wrap items-center gap-3">
          <span className="text-xs font-bold uppercase tracking-wider clinical-muted">
            Session size
          </span>
          {SESSION_SIZES.map((n) => (
            <button
              key={n}
              type="button"
              onClick={() => setLimit(n)}
              className={cn(
                'rounded-full border px-3 py-1 text-xs font-semibold tabular-nums transition-colors',
                limit === n
                  ? 'border-amber-500 bg-amber-500 text-white'
                  : 'clinical-border clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
              )}
            >
              {n} items
            </button>
          ))}
        </div>

        {/* Queue preview */}
        <section className="clinical-card p-5 md:p-6">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div>
              <h3 className="text-sm font-bold">
                Queue preview — {selectedMeta.title}
              </h3>
              <p className="mt-0.5 text-xs clinical-muted">
                {queue.length} of {countForPreset(allEntries, preset)} eligible · top {limit}{' '}
                selected
              </p>
            </div>
            <button
              type="button"
              onClick={handleStart}
              disabled={queue.length === 0}
              className="inline-flex items-center gap-2 rounded-xl bg-amber-600 px-5 py-2.5 text-sm font-bold text-white shadow-md transition-all hover:bg-amber-700 disabled:cursor-not-allowed disabled:opacity-50"
            >
              <Play className="h-4 w-4 fill-current" />
              Start revision mode
            </button>
          </div>

          {queue.length === 0 ? (
            <p className="mt-4 text-sm clinical-muted">
              No items match this mode. Try <strong>All Flagged</strong> or add more study marks.
            </p>
          ) : (
            <ol className="mt-4 space-y-2">
              {queue.map(({ item, breakdown }, i) => (
                <li
                  key={item.id}
                  className="flex items-center gap-3 rounded-lg border clinical-border px-3 py-2.5"
                >
                  <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-bold text-amber-800 dark:bg-amber-950/50 dark:text-amber-200">
                    {i + 1}
                  </span>
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{item.title}</p>
                    <div className="mt-0.5 flex flex-wrap gap-1">
                      {item.tags.slice(0, 4).map((t) => (
                        <span
                          key={t}
                          className="rounded bg-slate-100 px-1.5 py-0.5 text-[9px] font-semibold uppercase text-slate-600 dark:bg-zinc-800 dark:text-zinc-400"
                        >
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>
                  <div className="shrink-0 text-right">
                    <p className="text-sm font-bold tabular-nums text-amber-700 dark:text-amber-300">
                      {preset === 'smart' ? computeSmartScore({ item, breakdown }) : breakdown.rps}
                    </p>
                    <p className="text-[9px] uppercase clinical-muted">
                      {preset === 'smart' ? 'score' : 'RPS'}
                    </p>
                  </div>
                </li>
              ))}
            </ol>
          )}
        </section>
      </div>

      <SmartTriageModal open={sessionOpen} onClose={() => setSessionOpen(false)} />
    </>
  )
}
