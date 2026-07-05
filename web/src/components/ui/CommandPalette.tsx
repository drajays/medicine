import { useEffect, useRef, useState } from 'react'
import { Command } from 'cmdk'
import { Search, BookOpen, FileQuestion, Download, Upload, ScrollText } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { CONTENT_LOG_KEY } from '@/components/chapter/LandingPage'
import type { SearchResult } from '@/lib/types'
import { cn } from '@/lib/utils'
import {
  buildStudyExport,
  downloadJSON,
  exportFilename,
  isStudyDataEmpty,
  parseStudyExport,
} from '@/lib/studyData'

interface PaletteAction {
  id: string
  label: string
  subtitle: string
  keywords: string[]
  icon: typeof Download
  run: () => void
}

export function CommandPalette() {
  const open = useAppStore((s) => s.commandOpen)
  const setOpen = useAppStore((s) => s.setCommandOpen)
  const getSearchResults = useAppStore((s) => s.getSearchResults)
  const selectChapter = useAppStore((s) => s.selectChapter)
  const selectItem = useAppStore((s) => s.selectItem)
  const exportStudyData = useAppStore((s) => s.exportStudyData)
  const importStudyData = useAppStore((s) => s.importStudyData)
  const showLanding = useAppStore((s) => s.showLanding)
  const [query, setQuery] = useState('')
  const [actionMsg, setActionMsg] = useState<string | null>(null)
  const fileInput = useRef<HTMLInputElement>(null)
  const importMode = useRef<'merge' | 'replace'>('merge')

  useEffect(() => {
    if (!open) {
      setQuery('')
      setActionMsg(null)
    }
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

  const onExport = () => {
    const data = exportStudyData()
    if (isStudyDataEmpty(data)) {
      setActionMsg('Nothing to export yet — mark or rate some items first.')
      return
    }
    downloadJSON(exportFilename(), buildStudyExport(data))
    setOpen(false)
  }

  const triggerImport = (mode: 'merge' | 'replace') => {
    if (mode === 'replace' && !window.confirm('Replace ALL your current study data with a backup file?'))
      return
    importMode.current = mode
    fileInput.current?.click()
  }

  const onPickFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    e.target.value = ''
    if (!file) return
    const result = parseStudyExport(await file.text())
    if (!result.ok) {
      setActionMsg(`Import failed: ${result.error}`)
      return
    }
    importStudyData(result.value.data, importMode.current)
    setOpen(false)
  }

  const actions: PaletteAction[] = [
    {
      id: 'action-content-log',
      label: 'View content update log',
      subtitle: 'Chronological record of new and updated study modules',
      keywords: ['updates', 'changelog', 'log', 'new', 'content', 'history'],
      icon: ScrollText,
      run: () => {
        showLanding(CONTENT_LOG_KEY)
        setOpen(false)
      },
    },
    {
      id: 'action-export',
      label: 'Export study backup (.json)',
      subtitle: 'Download all your marks, ratings, flags & bookmarks',
      keywords: ['export', 'backup', 'download', 'save', 'data'],
      icon: Download,
      run: onExport,
    },
    {
      id: 'action-import-merge',
      label: 'Import backup — merge',
      subtitle: 'Restore a backup, keeping your current data',
      keywords: ['import', 'restore', 'backup', 'merge', 'upload', 'data'],
      icon: Upload,
      run: () => triggerImport('merge'),
    },
    {
      id: 'action-import-replace',
      label: 'Import backup — replace all',
      subtitle: 'Restore a backup, overwriting your current data',
      keywords: ['import', 'restore', 'backup', 'replace', 'overwrite', 'upload', 'data'],
      icon: Upload,
      run: () => triggerImport('replace'),
    },
  ]

  const q = query.trim().toLowerCase()
  const shownActions = actions.filter(
    (a) => !q || a.label.toLowerCase().includes(q) || a.keywords.some((k) => k.includes(q)),
  )

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
          <input
            ref={fileInput}
            type="file"
            accept="application/json,.json"
            className="hidden"
            onChange={onPickFile}
          />
          <Command.List className="max-h-80 overflow-y-auto p-2">
            {actionMsg && (
              <p className="mx-1 mb-1 rounded-md bg-amber-50 px-3 py-2 text-xs text-amber-800 dark:bg-amber-500/10 dark:text-amber-300">
                {actionMsg}
              </p>
            )}

            {shownActions.length > 0 && (
              <Command.Group
                heading="Actions"
                className="[&_[cmdk-group-heading]]:px-3 [&_[cmdk-group-heading]]:py-1.5 [&_[cmdk-group-heading]]:text-[10px] [&_[cmdk-group-heading]]:font-bold [&_[cmdk-group-heading]]:uppercase [&_[cmdk-group-heading]]:tracking-wider [&_[cmdk-group-heading]]:clinical-muted"
              >
                {shownActions.map((action) => (
                  <Command.Item
                    key={action.id}
                    value={action.id}
                    keywords={action.keywords}
                    onSelect={action.run}
                    className={cn(
                      'flex cursor-pointer items-start gap-3 rounded-lg px-3 py-2.5 text-sm',
                      'aria-selected:bg-blue-50 dark:aria-selected:bg-blue-500/10',
                    )}
                  >
                    <action.icon className="mt-0.5 h-4 w-4 shrink-0 text-amber-500" />
                    <div className="min-w-0">
                      <div className="truncate font-medium">{action.label}</div>
                      <div className="truncate text-xs clinical-muted">{action.subtitle}</div>
                    </div>
                  </Command.Item>
                ))}
              </Command.Group>
            )}

            {!query.trim() ? (
              <p className="px-3 py-4 text-xs clinical-muted">
                Type to search — try &ldquo;heart&rdquo;, &ldquo;thyroid&rdquo;, or &ldquo;AKI&rdquo;
              </p>
            ) : results.length === 0 && shownActions.length === 0 ? (
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
