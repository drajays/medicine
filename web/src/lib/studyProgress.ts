import type { HeaderKind, ItemMark, NavRow, StudyItem } from '@/lib/types'

/**
 * Engagement rules — scrolling alone never counts.
 *
 * An item is ENGAGED (counts toward completion) when ANY of:
 *   • revealed[itemId]           — answer revealed / question attempted
 *   • mcqSelections[itemId] set    — MCQ option chosen
 *   • readItems[itemId]          — explicit "Mark as read" (notes, why/how)
 *   • marks[itemId].timesDone>0  — any study-mark toggle on the item
 *
 * Time credit (engagedMs) accrues ONLY on qualifying actions + bounded
 * post-engage dwell while the item is ≥50% visible and the tab is active.
 * Passive scrolling past an item awards zero time.
 */

export interface ItemStudyContext {
  chapterId?: string
  chapterTitle?: string
  label?: string
  itemType?: string
}

/** Derive catalog chapter id from item id when that chapter is not open. */
export function resolveChapterIdForItem(
  itemId: string,
  hints: {
    explicit?: string | null
    marks?: Record<string, ItemMark>
    currentChapterId?: string | null
  } = {},
): string | null {
  if (hints.explicit) return hints.explicit
  const fromMark = hints.marks?.[itemId]?.chapterId
  if (fromMark) return fromMark
  if (hints.currentChapterId && itemId.startsWith(`${hints.currentChapterId}-`)) {
    return hints.currentChapterId
  }
  const m = itemId.match(/^(pe-cr-\d+|tr-nejm-\d+|tr-\d+|ht-\d+|cr-\d+|story-\d+|h[12]-\d+)/)
  if (m) return m[1]
  return hints.currentChapterId ?? null
}

export type EngagementKind = 'reveal' | 'answer' | 'mark' | 'read' | 'revise' | 'mock'

/** Base milliseconds credited per explicit engagement action. */
export const ENGAGEMENT_BASE_MS: Record<EngagementKind, number> = {
  reveal: 45_000,
  answer: 60_000,
  mark: 30_000,
  read: 75_000,
  revise: 45_000,
  mock: 60_000,
}

/** Max extra dwell time per item per chapter visit (after first engage). */
export const DWELL_CAP_PER_VISIT_MS = 90_000

/** Dwell tick interval while item stays in view after engage. */
export const DWELL_TICK_MS = 5_000

export interface ItemEngagementRecord {
  engagedMs: number
  engagementCount: number
  firstEngagedAt?: number
  lastEngagedAt?: number
  kinds: EngagementKind[]
}

export interface ChapterProgress {
  completed: number
  total: number
  percent: number
  engagedMs: number
}

export interface SectionProgress {
  key: string
  title: string
  kind: HeaderKind
  completed: number
  total: number
  percent: number
  engagedMs: number
  chapters: Array<ChapterProgress & { id: string; title: string }>
}

export interface OverallProgress {
  completed: number
  total: number
  percent: number
  engagedMs: number
  chaptersStarted: number
  chaptersComplete: number
}

export interface EngagementInput {
  revealed: Record<string, boolean>
  readItems: Record<string, boolean>
  mcqSelections: Record<string, number | null>
  marks: Record<string, ItemMark>
}

export function itemRequiresExplicitRead(type: string): boolean {
  return type === 'note' || type === 'why' || type === 'how'
}

export function isItemEngaged(
  itemId: string,
  input: EngagementInput,
): boolean {
  if (input.revealed[itemId]) return true
  if (input.readItems[itemId]) return true
  if (input.mcqSelections[itemId] != null) return true
  const mark = input.marks[itemId]
  if (mark && mark.timesDone > 0) return true
  return false
}

/** Count engaged items in a chapter, including when JSON is not loaded (id prefix / mark.chapterId). */
export function countEngagedForChapter(
  chapterId: string,
  items: StudyItem[],
  input: EngagementInput,
): number {
  if (items.length) return countEngagedItems(items, input)

  const ids = new Set<string>()
  const belongs = (id: string) =>
    id.startsWith(`${chapterId}-`) || input.marks[id]?.chapterId === chapterId

  for (const id of Object.keys(input.marks)) {
    if (belongs(id) && isItemEngaged(id, input)) ids.add(id)
  }
  for (const id of Object.keys(input.revealed)) {
    if (belongs(id) && isItemEngaged(id, input)) ids.add(id)
  }
  for (const id of Object.keys(input.readItems)) {
    if (belongs(id) && input.readItems[id]) ids.add(id)
  }
  for (const id of Object.keys(input.mcqSelections)) {
    if (belongs(id) && isItemEngaged(id, input)) ids.add(id)
  }
  return ids.size
}

export function countEngagedItems(
  items: StudyItem[],
  input: EngagementInput,
): number {
  return items.filter((i) => isItemEngaged(i.id, input)).length
}

export function buildChapterProgress(
  items: StudyItem[],
  input: EngagementInput,
  engagedMs: number,
): ChapterProgress {
  const total = items.length
  const completed = countEngagedItems(items, input)
  return {
    completed,
    total,
    percent: total > 0 ? Math.round((completed / total) * 100) : 0,
    engagedMs,
  }
}

const TOP_LEVEL: HeaderKind[] = [
  'hot_topics',
  'case_reports',
  'pediatric_endo',
  'sub_apps',
  'stories',
  'calculators',
  'imaging_resources',
  'trials',
  'harrison_banner',
]

export function aggregateProgress(
  navRows: NavRow[],
  chapters: Record<string, { items: StudyItem[] }>,
  chapterTotals: Record<string, number>,
  chapterEngagedMs: Record<string, number>,
  input: EngagementInput,
): {
  overall: OverallProgress
  sections: SectionProgress[]
  byChapter: Record<string, ChapterProgress>
} {
  const byChapter: Record<string, ChapterProgress> = {}
  const sections: SectionProgress[] = []

  let currentSection: SectionProgress | null = null
  let overallCompleted = 0
  let overallTotal = 0
  let overallMs = 0
  let chaptersStarted = 0
  let chaptersComplete = 0

  for (const row of navRows) {
    if (row.type === 'header' && TOP_LEVEL.includes(row.headerKind)) {
      currentSection = {
        key: row.id,
        title: row.title,
        kind: row.headerKind,
        completed: 0,
        total: 0,
        percent: 0,
        engagedMs: 0,
        chapters: [],
      }
      sections.push(currentSection)
      continue
    }

    if (row.type !== 'entry' || !currentSection) continue

    const entry = row.entry
    const data = chapters[entry.id]
    const items = data?.items ?? []
    const total = items.length > 0 ? items.length : (chapterTotals[entry.id] ?? 0)
    const completed = countEngagedForChapter(entry.id, items, input)
    const ms = chapterEngagedMs[entry.id] ?? 0

    const chapterProg: ChapterProgress & { id: string; title: string } = {
      id: entry.id,
      title: entry.title,
      completed,
      total,
      percent: total > 0 ? Math.round((completed / total) * 100) : 0,
      engagedMs: ms,
    }

    byChapter[entry.id] = chapterProg
    currentSection.chapters.push(chapterProg)
    currentSection.completed += completed
    currentSection.total += total
    currentSection.engagedMs += ms

    overallCompleted += completed
    overallTotal += total
    overallMs += ms

    if (completed > 0) chaptersStarted += 1
    if (total > 0 && completed >= total) chaptersComplete += 1
  }

  for (const section of sections) {
    section.percent =
      section.total > 0 ? Math.round((section.completed / section.total) * 100) : 0
  }

  return {
    overall: {
      completed: overallCompleted,
      total: overallTotal,
      percent: overallTotal > 0 ? Math.round((overallCompleted / overallTotal) * 100) : 0,
      engagedMs: overallMs,
      chaptersStarted,
      chaptersComplete,
    },
    sections: sections.filter((s) => s.total > 0 || s.chapters.some((c) => c.completed > 0)),
    byChapter,
  }
}

export function formatStudyDuration(ms: number): string {
  if (ms < 60_000) return `${Math.max(1, Math.round(ms / 1000))}s`
  const mins = Math.floor(ms / 60_000)
  if (mins < 60) return `${mins}m`
  const hrs = Math.floor(mins / 60)
  const rem = mins % 60
  return rem > 0 ? `${hrs}h ${rem}m` : `${hrs}h`
}

export function creditEngagement(
  prev: ItemEngagementRecord | undefined,
  kind: EngagementKind,
  at: number,
): ItemEngagementRecord {
  const base = ENGAGEMENT_BASE_MS[kind]
  const kinds = prev?.kinds ?? []
  return {
    engagedMs: (prev?.engagedMs ?? 0) + base,
    engagementCount: (prev?.engagementCount ?? 0) + 1,
    firstEngagedAt: prev?.firstEngagedAt ?? at,
    lastEngagedAt: at,
    kinds: kinds.includes(kind) ? kinds : [...kinds, kind],
  }
}

export function creditDwell(
  prev: ItemEngagementRecord,
  deltaMs: number,
  dwellAccruedThisVisit: number,
): { record: ItemEngagementRecord; dwellAdded: number } {
  const room = DWELL_CAP_PER_VISIT_MS - dwellAccruedThisVisit
  const dwellAdded = Math.min(deltaMs, room)
  if (dwellAdded <= 0) return { record: prev, dwellAdded: 0 }
  return {
    record: {
      ...prev,
      engagedMs: prev.engagedMs + dwellAdded,
      lastEngagedAt: Date.now(),
    },
    dwellAdded,
  }
}
