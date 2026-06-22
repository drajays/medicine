import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { buildNavEntries, buildNavRows } from '@/lib/catalog'
import { fetchJSON } from '@/lib/data'
import type {
  ChapterData,
  NavEntry,
  NavRow,
  RawCatalog,
  SearchResult,
  StudyItem,
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
  currentItemIndex: number
  revealed: Record<string, boolean>
  bookmarks: Record<string, boolean>
  mcqSelections: Record<string, number | null>

  initCatalog: () => Promise<void>
  loadChapter: (chapterId: string) => Promise<ChapterData | null>
  selectChapter: (chapterId: string) => Promise<void>
  clearSelection: () => void
  selectItem: (chapterId: string, itemIndex: number) => void
  goNext: () => void
  goPrev: () => void
  toggleReveal: (itemId?: string) => void
  selectMcqOption: (itemId: string, option: number) => void
  toggleBookmark: (itemId?: string) => void
  toggleTheme: () => void
  toggleSidebar: () => void
  setCommandOpen: (open: boolean) => void
  getSearchResults: (query: string) => SearchResult[]
  getCurrentItem: () => StudyItem | null
  getCurrentChapter: () => ChapterData | null
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
      currentItemIndex: 0,
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
        set({ currentChapterId: chapterId, currentItemIndex: 0 })
      },

      clearSelection: () => {
        set({ currentChapterId: null, currentItemIndex: 0 })
      },

      selectItem: async (chapterId, itemIndex) => {
        await get().loadChapter(chapterId)
        set({ currentChapterId: chapterId, currentItemIndex: itemIndex })
      },

      goNext: () => {
        const { currentChapterId, currentItemIndex, chapters, navEntries } = get()
        if (!currentChapterId) return
        const items = chapters[currentChapterId]?.items ?? []
        if (currentItemIndex < items.length - 1) {
          set({ currentItemIndex: currentItemIndex + 1 })
          return
        }
        const idx = navEntries.findIndex((e) => e.id === currentChapterId)
        if (idx >= 0 && idx < navEntries.length - 1) {
          const nextId = navEntries[idx + 1].id
          get().selectChapter(nextId)
        }
      },

      goPrev: async () => {
        const { currentChapterId, currentItemIndex, navEntries } = get()
        if (!currentChapterId) return
        if (currentItemIndex > 0) {
          set({ currentItemIndex: currentItemIndex - 1 })
          return
        }
        const idx = navEntries.findIndex((e) => e.id === currentChapterId)
        if (idx > 0) {
          const prevId = navEntries[idx - 1].id
          await get().loadChapter(prevId)
          const prevItems = get().chapters[prevId]?.items ?? []
          set({
            currentChapterId: prevId,
            currentItemIndex: Math.max(prevItems.length - 1, 0),
          })
        }
      },

      toggleReveal: (itemId) => {
        const item = itemId ? null : get().getCurrentItem()
        const id = itemId ?? item?.id
        if (!id) return
        const revealed = { ...get().revealed, [id]: !get().revealed[id] }
        const { navEntries, chapters } = get()
        set({
          revealed,
          progress: buildProgress(navEntries, chapters, revealed),
        })
      },

      selectMcqOption: (itemId, option) => {
        set({ mcqSelections: { ...get().mcqSelections, [itemId]: option } })
      },

      toggleBookmark: (itemId) => {
        const id = itemId ?? get().getCurrentItem()?.id
        if (!id) return
        set({ bookmarks: { ...get().bookmarks, [id]: !get().bookmarks[id] } })
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
                subtitle: `${entry.title} · Q${index + 1}`,
                chapterId: entry.id,
                itemIndex: index,
              })
            }
          })
        }
        return results.slice(0, 24)
      },

      getCurrentItem: () => {
        const { currentChapterId, currentItemIndex, chapters } = get()
        if (!currentChapterId) return null
        return chapters[currentChapterId]?.items[currentItemIndex] ?? null
      },

      getCurrentChapter: () => {
        const { currentChapterId, chapters } = get()
        if (!currentChapterId) return null
        return chapters[currentChapterId] ?? null
      },

      isBookmarked: (itemId) => Boolean(get().bookmarks[itemId]),
    }),
    {
      name: 'h22-ui-store',
      partialize: (state) => ({
        theme: state.theme,
        sidebarCollapsed: state.sidebarCollapsed,
        revealed: state.revealed,
        bookmarks: state.bookmarks,
        mcqSelections: state.mcqSelections,
        currentChapterId: state.currentChapterId,
        currentItemIndex: state.currentItemIndex,
      }),
      onRehydrateStorage: () => (state) => {
        if (state) applyTheme(state.theme)
      },
    },
  ),
)
