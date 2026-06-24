import type { ItemMark, NavEntry, StudyItem } from '@/lib/types'
import {
  buildChapterProgress,
  countEngagedItems,
  type EngagementInput,
} from '@/lib/studyProgress'

export function applyTheme(theme: 'light' | 'dark') {
  document.documentElement.setAttribute('data-theme', theme)
  document.documentElement.classList.toggle('dark', theme === 'dark')
}

export function engagementInputFromStore(state: {
  revealed: Record<string, boolean>
  readItems: Record<string, boolean>
  mcqSelections: Record<string, number | null>
  marks: Record<string, ItemMark>
}): EngagementInput {
  return {
    revealed: state.revealed,
    readItems: state.readItems,
    mcqSelections: state.mcqSelections,
    marks: state.marks,
  }
}

export function buildProgress(
  navEntries: NavEntry[],
  chapters: Record<string, { items: StudyItem[] }>,
  input: EngagementInput,
  chapterEngagedMs: Record<string, number> = {},
) {
  const progress: Record<string, { completed: number; total: number; engagedMs: number }> = {}
  for (const entry of navEntries) {
    const data = chapters[entry.id]
    const items = data?.items ?? []
    const ms = chapterEngagedMs[entry.id] ?? 0
    if (items.length) {
      const p = buildChapterProgress(items, input, ms)
      progress[entry.id] = {
        completed: p.completed,
        total: p.total,
        engagedMs: p.engagedMs,
      }
    } else {
      progress[entry.id] = { completed: 0, total: 0, engagedMs: ms }
    }
  }
  return progress
}

export function itemSearchText(item: StudyItem): string {
  switch (item.type) {
    case 'note':
      return `${item.title} ${item.content}`
    case 'mcq':
      return item.stem
    case 'true_false':
      return item.statement
    case 'assertion_reason':
      return `${item.assertion} ${item.reason}`
    case 'why':
    case 'how':
    case 'shortanswer':
      return item.question
    default:
      return ''
  }
}

export { countEngagedItems }
