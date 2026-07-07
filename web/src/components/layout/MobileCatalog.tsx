import { X } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { SectionHeader, entryKindAccent } from '@/components/layout/SectionHeader'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'
import type { NavRow } from '@/lib/types'

const BASE = import.meta.env.BASE_URL

interface MobileCatalogProps {
  open: boolean
  onClose: () => void
}

export function MobileCatalog({ open, onClose }: MobileCatalogProps) {
  const navRows = useAppStore((s) => s.navRows)
  const currentChapterId = useAppStore((s) => s.currentChapterId)
  const progress = useAppStore((s) => s.progress)
  const selectChapter = useAppStore((s) => s.selectChapter)

  if (!open) return null

  const handleSelect = async (id: string) => {
    await selectChapter(id)
    onClose()
  }

  return (
    <div className="fixed inset-0 z-40 md:hidden">
      <button
        type="button"
        aria-label="Close catalog"
        className="absolute inset-0 bg-black/45 backdrop-blur-[1px]"
        onClick={onClose}
      />
      <div className="absolute inset-x-0 bottom-0 top-14 flex flex-col rounded-t-2xl clinical-border border-b-0 bg-[var(--color-clinical-card-light)] shadow-2xl dark:bg-[var(--color-clinical-card-dark)]">
        <div className="flex items-center justify-between border-b border-zinc-200 px-4 py-3 dark:border-zinc-800">
          <div>
            <p className="text-sm font-semibold">Browse Catalog</p>
            <p className="text-xs clinical-muted">Hot topics · Cases · Trials · Chapters</p>
          </div>
          <Button variant="ghost" size="icon" onClick={onClose} aria-label="Close">
            <X className="h-4 w-4" />
          </Button>
        </div>
        <div className="min-h-0 flex-1 overflow-y-auto px-1 py-2 pb-24">
          {navRows.map((row) => (
            <MobileNavRow
              key={
                row.type === 'header'
                  ? row.id
                  : row.type === 'calculator' || row.type === 'imaging' || row.type === 'sub_app'
                    ? row.id
                    : row.entry.id
              }
              row={row}
              activeId={currentChapterId}
              progress={progress}
              onSelect={handleSelect}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

function MobileNavRow({
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
        className={cn(
          'mx-1 flex items-center rounded-lg px-3 py-3',
          entryKindAccent('calculator'),
        )}
      >
        <div className="min-w-0">
          <p className="text-sm font-medium">{row.title}</p>
          <p className="text-xs clinical-muted">{row.subtitle} · Opens in new tab</p>
        </div>
      </a>
    )
  }

  if (row.type === 'imaging') {
    return (
      <a
        href={`${BASE}${row.href}`}
        target="_blank"
        rel="noopener noreferrer"
        className={cn('mx-1 flex items-center rounded-lg px-3 py-3', entryKindAccent('imaging'))}
      >
        <div className="min-w-0">
          <p className="text-sm font-medium">{row.title}</p>
          <p className="text-xs clinical-muted">{row.subtitle} · Opens in new tab</p>
        </div>
      </a>
    )
  }

  if (row.type === 'sub_app') {
    return (
      <a
        href={`${BASE}${row.href}`}
        target="_blank"
        rel="noopener noreferrer"
        className={cn('mx-1 flex items-center rounded-lg px-3 py-3', entryKindAccent('sub_app'))}
      >
        <div className="min-w-0">
          <p className="text-sm font-medium">{row.title}</p>
          <p className="text-xs clinical-muted">{row.subtitle} · Opens in new tab</p>
        </div>
      </a>
    )
  }

  const entry = row.entry
  const prog = progress[entry.id]
  const active = activeId === entry.id

  return (
    <button
      type="button"
      onClick={() => onSelect(entry.id)}
      className={cn(
        'mx-1 flex w-[calc(100%-0.5rem)] flex-col rounded-lg px-3 py-3 text-left',
        entryKindAccent(entry.kind),
        active ? 'bg-blue-50 dark:bg-blue-500/10' : 'active:bg-slate-100 dark:active:bg-zinc-800',
        entry.kind === 'harrison' && 'ml-2',
      )}
    >
      <p className="text-sm font-medium leading-snug">{entry.title}</p>
      <p className="mt-0.5 text-xs clinical-muted">
        {entry.subtitle}
        {prog?.total ? ` · ${prog.completed}/${prog.total}` : ''}
      </p>
    </button>
  )
}
