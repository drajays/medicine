import { useEffect } from 'react'
import { useAppStore } from '@/store/useAppStore'
import { QuestionSkeleton } from '@/components/ui/Skeleton'
import { ChapterHeader } from '@/components/chapter/ChapterHeader'
import { CaseDescription } from '@/components/chapter/CaseDescription'
import { TrialSummary } from '@/components/chapter/TrialSummary'
import { ChapterTabs } from '@/components/chapter/ChapterTabs'
import { StudyItemCard } from '@/components/chapter/StudyItemCard'
import {
  defaultTab,
  getChapterTabs,
  itemsForTab,
  type ChapterTab,
} from '@/lib/chapterTabs'
import type { ChapterData } from '@/lib/types'

function CriteriaList({
  title,
  items,
  variant,
}: {
  title: string
  items: string[]
  variant: 'inclusion' | 'exclusion'
}) {
  return (
    <section className="clinical-card p-5 md:p-6">
      <h3
        className={
          variant === 'inclusion'
            ? 'text-sm font-bold text-emerald-800 dark:text-emerald-300'
            : 'text-sm font-bold text-red-800 dark:text-red-300'
        }
      >
        {title}
      </h3>
      <ul className="mt-3 list-disc space-y-2 pl-5 text-sm leading-relaxed">
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </section>
  )
}

function TakeawaysList({ items }: { items: string[] }) {
  return (
    <div className="space-y-3">
      {items.map((t, i) => (
        <section key={i} className="clinical-card p-5 md:p-6">
          <p className="text-xs font-semibold uppercase text-blue-700 dark:text-blue-300">
            Takeaway {i + 1}
          </p>
          <p className="clinical-serif mt-2 text-[15px] leading-relaxed">{t}</p>
        </section>
      ))}
    </div>
  )
}

function TabBody({ chapter, tab }: { chapter: ChapterData; tab: ChapterTab }) {
  if (tab === 'inclusion' && chapter.inclusionCriteria?.length) {
    return (
      <CriteriaList title="Inclusion Criteria" items={chapter.inclusionCriteria} variant="inclusion" />
    )
  }
  if (tab === 'exclusion' && chapter.exclusionCriteria?.length) {
    return (
      <CriteriaList title="Exclusion Criteria" items={chapter.exclusionCriteria} variant="exclusion" />
    )
  }
  if (tab === 'takeaways' && chapter.keyTakeaways?.length) {
    return <TakeawaysList items={chapter.keyTakeaways} />
  }

  const items = itemsForTab(chapter, tab)
  if (!items.length) {
    return (
      <p className="clinical-card p-8 text-center text-sm clinical-muted">
        No items in this section.
      </p>
    )
  }

  return (
    <div className="space-y-4">
      {items.map((item, i) => (
        <StudyItemCard key={item.id} item={item} index={i + 1} />
      ))}
    </div>
  )
}

export function ChapterView() {
  const chapterLoading = useAppStore((s) => s.chapterLoading)
  const chapter = useAppStore((s) => s.getCurrentChapter())
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const navEntries = useAppStore((s) => s.navEntries)
  const activeTab = useAppStore((s) => s.activeTab)
  const setActiveTab = useAppStore((s) => s.setActiveTab)
  const scrollToItemId = useAppStore((s) => s.scrollToItemId)
  const setScrollToItemId = useAppStore((s) => s.setScrollToItemId)

  const navEntry = navEntries.find((e) => e.id === currentChapterId)
  const kind = navEntry?.kind ?? 'harrison'

  useEffect(() => {
    if (!scrollToItemId) return
    const el = document.getElementById(`item-${scrollToItemId}`)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' })
      setScrollToItemId(null)
    }
  }, [scrollToItemId, activeTab, chapter, setScrollToItemId])

  if (!currentChapterId) {
    return (
      <div className="mx-auto max-w-2xl px-4 py-12 md:py-20">
        <div className="clinical-card p-8 text-center">
          <h2 className="text-xl font-semibold">Welcome to Harrison&apos;s 22e</h2>
          <p className="clinical-serif mt-3 text-[15px] leading-relaxed clinical-muted">
            Select a topic from the index or press{' '}
            <kbd className="rounded border px-1.5 py-0.5 text-xs">⌘K</kbd> to search.
            Each topic opens with all notes and questions organized by type.
          </p>
        </div>
      </div>
    )
  }

  if (chapterLoading || !chapter) {
    return <QuestionSkeleton />
  }

  const tabs = getChapterTabs(chapter, kind)
  const tab = tabs.some((t) => t.id === activeTab) ? activeTab : defaultTab(chapter, kind)

  return (
    <div className="mx-auto max-w-3xl px-4 py-4 md:px-8 md:py-6">
      <ChapterHeader chapter={chapter} kind={kind} />
      {kind === 'case_report' && <CaseDescription chapter={chapter} />}
      {kind === 'trial' && <TrialSummary chapter={chapter} />}
      <div className="mt-4">
        <ChapterTabs tabs={tabs} active={tab} onChange={setActiveTab} />
        <div className="mt-4">
          <TabBody chapter={chapter} tab={tab} />
        </div>
      </div>
    </div>
  )
}
