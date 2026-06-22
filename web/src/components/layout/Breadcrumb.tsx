import { useAppStore } from '@/store/useAppStore'

export function Breadcrumb() {
  const chapter = useAppStore((s) => s.getCurrentChapter())
  const itemIndex = useAppStore((s) => s.currentItemIndex)
  const item = useAppStore((s) => s.getCurrentItem())

  if (!chapter || !item) {
    return (
      <nav aria-label="Breadcrumb" className="text-sm clinical-muted">
        Select a chapter to begin
      </nav>
    )
  }

  const sectionLabel = chapter.section.split('—')[0]?.trim() ?? chapter.section

  return (
    <nav aria-label="Breadcrumb" className="flex flex-wrap items-center gap-1.5 text-sm">
      <span className="clinical-muted">{sectionLabel}</span>
      <span className="clinical-muted">›</span>
      <span className="font-medium">{chapter.title}</span>
      <span className="clinical-muted">›</span>
      <span className="rounded-md bg-blue-50 px-2 py-0.5 text-xs font-semibold text-blue-700 dark:bg-blue-500/15 dark:text-blue-300">
        Q{itemIndex + 1}
      </span>
    </nav>
  )
}
