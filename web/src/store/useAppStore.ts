import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { buildNavEntries, buildNavRows } from '@/lib/catalog'
import { defaultTab, tabForItemType, type ChapterTab } from '@/lib/chapterTabs'
import { fetchJSON } from '@/lib/data'
import type {
  ChapterData,
  ItemMark,
  NavEntry,
  NavRow,
  RawCatalog,
  SearchResult,
  StudyItem,
} from '@/lib/types'
import { emptyMark, itemMarkLabel, type MarkAxis } from '@/lib/studyMarks'
import {
  aggregateProgress,
  creditDwell,
  creditEngagement,
  itemRequiresExplicitRead,
  resolveChapterIdForItem,
  type EngagementKind,
  type ItemEngagementRecord,
  type ItemStudyContext,
  type OverallProgress,
  type SectionProgress,
} from '@/lib/studyProgress'
import {
  mergeMarks,
  mergeRecord,
  mergeRevisionBackup,
  type RevisionBackup,
  type StudyDataPayload,
} from '@/lib/studyData'
import { useRevisionStore } from '@/stores/revisionStore'
import { applyTheme, buildProgress, engagementInputFromStore, itemSearchText } from '@/store/helpers'

export interface FeedbackCtx {
  chapterId: string
  chapterTitle: string
  label: string
  type: string
}

interface AppState {
  theme: 'light' | 'dark'
  sidebarCollapsed: boolean
  commandOpen: boolean
  catalogLoading: boolean
  chapterLoading: boolean
  catalog: RawCatalog | null
  navEntries: NavEntry[]
  navRows: NavRow[]
  chapters: Record<string, ChapterData>
  progress: Record<string, { completed: number; total: number; engagedMs: number }>
  readItems: Record<string, boolean>
  itemEngagement: Record<string, ItemEngagementRecord>
  chapterTotals: Record<string, number>
  chapterEngagedMs: Record<string, number>
  totalEngagementMs: number
  currentChapterId: string | null
  activeTab: ChapterTab
  scrollToItemId: string | null
  /** The active landing-page section key (null = first section). Lives in the
   * store so the header "due today" badge can open the Revise tab directly. */
  landingTarget: string | null
  revealed: Record<string, boolean>
  bookmarks: Record<string, boolean>
  mcqSelections: Record<string, number | null>
  ratings: Record<string, number>
  flags: Record<string, string>
  feedbackCtx: Record<string, FeedbackCtx>
  marks: Record<string, ItemMark>
  history: (string | null)[]
  historyIndex: number

  initCatalog: () => Promise<void>
  loadChapter: (chapterId: string) => Promise<ChapterData | null>
  selectChapter: (chapterId: string) => Promise<void>
  clearSelection: () => void
  showLanding: (target?: string | null) => void
  setLandingTarget: (target: string | null) => void
  selectItem: (chapterId: string, itemId: string) => Promise<void>
  pushHistory: (id: string | null) => void
  applyHistoryTarget: (id: string | null) => Promise<void>
  goBack: () => void
  goForward: () => void
  canGoBack: () => boolean
  canGoForward: () => boolean
  goNextChapter: () => void
  goPrevChapter: () => void
  setActiveTab: (tab: ChapterTab) => void
  setScrollToItemId: (id: string | null) => void
  toggleReveal: (itemId: string) => void
  selectMcqOption: (itemId: string, option: number) => void
  rateItem: (itemId: string, n: number, ctx?: FeedbackCtx) => void
  flagItem: (itemId: string, comment: string | null, ctx?: FeedbackCtx) => void
  clearFeedback: () => void
  setMark: (itemId: string, axis: MarkAxis, value: string) => void
  markRevised: (itemId: string, ctx?: ItemStudyContext) => void
  markItemRead: (itemId: string, ctx?: ItemStudyContext) => void
  recordSeen: (itemId: string, ctx?: ItemStudyContext) => void
  recordItemReveal: (itemId: string, ctx?: ItemStudyContext) => void
  recordMockExamResponse: (item: StudyItem, value: unknown) => void
  creditItemDwell: (itemId: string, deltaMs: number, dwellAccruedThisVisit: number) => number
  getStudyProgress: () => { overall: OverallProgress; sections: SectionProgress[] }
  getMark: (itemId: string) => ItemMark | undefined
  _recordEngagement: (itemId: string, kind: EngagementKind, chapterIdHint?: string | null) => void
  _rebuildProgress: () => void
  _markCtx: (itemId: string, prev: ItemMark, ctx?: ItemStudyContext) => Partial<ItemMark>
  _resolveChapterId: (itemId: string, explicit?: string | null) => string | null
  exportStudyData: () => StudyDataPayload
  importStudyData: (data: StudyDataPayload, mode: 'merge' | 'replace') => void
  toggleBookmark: (itemId?: string) => void
  toggleTheme: () => void
  toggleSidebar: () => void
  setCommandOpen: (open: boolean) => void
  getSearchResults: (query: string) => SearchResult[]
  getCurrentChapter: () => ChapterData | null
  getNavKind: () => NavEntry['kind'] | null
  isBookmarked: (itemId: string) => boolean
}

export const useAppStore = create<AppState>()(
  persist(
    (set, get) => ({
      theme: 'light',
      sidebarCollapsed: false,
      commandOpen: false,
      catalogLoading: true,
      chapterLoading: false,
      catalog: null,
      navEntries: [],
      navRows: [],
      chapters: {},
      progress: {},
      currentChapterId: null,
      activeTab: 'notes',
      scrollToItemId: null,
      landingTarget: null,
      revealed: {},
      bookmarks: {},
      mcqSelections: {},
      ratings: {},
      flags: {},
      feedbackCtx: {},
      marks: {},
      readItems: {},
      itemEngagement: {},
      chapterTotals: {},
      chapterEngagedMs: {},
      totalEngagementMs: 0,
      history: [null],
      historyIndex: 0,

      initCatalog: async () => {
        set({ catalogLoading: true })
        try {
          const catalog = await fetchJSON<RawCatalog>('index.json')
          const navRows = buildNavRows(catalog)
          const navEntries = buildNavEntries(catalog)
          const s = get()
          set({
            catalog,
            navRows,
            navEntries,
            progress: buildProgress(
              navEntries,
              s.chapters,
              engagementInputFromStore(s),
              s.chapterEngagedMs,
            ),
            catalogLoading: false,
          })
          applyTheme(get().theme)
        } catch {
          set({ catalogLoading: false })
        }
      },

      loadChapter: async (chapterId) => {
        const { chapters, navEntries } = get()
        if (chapters[chapterId]) return chapters[chapterId]

        const entry = navEntries.find((e) => e.id === chapterId)
        if (!entry) return null

        set({ chapterLoading: true })
        try {
          const data = await fetchJSON<ChapterData>(entry.file)
          const nextChapters = { ...get().chapters, [chapterId]: data }
          const chapterTotals = {
            ...get().chapterTotals,
            [chapterId]: data.items.length,
          }
          const s = get()
          set({
            chapters: nextChapters,
            chapterTotals,
            progress: buildProgress(
              s.navEntries,
              nextChapters,
              engagementInputFromStore(s),
              s.chapterEngagedMs,
            ),
            chapterLoading: false,
          })
          return data
        } catch {
          set({ chapterLoading: false })
          return null
        }
      },

      // Record a destination on the navigation history stack, truncating any
      // forward entries (standard back/forward behaviour). No-op if unchanged.
      pushHistory: (id: string | null) => {
        const { history, historyIndex } = get()
        if (history[historyIndex] === id) return
        const next = history.slice(0, historyIndex + 1)
        next.push(id)
        set({ history: next, historyIndex: next.length - 1 })
      },

      selectChapter: async (chapterId) => {
        const data = await get().loadChapter(chapterId)
        if (!data) return
        const entry = get().navEntries.find((e) => e.id === chapterId)
        const kind = entry?.kind ?? 'harrison'
        set({
          currentChapterId: chapterId,
          activeTab: defaultTab(data, kind),
          scrollToItemId: null,
        })
        get().pushHistory(chapterId)
      },

      clearSelection: () => {
        set({ currentChapterId: null, scrollToItemId: null })
        get().pushHistory(null)
      },

      // Go to the landing page and ask it to open a specific section (e.g. the
      // Revise tab) — used by the app-wide "due today" badge.
      showLanding: (target = null) => {
        set({ currentChapterId: null, scrollToItemId: null, landingTarget: target })
        get().pushHistory(null)
      },

      setLandingTarget: (target) => set({ landingTarget: target }),

      selectItem: async (chapterId, itemId) => {
        const data = await get().loadChapter(chapterId)
        if (!data) return
        const item = data.items.find((i) => i.id === itemId)
        if (!item) return
        set({
          currentChapterId: chapterId,
          activeTab: tabForItemType(item.type),
          scrollToItemId: itemId,
        })
        get().pushHistory(chapterId)
      },

      // Move along the history stack WITHOUT recording a new entry.
      applyHistoryTarget: async (id: string | null) => {
        if (id === null) {
          set({ currentChapterId: null, scrollToItemId: null })
          return
        }
        const data = await get().loadChapter(id)
        const entry = get().navEntries.find((e) => e.id === id)
        const kind = entry?.kind ?? 'harrison'
        set({
          currentChapterId: id,
          activeTab: data ? defaultTab(data, kind) : get().activeTab,
          scrollToItemId: null,
        })
      },

      goBack: () => {
        const { historyIndex, history } = get()
        if (historyIndex <= 0) return
        const newIndex = historyIndex - 1
        set({ historyIndex: newIndex })
        get().applyHistoryTarget(history[newIndex])
      },

      goForward: () => {
        const { historyIndex, history } = get()
        if (historyIndex >= history.length - 1) return
        const newIndex = historyIndex + 1
        set({ historyIndex: newIndex })
        get().applyHistoryTarget(history[newIndex])
      },

      canGoBack: () => get().historyIndex > 0,
      canGoForward: () => get().historyIndex < get().history.length - 1,

      goNextChapter: () => {
        const { currentChapterId, navEntries } = get()
        if (!currentChapterId) return
        const idx = navEntries.findIndex((e) => e.id === currentChapterId)
        if (idx >= 0 && idx < navEntries.length - 1) {
          get().selectChapter(navEntries[idx + 1].id)
        }
      },

      goPrevChapter: () => {
        const { currentChapterId, navEntries } = get()
        if (!currentChapterId) return
        const idx = navEntries.findIndex((e) => e.id === currentChapterId)
        if (idx > 0) {
          get().selectChapter(navEntries[idx - 1].id)
        }
      },

      setActiveTab: (tab) => set({ activeTab: tab }),

      setScrollToItemId: (id) => set({ scrollToItemId: id }),

      toggleReveal: (itemId) => {
        if (get().revealed[itemId]) {
          set({ revealed: { ...get().revealed, [itemId]: false } })
          get()._rebuildProgress()
          return
        }
        get().recordItemReveal(itemId)
      },

      selectMcqOption: (itemId, option) => {
        const hadAnswer = get().mcqSelections[itemId] != null
        set({
          mcqSelections: { ...get().mcqSelections, [itemId]: option },
          revealed: { ...get().revealed, [itemId]: true },
        })
        get().recordSeen(itemId)
        if (!hadAnswer) get()._recordEngagement(itemId, 'answer')
        get()._rebuildProgress()
      },

      recordItemReveal: (itemId, ctx) => {
        const itemType = ctx?.itemType
        if (itemType && itemRequiresExplicitRead(itemType)) {
          if (!get().readItems[itemId]) {
            get().markItemRead(itemId, ctx)
          }
          return
        }

        if (get().revealed[itemId]) return

        set({ revealed: { ...get().revealed, [itemId]: true } })
        get().recordSeen(itemId, ctx)
        get()._recordEngagement(itemId, 'reveal', ctx?.chapterId)
        get()._rebuildProgress()
      },

      recordMockExamResponse: (item, value) => {
        if (value === undefined || value === null || value === '') return

        const itemId = item.id
        const ctx: ItemStudyContext = {
          chapterId: resolveChapterIdForItem(itemId, {
            marks: get().marks,
            currentChapterId: get().currentChapterId,
          }) ?? undefined,
          itemType: item.type,
        }

        get().recordSeen(itemId, ctx)

        if (item.type === 'mcq' && typeof value === 'number') {
          const hadAnswer = get().mcqSelections[itemId] != null
          set({
            mcqSelections: { ...get().mcqSelections, [itemId]: value },
            revealed: { ...get().revealed, [itemId]: true },
          })
          if (!hadAnswer) get()._recordEngagement(itemId, 'mock', ctx.chapterId)
        } else {
          const wasRevealed = get().revealed[itemId]
          if (!wasRevealed) {
            set({ revealed: { ...get().revealed, [itemId]: true } })
            get()._recordEngagement(itemId, 'mock', ctx.chapterId)
          }
        }
        get()._rebuildProgress()
      },

      rateItem: (itemId, n, ctx) => {
        const ratings = { ...get().ratings }
        const feedbackCtx = { ...get().feedbackCtx }
        if (n > 0) {
          ratings[itemId] = n
          if (ctx) feedbackCtx[itemId] = ctx
        } else {
          delete ratings[itemId]
          if (!get().flags[itemId]) delete feedbackCtx[itemId]
        }
        set({ ratings, feedbackCtx })
      },

      flagItem: (itemId, comment, ctx) => {
        const flags = { ...get().flags }
        const feedbackCtx = { ...get().feedbackCtx }
        if (comment === null) {
          delete flags[itemId]
          if (!get().ratings[itemId]) delete feedbackCtx[itemId]
        } else {
          flags[itemId] = comment
          if (ctx) feedbackCtx[itemId] = ctx
        }
        set({ flags, feedbackCtx })
      },

      clearFeedback: () => set({ ratings: {}, flags: {}, feedbackCtx: {} }),

      setMark: (itemId, axis, value) => {
        const marks = { ...get().marks }
        const prev = marks[itemId] ?? emptyMark()
        const next: ItemMark = { ...prev }
        const rec = next as unknown as Record<string, unknown>
        // tap the active side again to clear it
        if (rec[axis] === value) {
          delete rec[axis]
        } else {
          rec[axis] = value
        }
        // a mark is an interaction → the item counts as "done" (esp. notes)
        const engaging = next.timesDone === 0
        if (engaging) {
          next.timesDone = 1
          next.firstSeenAt = Date.now()
        }
        next.lastSeenAt = Date.now()
        Object.assign(next, get()._markCtx(itemId, prev))
        marks[itemId] = next
        set({ marks })
        if (engaging) get()._recordEngagement(itemId, 'mark')
        get()._rebuildProgress()
      },

      markRevised: (itemId, ctx) => {
        const marks = { ...get().marks }
        const prev = marks[itemId] ?? emptyMark()
        const next: ItemMark = {
          ...prev,
          timesDone: prev.timesDone === 0 ? 1 : prev.timesDone,
          timesRevised: prev.timesRevised + 1,
          firstSeenAt: prev.firstSeenAt ?? Date.now(),
          lastSeenAt: Date.now(),
        }
        Object.assign(next, get()._markCtx(itemId, prev, ctx))
        marks[itemId] = next
        set({ marks })
        get()._recordEngagement(itemId, 'revise', ctx?.chapterId)
        get()._rebuildProgress()
      },

      markItemRead: (itemId, ctx) => {
        if (get().readItems[itemId]) return
        set({ readItems: { ...get().readItems, [itemId]: true } })
        get().recordSeen(itemId, ctx)
        get()._recordEngagement(itemId, 'read', ctx?.chapterId)
        get()._rebuildProgress()
      },

      recordSeen: (itemId, ctx) => {
        const prev = get().marks[itemId]
        if (prev && prev.timesDone > 0) {
          const next = {
            ...prev,
            lastSeenAt: Date.now(),
            ...get()._markCtx(itemId, prev, ctx),
          }
          set({ marks: { ...get().marks, [itemId]: next } })
          return
        }
        const base = prev ?? emptyMark()
        const next: ItemMark = {
          ...base,
          timesDone: 1,
          firstSeenAt: base.firstSeenAt ?? Date.now(),
          lastSeenAt: Date.now(),
          ...get()._markCtx(itemId, base, ctx),
        }
        set({ marks: { ...get().marks, [itemId]: next } })
      },

      // Resolve chapter context for a mark from the loaded chapter, preserving any
      // context already stored. Returns a partial to merge into the mark.
      _markCtx: (itemId, prev, ctx) => {
        if (ctx?.chapterId) {
          return {
            chapterId: ctx.chapterId,
            chapterTitle: ctx.chapterTitle ?? prev.chapterTitle,
            label: ctx.label ?? prev.label,
            itemType: ctx.itemType ?? prev.itemType,
          }
        }
        if (prev.chapterId) return {}
        const chapterId = get()._resolveChapterId(itemId)
        const chapter = chapterId ? get().chapters[chapterId] : get().getCurrentChapter()
        const resolvedId = chapterId ?? get().currentChapterId
        if (!resolvedId || !chapter) {
          if (resolvedId) return { chapterId: resolvedId }
          return {}
        }
        const item = chapter.items.find((i) => i.id === itemId)
        if (!item) return { chapterId: resolvedId, chapterTitle: chapter.title }
        return {
          chapterId: resolvedId,
          chapterTitle: chapter.title,
          label: itemMarkLabel(item),
          itemType: item.type,
        }
      },

      _resolveChapterId: (itemId, explicit) =>
        resolveChapterIdForItem(itemId, {
          explicit,
          marks: get().marks,
          currentChapterId: get().currentChapterId,
        }),

      getMark: (itemId) => get().marks[itemId],

      _recordEngagement: (itemId, kind, chapterIdHint) => {
        const at = Date.now()
        const prev = get().itemEngagement[itemId]
        const record = creditEngagement(prev, kind, at)
        const chapterId = get()._resolveChapterId(itemId, chapterIdHint)
        const chapterEngagedMs = { ...get().chapterEngagedMs }
        let totalEngagementMs = get().totalEngagementMs
        const baseAdded = record.engagedMs - (prev?.engagedMs ?? 0)

        if (chapterId && baseAdded > 0) {
          chapterEngagedMs[chapterId] = (chapterEngagedMs[chapterId] ?? 0) + baseAdded
        }
        totalEngagementMs += baseAdded

        set({
          itemEngagement: { ...get().itemEngagement, [itemId]: record },
          chapterEngagedMs,
          totalEngagementMs,
        })
      },

      creditItemDwell: (itemId, deltaMs, dwellAccruedThisVisit) => {
        const prev = get().itemEngagement[itemId]
        if (!prev) return 0
        const { record, dwellAdded } = creditDwell(prev, deltaMs, dwellAccruedThisVisit)
        if (dwellAdded <= 0) return 0

        const chapterId = get()._resolveChapterId(itemId)
        const chapterEngagedMs = { ...get().chapterEngagedMs }
        if (chapterId) {
          chapterEngagedMs[chapterId] = (chapterEngagedMs[chapterId] ?? 0) + dwellAdded
        }

        set({
          itemEngagement: { ...get().itemEngagement, [itemId]: record },
          chapterEngagedMs,
          totalEngagementMs: get().totalEngagementMs + dwellAdded,
        })
        get()._rebuildProgress()
        return dwellAdded
      },

      _rebuildProgress: () => {
        const s = get()
        set({
          progress: buildProgress(
            s.navEntries,
            s.chapters,
            engagementInputFromStore(s),
            s.chapterEngagedMs,
          ),
        })
      },

      getStudyProgress: () => {
        const s = get()
        return aggregateProgress(
          s.navRows,
          s.chapters,
          s.chapterTotals,
          s.chapterEngagedMs,
          engagementInputFromStore(s),
        )
      },

      // Snapshot every per-item map the user has generated, for backup/export —
      // including the revision engine's persisted slice (FSRS cards, review
      // history, streaks, daily stats) so a restore loses no progress.
      exportStudyData: () => {
        const s = get()
        const rev = useRevisionStore.getState()
        return {
          marks: s.marks,
          ratings: s.ratings,
          flags: s.flags,
          feedbackCtx: s.feedbackCtx,
          bookmarks: s.bookmarks,
          mcqSelections: s.mcqSelections,
          revealed: s.revealed,
          readItems: s.readItems,
          itemEngagement: s.itemEngagement,
          chapterTotals: s.chapterTotals,
          chapterEngagedMs: s.chapterEngagedMs,
          totalEngagementMs: s.totalEngagementMs,
          revision: {
            items: rev.items,
            reviews: rev.reviews,
            streak: rev.streak,
            lastStudyDate: rev.lastStudyDate,
            dailyStats: rev.dailyStats,
            sessionHistory: rev.sessionHistory,
            showTimeAfterReveal: rev.showTimeAfterReveal,
          },
        }
      },

      // Restore a backup. 'replace' overwrites each provided map wholesale;
      // 'merge' folds it into the current state (marks merge by recency, the
      // rest let incoming entries win on a conflict). Maps absent from the
      // backup are left untouched in both modes.
      importStudyData: (data, mode) => {
        const s = get()
        const fc = (data.feedbackCtx ?? {}) as Record<string, FeedbackCtx>
        const next =
          mode === 'replace'
            ? {
                marks: data.marks ?? s.marks,
                ratings: data.ratings ?? s.ratings,
                flags: data.flags ?? s.flags,
                feedbackCtx: data.feedbackCtx ? fc : s.feedbackCtx,
                bookmarks: data.bookmarks ?? s.bookmarks,
                mcqSelections: data.mcqSelections ?? s.mcqSelections,
                revealed: data.revealed ?? s.revealed,
                readItems: data.readItems ?? s.readItems,
                itemEngagement: data.itemEngagement ?? s.itemEngagement,
                chapterTotals: data.chapterTotals ?? s.chapterTotals,
                chapterEngagedMs: data.chapterEngagedMs ?? s.chapterEngagedMs,
                totalEngagementMs: data.totalEngagementMs ?? s.totalEngagementMs,
              }
            : {
                marks: mergeMarks(s.marks, data.marks),
                ratings: mergeRecord(s.ratings, data.ratings),
                flags: mergeRecord(s.flags, data.flags),
                feedbackCtx: mergeRecord(s.feedbackCtx, fc),
                bookmarks: mergeRecord(s.bookmarks, data.bookmarks),
                mcqSelections: mergeRecord(s.mcqSelections, data.mcqSelections),
                revealed: mergeRecord(s.revealed, data.revealed),
                readItems: mergeRecord(s.readItems, data.readItems),
                itemEngagement: mergeRecord(s.itemEngagement, data.itemEngagement),
                chapterTotals: mergeRecord(s.chapterTotals, data.chapterTotals),
                chapterEngagedMs: mergeRecord(s.chapterEngagedMs, data.chapterEngagedMs),
                totalEngagementMs: Math.max(
                  s.totalEngagementMs,
                  data.totalEngagementMs ?? 0,
                ),
              }
        set(next)
        get()._rebuildProgress()

        // Restore the revision engine slice into its own store (persists itself).
        if (data.revision) {
          const rev = useRevisionStore.getState()
          const current: RevisionBackup = {
            items: rev.items,
            reviews: rev.reviews,
            streak: rev.streak,
            lastStudyDate: rev.lastStudyDate,
            dailyStats: rev.dailyStats,
            sessionHistory: rev.sessionHistory,
            showTimeAfterReveal: rev.showTimeAfterReveal,
          }
          const merged = mergeRevisionBackup(current, data.revision, mode)
          useRevisionStore.setState({
            items: merged.items,
            reviews: merged.reviews,
            streak: merged.streak,
            lastStudyDate: merged.lastStudyDate,
            dailyStats: merged.dailyStats,
            sessionHistory: merged.sessionHistory,
            showTimeAfterReveal: merged.showTimeAfterReveal,
          })
        }
      },

      toggleBookmark: (itemId) => {
        if (!itemId) return
        set({ bookmarks: { ...get().bookmarks, [itemId]: !get().bookmarks[itemId] } })
      },

      toggleTheme: () => {
        const theme = get().theme === 'light' ? 'dark' : 'light'
        applyTheme(theme)
        set({ theme })
      },

      toggleSidebar: () => set({ sidebarCollapsed: !get().sidebarCollapsed }),

      setCommandOpen: (open) => set({ commandOpen: open }),

      getSearchResults: (query) => {
        const { navEntries, chapters } = get()
        if (!query.trim()) return []
        const q = query.toLowerCase()
        const results: SearchResult[] = []

        for (const entry of navEntries) {
          if (
            entry.title.toLowerCase().includes(q) ||
            entry.subtitle.toLowerCase().includes(q) ||
            entry.sectionTitle.toLowerCase().includes(q)
          ) {
            results.push({
              id: `ch-${entry.id}`,
              kind: 'chapter',
              label: entry.title,
              subtitle: entry.subtitle,
              chapterId: entry.id,
            })
          }
          const data = chapters[entry.id]
          if (!data) continue
          data.items.forEach((item, index) => {
            const text = itemSearchText(item)
            if (text.toLowerCase().includes(q) || item.id.toLowerCase().includes(q)) {
              results.push({
                id: item.id,
                kind: 'item',
                label: text.slice(0, 72) + (text.length > 72 ? '…' : ''),
                subtitle: `${entry.title} · #${index + 1}`,
                chapterId: entry.id,
                itemId: item.id,
              })
            }
          })
        }
        return results.slice(0, 24)
      },

      getCurrentChapter: () => {
        const { currentChapterId, chapters } = get()
        if (!currentChapterId) return null
        return chapters[currentChapterId] ?? null
      },

      getNavKind: () => {
        const { currentChapterId, navEntries } = get()
        if (!currentChapterId) return null
        return navEntries.find((e) => e.id === currentChapterId)?.kind ?? null
      },

      isBookmarked: (itemId) => Boolean(get().bookmarks[itemId]),
    }),
    {
      name: 'h22-ui-store',
      // Note: currentChapterId / activeTab are intentionally NOT persisted so
      // the app always opens on the landing page (all sections), never a stale
      // or half-loaded chapter.
      partialize: (state) => ({
        theme: state.theme,
        sidebarCollapsed: state.sidebarCollapsed,
        revealed: state.revealed,
        bookmarks: state.bookmarks,
        mcqSelections: state.mcqSelections,
        ratings: state.ratings,
        flags: state.flags,
        feedbackCtx: state.feedbackCtx,
        marks: state.marks,
        readItems: state.readItems,
        itemEngagement: state.itemEngagement,
        chapterTotals: state.chapterTotals,
        chapterEngagedMs: state.chapterEngagedMs,
        totalEngagementMs: state.totalEngagementMs,
      }),
      // Drop any previously persisted selection so reloads land on the home
      // page even for users whose old localStorage still holds currentChapterId.
      merge: (persisted, current) => ({
        ...current,
        ...(persisted as Partial<AppState>),
        currentChapterId: null,
        activeTab: current.activeTab,
        scrollToItemId: null,
      }),
      onRehydrateStorage: () => (state) => {
        if (state) applyTheme(state.theme)
      },
    },
  ),
)
