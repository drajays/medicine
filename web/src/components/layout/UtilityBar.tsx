import {
  ChevronLeft,
  ChevronRight,
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
  const goNextChapter = useAppStore((s) => s.goNextChapter)
  const goPrevChapter = useAppStore((s) => s.goPrevChapter)
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const chapter = useAppStore((s) => s.getCurrentChapter())

  return (
    <div
      className={cn(
        'sticky bottom-0 z-20 hidden border-t clinical-border md:block',
        'bg-[var(--color-clinical-bg-light)]/90 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/90',
      )}
    >
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-2.5">
        <div className="flex items-center gap-1">
          <Button
            variant="ghost"
            size="sm"
            onClick={goPrevChapter}
            disabled={!currentChapterId}
            aria-label="Previous topic"
          >
            <ChevronLeft className="h-4 w-4" />
            Prev topic
          </Button>
          <Button
            variant="ghost"
            size="sm"
            onClick={goNextChapter}
            disabled={!currentChapterId}
            aria-label="Next topic"
          >
            Next topic
            <ChevronRight className="h-4 w-4" />
          </Button>
        </div>

        <p className="max-w-md truncate text-xs clinical-muted">
          {chapter?.title ?? 'Select a topic'}
        </p>

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
          <Button variant="ghost" size="icon" onClick={toggleTheme} aria-label="Toggle theme">
            {theme === 'dark' ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </Button>
        </div>
      </div>
    </div>
  )
}
