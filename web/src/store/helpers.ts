import type { NavEntry, StudyItem } from '@/lib/types'

export function applyTheme(theme: 'light' | 'dark') {
  document.documentElement.setAttribute('data-theme', theme)
  document.documentElement.classList.toggle('dark', theme === 'dark')
}

export function buildProgress(
  navEntries: NavEntry[],
  chapters: Record<string, { items: StudyItem[] }>,
  revealed: Record<string, boolean>,
) {
  const progress: Record<string, { completed: number; total: number }> = {}
  for (const entry of navEntries) {
    const data = chapters[entry.id]
    const total = data?.items.length ?? 0
    const completed = data
      ? data.items.filter((item) => revealed[item.id]).length
      : 0
    progress[entry.id] = { completed, total }
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
