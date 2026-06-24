import { useMemo, type ReactNode } from 'react'
import { BarChart3, BookOpen, Clock, Layers } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { formatStudyDuration } from '@/lib/studyProgress'
import { cn } from '@/lib/utils'
import type { HeaderKind } from '@/lib/types'

const SECTION_ICON: Partial<Record<HeaderKind, string>> = {
  hot_topics: '🔥',
  case_reports: '📋',
  pediatric_endo: '🧒',
  stories: '💬',
  calculators: '🧮',
  trials: '📊',
  harrison_banner: '📖',
}

function ProgressBar({ percent, className }: { percent: number; className?: string }) {
  const color =
    percent >= 80 ? 'bg-emerald-500' : percent >= 40 ? 'bg-amber-500' : 'bg-slate-400'
  return (
    <div className={cn('h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-zinc-800', className)}>
      <div
        className={cn('h-full rounded-full transition-all duration-300', color)}
        style={{ width: `${Math.min(100, percent)}%` }}
      />
    </div>
  )
}

function StatTile({
  icon,
  label,
  value,
  sub,
}: {
  icon: ReactNode
  label: string
  value: string
  sub?: string
}) {
  return (
    <div className="clinical-card p-4">
      <div className="flex items-center gap-2 text-indigo-700 dark:text-indigo-300">
        {icon}
        <span className="text-[10px] font-bold uppercase tracking-wider">{label}</span>
      </div>
      <p className="mt-2 text-2xl font-bold tabular-nums">{value}</p>
      {sub && <p className="mt-0.5 text-xs clinical-muted">{sub}</p>}
    </div>
  )
}

export function StudyProgressDashboard() {
  const getStudyProgress = useAppStore((s) => s.getStudyProgress)
  const selectChapter = useAppStore((s) => s.selectChapter)

  const { overall, sections } = useMemo(() => getStudyProgress(), [getStudyProgress])

  const hasAny =
    overall.completed > 0 || overall.engagedMs > 0 || sections.some((s) => s.completed > 0)

  if (!hasAny) {
    return (
      <div className="clinical-card p-8 text-center">
        <BarChart3 className="mx-auto h-10 w-10 text-indigo-600 dark:text-indigo-400" />
        <h2 className="mt-4 text-lg font-semibold">No study progress yet</h2>
        <p className="clinical-serif mx-auto mt-2 max-w-md text-[15px] leading-relaxed clinical-muted">
          Progress counts when you <strong>reveal an answer</strong>, <strong>solve a question</strong>,{' '}
          <strong>mark an item</strong>, or tap <strong>Mark as read</strong> on notes — not from scrolling
          alone.
        </p>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="clinical-card border-l-4 border-l-indigo-500 p-5 md:p-6">
        <p className="text-xs font-bold uppercase tracking-wider text-indigo-700 dark:text-indigo-300">
          Overall
        </p>
        <div className="mt-3 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="text-3xl font-bold tabular-nums">{overall.percent}%</p>
            <p className="mt-1 text-sm clinical-muted">
              {overall.completed} of {overall.total} items engaged
            </p>
            <p className="text-xs clinical-muted">
              {overall.chaptersComplete} chapters complete · {overall.chaptersStarted} started
            </p>
          </div>
          <div className="md:min-w-[240px] md:flex-1">
            <ProgressBar percent={overall.percent} />
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 md:grid-cols-3">
        <StatTile
          icon={<BookOpen className="h-4 w-4" />}
          label="Items engaged"
          value={`${overall.completed}/${overall.total}`}
        />
        <StatTile
          icon={<Layers className="h-4 w-4" />}
          label="Sections active"
          value={String(sections.filter((s) => s.completed > 0).length)}
          sub={`of ${sections.length} with loaded totals`}
        />
        <StatTile
          icon={<Clock className="h-4 w-4" />}
          label="Engaged time"
          value={formatStudyDuration(overall.engagedMs)}
          sub="Actions + bounded read dwell"
        />
      </div>

      <section className="space-y-4">
        <h3 className="px-1 text-sm font-bold">By section</h3>
        {sections.map((section) => (
          <div key={section.key} className="clinical-card p-4 md:p-5">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <span aria-hidden>{SECTION_ICON[section.kind] ?? '📚'}</span>
                <h4 className="font-semibold">{section.title}</h4>
              </div>
              <span className="text-sm tabular-nums clinical-muted">
                {section.completed}/{section.total} · {section.percent}% ·{' '}
                {formatStudyDuration(section.engagedMs)}
              </span>
            </div>
            <ProgressBar percent={section.percent} className="mt-3" />

            {section.chapters.filter((c) => c.total > 0 || c.completed > 0).length > 0 && (
              <div className="mt-4 space-y-2 border-t clinical-border pt-3">
                {section.chapters
                  .filter((c) => c.total > 0 || c.completed > 0)
                  .slice(0, 12)
                  .map((ch) => (
                    <button
                      key={ch.id}
                      type="button"
                      onClick={() => selectChapter(ch.id)}
                      className="flex w-full items-center gap-3 rounded-lg px-2 py-1.5 text-left transition-colors hover:bg-slate-50 dark:hover:bg-zinc-800/60"
                    >
                      <div className="min-w-0 flex-1">
                        <p className="truncate text-sm">{ch.title}</p>
                        <ProgressBar percent={ch.percent} className="mt-1.5" />
                      </div>
                      <span className="shrink-0 text-xs tabular-nums clinical-muted">
                        {ch.completed}/{ch.total}
                      </span>
                    </button>
                  ))}
                {section.chapters.filter((c) => c.total > 0).length > 12 && (
                  <p className="px-2 text-[10px] clinical-muted">
                    +{section.chapters.filter((c) => c.total > 0).length - 12} more chapters
                  </p>
                )}
              </div>
            )}
          </div>
        ))}
      </section>

      <p className="px-1 text-[11px] leading-relaxed clinical-muted">
        Engaged time = base credit per action (reveal 45s, answer 60s, mark 30s, read 75s) plus up to
        90s dwell per item while it stays in view after you engage. Scrolling without engaging awards
        nothing.
      </p>
    </div>
  )
}
