import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { Catalog, ChapterData, SearchResult, StudyItem } from '@/lib/types'
import { delay } from '@/lib/utils'
import catalogJson from '@/data/mockCatalog.json'
import hfJson from '@/data/mock-hf.json'
import thyroidJson from '@/data/mock-thyroid.json'
import akiJson from '@/data/mock-aki.json'

const CHAPTER_FILES: Record<string, ChapterData> = {
  'mock-hf.json': hfJson as ChapterData,
  'mock-thyroid.json': thyroidJson as ChapterData,
  'mock-aki.json': akiJson as ChapterData,
}

interface ProgressEntry {
  completed: number
  total: number
}

interface AppState {
  theme: 'light' | 'dark'
  sidebarCollapsed: boolean
  commandOpen: boolean
  catalogLoading: boolean
  chapterLoading: boolean
  catalog: Catalog | null
  chapters: Record<string, ChapterData>
  progress: Record<string, ProgressEntry>
  currentChapterId: string | null
  currentItemIndex: number
  revealed: Record<string, boolean>
  bookmarks: Record<string, boolean>
  mcqSelections: Record<string, number | null>

  initCatalog: () => Promise<void>
  loadChapter: (chapterId: string) => Promise<void>
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
  markCompleted: (chapterId: string, itemId: string) => void
  getSearchResults: (query: string) => SearchResult[]
  getCurrentItem: () => StudyItem | null
  getCurrentChapter: () => ChapterData | null
  isBookmarked: (itemId: string) => boolean
}

function buildProgress(
  catalog: Catalog,
  chapters: Record<string, ChapterData>,
  revealed: Record<string, boolean>,
): Record<string, ProgressEntry> {
  const progress: Record<string, ProgressEntry> = {}
  for (const section of catalog.sections) {
    for (const ch of section.chapters) {
      const data = chapters[ch.id]
      const total = data?.items.length ?? ch.itemCount
      const completed = data
        ? data.items.filter((item) => revealed[item.id]).length
        : 0
      progress[ch.id] = { completed, total }
    }
  }
  return progress
}

function applyTheme(theme: 'light' | 'dark') {
  document.documentElement.setAttribute('data-theme', theme)
  document.documentElement.classList.toggle('dark', theme === 'dark')
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
      chapters: {},
      progress: {},
      currentChapterId: null,
      currentItemIndex: 0,
      revealed: {},
      bookmarks: {},
      mcqSelections: {},

      initCatalog: async () => {
        set({ catalogLoading: true })
        await delay(420)
        const catalog = catalogJson as Catalog
        const chapters: Record<string, ChapterData> = {}
        for (const section of catalog.sections) {
          for (const ch of section.chapters) {
            chapters[ch.id] = CHAPTER_FILES[ch.file]
          }
        }
        const { revealed } = get()
        set({
          catalog,
          chapters,
          progress: buildProgress(catalog, chapters, revealed),
          catalogLoading: false,
        })
        applyTheme(get().theme)
      },

      loadChapter: async (_chapterId) => {
        set({ chapterLoading: true })
        await delay(280)
        set({ chapterLoading: false })
      },

      selectChapter: async (chapterId) => {
        const { chapters, loadChapter } = get()
        if (!chapters[chapterId]) return
        await loadChapter(chapterId)
        set({ currentChapterId: chapterId, currentItemIndex: 0 })
      },

      clearSelection: () => {
        set({ currentChapterId: null, currentItemIndex: 0 })
      },

      selectItem: (chapterId, itemIndex) => {
        set({ currentChapterId: chapterId, currentItemIndex: itemIndex })
      },

      goNext: () => {
        const { currentChapterId, currentItemIndex, chapters, catalog } = get()
        if (!currentChapterId || !catalog) return
        const items = chapters[currentChapterId]?.items ?? []
        if (currentItemIndex < items.length - 1) {
          set({ currentItemIndex: currentItemIndex + 1 })
          return
        }
        const allChapters = catalog.sections.flatMap((s) => s.chapters)
        const idx = allChapters.findIndex((c) => c.id === currentChapterId)
        if (idx >= 0 && idx < allChapters.length - 1) {
          const nextId = allChapters[idx + 1].id
          set({ currentChapterId: nextId, currentItemIndex: 0 })
        }
      },

      goPrev: () => {
        const { currentChapterId, currentItemIndex, chapters, catalog } = get()
        if (!currentChapterId || !catalog) return
        if (currentItemIndex > 0) {
          set({ currentItemIndex: currentItemIndex - 1 })
          return
        }
        const allChapters = catalog.sections.flatMap((s) => s.chapters)
        const idx = allChapters.findIndex((c) => c.id === currentChapterId)
        if (idx > 0) {
          const prevId = allChapters[idx - 1].id
          const prevItems = chapters[prevId]?.items ?? []
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
        const { catalog, chapters } = get()
        set({
          revealed,
          progress: catalog ? buildProgress(catalog, chapters, revealed) : get().progress,
        })
        if (revealed[id]) {
          const chapterId = get().currentChapterId
          if (chapterId) get().markCompleted(chapterId, id)
        }
      },

      selectMcqOption: (itemId, option) => {
        set({
          mcqSelections: { ...get().mcqSelections, [itemId]: option },
        })
      },

      toggleBookmark: (itemId) => {
        const id = itemId ?? get().getCurrentItem()?.id
        if (!id) return
        const bookmarks = { ...get().bookmarks, [id]: !get().bookmarks[id] }
        set({ bookmarks })
      },

      toggleTheme: () => {
        const theme = get().theme === 'light' ? 'dark' : 'light'
        applyTheme(theme)
        set({ theme })
      },

      toggleSidebar: () => set({ sidebarCollapsed: !get().sidebarCollapsed }),

      setCommandOpen: (open) => set({ commandOpen: open }),

      markCompleted: (_chapterId, _itemId) => {
        /* progress derived from revealed map */
      },

      getSearchResults: (query) => {
        const { catalog, chapters } = get()
        if (!catalog || !query.trim()) return []
        const q = query.toLowerCase()
        const results: SearchResult[] = []

        for (const section of catalog.sections) {
          for (const ch of section.chapters) {
            if (
              ch.title.toLowerCase().includes(q) ||
              ch.section.toLowerCase().includes(q)
            ) {
              results.push({
                id: `ch-${ch.id}`,
                kind: 'chapter',
                label: ch.title,
                subtitle: ch.section,
                chapterId: ch.id,
              })
            }
            const data = chapters[ch.id]
            if (!data) continue
            data.items.forEach((item, index) => {
              const text =
                item.type === 'note'
                  ? `${item.title} ${item.content}`
                  : item.type === 'mcq'
                    ? item.stem
                    : item.statement
              if (text.toLowerCase().includes(q) || item.id.toLowerCase().includes(q)) {
                results.push({
                  id: item.id,
                  kind: 'item',
                  label:
                    item.type === 'note'
                      ? item.title
                      : item.type === 'mcq'
                        ? item.stem.slice(0, 72) + (item.stem.length > 72 ? '…' : '')
                        : item.statement.slice(0, 72),
                  subtitle: `${ch.title} · Q${index + 1}`,
                  chapterId: ch.id,
                  itemIndex: index,
                })
              }
            })
          }
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
