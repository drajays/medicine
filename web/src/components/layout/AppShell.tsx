import { useEffect, useState } from 'react'
import { Command, List } from 'lucide-react'
import { Sidebar } from '@/components/layout/Sidebar'
import { Breadcrumb } from '@/components/layout/Breadcrumb'
import { UtilityBar } from '@/components/layout/UtilityBar'
import { MobileNav } from '@/components/layout/MobileNav'
import { MobileCatalog } from '@/components/layout/MobileCatalog'
import { QuestionCard } from '@/components/question/QuestionCard'
import { CommandPalette } from '@/components/ui/CommandPalette'
import { Button } from '@/components/ui/Button'
import { useAppStore } from '@/store/useAppStore'
import { useKeyboardShortcuts } from '@/hooks/useKeyboardShortcuts'

export function AppShell() {
  const initCatalog = useAppStore((s) => s.initCatalog)
  const catalog = useAppStore((s) => s.catalog)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)
  const [mobileCatalogOpen, setMobileCatalogOpen] = useState(false)

  useKeyboardShortcuts()

  useEffect(() => {
    initCatalog()
  }, [initCatalog])

  return (
    <div className="flex min-h-dvh flex-col">
      <header className="sticky top-0 z-20 border-b clinical-border bg-[var(--color-clinical-bg-light)]/90 backdrop-blur-md dark:bg-[var(--color-clinical-bg-dark)]/90">
        <div className="flex items-center justify-between gap-3 px-4 py-3 md:px-6">
          <div className="min-w-0">
            <h1 className="truncate text-sm font-semibold md:text-base">
              {catalog?.title ?? "Harrison's 22e — Clinical Q-Bank & Notes"}
            </h1>
            <div className="mt-0.5 hidden md:block">
              <Breadcrumb />
            </div>
          </div>
          <div className="flex items-center gap-2">
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
          <QuestionCard />
        </main>
      </div>

      <UtilityBar />
      <MobileNav onBrowse={() => setMobileCatalogOpen(true)} />
      <MobileCatalog open={mobileCatalogOpen} onClose={() => setMobileCatalogOpen(false)} />
      <CommandPalette />
    </div>
  )
}
