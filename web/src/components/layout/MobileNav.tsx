import { useMemo, type ChangeEvent, type ReactNode } from 'react'
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Command,
  Compass,
  List,
  Moon,
  Sun,
} from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { buildSections } from '@/lib/sections'
import { cn } from '@/lib/utils'
import type { HeaderKind } from '@/lib/types'

const BASE = import.meta.env.BASE_URL

const ICON: Partial<Record<HeaderKind, string>> = {
  hot_topics: '🔥',
  case_reports: '📋',
  pediatric_endo: '🧒',
  stories: '💬',
  calculators: '🧮',
  imaging_resources: '🩻',
  trials: '📊',
  harrison_banner: '📖',
}

export function MobileNav({ onBrowse }: { onBrowse: () => void }) {
  const theme = useAppStore((s) => s.theme)
  const toggleTheme = useAppStore((s) => s.toggleTheme)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)
  const goBack = useAppStore((s) => s.goBack)
  const goForward = useAppStore((s) => s.goForward)
  const historyIndex = useAppStore((s) => s.historyIndex)
  const historyLen = useAppStore((s) => s.history.length)
  const navRows = useAppStore((s) => s.navRows)
  const selectChapter = useAppStore((s) => s.selectChapter)
  const clearSelection = useAppStore((s) => s.clearSelection)

  const sections = useMemo(() => buildSections(navRows), [navRows])
  const canBack = historyIndex > 0
  const canFwd = historyIndex < historyLen - 1

  const onJump = (e: ChangeEvent<HTMLSelectElement>) => {
    const value = e.target.value
    if (!value) return
    if (value === '__home__') {
      clearSelection()
      return
    }
    for (const section of sections) {
      const item = section.items.find((it) => it.id === value)
      if (item) {
        if (item.href) window.open(`${BASE}${item.href}`, '_blank', 'noopener,noreferrer')
        else selectChapter(item.id)
        return
      }
    }
  }

  return (
    <nav
      className={cn(
        'fixed inset-x-0 bottom-0 z-30 border-t clinical-border md:hidden',
        'bg-[var(--color-clinical-card-light)]/95 backdrop-blur-lg dark:bg-[var(--color-clinical-card-dark)]/95',
        'pb-[env(safe-area-inset-bottom)]',
      )}
      aria-label="Mobile navigation"
    >
      <div className="grid grid-cols-6">
        <MobileNavButton label="Back" onClick={goBack} disabled={!canBack}>
          <ArrowLeft className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Fwd" onClick={goForward} disabled={!canFwd}>
          <ArrowRight className="h-5 w-5" />
        </MobileNavButton>

        {/* Jump: a transparent native select overlays the icon+label cell */}
        <div className="relative flex flex-col items-center gap-0.5 py-2.5 text-[10px] font-medium clinical-muted active:bg-slate-100 dark:active:bg-zinc-800">
          <Compass className="h-5 w-5" />
          Jump
          <select
            aria-label="Jump to a section or topic"
            value=""
            onChange={onJump}
            disabled={!sections.length}
            className="absolute inset-0 h-full w-full cursor-pointer opacity-0"
          >
            <option value="" disabled>
              Jump to…
            </option>
            <option value="__home__">🏠 Home — all sections</option>
            {sections.map((section) => (
              <optgroup key={section.key} label={`${ICON[section.kind] ?? ''} ${section.title}`}>
                {section.items.map((item) => (
                  <option key={item.id} value={item.id}>
                    {item.title}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </div>

        <MobileNavButton label="Browse" onClick={onBrowse}>
          <List className="h-5 w-5" />
        </MobileNavButton>
        <MobileNavButton label="Search" onClick={() => setCommandOpen(true)}>
          <Command className="h-5 w-5" />
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
  children: ReactNode
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
