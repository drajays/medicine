import { useMemo, useEffect } from 'react'
import { ChevronRight, ExternalLink } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { buildSections, type LandingItem, type LandingSection } from '@/lib/sections'
import { cn } from '@/lib/utils'
import { useRevisionStore } from '@/stores/revisionStore'
import { ReviseDashboard } from '@/components/ReviseDashboard'
import { StudyProgressDashboard } from '@/components/StudyProgressDashboard'
import { MockExamDashboard } from '@/components/MockExamDashboard'
import { ContentLogDashboard } from '@/components/ContentLogDashboard'
import { OfflineButton } from '@/components/OfflineButton'
import { RefreshButton } from '@/components/RefreshButton'
import type { HeaderKind } from '@/lib/types'

export const REVISE_KEY = '__revise__'
export const MOCK_EXAM_KEY = '__mock_exam__'
export const CONTENT_LOG_KEY = '__content_log__'
const PROGRESS_KEY = '__progress__'

const BASE = import.meta.env.BASE_URL

const META: Record<
  HeaderKind,
  { icon: string; active: string; chip: string; bar: string }
> = {
  hot_topics: {
    icon: '🔥',
    active: 'bg-amber-600 text-white shadow-sm',
    chip: 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-200',
    bar: 'border-l-amber-500',
  },
  case_reports: {
    icon: '📋',
    active: 'bg-teal-600 text-white shadow-sm',
    chip: 'bg-teal-100 text-teal-800 dark:bg-teal-950/50 dark:text-teal-200',
    bar: 'border-l-teal-600',
  },
  pediatric_endo: {
    icon: '🧒',
    active: 'bg-green-600 text-white shadow-sm',
    chip: 'bg-green-100 text-green-800 dark:bg-green-950/50 dark:text-green-200',
    bar: 'border-l-green-600',
  },
  sub_apps: {
    icon: '⚕️',
    active: 'bg-emerald-600 text-white shadow-sm',
    chip: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-200',
    bar: 'border-l-emerald-600',
  },
  stories: {
    icon: '💬',
    active: 'bg-rose-600 text-white shadow-sm',
    chip: 'bg-rose-100 text-rose-800 dark:bg-rose-950/50 dark:text-rose-200',
    bar: 'border-l-rose-500',
  },
  calculators: {
    icon: '🧮',
    active: 'bg-violet-600 text-white shadow-sm',
    chip: 'bg-violet-100 text-violet-800 dark:bg-violet-950/50 dark:text-violet-200',
    bar: 'border-l-violet-600',
  },
  imaging_resources: {
    icon: '🩻',
    active: 'bg-cyan-600 text-white shadow-sm',
    chip: 'bg-cyan-100 text-cyan-800 dark:bg-cyan-950/50 dark:text-cyan-200',
    bar: 'border-l-cyan-600',
  },
  trials: {
    icon: '📊',
    active: 'bg-blue-600 text-white shadow-sm',
    chip: 'bg-blue-100 text-blue-800 dark:bg-blue-950/50 dark:text-blue-200',
    bar: 'border-l-blue-600',
  },
  trial_sub: { icon: '›', active: '', chip: '', bar: '' },
  harrison_banner: {
    icon: '📖',
    active: 'bg-indigo-600 text-white shadow-sm',
    chip: 'bg-indigo-100 text-indigo-800 dark:bg-indigo-950/50 dark:text-indigo-200',
    bar: 'border-l-indigo-600',
  },
  harrison_section: { icon: '§', active: '', chip: '', bar: '' },
}

function groupItems(items: LandingItem[]): Array<{ label?: string; items: LandingItem[] }> {
  const groups: Array<{ label?: string; items: LandingItem[] }> = []
  let last: { label?: string; items: LandingItem[] } | null = null
  for (const item of items) {
    if (!last || last.label !== item.group) {
      last = { label: item.group, items: [] }
      groups.push(last)
    }
    last.items.push(item)
  }
  return groups
}

function SectionGrid({ section }: { section: LandingSection }) {
  const selectChapter = useAppStore((s) => s.selectChapter)
  const meta = META[section.kind]
  const groups = groupItems(section.items)

  const open = (item: LandingItem) => {
    if (item.href) {
      window.open(`${BASE}${item.href}`, '_blank', 'noopener,noreferrer')
    } else {
      selectChapter(item.id)
    }
  }

  return (
    <div className="space-y-6">
      {groups.map((group, gi) => (
        <div key={group.label ?? gi}>
          {group.label && (
            <p className="mb-2 px-1 text-[11px] font-bold uppercase tracking-wider clinical-muted">
              {group.label}
            </p>
          )}
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-3">
            {group.items.map((item) => (
              <button
                key={item.id}
                type="button"
                onClick={() => open(item)}
                className={cn(
                  'clinical-card group flex items-center gap-3 border-l-[3px] p-4 text-left transition-all duration-150',
                  'hover:-translate-y-0.5 hover:shadow-md',
                  meta.bar,
                )}
              >
                <div className="min-w-0 flex-1">
                  <p className="truncate text-sm font-semibold">{item.title}</p>
                  <p className="truncate text-xs clinical-muted">{item.subtitle}</p>
                </div>
                {item.href ? (
                  <ExternalLink
                    className={cn(
                      'h-4 w-4 shrink-0',
                      section.kind === 'imaging_resources'
                        ? 'text-cyan-500'
                        : section.kind === 'sub_apps'
                          ? 'text-emerald-500'
                          : 'text-violet-500',
                    )}
                  />
                ) : (
                  <ChevronRight className="h-4 w-4 shrink-0 clinical-muted transition-transform group-hover:translate-x-0.5" />
                )}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

export function LandingPage() {
  const navRows = useAppStore((s) => s.navRows)
  const marks = useAppStore((s) => s.marks)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const reviseN = useRevisionStore((s) => Object.keys(s.items).length)
  const criticalN = useRevisionStore((s) => s.getCriticalCount())
  const overallPercent = useAppStore((s) => s.getStudyProgress().overall.percent)
  // The active landing section lives in the store so the header "due today"
  // badge can switch to the Revise tab from anywhere in the app.
  const activeKey = useAppStore((s) => s.landingTarget)
  const setActiveKey = useAppStore((s) => s.setLandingTarget)
  const sections = useMemo(() => buildSections(navRows), [navRows])

  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  const isRevise = activeKey === REVISE_KEY
  const isProgress = activeKey === PROGRESS_KEY
  const isMockExam = activeKey === MOCK_EXAM_KEY
  const isContentLog = activeKey === CONTENT_LOG_KEY
  const active = sections.find((s) => s.key === activeKey) ?? sections[0]

  if (!sections.length) {
    return (
      <div className="mx-auto max-w-2xl px-4 py-12 md:py-20">
        <div className="clinical-card p-8 text-center">
          <h2 className="text-xl font-semibold">Welcome to Harrison&apos;s 22e</h2>
          <p className="clinical-serif mt-3 text-[15px] leading-relaxed clinical-muted">
            The study catalog is still loading.
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-5xl px-4 py-6 md:px-8 md:py-8">
      <header className="mb-5">
        <h1 className="text-2xl font-semibold tracking-tight md:text-3xl">
          Harrison&apos;s Principles of Internal Medicine
        </h1>
        <p className="clinical-serif mt-2 text-[15px] leading-relaxed clinical-muted">
          Pick a section to explore, then open any topic. Press{' '}
          <kbd className="rounded border px-1.5 py-0.5 text-xs">⌘K</kbd> to search across everything.
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <RefreshButton />
        </div>
        <OfflineButton />
      </header>

      {/* Section tabs */}
      <div className="sticky top-0 z-10 -mx-4 mb-5 border-b clinical-border bg-[var(--color-clinical-bg-light)]/95 px-4 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/95 md:-mx-8 md:px-8">
        <div className="flex flex-wrap gap-1.5 py-2">
          <button
            type="button"
            onClick={() => setActiveKey(REVISE_KEY)}
            className={cn(
              'flex shrink-0 items-center gap-2 rounded-lg px-3.5 py-2 transition-colors duration-100',
              isRevise
                ? 'bg-amber-500 text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
            )}
          >
            <span aria-hidden className="text-base leading-none">
              📌
            </span>
            <span className="text-sm font-semibold">Revise</span>
            {(criticalN > 0 || reviseN > 0) && (
              <span
                className={cn(
                  'rounded-full px-1.5 py-0.5 text-[10px] font-bold tabular-nums',
                  isRevise
                    ? 'bg-white/25 text-white'
                    : criticalN > 0
                      ? 'bg-red-100 text-red-800 dark:bg-red-950/50 dark:text-red-300'
                      : 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-200',
                )}
              >
                {criticalN > 0 ? criticalN : reviseN}
              </span>
            )}
          </button>
          <button
            type="button"
            onClick={() => setActiveKey(PROGRESS_KEY)}
            className={cn(
              'flex shrink-0 items-center gap-2 rounded-lg px-3.5 py-2 transition-colors duration-100',
              isProgress
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
            )}
          >
            <span aria-hidden className="text-base leading-none">
              📊
            </span>
            <span className="text-sm font-semibold">Progress</span>
            {overallPercent > 0 && (
              <span
                className={cn(
                  'rounded-full px-1.5 py-0.5 text-[10px] font-bold tabular-nums',
                  isProgress
                    ? 'bg-white/25 text-white'
                    : 'bg-indigo-100 text-indigo-800 dark:bg-indigo-950/50 dark:text-indigo-200',
                )}
              >
                {overallPercent}%
              </span>
            )}
          </button>
          <button
            type="button"
            onClick={() => setActiveKey(MOCK_EXAM_KEY)}
            className={cn(
              'flex shrink-0 items-center gap-2 rounded-lg px-3.5 py-2 transition-colors duration-100',
              isMockExam
                ? 'bg-blue-600 text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
            )}
          >
            <span aria-hidden className="text-base leading-none">
              📝
            </span>
            <span className="text-sm font-semibold">Mock Exam</span>
          </button>
          <button
            type="button"
            onClick={() => setActiveKey(CONTENT_LOG_KEY)}
            className={cn(
              'flex shrink-0 items-center gap-2 rounded-lg px-3.5 py-2 transition-colors duration-100',
              isContentLog
                ? 'bg-teal-600 text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
            )}
          >
            <span aria-hidden className="text-base leading-none">
              📜
            </span>
            <span className="text-sm font-semibold">Updates</span>
          </button>
          {sections.map((section) => {
            const meta = META[section.kind]
            const isActive =
              !isRevise && !isProgress && !isMockExam && !isContentLog && section.key === active.key
            return (
              <button
                key={section.key}
                type="button"
                onClick={() => setActiveKey(section.key)}
                className={cn(
                  'flex shrink-0 items-center gap-2 rounded-lg px-3.5 py-2 transition-colors duration-100',
                  isActive
                    ? meta.active
                    : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
                )}
              >
                <span aria-hidden className="text-base leading-none">
                  {meta.icon}
                </span>
                <span className="text-sm font-semibold">{section.title}</span>
                <span
                  className={cn(
                    'rounded-full px-1.5 py-0.5 text-[10px] font-bold tabular-nums',
                    isActive ? 'bg-white/25 text-white' : meta.chip,
                  )}
                >
                  {section.count}
                </span>
              </button>
            )
          })}
        </div>
      </div>

      {isRevise ? (
        <ReviseDashboard />
      ) : isProgress ? (
        <StudyProgressDashboard />
      ) : isMockExam ? (
        <MockExamDashboard />
      ) : isContentLog ? (
        <ContentLogDashboard />
      ) : (
        <>
          {active.subtitle && (
            <p className="mb-4 max-w-2xl text-sm clinical-muted">{active.subtitle}</p>
          )}
          <SectionGrid section={active} />
        </>
      )}
    </div>
  )
}
