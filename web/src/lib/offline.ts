import { DATA_BASE } from '@/lib/constants'

const STATUS_KEY = 'h22-offline-status'

export interface OfflineStatus {
  /** number of data files successfully cached on the last run */
  count: number
  /** epoch ms of the last successful download */
  at: number
}

/** Register the service worker (no-op if unsupported, e.g. older browsers). */
export function registerServiceWorker(): void {
  if (typeof navigator === 'undefined' || !('serviceWorker' in navigator)) return
  window.addEventListener('load', () => {
    const url = `${import.meta.env.BASE_URL}sw.js`
    navigator.serviceWorker.register(url, { scope: import.meta.env.BASE_URL }).catch(() => {
      /* registration failures are non-fatal — the app still works online */
    })
  })
}

export function getOfflineStatus(): OfflineStatus | null {
  try {
    const raw = localStorage.getItem(STATUS_KEY)
    return raw ? (JSON.parse(raw) as OfflineStatus) : null
  } catch {
    return null
  }
}

function setOfflineStatus(status: OfflineStatus): void {
  try {
    localStorage.setItem(STATUS_KEY, JSON.stringify(status))
  } catch {
    /* storage full / disabled — ignore */
  }
}

/**
 * Fetch the catalog index plus every provided data file so the service worker
 * caches them for offline use. Runs with bounded concurrency and reports
 * progress. Returns the number of files successfully cached.
 */
export async function downloadAllContent(
  files: string[],
  onProgress?: (done: number, total: number) => void,
): Promise<number> {
  // Make sure the service worker is active so its fetch handler caches responses.
  if ('serviceWorker' in navigator) {
    try {
      await navigator.serviceWorker.ready
    } catch {
      /* proceed anyway — caches.match still works once registered */
    }
  }

  // Dedupe + always include the catalog itself.
  const targets = Array.from(new Set(['index.json', ...files.filter(Boolean)]))
  const total = targets.length
  let done = 0
  let ok = 0
  const CONCURRENCY = 6

  async function worker(queue: string[]) {
    for (const file of queue) {
      try {
        const res = await fetch(`${DATA_BASE}${file}`, { cache: 'reload' })
        if (res.ok) ok += 1
      } catch {
        /* offline / missing — skip */
      } finally {
        done += 1
        onProgress?.(done, total)
      }
    }
  }

  // Split into round-robin lanes for simple bounded concurrency.
  const lanes: string[][] = Array.from({ length: CONCURRENCY }, () => [])
  targets.forEach((f, i) => lanes[i % CONCURRENCY].push(f))
  await Promise.all(lanes.map(worker))

  const status: OfflineStatus = { count: ok, at: Date.now() }
  setOfflineStatus(status)
  return ok
}
