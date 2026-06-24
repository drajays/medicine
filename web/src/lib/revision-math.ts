/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * PHASE 0: CONSTANTS & CONTRACTS
 * ═══════════════════════════════════════════════════════════════════════════════
 *
 * Single source of truth for the Glassbox Revision Engine v2 math layer.
 * All UI and store code must treat these values as immutable contracts unless
 * this block is deliberately revised.
 *
 * ─── TAG WEIGHTS (additive, deduplicated per item) ─────────────────────────────
 *
 *   Doubt        25
 *   ConceptGap   22
 *   Guessed      18
 *   Tough        15
 *   Important    12
 *   Formula       8
 *   Theory        5
 *
 *   additiveScore = Σ TAG_WEIGHTS[tag] for each unique tag on the item
 *
 * ─── HAZARD CLUSTERS (multiplicative, compounding) ───────────────────────────
 *
 * A cluster activates when ≥ minMatch of its tags are present on the item.
 * All matching clusters multiply into combinedMultiplier (product, not sum).
 *
 *   id                  label                      tags                          minMatch  ×mult
 *   confidence_crisis   Confidence crisis          Doubt, Guessed, ConceptGap         2   1.65
 *   knowledge_gap       Knowledge gap cluster      ConceptGap, Doubt, Tough           2   1.45
 *   hard_important      High-stakes difficulty     Tough, Important                   2   1.35
 *   rote_trap           Rote without understanding Guessed, Formula                   2   1.25
 *   theory_doubt        Conceptual uncertainty     Theory, Doubt, ConceptGap          2   1.20
 *
 * ─── PENALTY / BOOST CONSTANTS ───────────────────────────────────────────────
 *
 *   MS_PER_DAY                    86_400_000
 *   TIME_PRESSURE_HALF_LIFE_DAYS  3
 *   TIME_PRESSURE_SCALE           20
 *   STABILITY_PENALTY_SCALE       30
 *   DIFFICULTY_PENALTY_SCALE      2.5
 *   LAPSE_BOOST_PER_LAPSE         8
 *   MIN_STABILITY                 0.5
 *   MIN_DIFFICULTY                1
 *   MAX_DIFFICULTY                10
 *   CRITICAL_RPS_THRESHOLD        55
 *   DEFAULT_TRIAGE_LIMIT          25
 *
 * ─── TYPESCRIPT: StudyItem (engine item — not chapter JSON StudyItem) ─────────
 *
 *   export type Tag =
 *     | 'Tough' | 'Important' | 'Doubt' | 'ConceptGap'
 *     | 'Guessed' | 'Formula' | 'Theory'
 *
 *   export type RecallRating = 0 | 1 | 2 | 3 | 4 | 5
 *   // 0 Blackout · 1 Wrong · 2 Hard · 3 Good · 4 Easy · 5 Perfect
 *
 *   export interface StudyItem {
 *     id: string
 *     chapterId: string
 *     subject: string
 *     title: string
 *     itemType: string
 *     tags: Tag[]
 *     stability: number       // memory strength in days (FSRS-like)
 *     difficulty: number      // intrinsic difficulty 1–10
 *     interval: number        // scheduled gap in days
 *     dueAt: number           // epoch ms — next review due
 *     lastReviewedAt?: number
 *     reviewCount: number
 *     lapseCount: number
 *     createdAt: number
 *   }
 *
 * ─── TYPESCRIPT: ReviewRecord ────────────────────────────────────────────────
 *
 *   export interface ReviewRecord {
 *     itemId: string
 *     rating: RecallRating
 *     reviewedAt: number
 *     durationMs?: number
 *     prevStability: number
 *     prevInterval: number
 *     newStability: number
 *     newInterval: number
 *     rpsAtReview: number
 *   }
 *
 * ─── RPS FORMULA (pseudocode) ────────────────────────────────────────────────
 *
 *   INPUT:  item (StudyItem), now (epoch ms)
 *   OUTPUT: rps (number), breakdown (inspectable parts)
 *
 *   // 1. Additive tag score
 *   additiveScore ← Σ TAG_WEIGHTS[t] for unique t in item.tags
 *
 *   // 2. Stability penalty — lower stability ⇒ higher urgency
 *   stabilityPenalty ← STABILITY_PENALTY_SCALE / (max(item.stability, MIN_STABILITY) + 1)
 *
 *   // 3. Difficulty penalty — clamp difficulty to [MIN_DIFFICULTY, MAX_DIFFICULTY]
 *   difficultyPenalty ← clamp(item.difficulty) × DIFFICULTY_PENALTY_SCALE
 *
 *   // 4. Lapse boost — each failed recall adds fixed urgency
 *   lapseBoost ← max(0, item.lapseCount) × LAPSE_BOOST_PER_LAPSE
 *
 *   // 5. Time-pressure (exponential, only when overdue)
 *   daysOverdue ← (now − item.dueAt) / MS_PER_DAY
 *   IF daysOverdue ≤ 0:
 *     timePressure ← 0
 *   ELSE:
 *     timePressure ← TIME_PRESSURE_SCALE × (exp(daysOverdue / TIME_PRESSURE_HALF_LIFE_DAYS) − 1)
 *
 *   // 6. Hazard cluster multipliers (compounding product)
 *   combinedMultiplier ← 1
 *   FOR EACH cluster IN HAZARD_CLUSTERS:
 *     matched ← cluster.tags ∩ item.tags
 *     IF |matched| ≥ cluster.minMatch:
 *       combinedMultiplier ← combinedMultiplier × cluster.multiplier
 *
 *   // 7. Final score
 *   subtotal ← additiveScore + stabilityPenalty + difficultyPenalty + lapseBoost + timePressure
 *   rps ← round(subtotal × combinedMultiplier, 1 decimal)
 *
 *   // Recommendation bands
 *   rps ≥ 80                          → "Critical — review immediately"
 *   rps ≥ CRITICAL_RPS_THRESHOLD (55) → "High priority — include in today's triage"
 *   rps ≥ 35                          → "Moderate — schedule within 48 hours"
 *   daysOverdue > 0                   → "Due — review soon"
 *   else                              → "Stable — on track"
 *
 * ═══════════════════════════════════════════════════════════════════════════════
 * PHASE 1+: Implementation below — must stay aligned with Phase 0 contracts.
 * ═══════════════════════════════════════════════════════════════════════════════
 */

export type Tag =
  | 'Tough'
  | 'Important'
  | 'Doubt'
  | 'ConceptGap'
  | 'Guessed'
  | 'Formula'
  | 'Theory'

/** 0 = Blackout … 5 = Perfect recall */
export type RecallRating = 0 | 1 | 2 | 3 | 4 | 5

export const RECALL_LABELS: Record<RecallRating, string> = {
  0: 'Blackout',
  1: 'Wrong',
  2: 'Hard',
  3: 'Good',
  4: 'Easy',
  5: 'Perfect',
}

export interface ReviewRecord {
  itemId: string
  rating: RecallRating
  reviewedAt: number
  durationMs?: number
  prevStability: number
  prevInterval: number
  newStability: number
  newInterval: number
  rpsAtReview: number
}

export interface RevisionStudyItem {
  id: string
  chapterId: string
  subject: string
  title: string
  itemType: string
  tags: Tag[]
  stability: number
  difficulty: number
  interval: number
  dueAt: number
  lastReviewedAt?: number
  reviewCount: number
  lapseCount: number
  createdAt: number
}

/** Engine StudyItem — distinct from chapter JSON `StudyItem` in `@/lib/types`. */
export type StudyItem = RevisionStudyItem

export const TAG_WEIGHTS: Record<Tag, number> = {
  Doubt: 25,
  ConceptGap: 22,
  Guessed: 18,
  Tough: 15,
  Important: 12,
  Formula: 8,
  Theory: 5,
}

export interface HazardCluster {
  id: string
  label: string
  tags: Tag[]
  /** Minimum overlapping severe tags to activate this cluster */
  minMatch: number
  multiplier: number
}

/**
 * Compounding multipliers when multiple severe tags overlap on one item.
 * Each matching cluster multiplies into the final RPS.
 */
export const HAZARD_CLUSTERS: HazardCluster[] = [
  {
    id: 'confidence_crisis',
    label: 'Confidence crisis',
    tags: ['Doubt', 'Guessed', 'ConceptGap'],
    minMatch: 2,
    multiplier: 1.65,
  },
  {
    id: 'knowledge_gap',
    label: 'Knowledge gap cluster',
    tags: ['ConceptGap', 'Doubt', 'Tough'],
    minMatch: 2,
    multiplier: 1.45,
  },
  {
    id: 'hard_important',
    label: 'High-stakes difficulty',
    tags: ['Tough', 'Important'],
    minMatch: 2,
    multiplier: 1.35,
  },
  {
    id: 'rote_trap',
    label: 'Rote without understanding',
    tags: ['Guessed', 'Formula'],
    minMatch: 2,
    multiplier: 1.25,
  },
  {
    id: 'theory_doubt',
    label: 'Conceptual uncertainty',
    tags: ['Theory', 'Doubt', 'ConceptGap'],
    minMatch: 2,
    multiplier: 1.2,
  },
]

export const MS_PER_DAY = 86_400_000
export const CRITICAL_RPS_THRESHOLD = 55
export const DEFAULT_TRIAGE_LIMIT = 25

/** Exported tuning constants — see Phase 0 block for semantics. */
export const TIME_PRESSURE_HALF_LIFE_DAYS = 3
export const TIME_PRESSURE_SCALE = 20
export const STABILITY_PENALTY_SCALE = 30
export const DIFFICULTY_PENALTY_SCALE = 2.5
export const LAPSE_BOOST_PER_LAPSE = 8
export const MIN_STABILITY = 0.5
export const MIN_DIFFICULTY = 1
export const MAX_DIFFICULTY = 10

export interface TagContribution {
  tag: Tag
  weight: number
}

export interface HazardMultiplier {
  clusterId: string
  label: string
  multiplier: number
  matchedTags: Tag[]
}

export interface RPSBreakdown {
  additiveScore: number
  tagContributions: TagContribution[]
  stabilityPenalty: number
  difficultyPenalty: number
  lapseBoost: number
  timePressure: number
  daysOverdue: number
  hazardMultipliers: HazardMultiplier[]
  combinedMultiplier: number
  subtotal: number
  rps: number
  recommendation: string
}

export interface NextState {
  stability: number
  difficulty: number
  interval: number
  dueAt: number
  lapseCount: number
  reviewCount: number
}

function uniqueTags(tags: Tag[]): Tag[] {
  return [...new Set(tags)]
}

export function computeTagAdditive(tags: Tag[]): { score: number; contributions: TagContribution[] } {
  const contributions: TagContribution[] = []
  let score = 0
  for (const tag of uniqueTags(tags)) {
    const weight = TAG_WEIGHTS[tag] ?? 0
    if (weight > 0) {
      contributions.push({ tag, weight })
      score += weight
    }
  }
  return { score, contributions }
}

/** Lower stability → higher penalty (item is fragile in memory). */
export function computeStabilityPenalty(stability: number): number {
  return STABILITY_PENALTY_SCALE / (Math.max(stability, MIN_STABILITY) + 1)
}

/** Higher intrinsic difficulty → higher priority. */
export function computeDifficultyPenalty(difficulty: number): number {
  const d = Math.min(MAX_DIFFICULTY, Math.max(MIN_DIFFICULTY, difficulty))
  return d * DIFFICULTY_PENALTY_SCALE
}

/** Each lapse compounds urgency. */
export function computeLapseBoost(lapseCount: number): number {
  return Math.max(0, lapseCount) * LAPSE_BOOST_PER_LAPSE
}

/**
 * Exponential urgency once past due date.
 * Subdued when not yet due (returns 0).
 */
export function computeTimePressure(dueAt: number, now: number): { pressure: number; daysOverdue: number } {
  const daysOverdue = (now - dueAt) / MS_PER_DAY
  if (daysOverdue <= 0) return { pressure: 0, daysOverdue }
  const pressure = TIME_PRESSURE_SCALE * (Math.exp(daysOverdue / TIME_PRESSURE_HALF_LIFE_DAYS) - 1)
  return { pressure, daysOverdue }
}

export function computeHazardMultipliers(tags: Tag[]): {
  multipliers: HazardMultiplier[]
  combined: number
} {
  const tagSet = new Set(tags)
  const multipliers: HazardMultiplier[] = []
  let combined = 1

  for (const cluster of HAZARD_CLUSTERS) {
    const matchedTags = cluster.tags.filter((t) => tagSet.has(t))
    if (matchedTags.length >= cluster.minMatch) {
      multipliers.push({
        clusterId: cluster.id,
        label: cluster.label,
        multiplier: cluster.multiplier,
        matchedTags,
      })
      combined *= cluster.multiplier
    }
  }

  return { multipliers, combined }
}

function recommendationText(rps: number, daysOverdue: number): string {
  if (rps >= 80) return 'Critical — review immediately'
  if (rps >= CRITICAL_RPS_THRESHOLD) return 'High priority — include in today\'s triage'
  if (rps >= 35) return 'Moderate — schedule within 48 hours'
  if (daysOverdue > 0) return 'Due — review soon'
  return 'Stable — on track'
}

/**
 * Compute the full Revision Priority Score with an inspectable breakdown.
 *
 * RPS = (additive + stabilityPenalty + difficultyPenalty + lapseBoost + timePressure) × hazardMultiplier
 */
export function computeRPS(item: RevisionStudyItem, now = Date.now()): RPSBreakdown {
  const { score: additiveScore, contributions: tagContributions } = computeTagAdditive(item.tags)
  const stabilityPenalty = computeStabilityPenalty(item.stability)
  const difficultyPenalty = computeDifficultyPenalty(item.difficulty)
  const lapseBoost = computeLapseBoost(item.lapseCount)
  const { pressure: timePressure, daysOverdue } = computeTimePressure(item.dueAt, now)
  const { multipliers: hazardMultipliers, combined: combinedMultiplier } = computeHazardMultipliers(item.tags)

  const subtotal = additiveScore + stabilityPenalty + difficultyPenalty + lapseBoost + timePressure
  const rps = Math.round(subtotal * combinedMultiplier * 10) / 10

  return {
    additiveScore,
    tagContributions,
    stabilityPenalty: Math.round(stabilityPenalty * 10) / 10,
    difficultyPenalty: Math.round(difficultyPenalty * 10) / 10,
    lapseBoost,
    timePressure: Math.round(timePressure * 10) / 10,
    daysOverdue: Math.round(daysOverdue * 10) / 10,
    hazardMultipliers,
    combinedMultiplier: Math.round(combinedMultiplier * 100) / 100,
    subtotal: Math.round(subtotal * 10) / 10,
    rps,
    recommendation: recommendationText(rps, daysOverdue),
  }
}

/**
 * SM-2 / FSRS-inspired interval scheduler.
 * Ratings 0–2 = lapse (reset); 3–5 = success (grow stability & interval).
 */
export function computeNextState(
  item: Pick<RevisionStudyItem, 'stability' | 'difficulty' | 'interval' | 'lapseCount' | 'reviewCount'>,
  rating: RecallRating,
  reviewedAt: number,
): NextState {
  const isLapse = rating < 3

  if (isLapse) {
    const severity = 3 - rating
    const newDifficulty = Math.min(MAX_DIFFICULTY, item.difficulty + 0.6 + severity * 0.35)
    const newStability = Math.max(MIN_STABILITY, item.stability * (0.35 + rating * 0.05))
    return {
      stability: Math.round(newStability * 100) / 100,
      difficulty: Math.round(newDifficulty * 100) / 100,
      interval: 1,
      dueAt: reviewedAt + MS_PER_DAY,
      lapseCount: item.lapseCount + 1,
      reviewCount: item.reviewCount + 1,
    }
  }

  const quality = rating
  const newDifficulty = Math.max(
    MIN_DIFFICULTY,
    Math.round((item.difficulty - (quality - 3) * 0.28) * 100) / 100,
  )

  let newStability: number
  let newInterval: number

  if (item.reviewCount === 0) {
    newInterval = quality === 5 ? 4 : quality === 4 ? 3 : 1
    newStability = newInterval
  } else {
    const gainFactor = 1.15 + (quality - 3) * 0.32
    newStability = Math.max(item.stability + 0.4, item.stability * gainFactor)
    const intervalFactor = quality === 5 ? 2.5 : quality === 4 ? 1.75 : 1.25
    newInterval = item.interval * intervalFactor
  }

  newInterval = Math.max(1, Math.round(newInterval * 10) / 10)
  newStability = Math.max(MIN_STABILITY, Math.round(newStability * 100) / 100)

  return {
    stability: newStability,
    difficulty: newDifficulty,
    interval: newInterval,
    dueAt: reviewedAt + newInterval * MS_PER_DAY,
    lapseCount: item.lapseCount,
    reviewCount: item.reviewCount + 1,
  }
}

export function isCriticalRPS(rps: number): boolean {
  return rps >= CRITICAL_RPS_THRESHOLD
}

export function isDue(item: RevisionStudyItem, now = Date.now()): boolean {
  return item.dueAt <= now
}

export function todayKey(now = Date.now()): string {
  return new Date(now).toISOString().slice(0, 10)
}
