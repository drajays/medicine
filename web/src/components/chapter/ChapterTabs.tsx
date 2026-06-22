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
      <div className="flex gap-1 overflow-x-auto py-2 scrollbar-thin">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            type="button"
            onClick={() => onChange(tab.id)}
            className={cn(
              'shrink-0 rounded-lg px-3 py-2 text-left transition-colors duration-100',
              active === tab.id
                ? 'bg-blue-600 text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:bg-zinc-700',
            )}
          >
            <span className="block text-xs font-semibold">{tab.label}</span>
            <span
              className={cn(
                'block text-[10px] tabular-nums',
                active === tab.id ? 'text-blue-100' : 'clinical-muted',
              )}
            >
              {tab.count}
            </span>
          </button>
        ))}
      </div>
    </div>
  )
}
