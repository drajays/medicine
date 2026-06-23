import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { buildNavEntries, buildNavRows } from '@/lib/catalog'
import { defaultTab, tabForItemType, type ChapterTab } from '@/lib/chapterTabs'
import { fetchJSON } from '@/lib/data'
import type {
  ChapterData,
  NavEntry,
  NavRow,
  RawCatalog,
  SearchResult,
} from '@/lib/types'
import { applyTheme, buildProgress, itemSearchText } from '@/store/helpers'

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
  progress: Record<string, { completed: number; total: number }>
  currentChapterId: string | null
  activeTab: ChapterTab
  scrollToItemId: string | null
  revealed: Record<string, boolean>
  bookmarks: Record<string, boolean>
  mcqSelections: Record<string, number | null>

  initCatalog: () => Promise<void>
  loadChapter: (chapterId: string) => Promise<ChapterData | null>
  selectChapter: (chapterId: string) => Promise<void>
  clearSelection: () => void
  selectItem: (chapterId: string, itemId: string) => Promise<void>
  goNextChapter: () => void
  goPrevChapter: () => void
  setActiveTab: (tab: ChapterTab) => void
  setScrollToItemId: (id: string | null) => void
  toggleReveal: (itemId: string) => void
  selectMcqOption: (itemId: string, option: number) => void
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
      revealed: {},
      bookmarks: {},
      mcqSelections: {},

      initCatalog: async () => {
        set({ catalogLoading: true })
        try {
          const catalog = await fetchJSON<RawCatalog>('index.json')
          const navRows = buildNavRows(catalog)
          const navEntries = buildNavEntries(catalog)
          const { revealed, chapters } = get()
          set({
            catalog,
            navRows,
            navEntries,
            progress: buildProgress(navEntries, chapters, revealed),
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
          const { revealed, navEntries: nav } = get()
          set({
            chapters: nextChapters,
            progress: buildProgress(nav, nextChapters, revealed),
            chapterLoading: false,
          })
          return data
        } catch {
          set({ chapterLoading: false })
          return null
        }
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
      },

      clearSelection: () => {
        set({ currentChapterId: null, scrollToItemId: null })
      },

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
      },

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
        const revealed = { ...get().revealed, [itemId]: !get().revealed[itemId] }
        const { navEntries, chapters } = get()
        set({
          revealed,
          progress: buildProgress(navEntries, chapters, revealed),
        })
      },

      selectMcqOption: (itemId, option) => {
        const revealed = { ...get().revealed, [itemId]: true }
        set({
          mcqSelections: { ...get().mcqSelections, [itemId]: option },
          revealed,
          progress: buildProgress(get().navEntries, get().chapters, revealed),
        })
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
