import { RotateCw, SlidersHorizontal } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import { axesForType, progressOf, type AxisDef } from '@/lib/studyMarks'
import type { ItemMark, StudyItem } from '@/lib/types'

const PROGRESS_STYLE: Record<'new' | 'done' | 'revised', string> = {
  new: 'bg-slate-100 text-slate-500 dark:bg-zinc-800 dark:text-zinc-400',
  done: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-950/50 dark:text-emerald-300',
  revised: 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-200',
}

function SidePill({
  label,
  active,
  onClick,
}: {
  label: string
  active: boolean
  onClick: () => void
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-pressed={active}
      className={cn(
        'rounded-md px-2 py-0.5 text-[11px] font-semibold transition-colors',
        active
          ? 'bg-[var(--color-clinical-accent)] text-white shadow-sm'
          : 'clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
      )}
    >
      {label}
    </button>
  )
}

function AxisRow({
  axis,
  mark,
  onSet,
}: {
  axis: AxisDef
  mark: ItemMark | undefined
  onSet: (value: string) => void
}) {
  const current = mark?.[axis.key] as string | undefined
  return (
    <div className="flex items-center justify-between gap-2">
      <span className="text-[11px] font-medium clinical-muted">{axis.label}</span>
      <div className="flex items-center gap-0.5 rounded-lg border clinical-border p-0.5">
        <SidePill
          label={axis.sideA.label}
          active={current === axis.sideA.value}
          onClick={() => onSet(axis.sideA.value)}
        />
        <SidePill
          label={axis.sideB.label}
          active={current === axis.sideB.value}
          onClick={() => onSet(axis.sideB.value)}
        />
      </div>
    </div>
  )
}

/**
 * Per-item study toggles (the 7 minimalist axes) + a "Revised ×N" counter and a
 * New/Done/Revised chip. The segmented controls are always visible (no collapse)
 * so marking is one tap. All state is local (persisted store).
 */
export function StudyMarks({ item }: { item: StudyItem }) {
  const mark = useAppStore((s) => s.marks[item.id])
  const setMark = useAppStore((s) => s.setMark)
  const markRevised = useAppStore((s) => s.markRevised)

  const axes = axesForType(item.type)
  const progress = progressOf(mark)
  const setCount = axes.filter((a) => mark?.[a.key] !== undefined).length

  return (
    <div className="mt-2 px-1">
      <div className="flex items-center gap-2 text-xs clinical-muted">
        <span className="inline-flex items-center gap-1.5 font-medium">
          <SlidersHorizontal className="h-3 w-3" />
          Marks{setCount ? ` · ${setCount}` : ''}
        </span>

        <span
          className={cn(
            'rounded-full px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide',
            PROGRESS_STYLE[progress],
          )}
        >
          {progress}
        </span>

        <button
          type="button"
          onClick={() => markRevised(item.id)}
          title="Mark as revised"
          className="ml-auto inline-flex items-center gap-1 rounded-md border px-2 py-1 font-medium clinical-border hover:text-[var(--color-clinical-accent)]"
        >
          <RotateCw className="h-3 w-3" />
          Revised{mark?.timesRevised ? ` ×${mark.timesRevised}` : ''}
        </button>
      </div>

      <div className="mt-2 grid grid-cols-1 gap-2 rounded-lg border clinical-border bg-black/[0.015] p-2.5 dark:bg-white/[0.02] sm:grid-cols-2">
        {axes.map((axis) => (
          <AxisRow
            key={axis.key}
            axis={axis}
            mark={mark}
            onSet={(value) => setMark(item.id, axis.key, value)}
          />
        ))}
      </div>
    </div>
  )
}
