import { useEffect, useState } from 'react'
import { CloudOff, Download, Check, Loader2, RefreshCw } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import { downloadAllContent, getOfflineStatus, type OfflineStatus } from '@/lib/offline'

const supported =
  typeof navigator !== 'undefined' && 'serviceWorker' in navigator && 'caches' in window

function timeAgo(ms: number): string {
  const d = Math.floor((Date.now() - ms) / 1000)
  if (d < 60) return 'just now'
  if (d < 3600) return `${Math.floor(d / 60)}m ago`
  if (d < 86400) return `${Math.floor(d / 3600)}h ago`
  return `${Math.floor(d / 86400)}d ago`
}

/**
 * Landing-page control to download all study content into the service-worker
 * cache so the Q-bank works without internet. Also reflects online/offline
 * status.
 */
export function OfflineButton() {
  const navEntries = useAppStore((s) => s.navEntries)
  const files = navEntries.map((e) => e.file).filter(Boolean)

  const [status, setStatus] = useState<OfflineStatus | null>(() => getOfflineStatus())
  const [progress, setProgress] = useState<{ done: number; total: number } | null>(null)
  const [online, setOnline] = useState<boolean>(() =>
    typeof navigator === 'undefined' ? true : navigator.onLine,
  )

  useEffect(() => {
    const on = () => setOnline(true)
    const off = () => setOnline(false)
    window.addEventListener('online', on)
    window.addEventListener('offline', off)
    return () => {
      window.removeEventListener('online', on)
      window.removeEventListener('offline', off)
    }
  }, [])

  if (!supported) return null

  const busy = progress !== null
  const total = files.length + 1 // + index.json

  async function run() {
    if (busy || !files.length) return
    setProgress({ done: 0, total })
    try {
      await downloadAllContent(files, (done, t) => setProgress({ done, total: t }))
      setStatus(getOfflineStatus())
    } finally {
      setProgress(null)
    }
  }

  const pct = progress ? Math.round((progress.done / Math.max(progress.total, 1)) * 100) : 0

  return (
    <div className="mt-3 flex flex-wrap items-center gap-2">
      <button
        type="button"
        onClick={run}
        disabled={busy || !files.length}
        aria-label="Download all content for offline use"
        className={cn(
          'inline-flex items-center gap-2 rounded-lg border px-3 py-1.5 text-xs font-semibold transition-colors',
          'border-amber-300/70 bg-amber-50 text-amber-900 hover:bg-amber-100',
          'dark:border-amber-500/30 dark:bg-amber-500/10 dark:text-amber-200 dark:hover:bg-amber-500/20',
          (busy || !files.length) && 'opacity-70',
        )}
      >
        {busy ? (
          <>
            <Loader2 className="h-3.5 w-3.5 animate-spin" />
            Saving {progress!.done}/{progress!.total} ({pct}%)
          </>
        ) : status ? (
          <>
            <RefreshCw className="h-3.5 w-3.5" />
            Update offline copy
          </>
        ) : (
          <>
            <Download className="h-3.5 w-3.5" />
            Save offline ({total} files)
          </>
        )}
      </button>

      {!busy && status && (
        <span className="inline-flex items-center gap-1 text-[11px] clinical-muted">
          <Check className="h-3.5 w-3.5 text-emerald-600 dark:text-emerald-400" />
          {status.count} files saved · {timeAgo(status.at)}
        </span>
      )}

      {!online && (
        <span className="inline-flex items-center gap-1 rounded-full bg-slate-200 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-slate-600 dark:bg-zinc-700 dark:text-zinc-200">
          <CloudOff className="h-3 w-3" /> Offline
        </span>
      )}
    </div>
  )
}
