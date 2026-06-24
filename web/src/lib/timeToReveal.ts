/** Pre-answer fluency: item shown → user reveals (not post-reveal thinking). */

export const TIME_TO_REVEAL_CAP_MS = 120_000
export const TIME_TO_REVEAL_FLOOR_MS = 200

/**
 * Compute capped time-to-reveal from item-shown timestamp to reveal timestamp.
 * Returns null if not revealed.
 */
export function computeTimeToRevealMs(
  itemShownAt: number,
  revealedAt: number | null,
): number | null {
  if (revealedAt == null) return null
  const raw = revealedAt - itemShownAt
  if (raw < TIME_TO_REVEAL_FLOOR_MS) return TIME_TO_REVEAL_FLOOR_MS
  return Math.min(raw, TIME_TO_REVEAL_CAP_MS)
}

export function formatTimeToReveal(ms: number | null): string {
  if (ms == null) return '—'
  const secs = Math.round(ms / 1000)
  return `${secs}s`
}

export interface TimeToRevealBucket {
  under10s: number
  s10to30: number
  s30to120: number
}

export interface TimeToRevealStats {
  count: number
  avgMs: number
  buckets: TimeToRevealBucket
}

export function bucketTimeToReveal(ms: number): keyof TimeToRevealBucket {
  const s = ms / 1000
  if (s < 10) return 'under10s'
  if (s < 30) return 's10to30'
  return 's30to120'
}

export function aggregateTimeToReveal(
  values: Array<number | null | undefined>,
): TimeToRevealStats {
  const samples = values.filter((v): v is number => v != null)
  const buckets: TimeToRevealBucket = { under10s: 0, s10to30: 0, s30to120: 0 }
  if (!samples.length) {
    return { count: 0, avgMs: 0, buckets }
  }
  let sum = 0
  for (const ms of samples) {
    sum += ms
    buckets[bucketTimeToReveal(ms)] += 1
  }
  return {
    count: samples.length,
    avgMs: Math.round(sum / samples.length),
    buckets,
  }
}

export function rollingAverageMs(values: number[], n = 5): number | null {
  const slice = values.slice(-n)
  if (!slice.length) return null
  return Math.round(slice.reduce((a, b) => a + b, 0) / slice.length)
}
