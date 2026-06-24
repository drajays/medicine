import type { ItemMark, StudyFilter, StudyItem } from '@/lib/types'

/** The toggle axes that live on ItemMark (excludes the counters/context). */
export type MarkAxis =
  | 'difficulty'
  | 'priority'
  | 'action'
  | 'status'
  | 'method'
  | 'confidence'
  | 'errorType'

export interface AxisSide {
  value: string
  label: string
}

export interface AxisDef {
  key: MarkAxis
  label: string
  sideA: AxisSide
  sideB: AxisSide
  /** Only meaningful for question items (mcq/tf/ar/why/how/shortanswer). */
  questionsOnly?: boolean
  /** sideA value that flags an item for revision / attention (Hub + presets). */
  attentionValue?: string
}

/**
 * Single source of truth for the 7 minimalist toggles. The per-item toggle bar,
 * the chapter filter bar, and the Revise Hub all derive their UI from this list,
 * so adding/renaming an axis is a one-line change here.
 */
export const MARK_AXES: AxisDef[] = [
  {
    key: 'difficulty',
    label: 'Difficulty',
    sideA: { value: 'tough', label: 'Tough' },
    sideB: { value: 'easy', label: 'Easy' },
    attentionValue: 'tough',
  },
  {
    key: 'priority',
    label: 'Priority',
    sideA: { value: 'important', label: 'Important' },
    sideB: { value: 'not', label: 'Not imp.' },
  },
  {
    key: 'action',
    label: 'Action',
    sideA: { value: 'revise', label: 'Revise' },
    sideB: { value: 'no_revise', label: 'No revise' },
    attentionValue: 'revise',
  },
  {
    key: 'status',
    label: 'Status',
    sideA: { value: 'clear', label: 'Clear' },
    sideB: { value: 'doubt', label: 'Doubt' },
    attentionValue: 'doubt',
  },
  {
    key: 'method',
    label: 'Method',
    sideA: { value: 'logic', label: 'Logic' },
    sideB: { value: 'rote', label: 'Rote' },
  },
  {
    key: 'confidence',
    label: 'Confidence',
    sideA: { value: 'knew', label: 'Knew it' },
    sideB: { value: 'guessed', label: 'Guessed' },
    questionsOnly: true,
    attentionValue: 'guessed',
  },
  {
    key: 'errorType',
    label: 'Error',
    sideA: { value: 'silly', label: 'Silly' },
    sideB: { value: 'concept', label: 'Concept gap' },
    questionsOnly: true,
    attentionValue: 'concept',
  },
]

export function isQuestion(type: string): boolean {
  return type !== 'note'
}

/** Short human label for an item, for the Revise Hub / mark context. */
export function itemMarkLabel(item: StudyItem): string {
  const raw =
    (item as { title?: string }).title ??
    (item as { stem?: string }).stem ??
    (item as { statement?: string }).statement ??
    (item as { assertion?: string }).assertion ??
    (item as { question?: string }).question ??
    ''
  return raw.length > 90 ? raw.slice(0, 90) + '…' : raw
}

/** Axes applicable to a given item type (hides questionsOnly axes for notes). */
export function axesForType(type: string): AxisDef[] {
  return isQuestion(type) ? MARK_AXES : MARK_AXES.filter((a) => !a.questionsOnly)
}

export function emptyMark(): ItemMark {
  return { timesDone: 0, timesRevised: 0 }
}

/** New (never seen) → Done (seen ≥1) → Revised (revised ≥1). */
export function progressOf(mark: ItemMark | undefined): 'new' | 'done' | 'revised' {
  if (!mark || mark.timesDone === 0) return 'new'
  return mark.timesRevised > 0 ? 'revised' : 'done'
}

export function isFilterActive(filter: StudyFilter): boolean {
  return Object.values(filter).some((v) => v !== undefined)
}

/** AND across every set facet. */
export function matchesFilter(
  mark: ItemMark | undefined,
  filter: StudyFilter,
): boolean {
  for (const axis of MARK_AXES) {
    const want = filter[axis.key]
    if (want !== undefined && (mark?.[axis.key] ?? undefined) !== want) return false
  }
  if (filter.progress !== undefined && progressOf(mark) !== filter.progress) return false
  return true
}

export function applyStudyFilter(
  items: StudyItem[],
  marks: Record<string, ItemMark>,
  filter: StudyFilter,
): StudyItem[] {
  if (!isFilterActive(filter)) return items
  return items.filter((i) => matchesFilter(marks[i.id], filter))
}

export interface ReviseEntry {
  itemId: string
  mark: ItemMark
}

/**
 * Items worth revising across the whole portal: anything marked Action=Revise or
 * Status=Doubt. Most-recently-touched first. Uses the chapter context stored on
 * each mark, so no chapter JSON needs to be loaded.
 */
export function reviseListFromMarks(marks: Record<string, ItemMark>): ReviseEntry[] {
  return Object.entries(marks)
    .filter(([, m]) => m.action === 'revise' || m.status === 'doubt')
    .map(([itemId, mark]) => ({ itemId, mark }))
    .sort((a, b) => (b.mark.lastSeenAt ?? 0) - (a.mark.lastSeenAt ?? 0))
}

export function reviseCount(marks: Record<string, ItemMark>): number {
  return reviseListFromMarks(marks).length
}
