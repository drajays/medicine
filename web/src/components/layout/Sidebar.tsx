import { useRef } from 'react'
import type { CSSProperties } from 'react'
import { useVirtualizer } from '@tanstack/react-virtual'
import { ChevronRight, ExternalLink, PanelLeftClose, PanelLeftOpen } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { Button } from '@/components/ui/Button'
import { SidebarSkeleton } from '@/components/ui/Skeleton'
import { SectionHeader } from '@/components/layout/SectionHeader'
import { navRowHeight } from '@/lib/catalog'
import { cn } from '@/lib/utils'
import type { NavEntry, NavRow } from '@/lib/types'

const BASE = import.meta.env.BASE_URL

/** Per-kind rail colour — the sidebar's running "book parts" coding. */
function railColor(kind: NavEntry['kind'] | 'calculator'): string {
  switch (kind) {
    case 'hot_topic':
      return '#c2872a'
    case 'case_report':
      return '#0d9488'
    case 'trial':
      return '#3b82f6'
    case 'story':
      return '#e11d48'
    case 'calculator':
      return '#7c3aed'
    default:
      return '#6366f1'
  }
}

export function Sidebar() {
  const catalogLoading = useAppStore((s) => s.catalogLoading)
  const navRows = useAppStore((s) => s.navRows)
  const collapsed = useAppStore((s) => s.sidebarCollapsed)
  const toggleSidebar = useAppStore((s) => s.toggleSidebar)
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const progress = useAppStore((s) => s.progress)
  const selectChapter = useAppStore((s) => s.selectChapter)

  const parentRef = useRef<HTMLDivElement>(null)
  const virtualizer = useVirtualizer({
    count: navRows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: (i) => navRowHeight(navRows[i]),
    overscan: 14,
  })

  if (collapsed) {
    return (
      <aside className="hidden w-12 shrink-0 clinical-border border-r bg-[var(--color-clinical-card-light)] dark:bg-[var(--color-clinical-card-dark)] md:flex md:flex-col md:items-center md:py-3">
        <Button
          variant="ghost"
          size="icon"
          onClick={toggleSidebar}
          aria-label="Expand sidebar"
        >
          <PanelLeftOpen className="h-4 w-4" />
        </Button>
      </aside>
    )
  }

  const entryCount = navRows.filter((r) => r.type === 'entry').length

  return (
    <aside className="hidden w-80 shrink-0 flex-col clinical-border border-r bg-[var(--color-clinical-card-light)] dark:bg-[var(--color-clinical-card-dark)] md:flex">
      <div className="flex items-center justify-between border-b border-zinc-200 px-4 py-3 dark:border-zinc-800">
        <div>
          <p className="text-xs font-semibold uppercase tracking-wide clinical-muted">
            Study Index
          </p>
          <p className="text-sm font-medium">{entryCount} topics ready</p>
        </div>
        <Button variant="ghost" size="icon" onClick={toggleSidebar} aria-label="Collapse sidebar">
          <PanelLeftClose className="h-4 w-4" />
        </Button>
      </div>

      {catalogLoading ? (
        <SidebarSkeleton />
      ) : (
        <div ref={parentRef} className="min-h-0 flex-1 overflow-y-auto">
          <div
            style={{ height: virtualizer.getTotalSize(), position: 'relative' }}
            className="px-1.5 py-2"
          >
            {virtualizer.getVirtualItems().map((row) => {
              const item = navRows[row.index]
              return (
                <div
                  key={row.key}
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: `${row.size}px`,
                    transform: `translateY(${row.start}px)`,
                  }}
                >
                  <NavRowView
                    row={item}
                    activeId={currentChapterId}
                    progress={progress}
                    onSelect={selectChapter}
                  />
                </div>
              )
            })}
          </div>
        </div>
      )}
    </aside>
  )
}

function NavRowView({
  row,
  activeId,
  progress,
  onSelect,
}: {
  row: NavRow
  activeId: string | null
  progress: Record<string, { completed: number; total: number }>
  onSelect: (id: string) => void
}) {
  if (row.type === 'header') {
    return (
      <SectionHeader
        kind={row.headerKind}
        title={row.title}
        subtitle={row.subtitle}
        count={row.count}
      />
    )
  }

  if (row.type === 'calculator') {
    return (
      <a
        href={`${BASE}${row.href}`}
        target="_blank"
        rel="noopener noreferrer"
        style={{ '--rail': railColor('calculator') } as CSSProperties}
        className={cn(
          'group relative mx-1 flex items-center gap-3 rounded-lg py-2.5 pl-4 pr-3 text-left transition-colors duration-100',
          'hover:bg-slate-100/70 dark:hover:bg-zinc-800/50',
        )}
      >
        <span
          aria-hidden
          className="absolute left-1 top-2.5 bottom-2.5 w-[3px] rounded-full opacity-40 transition-opacity group-hover:opacity-80"
          style={{ background: 'var(--rail)' }}
        />
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-medium">{row.title}</p>
          <p className="truncate text-xs clinical-muted">{row.subtitle}</p>
        </div>
        <ExternalLink className="h-3.5 w-3.5 shrink-0 text-violet-500" />
      </a>
    )
  }

  const entry = row.entry
  const prog = progress[entry.id]
  const active = activeId === entry.id
  const total = prog?.total ?? 0
  const completed = prog?.completed ?? 0
  const pct = total > 0 ? Math.round((completed / total) * 100) : 0

  return (
    <button
      type="button"
      onClick={() => onSelect(entry.id)}
      aria-current={active ? 'true' : undefined}
      style={{ '--rail': railColor(entry.kind) } as CSSProperties}
      className={cn(
        'group relative mx-1 flex w-[calc(100%-0.5rem)] flex-col gap-1 rounded-lg py-2 pl-4 pr-3 text-left transition-colors duration-100',
        active ? 'bg-[#efe6d6] dark:bg-zinc-800' : 'hover:bg-slate-100/70 dark:hover:bg-zinc-800/50',
        entry.kind === 'harrison' && 'ml-2',
      )}
    >
      <span
        aria-hidden
        className={cn(
          'absolute left-1 top-2 bottom-2 w-[3px] rounded-full transition-opacity',
          active ? 'opacity-100' : 'opacity-30 group-hover:opacity-70',
        )}
        style={{ background: 'var(--rail)' }}
      />
      <div className="flex items-center gap-2">
        <p className={cn('min-w-0 flex-1 truncate text-sm', active ? 'font-semibold' : 'font-medium')}>
          {entry.title}
        </p>
        {total > 0 && (
          <span className="shrink-0 text-[10px] tabular-nums clinical-muted">
            {completed}/{total}
          </span>
        )}
        <ChevronRight
          className={cn(
            'h-3.5 w-3.5 shrink-0 clinical-muted transition-transform',
            active ? 'translate-x-0' : '-translate-x-0.5 group-hover:translate-x-0',
          )}
        />
      </div>
      <p className="truncate text-xs clinical-muted">{entry.subtitle}</p>
      {total > 0 && (
        <div className="mt-0.5 h-[3px] w-full overflow-hidden rounded-full bg-slate-200/70 dark:bg-zinc-800">
          <div
            className="h-full rounded-full transition-[width] duration-500"
            style={{ width: `${pct}%`, background: 'var(--rail)' }}
          />
        </div>
      )}
    </button>
  )
}
