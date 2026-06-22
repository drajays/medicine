import { useRef } from 'react'
import { useVirtualizer } from '@tanstack/react-virtual'
import { ChevronRight, PanelLeftClose, PanelLeftOpen } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { Button } from '@/components/ui/Button'
import { SidebarSkeleton } from '@/components/ui/Skeleton'
import { cn } from '@/lib/utils'

const ROW_HEIGHT = 56

export function Sidebar() {
  const catalogLoading = useAppStore((s) => s.catalogLoading)
  const navEntries = useAppStore((s) => s.navEntries)
  const collapsed = useAppStore((s) => s.sidebarCollapsed)
  const toggleSidebar = useAppStore((s) => s.toggleSidebar)
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const progress = useAppStore((s) => s.progress)
  const selectChapter = useAppStore((s) => s.selectChapter)

  const parentRef = useRef<HTMLDivElement>(null)
  const virtualizer = useVirtualizer({
    count: navEntries.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => ROW_HEIGHT,
    overscan: 12,
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

  return (
    <aside className="hidden w-72 shrink-0 flex-col clinical-border border-r bg-[var(--color-clinical-card-light)] dark:bg-[var(--color-clinical-card-dark)] md:flex">
      <div className="flex items-center justify-between border-b border-zinc-200 px-4 py-3 dark:border-zinc-800">
        <div>
          <p className="text-xs font-semibold uppercase tracking-wide clinical-muted">
            Index
          </p>
          <p className="text-sm font-medium">{navEntries.length} ready</p>
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
            className="px-2 py-2"
          >
            {virtualizer.getVirtualItems().map((row) => {
              const entry = navEntries[row.index]
              const prog = progress[entry.id]
              const active = currentChapterId === entry.id
              const total = prog?.total ?? 0
              const completed = prog?.completed ?? 0
              return (
                <button
                  key={entry.id}
                  type="button"
                  onClick={() => selectChapter(entry.id)}
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: `${row.size}px`,
                    transform: `translateY(${row.start}px)`,
                  }}
                  className={cn(
                    'flex items-center gap-3 rounded-lg px-3 text-left transition-colors duration-100',
                    active
                      ? 'bg-blue-50 dark:bg-blue-500/10'
                      : 'hover:bg-slate-50 dark:hover:bg-zinc-800/60',
                  )}
                >
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{entry.title}</p>
                    <p className="truncate text-xs clinical-muted">{entry.sectionTitle}</p>
                  </div>
                  <div className="flex shrink-0 items-center gap-1 text-xs clinical-muted">
                    <span className="tabular-nums">
                      {total > 0 ? `${completed}/${total}` : '·'}
                    </span>
                    <ChevronRight className="h-3.5 w-3.5" />
                  </div>
                </button>
              )
            })}
          </div>
        </div>
      )}
    </aside>
  )
}
