import { useState } from 'react'
import { Filter, X } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import { MARK_AXES, isFilterActive, type MarkAxis } from '@/lib/studyMarks'
import type { StudyFilter } from '@/lib/types'

interface Preset {
  label: string
  facet: Partial<StudyFilter>
}

// One-tap presets covering the most common "what do I revise now?" questions.
const PRESETS: Preset[] = [
  { label: 'To revise', facet: { action: 'revise' } },
  { label: 'Doubt', facet: { status: 'doubt' } },
  { label: 'Tough', facet: { difficulty: 'tough' } },
  { label: 'Important', facet: { priority: 'important' } },
  { label: 'New', facet: { progress: 'new' } },
]

function Chip({
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
        'shrink-0 rounded-full border px-3 py-1 text-xs font-semibold transition-colors',
        active
          ? 'border-[var(--color-clinical-accent)] bg-[var(--color-clinical-accent)] text-white'
          : 'clinical-border clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
      )}
    >
      {label}
    </button>
  )
}

/**
 * In-chapter filter for the study marks. Quick presets set a single facet;
 * the expandable panel exposes every axis + progress. Writes to the shared
 * (session-only) studyFilter; TabBody applies it to the visible items.
 */
export function ChapterFilterBar() {
  const filter = useAppStore((s) => s.studyFilter)
  const setStudyFilter = useAppStore((s) => s.setStudyFilter)
  const clearStudyFilter = useAppStore((s) => s.clearStudyFilter)
  const [open, setOpen] = useState(false)

  const active = isFilterActive(filter)

  const toggleFacet = (axis: MarkAxis | 'progress', value: string) => {
    const current = filter[axis] as string | undefined
    setStudyFilter({ [axis]: current === value ? undefined : value } as Partial<StudyFilter>)
  }

  const presetActive = (p: Preset) =>
    Object.entries(p.facet).every(([k, v]) => filter[k as keyof StudyFilter] === v)

  return (
    <div className="mb-3">
      <div className="flex items-center gap-2 overflow-x-auto py-1 scrollbar-thin">
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-expanded={open}
          className={cn(
            'inline-flex shrink-0 items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-semibold transition-colors',
            open || active
              ? 'border-[var(--color-clinical-accent)] text-[var(--color-clinical-accent)]'
              : 'clinical-border clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
          )}
        >
          <Filter className="h-3 w-3" />
          Filter
        </button>

        {PRESETS.map((p) => (
          <Chip
            key={p.label}
            label={p.label}
            active={presetActive(p)}
            onClick={() => setStudyFilter(presetActive(p) ? clearFacet(p) : p.facet)}
          />
        ))}

        {active && (
          <button
            type="button"
            onClick={clearStudyFilter}
            className="inline-flex shrink-0 items-center gap-1 rounded-full px-2 py-1 text-xs font-medium text-red-600 hover:bg-red-50 dark:text-red-400 dark:hover:bg-red-500/10"
          >
            <X className="h-3 w-3" /> Clear
          </button>
        )}
      </div>

      {open && (
        <div className="mt-2 grid grid-cols-1 gap-2.5 rounded-lg border clinical-border bg-black/[0.015] p-3 dark:bg-white/[0.02] sm:grid-cols-2">
          {MARK_AXES.map((axis) => (
            <div key={axis.key} className="flex items-center justify-between gap-2">
              <span className="text-[11px] font-medium clinical-muted">{axis.label}</span>
              <div className="flex items-center gap-0.5 rounded-lg border clinical-border p-0.5">
                {[axis.sideA, axis.sideB].map((side) => (
                  <Chip
                    key={side.value}
                    label={side.label}
                    active={filter[axis.key] === side.value}
                    onClick={() => toggleFacet(axis.key, side.value)}
                  />
                ))}
              </div>
            </div>
          ))}
          <div className="flex items-center justify-between gap-2">
            <span className="text-[11px] font-medium clinical-muted">Progress</span>
            <div className="flex items-center gap-0.5 rounded-lg border clinical-border p-0.5">
              {(['new', 'done', 'revised'] as const).map((v) => (
                <Chip
                  key={v}
                  label={v[0].toUpperCase() + v.slice(1)}
                  active={filter.progress === v}
                  onClick={() => toggleFacet('progress', v)}
                />
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

// Clearing a preset only unsets the facets it owns (leaves other filters intact).
function clearFacet(p: Preset): Partial<StudyFilter> {
  const cleared: Partial<StudyFilter> = {}
  for (const k of Object.keys(p.facet)) cleared[k as keyof StudyFilter] = undefined
  return cleared
}
