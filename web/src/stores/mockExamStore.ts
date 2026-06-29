import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { StudyItem } from '@/lib/types'
import { useAppStore } from '@/store/useAppStore'

export type MockExamPhase = 'setup' | 'instructions' | 'active' | 'results'

export interface MockExamConfig {
  source: 'chapter' | 'random' | 'mistakes' | 'all_live'
  chapterId?: string
  subtopic?: string
  count: number
  durationMin: number
}

export interface MockExamResult {
  correct: number
  attempted: number
  total: number
  accuracy: number
}

export interface MockExamResponse {
  value: any
  savedAt: number
}

interface MockExamState {
  phase: MockExamPhase
  config: MockExamConfig
  
  examItems: StudyItem[]
  index: number
  responses: Record<string, MockExamResponse>
  marked: Record<string, boolean>
  visited: Record<string, boolean>
  draft: Record<string, any>
  
  startedAt: number | null
  endsAt: number | null
  paletteHidden: boolean
  instructionsAccepted: boolean
  results: MockExamResult | null
  autoSubmitted: boolean

  // Actions
  setConfig: (config: Partial<MockExamConfig>) => void
  setPhase: (phase: MockExamPhase) => void
  setInstructionsAccepted: (accepted: boolean) => void
  startTest: (items: StudyItem[]) => void
  quitTest: () => void
  
  // CBT Actions
  setDraft: (itemId: string, value: any) => void
  clearResponse: (itemId: string) => void
  saveCurrent: () => void
  saveAndNext: () => void
  saveAndMarkReview: () => void
  markReviewAndNext: () => void
  goToIndex: (index: number, autoSave?: boolean) => void
  submitExam: () => void
  togglePalette: () => void
}

export const useMockExamStore = create<MockExamState>()(
  persist(
    (set, get) => ({
      phase: 'setup',
      config: {
        source: 'chapter',
        count: 20,
        durationMin: 180,
      },
      
      examItems: [],
      index: 0,
      responses: {},
      marked: {},
      visited: {},
      draft: {},
      
      startedAt: null,
      endsAt: null,
      paletteHidden: false,
      instructionsAccepted: false,
      results: null,
      autoSubmitted: false,

      setConfig: (config) => set((state) => ({ config: { ...state.config, ...config } })),
      
      setPhase: (phase) => set({ phase }),
      
      setInstructionsAccepted: (accepted) => set({ instructionsAccepted: accepted }),
      
      startTest: (items) => {
        const { config } = get()
        const now = Date.now()
        set({
          phase: 'active',
          examItems: items,
          index: 0,
          responses: {},
          marked: {},
          visited: { [items[0]?.id]: true },
          draft: {},
          startedAt: now,
          endsAt: config.durationMin > 0 ? now + config.durationMin * 60 * 1000 : null,
          results: null,
          autoSubmitted: false,
        })
      },
      
      quitTest: () => set({ phase: 'setup', examItems: [], startedAt: null, endsAt: null }),
      
      setDraft: (itemId, value) => {
        set((state) => ({ draft: { ...state.draft, [itemId]: value } }))
      },
      
      clearResponse: (itemId) => {
        set((state) => {
          const newDraft = { ...state.draft }
          delete newDraft[itemId]
          const newResponses = { ...state.responses }
          delete newResponses[itemId]
          return { draft: newDraft, responses: newResponses }
        })
      },
      
      saveCurrent: () => {
        const { examItems, index, draft, responses } = get()
        const item = examItems[index]
        if (!item) return
        
        const currentDraft = draft[item.id]
        if (currentDraft !== undefined && currentDraft !== null && currentDraft !== '') {
          set({
            responses: {
              ...responses,
              [item.id]: { value: currentDraft, savedAt: Date.now() }
            }
          })
          useAppStore.getState().recordMockExamResponse(item, currentDraft)
        }
      },
      
      saveAndNext: () => {
        get().saveCurrent()
        get().goToIndex(get().index + 1, false)
      },
      
      saveAndMarkReview: () => {
        get().saveCurrent()
        const { examItems, index, marked } = get()
        const item = examItems[index]
        if (item) {
          set({ marked: { ...marked, [item.id]: true } })
        }
        get().goToIndex(get().index + 1, false)
      },
      
      markReviewAndNext: () => {
        const { examItems, index, marked } = get()
        const item = examItems[index]
        if (item) {
          set({ marked: { ...marked, [item.id]: true } })
        }
        get().goToIndex(get().index + 1, true)
      },
      
      goToIndex: (idx, autoSave = true) => {
        if (autoSave) get().saveCurrent()
        const { examItems, visited } = get()
        if (idx < 0 || idx >= examItems.length) {
          return
        }
        const item = examItems[idx]
        set({
          index: idx,
          visited: { ...visited, [item.id]: true }
        })
      },
      
      submitExam: () => {
        get().saveCurrent()
        const { examItems, responses } = get()

        // Ensure every saved response is reflected in study progress stats.
        for (const item of examItems) {
          const resp = responses[item.id]
          if (resp?.value !== undefined && resp.value !== null && resp.value !== '') {
            useAppStore.getState().recordMockExamResponse(item, resp.value)
          }
        }
        
        let correct = 0
        let attempted = 0
        
        for (const item of examItems) {
          const resp = responses[item.id]
          if (!resp || resp.value === undefined || resp.value === null || resp.value === '') continue
          attempted++
          
          let ok = false
          if (item.type === 'mcq') ok = resp.value === item.correctOption
          else if (item.type === 'true_false') ok = String(resp.value) === String(item.correctAnswer)
          else if (item.type === 'assertion_reason') ok = resp.value === item.correctOption
          else if (item.type === 'shortanswer' || item.type === 'why' || item.type === 'how') {
             const answer = (item as any).answer || ''
             ok = String(resp.value).toLowerCase().trim() === String(answer).toLowerCase().trim()
          }
          
          if (ok) correct++
        }
        
        set({
          phase: 'results',
          endsAt: null, // stop timer
          results: {
            correct,
            attempted,
            total: examItems.length,
            accuracy: attempted ? Math.round((correct / attempted) * 100) : 0
          }
        })
      },
      
      togglePalette: () => set((state) => ({ paletteHidden: !state.paletteHidden })),
    }),
    {
      name: 'h22-mock-exam-store',
      partialize: (state) => ({ config: state.config }), // only persist config
    }
  )
)
