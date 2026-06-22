import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import type { NavEntry } from '@/lib/types'
import type { ChapterTab } from '@/lib/chapterTabs'

export const KIND_BADGE: Record<NavEntry['kind'], string> = {
  hot_topic:
    'bg-amber-100 text-amber-900 dark:bg-amber-500/20 dark:text-amber-200',
  case_report:
    'bg-teal-100 text-teal-900 dark:bg-teal-500/20 dark:text-teal-200',
  trial:
    'bg-blue-100 text-blue-900 dark:bg-blue-500/20 dark:text-blue-200',
  harrison:
    'bg-indigo-100 text-indigo-900 dark:bg-indigo-500/20 dark:text-indigo-200',
}

export const KIND_LABEL: Record<NavEntry['kind'], string> = {
  hot_topic: 'Hot Topic',
  case_report: 'Case Report',
  trial: 'Trial',
  harrison: 'Chapter',
}

const TAB_LABEL: Record<ChapterTab, string> = {
  notes: 'Notes',
  inclusion: 'Inclusion',
  exclusion: 'Exclusion',
  takeaways: 'Takeaways',
  mcq: 'MCQs',
  tf: 'True/False',
  ar: 'Assertion–Reason',
  why: 'Why',
  how: 'How',
  shortanswer: 'Short Answer',
}

export function Breadcrumb() {
  const chapter = useAppStore((s) => s.getCurrentChapter())
  const activeTab = useAppStore((s) => s.activeTab)
  const navEntries = useAppStore((s) => s.navEntries)
  const currentChapterId = useAppStore((s) => s.currentChapterId)

  if (!chapter || !currentChapterId) {
    return (
      <nav aria-label="Breadcrumb" className="text-sm clinical-muted">
        Select a topic from the index
      </nav>
    )
  }

  const navEntry = navEntries.find((e) => e.id === currentChapterId)
  const sectionLabel = navEntry?.sectionTitle ?? chapter.section ?? 'Study'
  const kind = navEntry?.kind ?? 'harrison'

  return (
    <nav aria-label="Breadcrumb" className="flex flex-wrap items-center gap-1.5 text-sm">
      <span
        className={cn(
          'rounded-md px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide',
          KIND_BADGE[kind],
        )}
      >
        {KIND_LABEL[kind]}
      </span>
      <span className="clinical-muted">›</span>
      <span className="clinical-muted">{sectionLabel}</span>
      <span className="clinical-muted">›</span>
      <span className="max-w-[10rem] truncate font-medium sm:max-w-md">{chapter.title}</span>
      <span className="clinical-muted">›</span>
      <span className="rounded-md bg-blue-50 px-2 py-0.5 text-xs font-semibold text-blue-700 dark:bg-blue-500/15 dark:text-blue-300">
        {TAB_LABEL[activeTab]}
      </span>
    </nav>
  )
}
