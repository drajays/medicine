import { useEffect, useState } from 'react'
import { Command } from 'cmdk'
import { Search, BookOpen, FileQuestion } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import type { SearchResult } from '@/lib/types'
import { cn } from '@/lib/utils'

export function CommandPalette() {
  const open = useAppStore((s) => s.commandOpen)
  const setOpen = useAppStore((s) => s.setCommandOpen)
  const getSearchResults = useAppStore((s) => s.getSearchResults)
  const selectChapter = useAppStore((s) => s.selectChapter)
  const selectItem = useAppStore((s) => s.selectItem)
  const [query, setQuery] = useState('')

  useEffect(() => {
    if (!open) setQuery('')
  }, [open])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault()
        setOpen(!useAppStore.getState().commandOpen)
      }
      if (e.key === 'Escape') setOpen(false)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [setOpen])

  const results = query.trim() ? getSearchResults(query) : []

  const handleSelect = async (result: SearchResult) => {
    if (result.kind === 'chapter') {
      await selectChapter(result.chapterId)
    } else if (result.itemId) {
      await selectItem(result.chapterId, result.itemId)
    }
    setOpen(false)
  }

  if (!open) return null

  return (
    <div className="fixed inset-0 z-50">
      <button
        type="button"
        aria-label="Close command palette"
        className="absolute inset-0 bg-black/40 backdrop-blur-[2px]"
        onClick={() => setOpen(false)}
      />
      <div className="pointer-events-none absolute inset-x-0 top-[12dvh] flex justify-center px-4">
        <Command
          className={cn(
            'pointer-events-auto w-full max-w-xl overflow-hidden rounded-xl shadow-2xl',
            'clinical-border bg-[var(--color-clinical-card-light)] dark:bg-[var(--color-clinical-card-dark)]',
          )}
          label="Command palette"
          shouldFilter={false}
        >
          <div className="flex items-center gap-2 border-b border-zinc-200 px-3 dark:border-zinc-800">
            <Search className="h-4 w-4 clinical-muted shrink-0" />
            <Command.Input
              autoFocus
              value={query}
              onValueChange={setQuery}
              placeholder="Search chapters, topics, questions…"
              className="h-12 w-full bg-transparent text-sm outline-none placeholder:text-zinc-400"
            />
            <kbd className="hidden rounded border border-zinc-200 px-1.5 py-0.5 text-[10px] clinical-muted sm:inline dark:border-zinc-700">
              ESC
            </kbd>
          </div>
          <Command.List className="max-h-80 overflow-y-auto p-2">
            {!query.trim() ? (
              <p className="px-3 py-4 text-xs clinical-muted">
                Type to search — try &ldquo;heart&rdquo;, &ldquo;thyroid&rdquo;, or &ldquo;AKI&rdquo;
              </p>
            ) : results.length === 0 ? (
              <Command.Empty className="px-3 py-8 text-center text-sm clinical-muted">
                No results found.
              </Command.Empty>
            ) : (
              results.map((result) => (
                <Command.Item
                  key={result.id}
                  value={result.id}
                  onSelect={() => handleSelect(result)}
                  className={cn(
                    'flex cursor-pointer items-start gap-3 rounded-lg px-3 py-2.5 text-sm',
                    'aria-selected:bg-blue-50 dark:aria-selected:bg-blue-500/10',
                  )}
                >
                  {result.kind === 'chapter' ? (
                    <BookOpen className="mt-0.5 h-4 w-4 shrink-0 text-blue-500" />
                  ) : (
                    <FileQuestion className="mt-0.5 h-4 w-4 shrink-0 text-emerald-500" />
                  )}
                  <div className="min-w-0">
                    <div className="truncate font-medium">{result.label}</div>
                    <div className="truncate text-xs clinical-muted">{result.subtitle}</div>
                  </div>
                </Command.Item>
              ))
            )}
          </Command.List>
        </Command>
      </div>
    </div>
  )
}
