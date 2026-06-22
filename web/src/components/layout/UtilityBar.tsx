import {
  ChevronLeft,
  ChevronRight,
  Bookmark,
  Command,
  Moon,
  Sun,
} from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

export function UtilityBar() {
  const theme = useAppStore((s) => s.theme)
  const toggleTheme = useAppStore((s) => s.toggleTheme)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)
  const goNext = useAppStore((s) => s.goNext)
  const goPrev = useAppStore((s) => s.goPrev)
  const toggleBookmark = useAppStore((s) => s.toggleBookmark)
  const item = useAppStore((s) => s.getCurrentItem())
  const bookmarks = useAppStore((s) => s.bookmarks)
  const bookmarked = item ? Boolean(bookmarks[item.id]) : false

  return (
    <div
      className={cn(
        'sticky bottom-0 z-20 hidden border-t clinical-border md:block',
        'bg-[var(--color-clinical-bg-light)]/90 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/90',
      )}
    >
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-2.5">
        <div className="flex items-center gap-1">
          <Button variant="ghost" size="sm" onClick={goPrev} aria-label="Previous question">
            <ChevronLeft className="h-4 w-4" />
            Prev
          </Button>
          <Button variant="ghost" size="sm" onClick={goNext} aria-label="Next question">
            Next
            <ChevronRight className="h-4 w-4" />
          </Button>
        </div>

        <div className="flex items-center gap-1">
          <Button
            variant="ghost"
            size="icon"
            onClick={() => setCommandOpen(true)}
            aria-label="Open command palette"
            title="⌘K"
          >
            <Command className="h-4 w-4" />
          </Button>
          <Button
            variant="ghost"
            size="icon"
            onClick={() => toggleBookmark()}
            disabled={!item}
            aria-label="Toggle bookmark"
            className={bookmarked ? 'text-amber-500' : undefined}
          >
            <Bookmark className={cn('h-4 w-4', bookmarked && 'fill-current')} />
          </Button>
          <Button
            variant="ghost"
            size="icon"
            onClick={toggleTheme}
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </Button>
        </div>
      </div>
    </div>
  )
}
