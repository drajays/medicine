import type { ReviewRecord, RevisionStudyItem } from '@/lib/revision-math'

/**
 * Read-only analytics over the revision review log. Pure functions only — no
 * store/React deps — so they're trivially testable and cheap to memoize.
 *
 * "Pass" = a successful recall: rating ≥ 3 (Good/Easy/Perfect). Ratings 0–2
 * (Blackout/Wrong/Hard) are lapses.
 */
export const RECALL_PASS = 3

export function isPass(rating: number): boolean {
  return rating >= RECALL_PASS
}

export interface RetentionSummary {
  total: number
  correct: number
  /** 0–100; 0 when there are no reviews. */
  percent: number
}

export function summarize(reviews: ReviewRecord[]): RetentionSummary {
  const total = reviews.length
  const correct = reviews.reduce((n, r) => n + (isPass(r.rating) ? 1 : 0), 0)
  return { total, correct, percent: total ? Math.round((correct / total) * 100) : 0 }
}

const MS_PER_DAY = 86_400_000

function dayKeyUTC(ms: number): string {
  return new Date(ms).toISOString().slice(0, 10)
}

export interface DayAccuracy extends RetentionSummary {
  date: string
  label: string
}

/**
 * Recall accuracy per calendar day for the last `days` days (UTC, matching the
 * engine's daily-stats keys). Days with no reviews come back at percent 0 /
 * total 0 so the trend stays continuous.
 */
export function accuracyTrend(reviews: ReviewRecord[], days = 14): DayAccuracy[] {
  const byDay = new Map<string, { total: number; correct: number }>()
  for (const r of reviews) {
    const key = dayKeyUTC(r.reviewedAt)
    const e = byDay.get(key) ?? { total: 0, correct: 0 }
    e.total += 1
    if (isPass(r.rating)) e.correct += 1
    byDay.set(key, e)
  }

  const now = Date.now()
  const out: DayAccuracy[] = []
  for (let i = days - 1; i >= 0; i--) {
    const ms = now - i * MS_PER_DAY
    const key = dayKeyUTC(ms)
    const e = byDay.get(key) ?? { total: 0, correct: 0 }
    out.push({
      date: key,
      label: i === 0 ? 'Today' : String(new Date(ms).getUTCDate()),
      total: e.total,
      correct: e.correct,
      percent: e.total ? Math.round((e.correct / e.total) * 100) : 0,
    })
  }
  return out
}

export interface IntervalBand extends RetentionSummary {
  band: string
}

// Boundaries are the upper bound (in days) of the scheduled interval the card
// was on when reviewed — the classic "retention vs interval" curve.
const INTERVAL_BANDS: Array<{ label: string; max: number }> = [
  { label: '≤1d', max: 1 },
  { label: '2–3d', max: 3 },
  { label: '4–7d', max: 7 },
  { label: '1–3w', max: 21 },
  { label: '>3w', max: Infinity },
]

export function retentionByInterval(reviews: ReviewRecord[]): IntervalBand[] {
  return INTERVAL_BANDS.map((b, i) => {
    const min = i === 0 ? -Infinity : INTERVAL_BANDS[i - 1].max
    const inBand = reviews.filter((r) => r.prevInterval > min && r.prevInterval <= b.max)
    return { band: b.label, ...summarize(inBand) }
  })
}

export const DEFAULT_LEECH_THRESHOLD = 4

/**
 * Leeches: chronically-failed cards (lapseCount ≥ threshold) that eat
 * disproportionate review time and usually need reformulating or suspending.
 * Sorted worst-first.
 */
export function findLeeches(
  items: Record<string, RevisionStudyItem>,
  minLapses = DEFAULT_LEECH_THRESHOLD,
): RevisionStudyItem[] {
  return Object.values(items)
    .filter((i) => i.lapseCount >= minLapses)
    .sort((a, b) => b.lapseCount - a.lapseCount || b.reviewCount - a.reviewCount)
}
