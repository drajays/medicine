import { useState } from 'react'
import { RefreshCw } from 'lucide-react'
import { cn } from '@/lib/utils'
import { refreshContent } from '@/lib/offline'

/**
 * Landing-page control that pulls the latest deployed content (new chapters,
 * case reports, calculators, fixes) immediately — bypassing the offline cache —
 * then reloads. Useful because content JSON is served stale-while-revalidate,
 * so freshly published items would otherwise appear only on a later visit.
 */
export function RefreshButton() {
  const [busy, setBusy] = useState(false)

  async function run() {
    if (busy) return
    setBusy(true)
    // refreshContent() ends in a full page reload, so no need to reset `busy`.
    await refreshContent()
  }

  return (
    <button
      type="button"
      onClick={run}
      disabled={busy}
      title="Check for and load the latest content & updates"
      aria-label="Refresh content"
      className={cn(
        'inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs font-semibold transition-colors',
        'border-sky-300/70 bg-sky-50 text-sky-900 hover:bg-sky-100',
        'dark:border-sky-500/30 dark:bg-sky-500/10 dark:text-sky-200 dark:hover:bg-sky-500/20',
        busy && 'opacity-70',
      )}
    >
      <RefreshCw className={cn('h-3.5 w-3.5', busy && 'animate-spin')} />
      {busy ? 'Refreshing…' : 'Refresh / Update'}
    </button>
  )
}
