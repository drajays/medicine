import {
  DEFAULT_TRIAGE_LIMIT,
  isCriticalRPS,
  isDue,
  type Tag,
} from '@/lib/revision-math'
import type { PrioritizedEntry } from '@/stores/revisionStore'

export type RevisionModePreset = 'smart' | 'critical' | 'due' | 'weak' | 'flagged'

export interface RevisionModeOptions {
  preset: RevisionModePreset
  limit?: number
}

export interface RevisionModeMeta {
  preset: RevisionModePreset
  title: string
  description: string
  emoji: string
}

export const REVISION_MODES: RevisionModeMeta[] = [
  {
    preset: 'smart',
    title: 'Smart Auto',
    description:
      'Best overall queue — RPS plus due-date boost, lapse history, and weak-point tags. Recommended default.',
    emoji: '🧠',
  },
  {
    preset: 'critical',
    title: 'Critical Now',
    description: 'Only items with RPS ≥ 55 — highest urgency, hazard clusters, or severe overdue pressure.',
    emoji: '🔴',
  },
  {
    preset: 'due',
    title: 'Due Today',
    description: 'FSRS-scheduled items past their review date — spaced repetition catch-up.',
    emoji: '⏰',
  },
  {
    preset: 'weak',
    title: 'Weak Points',
    description: 'Tagged Doubt, Guessed, Concept gap, or Tough — your self-identified gaps.',
    emoji: '🎯',
  },
  {
    preset: 'flagged',
    title: 'All Flagged',
    description: 'Every item you marked for revision or attention — full pass by RPS order.',
    emoji: '📌',
  },
]

const WEAK_TAGS: Tag[] = ['Doubt', 'ConceptGap', 'Guessed', 'Tough']

/** Composite score for Smart Auto — transparent weighting on top of RPS. */
export function computeSmartScore(entry: PrioritizedEntry, now = Date.now()): number {
  let score = entry.breakdown.rps
  if (isDue(entry.item, now)) score += 15
  if (isCriticalRPS(entry.breakdown.rps)) score += 10
  score += entry.item.lapseCount * 6
  const weakHits = entry.item.tags.filter((t) => WEAK_TAGS.includes(t)).length
  score += weakHits * 8
  if (entry.item.tags.includes('Important')) score += 5
  return Math.round(score * 10) / 10
}

export function filterByPreset(
  entries: PrioritizedEntry[],
  preset: RevisionModePreset,
  now = Date.now(),
): PrioritizedEntry[] {
  switch (preset) {
    case 'critical':
      return entries.filter((e) => isCriticalRPS(e.breakdown.rps))
    case 'due':
      return entries.filter((e) => isDue(e.item, now))
    case 'weak':
      return entries.filter((e) => e.item.tags.some((t) => WEAK_TAGS.includes(t)))
    case 'flagged':
    case 'smart':
      return entries
  }
}

export function buildRevisionQueue(
  entries: PrioritizedEntry[],
  options: RevisionModeOptions,
  now = Date.now(),
): PrioritizedEntry[] {
  const limit = options.limit ?? DEFAULT_TRIAGE_LIMIT
  let pool = filterByPreset(entries, options.preset, now)

  if (options.preset === 'smart') {
    pool = [...pool].sort(
      (a, b) => computeSmartScore(b, now) - computeSmartScore(a, now),
    )
  } else {
    pool = [...pool].sort((a, b) => b.breakdown.rps - a.breakdown.rps)
  }

  return pool.slice(0, limit)
}

export function countForPreset(entries: PrioritizedEntry[], preset: RevisionModePreset): number {
  return filterByPreset(entries, preset).length
}
