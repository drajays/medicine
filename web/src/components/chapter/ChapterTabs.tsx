import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'
import type { TabDef } from '@/lib/chapterTabs'

export function ChapterTabs({
  tabs,
  active,
  onChange,
}: {
  tabs: TabDef[]
  active: string
  onChange: (id: TabDef['id']) => void
}) {
  return (
    <div className="sticky top-0 z-10 -mx-4 border-b clinical-border bg-[var(--color-clinical-bg-light)]/95 px-4 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/95 md:-mx-8 md:px-8">
      <div
        role="tablist"
        aria-label="Content sections"
        className="flex gap-0.5 overflow-x-auto py-2.5 scrollbar-thin"
      >
        {tabs.map((tab) => {
          const isActive = active === tab.id
          return (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={isActive}
              onClick={() => onChange(tab.id)}
              className={cn(
                'relative shrink-0 rounded-lg px-3.5 py-1.5 text-left transition-colors duration-150',
                'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-clinical-accent)]/40',
                isActive
                  ? 'text-[var(--color-clinical-accent)]'
                  : 'clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
              )}
            >
              {isActive && (
                <motion.span
                  layoutId="chapter-tab-pill"
                  aria-hidden
                  className="absolute inset-0 rounded-lg border-b-2 border-[var(--color-clinical-accent)] bg-[var(--color-clinical-card-light)] shadow-sm ring-1 ring-[var(--color-clinical-border-light)] dark:bg-[var(--color-clinical-card-dark)] dark:ring-[var(--color-clinical-border-dark)]"
                  transition={{ type: 'spring', stiffness: 520, damping: 40 }}
                />
              )}
              <span className="eyebrow relative block whitespace-nowrap">{tab.label}</span>
              <span
                className={cn(
                  'relative mt-0.5 block text-[11px] font-semibold tabular-nums',
                  isActive ? 'text-[var(--color-clinical-accent)]/75' : 'clinical-muted',
                )}
              >
                {tab.count}
              </span>
            </button>
          )
        })}
      </div>
    </div>
  )
}
