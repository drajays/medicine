import { useEffect } from 'react'
import { motion } from 'framer-motion'
import { useAppStore } from '@/store/useAppStore'
import { QuestionSkeleton } from '@/components/ui/Skeleton'
import { ChapterHeader } from '@/components/chapter/ChapterHeader'
import { CaseDescription } from '@/components/chapter/CaseDescription'
import { TrialSummary } from '@/components/chapter/TrialSummary'
import { ChapterTabs } from '@/components/chapter/ChapterTabs'
import { StudyItemCard } from '@/components/chapter/StudyItemCard'
import { LandingPage } from '@/components/chapter/LandingPage'
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
  const catalogLoading = useAppStore((s) => s.catalogLoading)
  const navEntries = useAppStore((s) => s.navEntries)
  const activeTab = useAppStore((s) => s.activeTab)
  const setActiveTab = useAppStore((s) => s.setActiveTab)
  const scrollToItemId = useAppStore((s) => s.scrollToItemId)
  const setScrollToItemId = useAppStore((s) => s.setScrollToItemId)
  const loadChapter = useAppStore((s) => s.loadChapter)
  const clearSelection = useAppStore((s) => s.clearSelection)

  const navEntry = navEntries.find((e) => e.id === currentChapterId)
  const kind = navEntry?.kind ?? 'harrison'

  // A chapter can be selected (e.g. restored from a deep link) before its JSON
  // is fetched. Pull it in here; if the id is unknown or the fetch fails, fall
  // back to the landing page instead of hanging on a skeleton forever.
  useEffect(() => {
    if (catalogLoading || !currentChapterId || chapter || chapterLoading) return
    loadChapter(currentChapterId).then((data) => {
      if (!data) clearSelection()
    })
  }, [catalogLoading, currentChapterId, chapter, chapterLoading, loadChapter, clearSelection])

  useEffect(() => {
    if (!scrollToItemId) return
    const el = document.getElementById(`item-${scrollToItemId}`)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' })
      setScrollToItemId(null)
    }
  }, [scrollToItemId, activeTab, chapter, setScrollToItemId])

  if (!currentChapterId) {
    return <LandingPage />
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
        <motion.div
          key={tab}
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.16, ease: 'easeOut' }}
          className="mt-5"
        >
          <TabBody chapter={chapter} tab={tab} />
        </motion.div>
      </div>
    </div>
  )
}
