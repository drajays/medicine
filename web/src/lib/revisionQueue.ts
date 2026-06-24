import {
  DEFAULT_TRIAGE_LIMIT,
  isCriticalRPS,
  isDue,
  type Tag,
} from '@/lib/revision-math'
import type { PrioritizedEntry } from '@/stores/revisionStore'

export type RevisionModePreset = 'manual' | 'smart' | 'mistakes' | 'critical' | 'due' | 'weak'

export type RevisionModeGroup = 'manual' | 'auto'

export interface RevisionModeOptions {
  preset: RevisionModePreset
  limit?: number
}

export interface RevisionModeMeta {
  preset: RevisionModePreset
  group: RevisionModeGroup
  title: string
  description: string
  emoji: string
}

export const REVISION_MODES: RevisionModeMeta[] = [
  // ── Manual: exactly what you chose to revise ──────────────────────────────
  {
    preset: 'manual',
    group: 'manual',
    title: 'Marked for revision',
    description:
      'Only items you explicitly marked Action = Revise. Your hand-picked list — nothing you already know sneaks in.',
    emoji: '📌',
  },
  // ── Auto: the engine decides from your mistakes + the RPS matrix ───────────
  {
    preset: 'smart',
    group: 'auto',
    title: 'Smart Auto',
    description:
      'Best overall queue — RPS plus due-date boost, lapse history, and weak-point tags. Recommended.',
    emoji: '🧠',
  },
  {
    preset: 'mistakes',
    group: 'auto',
    title: 'My Mistakes',
    description:
      'Cards you actually got wrong in review (lapses) plus ones you flagged Guessed or Concept gap.',
    emoji: '❌',
  },
  {
    preset: 'critical',
    group: 'auto',
    title: 'Critical Now',
    description: 'Only items with RPS ≥ 55 — highest urgency, hazard clusters, or severe overdue pressure.',
    emoji: '🔴',
  },
  {
    preset: 'due',
    group: 'auto',
    title: 'Due Today',
    description: 'FSRS-scheduled items past their review date — spaced repetition catch-up.',
    emoji: '⏰',
  },
  {
    preset: 'weak',
    group: 'auto',
    title: 'Weak Points',
    description: 'Tagged Doubt, Guessed, Concept gap, or Tough — your self-identified gaps.',
    emoji: '🎯',
  },
]

const WEAK_TAGS: Tag[] = ['Doubt', 'ConceptGap', 'Guessed', 'Tough']
const MISTAKE_TAGS: Tag[] = ['Guessed', 'ConceptGap']

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
    case 'manual':
      return entries.filter((e) => e.item.manual)
    case 'mistakes':
      return entries.filter(
        (e) => e.item.lapseCount > 0 || e.item.tags.some((t) => MISTAKE_TAGS.includes(t)),
      )
    case 'critical':
      return entries.filter((e) => isCriticalRPS(e.breakdown.rps))
    case 'due':
      return entries.filter((e) => isDue(e.item, now))
    case 'weak':
      return entries.filter((e) => e.item.tags.some((t) => WEAK_TAGS.includes(t)))
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
