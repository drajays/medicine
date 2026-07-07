import { useMemo, type ChangeEvent } from 'react'
import { useAppStore } from '@/store/useAppStore'
import { buildSections } from '@/lib/sections'
import { cn } from '@/lib/utils'
import type { HeaderKind } from '@/lib/types'

const BASE = import.meta.env.BASE_URL

const ICON: Partial<Record<HeaderKind, string>> = {
  hot_topics: '🔥',
  case_reports: '📋',
  pediatric_endo: '🧒',
  sub_apps: '⚕️',
  stories: '💬',
  calculators: '🧮',
  imaging_resources: '🩻',
  trials: '📊',
  harrison_banner: '📖',
}

/** A grouped dropdown to jump to any section or topic from anywhere. */
export function SectionJump({ className }: { className?: string }) {
  const navRows = useAppStore((s) => s.navRows)
  const selectChapter = useAppStore((s) => s.selectChapter)
  const clearSelection = useAppStore((s) => s.clearSelection)
  const sections = useMemo(() => buildSections(navRows), [navRows])

  const onChange = (e: ChangeEvent<HTMLSelectElement>) => {
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
    <select
      aria-label="Jump to a section or topic"
      title="Jump to a section or topic"
      value=""
      onChange={onChange}
      disabled={!sections.length}
      className={cn(
        'h-8 max-w-[10rem] rounded-lg border px-2 text-xs font-medium clinical-border',
        'bg-[var(--color-clinical-card-light)] text-slate-700 dark:bg-[var(--color-clinical-card-dark)] dark:text-zinc-200',
        'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-clinical-accent)]/40',
        'disabled:opacity-50',
        className,
      )}
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
  )
}
