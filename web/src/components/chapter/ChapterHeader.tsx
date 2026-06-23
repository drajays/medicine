import { cn } from '@/lib/utils'
import type { ChapterData, NavEntry } from '@/lib/types'
import { KIND_BADGE, KIND_LABEL } from '@/components/layout/Breadcrumb'

export function ChapterHeader({
  chapter,
  kind,
}: {
  chapter: ChapterData
  kind: NavEntry['kind']
}) {
  const isTrial = kind === 'trial'
  const isCase = kind === 'case_report'
  const isHot = kind === 'hot_topic'
  const isStory = kind === 'story'
  const isNejm = chapter.subsection === 'nejm'

  const byline = isTrial || isCase || isHot || isStory
    ? [chapter.section, chapter.category, chapter.authors].filter(Boolean).join(' · ')
    : [
            chapter.chapterNo ? `Chapter ${chapter.chapterNo}` : null,
            chapter.section,
            chapter.authors,
          ]
            .filter(Boolean)
            .join(' · ')

  return (
    <header className="clinical-card overflow-hidden">
      <div
        className={cn(
          'border-b px-5 py-4 md:px-8 md:py-5',
          isHot && 'border-amber-200/60 bg-amber-50/50 dark:border-amber-500/20 dark:bg-amber-950/20',
          isCase && 'border-teal-200/60 bg-teal-50/50 dark:border-teal-500/20 dark:bg-teal-950/20',
          isTrial && 'border-blue-200/60 bg-blue-50/50 dark:border-blue-500/20 dark:bg-blue-950/20',
          isStory && 'border-rose-200/60 bg-rose-50/50 dark:border-rose-500/20 dark:bg-rose-950/20',
          !isHot && !isCase && !isTrial && !isStory && 'border-indigo-200/60 bg-indigo-50/40 dark:border-indigo-500/20 dark:bg-indigo-950/20',
        )}
      >
        <span
          className={cn(
            'inline-block rounded-md px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide',
            KIND_BADGE[kind],
          )}
        >
          {KIND_LABEL[kind]}
          {isNejm ? ' · NEJM' : ''}
        </span>
        <h2 className="mt-2.5 text-2xl font-semibold leading-[1.12] tracking-tight md:text-[2.05rem]">
          {chapter.title}
        </h2>
        {chapter.subtitle && (
          <p className="clinical-serif mt-2 text-[15px] italic leading-snug clinical-muted md:text-base">
            {chapter.subtitle}
          </p>
        )}
        {byline && (
          <p className="eyebrow mt-3.5 border-t clinical-border pt-3 clinical-muted">{byline}</p>
        )}
      </div>
    </header>
  )
}
