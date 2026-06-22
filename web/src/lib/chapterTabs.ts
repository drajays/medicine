import type { ChapterData, NavEntry, StudyItem } from '@/lib/types'

export type ChapterTab =
  | 'notes'
  | 'inclusion'
  | 'exclusion'
  | 'takeaways'
  | 'mcq'
  | 'tf'
  | 'ar'
  | 'why'
  | 'how'
  | 'shortanswer'

export interface TabDef {
  id: ChapterTab
  label: string
  count: number
}

export function chapterCounts(ch: ChapterData) {
  const items = ch.items ?? []
  return {
    notes: items.filter((i) => i.type === 'note').length,
    inclusion: ch.inclusionCriteria?.length ?? 0,
    exclusion: ch.exclusionCriteria?.length ?? 0,
    takeaways: ch.keyTakeaways?.length ?? 0,
    mcq: items.filter((i) => i.type === 'mcq').length,
    tf: items.filter((i) => i.type === 'true_false').length,
    ar: items.filter((i) => i.type === 'assertion_reason').length,
    why: items.filter((i) => i.type === 'why').length,
    how: items.filter((i) => i.type === 'how').length,
    shortanswer: items.filter((i) => i.type === 'shortanswer').length,
  }
}

export function getChapterTabs(ch: ChapterData, kind: NavEntry['kind']): TabDef[] {
  const n = chapterCounts(ch)
  const isTrial = kind === 'trial'
  const tabs: TabDef[] = []

  tabs.push({ id: 'notes', label: 'Notes', count: n.notes })
  if (isTrial) {
    tabs.push({ id: 'inclusion', label: 'Inclusion', count: n.inclusion })
    tabs.push({ id: 'exclusion', label: 'Exclusion', count: n.exclusion })
    tabs.push({ id: 'takeaways', label: 'Takeaways', count: n.takeaways })
  }
  tabs.push({ id: 'mcq', label: 'MCQs', count: n.mcq })
  tabs.push({ id: 'tf', label: 'True/False', count: n.tf })
  if (!isTrial) tabs.push({ id: 'ar', label: 'Assertion–Reason', count: n.ar })
  if (n.why) tabs.push({ id: 'why', label: 'Why', count: n.why })
  if (n.how) tabs.push({ id: 'how', label: 'How', count: n.how })
  if (n.shortanswer) tabs.push({ id: 'shortanswer', label: 'Short Answer', count: n.shortanswer })

  return tabs.filter((t) => t.count > 0)
}

export function defaultTab(ch: ChapterData, kind: NavEntry['kind']): ChapterTab {
  return getChapterTabs(ch, kind)[0]?.id ?? 'notes'
}

export function tabForItemType(type: StudyItem['type']): ChapterTab {
  switch (type) {
    case 'note':
      return 'notes'
    case 'mcq':
      return 'mcq'
    case 'true_false':
      return 'tf'
    case 'assertion_reason':
      return 'ar'
    case 'why':
      return 'why'
    case 'how':
      return 'how'
    case 'shortanswer':
      return 'shortanswer'
    default:
      return 'notes'
  }
}

export function itemsForTab(ch: ChapterData, tab: ChapterTab): StudyItem[] {
  const items = ch.items ?? []
  switch (tab) {
    case 'notes':
      return items.filter((i) => i.type === 'note')
    case 'mcq':
      return items.filter((i) => i.type === 'mcq')
    case 'tf':
      return items.filter((i) => i.type === 'true_false')
    case 'ar':
      return items.filter((i) => i.type === 'assertion_reason')
    case 'why':
      return items.filter((i) => i.type === 'why')
    case 'how':
      return items.filter((i) => i.type === 'how')
    case 'shortanswer':
      return items.filter((i) => i.type === 'shortanswer')
    default:
      return []
  }
}
