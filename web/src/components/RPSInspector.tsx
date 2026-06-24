import { ChevronDown, ChevronUp, Microscope } from 'lucide-react'
import { useState } from 'react'
import { useRevisionStore } from '@/stores/revisionStore'
import {
  TIME_TO_REVEAL_CAP_MS,
  formatTimeToReveal,
} from '@/lib/timeToReveal'
import { cn } from '@/lib/utils'
import type { RPSBreakdown } from '@/lib/revision-math'

interface RPSInspectorProps {
  breakdown: RPSBreakdown
  itemId?: string
  className?: string
  defaultOpen?: boolean
}

function Row({ label, value, detail }: { label: string; value: string; detail?: string }) {
  return (
    <div className="flex items-baseline justify-between gap-3 text-xs">
      <span className="clinical-muted">{label}</span>
      <div className="text-right">
        <span className="font-semibold tabular-nums">{value}</span>
        {detail && <p className="mt-0.5 text-[10px] clinical-muted">{detail}</p>}
      </div>
    </div>
  )
}

export function RPSInspector({
  breakdown,
  itemId,
  className,
  defaultOpen = true,
}: RPSInspectorProps) {
  const [open, setOpen] = useState(defaultOpen)
  const revealStats = useRevisionStore((s) =>
    itemId ? s.getItemRevealStats(itemId) : null,
  )

  return (
    <div className={cn('clinical-card overflow-hidden', className)}>
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-2 px-4 py-3 text-left transition-colors hover:bg-slate-50/80 dark:hover:bg-zinc-800/50"
      >
        <Microscope className="h-4 w-4 shrink-0 text-amber-600 dark:text-amber-400" />
        <span className="text-sm font-semibold">RPS Inspector</span>
        <span className="ml-auto rounded-full bg-amber-100 px-2 py-0.5 text-xs font-bold tabular-nums text-amber-800 dark:bg-amber-950/50 dark:text-amber-200">
          {breakdown.rps}
        </span>
        {open ? (
          <ChevronUp className="h-4 w-4 clinical-muted" />
        ) : (
          <ChevronDown className="h-4 w-4 clinical-muted" />
        )}
      </button>

      {open && (
        <div className="space-y-4 border-t clinical-border px-4 py-4">
          {revealStats && revealStats.reviewCount > 0 && (
            <section className="space-y-2 rounded-lg bg-slate-50 px-3 py-3 dark:bg-zinc-900/60">
              <p className="text-[10px] font-bold uppercase tracking-wider clinical-muted">
                Time to reveal (fluency)
              </p>
              <Row
                label="Last reveal"
                value={formatTimeToReveal(revealStats.lastMs)}
                detail={`Capped at ${TIME_TO_REVEAL_CAP_MS / 1000}s`}
              />
              <Row
                label="Rolling avg (last 5)"
                value={formatTimeToReveal(revealStats.rollingAvgMs)}
                detail={`${revealStats.reviewCount} review${revealStats.reviewCount === 1 ? '' : 's'} on record`}
              />
              <p className="text-[10px] leading-relaxed clinical-muted">
                Stats only — does not change RPS or FSRS intervals.
              </p>
            </section>
          )}

          <section className="space-y-2">
            <p className="text-[10px] font-bold uppercase tracking-wider clinical-muted">
              Additive score
            </p>
            {breakdown.tagContributions.length === 0 ? (
              <p className="text-xs clinical-muted">No tags — base urgency from scheduling only.</p>
            ) : (
              <div className="space-y-1">
                {breakdown.tagContributions.map((t) => (
                  <Row key={t.tag} label={t.tag} value={`+${t.weight}`} />
                ))}
                <Row label="Tag subtotal" value={`${breakdown.additiveScore}`} />
              </div>
            )}
          </section>

          <section className="space-y-2">
            <p className="text-[10px] font-bold uppercase tracking-wider clinical-muted">
              Penalties &amp; boosts
            </p>
            <Row
              label="Stability penalty"
              value={`+${breakdown.stabilityPenalty}`}
              detail="Lower stability → higher penalty"
            />
            <Row
              label="Difficulty penalty"
              value={`+${breakdown.difficultyPenalty}`}
              detail="Intrinsic item difficulty"
            />
            <Row
              label="Lapse boost"
              value={`+${breakdown.lapseBoost}`}
              detail="8 pts per failed recall"
            />
            <Row
              label="Time pressure"
              value={`+${breakdown.timePressure}`}
              detail={
                breakdown.daysOverdue > 0
                  ? `${breakdown.daysOverdue}d overdue — exponential`
                  : 'Not yet due'
              }
            />
          </section>

          <section className="space-y-2">
            <p className="text-[10px] font-bold uppercase tracking-wider clinical-muted">
              Hazard clusters
            </p>
            {breakdown.hazardMultipliers.length === 0 ? (
              <p className="text-xs clinical-muted">No overlapping severe-tag clusters.</p>
            ) : (
              breakdown.hazardMultipliers.map((h) => (
                <Row
                  key={h.clusterId}
                  label={h.label}
                  value={`×${h.multiplier}`}
                  detail={h.matchedTags.join(' + ')}
                />
              ))
            )}
            <Row label="Combined multiplier" value={`×${breakdown.combinedMultiplier}`} />
          </section>

          <section className="rounded-lg bg-slate-50 px-3 py-3 dark:bg-zinc-900/60">
            <Row label="Subtotal" value={`${breakdown.subtotal}`} />
            <div className="my-2 border-t clinical-border" />
            <Row label="Result (RPS)" value={`${breakdown.rps}`} />
            <p className="mt-3 text-sm font-medium text-amber-800 dark:text-amber-200">
              {breakdown.recommendation}
            </p>
          </section>
        </div>
      )}
    </div>
  )
}
