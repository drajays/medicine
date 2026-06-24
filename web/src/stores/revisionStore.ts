import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { ItemMark } from '@/lib/types'
import { markWarrantsRevision } from '@/lib/studyMarks'
import {
  buildRevisionQueue,
  type RevisionModeOptions,
  type RevisionModePreset,
} from '@/lib/revisionQueue'
import {
  computeNextState,
  computeRPS,
  CRITICAL_RPS_THRESHOLD,
  DEFAULT_TRIAGE_LIMIT,
  isCriticalRPS,
  isDue,
  todayKey,
  MS_PER_DAY,
  type RecallRating,
  type RevisionStudyItem,
  type ReviewRecord,
  type RPSBreakdown,
  type Tag,
} from '@/lib/revision-math'
import {
  aggregateTimeToReveal,
  rollingAverageMs,
  type TimeToRevealStats,
} from '@/lib/timeToReveal'

export interface ItemRevealStats {
  lastMs: number | null
  rollingAvgMs: number | null
  reviewCount: number
}

function revealMsFromRecord(r: ReviewRecord): number | null {
  if (r.timeToRevealMs != null) return r.timeToRevealMs
  if (r.durationMs != null) return r.durationMs
  return null
}

export interface RevisionSession {
  id: string
  startedAt: number
  endedAt?: number
  itemIds: string[]
  currentIndex: number
  limit: number
  reviewedCount: number
  sessionMs: number
  mode: RevisionModePreset
}

export interface DailyStats {
  date: string
  reviewed: number
  totalRating: number
  sessionMs: number
}

export interface SessionHistoryEntry {
  id: string
  startedAt: number
  endedAt: number
  reviewed: number
  sessionMs: number
}

export interface SubjectSummary {
  subject: string
  itemCount: number
  dueCount: number
  criticalCount: number
  avgRps: number
  healthPercent: number
}

export interface TodayStats {
  reviewed: number
  avgRating: number
  sessionMs: number
  streak: number
}

export interface PrioritizedEntry {
  item: RevisionStudyItem
  breakdown: RPSBreakdown
}

export interface ForecastDay {
  /** YYYY-MM-DD for the day this bucket represents. */
  date: string
  /** Short label — 'Today' for index 0, otherwise a weekday abbreviation. */
  label: string
  /** Cards scheduled on this day (overdue cards roll into Today). */
  count: number
  /** Subset of count already past-due (only meaningful for Today). */
  overdue: number
}

function marksToTags(mark: ItemMark): Tag[] {
  const tags: Tag[] = []
  if (mark.difficulty === 'tough') tags.push('Tough')
  if (mark.priority === 'important') tags.push('Important')
  if (mark.status === 'doubt') tags.push('Doubt')
  if (mark.errorType === 'concept') tags.push('ConceptGap')
  if (mark.confidence === 'guessed') tags.push('Guessed')
  if (mark.method === 'rote') tags.push('Formula')
  if (mark.method === 'logic') tags.push('Theory')
  if (mark.action === 'revise' && !tags.includes('Important')) tags.push('Important')
  return tags
}

function updateStreak(
  lastStudyDate: string | null,
  streak: number,
  today: string,
): { streak: number; lastStudyDate: string } {
  if (lastStudyDate === today) return { streak, lastStudyDate: today }
  if (!lastStudyDate) return { streak: 1, lastStudyDate: today }

  const last = new Date(`${lastStudyDate}T12:00:00Z`)
  const cur = new Date(`${today}T12:00:00Z`)
  const diffDays = Math.round((cur.getTime() - last.getTime()) / 86_400_000)

  if (diffDays === 1) return { streak: streak + 1, lastStudyDate: today }
  return { streak: 1, lastStudyDate: today }
}

interface RevisionState {
  items: Record<string, RevisionStudyItem>
  reviews: ReviewRecord[]
  session: RevisionSession | null
  streak: number
  lastStudyDate: string | null
  dailyStats: Record<string, DailyStats>
  sessionHistory: SessionHistoryEntry[]
  showTimeAfterReveal: boolean

  addItem: (item: Omit<RevisionStudyItem, 'createdAt'> & { createdAt?: number }) => void
  updateItem: (id: string, patch: Partial<RevisionStudyItem>) => void
  deleteItem: (id: string) => void
  recordReview: (itemId: string, rating: RecallRating, timeToRevealMs: number | null) => void
  bootstrapFromMarks: (marks: Record<string, ItemMark>) => void
  setShowTimeAfterReveal: (show: boolean) => void

  startTriage: (limit?: number) => void
  startRevisionMode: (options?: RevisionModeOptions) => void
  getRevisionPlan: (options?: RevisionModeOptions) => PrioritizedEntry[]
  advanceSession: () => void
  endSession: () => void

  getPrioritized: (limit?: number) => PrioritizedEntry[]
  getCriticalCount: () => number
  getDueCount: () => number
  getForecast: (days?: number) => ForecastDay[]
  getSubjectSummary: () => SubjectSummary[]
  getTodayStats: () => TodayStats
  getTodayTimeToRevealStats: () => TimeToRevealStats
  getItemRevealStats: (itemId: string) => ItemRevealStats
  getItemBreakdown: (itemId: string) => RPSBreakdown | null
  getCurrentSessionItem: () => RevisionStudyItem | null
}

export const useRevisionStore = create<RevisionState>()(
  persist(
    (set, get) => ({
      items: {},
      reviews: [],
      session: null,
      streak: 0,
      lastStudyDate: null,
      dailyStats: {},
      sessionHistory: [],
      showTimeAfterReveal: true,

      addItem: (item) => {
        const now = Date.now()
        const created: RevisionStudyItem = {
          ...item,
          createdAt: item.createdAt ?? now,
        }
        set({ items: { ...get().items, [created.id]: created } })
      },

      updateItem: (id, patch) => {
        const existing = get().items[id]
        if (!existing) return
        set({ items: { ...get().items, [id]: { ...existing, ...patch } } })
      },

      deleteItem: (id) => {
        const items = { ...get().items }
        delete items[id]
        set({ items })
      },

      recordReview: (itemId, rating, timeToRevealMs) => {
        const item = get().items[itemId]
        if (!item) return

        const reviewedAt = Date.now()
        const breakdown = computeRPS(item, reviewedAt)
        const next = computeNextState(item, rating, reviewedAt)

        const review: ReviewRecord = {
          itemId,
          rating,
          reviewedAt,
          timeToRevealMs,
          prevStability: item.stability,
          prevInterval: item.interval,
          newStability: next.stability,
          newInterval: next.interval,
          rpsAtReview: breakdown.rps,
        }

        const updated: RevisionStudyItem = {
          ...item,
          stability: next.stability,
          difficulty: next.difficulty,
          interval: next.interval,
          dueAt: next.dueAt,
          lapseCount: next.lapseCount,
          reviewCount: next.reviewCount,
          lastReviewedAt: reviewedAt,
        }

        const today = todayKey(reviewedAt)
        const daily = { ...get().dailyStats }
        const day = daily[today] ?? { date: today, reviewed: 0, totalRating: 0, sessionMs: 0 }
        day.reviewed += 1
        day.totalRating += rating
        day.sessionMs += timeToRevealMs ?? 0
        daily[today] = day

        const { streak, lastStudyDate } = updateStreak(get().lastStudyDate, get().streak, today)

        const session = get().session
        let nextSession = session
        if (session && session.itemIds[session.currentIndex] === itemId) {
          nextSession = {
            ...session,
            reviewedCount: session.reviewedCount + 1,
            sessionMs: session.sessionMs + (timeToRevealMs ?? 0),
            currentIndex: session.currentIndex + 1,
          }
        }

        set({
          items: { ...get().items, [itemId]: updated },
          reviews: [...get().reviews, review],
          dailyStats: daily,
          streak,
          lastStudyDate,
          session: nextSession,
        })
      },

      setShowTimeAfterReveal: (show) => set({ showTimeAfterReveal: show }),

      // Reconcile the engine's item set with the current study marks. Unlike a
      // one-way seed, this REPLACES each item's tags from the live mark (so
      // unsetting a mark removes its tag and lowers RPS) and PRUNES items whose
      // mark no longer warrants revision — but only when the item has never been
      // reviewed in triage (reviewCount === 0). Items with real review history
      // survive as FSRS cards; if their mark vanished entirely their derived
      // tags are cleared so scheduling, not stale tags, drives their priority.
      bootstrapFromMarks: (marks) => {
        const now = Date.now()
        const prev = get().items
        const next: Record<string, RevisionStudyItem> = {}
        const ids = new Set<string>([...Object.keys(prev), ...Object.keys(marks)])

        for (const id of ids) {
          const mark = marks[id]
          const existing = prev[id]
          const reviewed = (existing?.reviewCount ?? 0) > 0

          if (!mark) {
            // Mark gone: keep the card only if it has review history (tags cleared).
            if (existing && reviewed) next[id] = { ...existing, tags: [] }
            continue
          }

          const warrants = markWarrantsRevision(mark)
          if (!warrants && !reviewed) continue // not (or no longer) a revision card
          if (!existing && !mark.chapterId) continue // can't create without context

          const tags = marksToTags(mark)

          if (existing) {
            next[id] = {
              ...existing,
              tags, // replace — reflects the mark's current state, not a union
              title: mark.label ?? existing.title,
              subject: mark.chapterTitle ?? existing.subject,
              itemType: mark.itemType ?? existing.itemType,
              lastReviewedAt: existing.lastReviewedAt ?? mark.lastSeenAt,
            }
          } else {
            next[id] = {
              id,
              chapterId: mark.chapterId!,
              subject: mark.chapterTitle ?? 'Unknown',
              title: mark.label ?? id,
              itemType: mark.itemType ?? 'note',
              tags,
              stability: 2,
              difficulty: 5,
              interval: 1,
              dueAt: now - 1,
              reviewCount: 0, // FSRS reviewCount starts at 0 — first triage = first review
              lapseCount: 0,
              createdAt: mark.firstSeenAt ?? now,
              lastReviewedAt: mark.lastSeenAt,
            }
          }
        }

        set({ items: next })
      },

      startTriage: (limit = DEFAULT_TRIAGE_LIMIT) => {
        get().startRevisionMode({ preset: 'smart', limit })
      },

      getRevisionPlan: (options = { preset: 'smart', limit: DEFAULT_TRIAGE_LIMIT }) => {
        const all = get().getPrioritized()
        return buildRevisionQueue(all, options)
      },

      startRevisionMode: (options = { preset: 'smart', limit: DEFAULT_TRIAGE_LIMIT }) => {
        const plan = get().getRevisionPlan(options)
        const itemIds = plan.map((e) => e.item.id)
        if (!itemIds.length) return

        set({
          session: {
            id: `session-${Date.now()}`,
            startedAt: Date.now(),
            itemIds,
            currentIndex: 0,
            limit: options.limit ?? DEFAULT_TRIAGE_LIMIT,
            reviewedCount: 0,
            sessionMs: 0,
            mode: options.preset,
          },
        })
      },

      advanceSession: () => {
        const session = get().session
        if (!session) return
        set({
          session: { ...session, currentIndex: session.currentIndex + 1 },
        })
      },

      endSession: () => {
        const session = get().session
        if (!session) return

        const endedAt = Date.now()
        const entry: SessionHistoryEntry = {
          id: session.id,
          startedAt: session.startedAt,
          endedAt,
          reviewed: session.reviewedCount,
          sessionMs: session.sessionMs + (endedAt - session.startedAt),
        }

        set({
          session: null,
          sessionHistory: [...get().sessionHistory, entry].slice(-50),
        })
      },

      getPrioritized: (limit) => {
        const now = Date.now()
        const entries: PrioritizedEntry[] = Object.values(get().items).map((item) => ({
          item,
          breakdown: computeRPS(item, now),
        }))
        entries.sort((a, b) => b.breakdown.rps - a.breakdown.rps)
        return limit ? entries.slice(0, limit) : entries
      },

      getCriticalCount: () => {
        const now = Date.now()
        return Object.values(get().items).filter((item) =>
          isCriticalRPS(computeRPS(item, now).rps),
        ).length
      },

      getDueCount: () => {
        const now = Date.now()
        return Object.values(get().items).filter((item) => isDue(item, now)).length
      },

      // Cards due per calendar day for the next `days` days. Overdue cards roll
      // into Today (index 0); cards scheduled beyond the horizon are excluded.
      getForecast: (days = 7) => {
        const now = Date.now()
        const start = new Date(now)
        start.setHours(0, 0, 0, 0)
        const base = start.getTime()

        const out: ForecastDay[] = []
        for (let i = 0; i < days; i++) {
          const d = new Date(base + i * MS_PER_DAY)
          out.push({
            date: d.toISOString().slice(0, 10),
            label: i === 0 ? 'Today' : d.toLocaleDateString(undefined, { weekday: 'short' }),
            count: 0,
            overdue: 0,
          })
        }

        for (const item of Object.values(get().items)) {
          let idx = Math.floor((item.dueAt - base) / MS_PER_DAY)
          if (idx < 0) idx = 0
          if (idx >= days) continue
          out[idx].count += 1
          if (item.dueAt <= now) out[idx].overdue += 1
        }

        return out
      },

      getSubjectSummary: () => {
        const now = Date.now()
        const bySubject = new Map<string, RevisionStudyItem[]>()

        for (const item of Object.values(get().items)) {
          const list = bySubject.get(item.subject) ?? []
          list.push(item)
          bySubject.set(item.subject, list)
        }

        const summaries: SubjectSummary[] = []
        for (const [subject, list] of bySubject) {
          const breakdowns = list.map((item) => computeRPS(item, now))
          const avgRps = breakdowns.reduce((s, b) => s + b.rps, 0) / list.length
          const dueCount = list.filter((item) => isDue(item, now)).length
          const criticalCount = breakdowns.filter((b) => b.rps >= CRITICAL_RPS_THRESHOLD).length
          const healthPercent = Math.max(
            0,
            Math.min(100, Math.round(100 - avgRps * 0.85 - criticalCount * 8)),
          )

          summaries.push({
            subject,
            itemCount: list.length,
            dueCount,
            criticalCount,
            avgRps: Math.round(avgRps * 10) / 10,
            healthPercent,
          })
        }

        return summaries.sort((a, b) => b.avgRps - a.avgRps)
      },

      getTodayStats: () => {
        const today = todayKey()
        const day = get().dailyStats[today]
        const session = get().session
        const liveSessionMs = session ? Date.now() - session.startedAt + session.sessionMs : 0

        return {
          reviewed: day?.reviewed ?? 0,
          avgRating:
            day && day.reviewed > 0
              ? Math.round((day.totalRating / day.reviewed) * 10) / 10
              : 0,
          sessionMs: (day?.sessionMs ?? 0) + (session ? liveSessionMs : 0),
          streak: get().streak,
        }
      },

      getTodayTimeToRevealStats: () => {
        const today = todayKey()
        const samples = get()
          .reviews.filter((r) => todayKey(r.reviewedAt) === today)
          .map(revealMsFromRecord)
        return aggregateTimeToReveal(samples)
      },

      getItemRevealStats: (itemId) => {
        const itemReviews = get()
          .reviews.filter((r) => r.itemId === itemId)
          .map(revealMsFromRecord)
        const withMs = itemReviews.filter((v): v is number => v != null)
        return {
          lastMs: withMs.length ? withMs[withMs.length - 1]! : null,
          rollingAvgMs: rollingAverageMs(withMs, 5),
          reviewCount: itemReviews.length,
        }
      },

      getItemBreakdown: (itemId) => {
        const item = get().items[itemId]
        if (!item) return null
        return computeRPS(item)
      },

      getCurrentSessionItem: () => {
        const session = get().session
        if (!session) return null
        const id = session.itemIds[session.currentIndex]
        if (!id) return null
        return get().items[id] ?? null
      },
    }),
    {
      name: 'h22-revision-engine-v2',
      partialize: (state) => ({
        items: state.items,
        reviews: state.reviews,
        streak: state.streak,
        lastStudyDate: state.lastStudyDate,
        dailyStats: state.dailyStats,
        sessionHistory: state.sessionHistory,
        showTimeAfterReveal: state.showTimeAfterReveal,
      }),
    },
  ),
)
