import {
  BookOpen,
  ChevronLeft,
  ChevronRight,
  Command,
  Home,
  Moon,
  Sun,
} from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'

export function MobileNav() {
  const theme = useAppStore((s) => s.theme)
  const toggleTheme = useAppStore((s) => s.toggleTheme)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)
  const goNext = useAppStore((s) => s.goNext)
  const goPrev = useAppStore((s) => s.goPrev)
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const clearSelection = useAppStore((s) => s.clearSelection)

  return (
    <nav
      className={cn(
        'fixed inset-x-0 bottom-0 z-30 border-t clinical-border md:hidden',
        'bg-[var(--color-clinical-card-light)]/95 backdrop-blur-lg dark:bg-[var(--color-clinical-card-dark)]/95',
        'pb-[env(safe-area-inset-bottom)]',
      )}
      aria-label="Mobile navigation"
    >
      <div className="grid grid-cols-5">
        <MobileNavButton label="Home" onClick={clearSelection}>
          <Home className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Prev" onClick={goPrev} disabled={!currentChapterId}>
          <ChevronLeft className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Search" onClick={() => setCommandOpen(true)}>
          <Command className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Next" onClick={goNext} disabled={!currentChapterId}>
          <ChevronRight className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Theme" onClick={toggleTheme}>
          {theme === 'dark' ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
        </MobileNavButton>
      </div>
      <p className="flex items-center justify-center gap-1 py-1 text-[10px] clinical-muted">
        <BookOpen className="h-3 w-3" />
        Swipe left/right on questions
      </p>
    </nav>
  )
}

function MobileNavButton({
  children,
  label,
  onClick,
  disabled,
}: {
  children: React.ReactNode
  label: string
  onClick: () => void
  disabled?: boolean
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={cn(
        'flex flex-col items-center gap-0.5 py-2.5 text-[10px] font-medium clinical-muted',
        'active:bg-slate-100 dark:active:bg-zinc-800',
        'disabled:opacity-30',
      )}
    >
      {children}
      {label}
    </button>
  )
}
