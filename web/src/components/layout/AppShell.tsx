import { useEffect, useState } from 'react'
import { ArrowLeft, ArrowRight, CalendarClock, Command, List, MessageSquare } from 'lucide-react'
import { Sidebar } from '@/components/layout/Sidebar'
import { REVISE_KEY } from '@/components/chapter/LandingPage'
import { useRevisionStore } from '@/stores/revisionStore'
import { Breadcrumb } from '@/components/layout/Breadcrumb'
import { SectionJump } from '@/components/layout/SectionJump'
import { FeedbackPanel } from '@/components/layout/FeedbackPanel'
import { UtilityBar } from '@/components/layout/UtilityBar'
import { MobileNav } from '@/components/layout/MobileNav'
import { MobileCatalog } from '@/components/layout/MobileCatalog'
import { ChapterView } from '@/components/chapter/ChapterView'
import { CommandPalette } from '@/components/ui/CommandPalette'
import { Button } from '@/components/ui/Button'
import { useAppStore } from '@/store/useAppStore'
import { useKeyboardShortcuts } from '@/hooks/useKeyboardShortcuts'
import { useAutoCloudSync } from '@/hooks/useAutoCloudSync'

export function AppShell() {
  const initCatalog = useAppStore((s) => s.initCatalog)
  const catalog = useAppStore((s) => s.catalog)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)
  const goBack = useAppStore((s) => s.goBack)
  const goForward = useAppStore((s) => s.goForward)
  const historyIndex = useAppStore((s) => s.historyIndex)
  const historyLen = useAppStore((s) => s.history.length)
  const feedbackCount = useAppStore(
    (s) => new Set([...Object.keys(s.ratings), ...Object.keys(s.flags)]).size,
  )
  const marks = useAppStore((s) => s.marks)
  const showLanding = useAppStore((s) => s.showLanding)
  const bootstrapFromMarks = useRevisionStore((s) => s.bootstrapFromMarks)
  const dueCount = useRevisionStore((s) => s.getDueCount())
  const [mobileCatalogOpen, setMobileCatalogOpen] = useState(false)
  const [feedbackOpen, setFeedbackOpen] = useState(false)

  const canBack = historyIndex > 0
  const canFwd = historyIndex < historyLen - 1

  useKeyboardShortcuts()
  useAutoCloudSync()

  useEffect(() => {
    initCatalog()
  }, [initCatalog])

  // Keep the revision engine reconciled with study marks app-wide, so the
  // "due today" badge is accurate even before the Revise tab is opened.
  useEffect(() => {
    bootstrapFromMarks(marks)
  }, [marks, bootstrapFromMarks])

  return (
    <div className="flex h-dvh flex-col overflow-hidden">
      <header className="z-20 shrink-0 border-b clinical-border bg-[var(--color-clinical-bg-light)]/90 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/90">
        <div className="flex items-center justify-between gap-2 px-3 py-2.5 md:px-6">
          <div className="flex min-w-0 items-center gap-1.5">
            <Button
              variant="ghost"
              size="icon"
              onClick={goBack}
              disabled={!canBack}
              aria-label="Go back"
              title="Back"
            >
              <ArrowLeft className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="icon"
              onClick={goForward}
              disabled={!canFwd}
              aria-label="Go forward"
              title="Forward"
            >
              <ArrowRight className="h-4 w-4" />
            </Button>
            <div className="min-w-0">
              <h1 className="truncate text-sm font-semibold md:text-base">
                {catalog?.title ?? "Harrison's 22e — Clinical Q-Bank & Notes"}
              </h1>
              <div className="mt-0.5 hidden md:block">
                <Breadcrumb />
              </div>
            </div>
          </div>
          <div className="flex shrink-0 items-center gap-2">
            {dueCount > 0 && (
              <Button
                variant="outline"
                size="sm"
                onClick={() => showLanding(REVISE_KEY)}
                title={`${dueCount} card${dueCount === 1 ? '' : 's'} due for revision`}
                aria-label={`${dueCount} cards due for revision`}
                className="border-amber-300 text-amber-700 dark:border-amber-500/40 dark:text-amber-300"
              >
                <CalendarClock className="h-3.5 w-3.5" />
                <span className="hidden sm:inline">Due</span>
                <span className="rounded-full bg-amber-500/20 px-1.5 text-[10px] font-bold tabular-nums text-amber-700 dark:text-amber-300">
                  {dueCount}
                </span>
              </Button>
            )}
            <Button
              variant="outline"
              size="sm"
              onClick={() => setFeedbackOpen(true)}
              title="My ratings & flags"
              aria-label="My ratings and flags"
            >
              <MessageSquare className="h-3.5 w-3.5" />
              {feedbackCount > 0 && (
                <span className="rounded-full bg-amber-500/20 px-1.5 text-[10px] font-bold text-amber-700 dark:text-amber-300">
                  {feedbackCount}
                </span>
              )}
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => showLanding('__mock_exam__')}
              title="CBT Mock Test"
              className="inline-flex text-blue-700 dark:text-blue-400 border-blue-200 dark:border-blue-900"
            >
              <span className="mr-1">📝</span> <span className="hidden sm:inline">Mock Test</span>
            </Button>
            <SectionJump />
            <Button
              variant="outline"
              size="sm"
              className="md:hidden"
              onClick={() => setMobileCatalogOpen(true)}
            >
              <List className="h-3.5 w-3.5" />
              Browse
            </Button>
            <Button
              variant="outline"
              size="sm"
              className="hidden sm:inline-flex"
              onClick={() => setCommandOpen(true)}
            >
              <Command className="h-3.5 w-3.5" />
              Search
              <kbd className="rounded border px-1 py-0.5 text-[10px] clinical-muted">⌘K</kbd>
            </Button>
          </div>
        </div>
        <div className="border-t border-zinc-200 px-4 py-2 md:hidden dark:border-zinc-800">
          <Breadcrumb />
        </div>
      </header>

      <div className="flex min-h-0 flex-1">
        <Sidebar />
        <main className="min-w-0 flex-1 overflow-y-auto pb-24 md:pb-0">
          <ChapterView />
        </main>
      </div>

      <UtilityBar />
      <MobileNav onBrowse={() => setMobileCatalogOpen(true)} />
      <MobileCatalog open={mobileCatalogOpen} onClose={() => setMobileCatalogOpen(false)} />
      <FeedbackPanel open={feedbackOpen} onClose={() => setFeedbackOpen(false)} />
      <CommandPalette />
    </div>
  )
}
