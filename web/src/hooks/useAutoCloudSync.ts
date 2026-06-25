import { useEffect, useRef } from 'react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { autoPushIfReady, useSyncStore } from '@/stores/syncStore'

const DEBOUNCE_MS = 45_000

/**
 * Debounced cloud upload after study activity when the student is signed in.
 */
export function useAutoCloudSync() {
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null)
  const restoreSession = useSyncStore((s) => s.restoreSession)

  const marks = useAppStore((s) => s.marks)
  const revealed = useAppStore((s) => s.revealed)
  const readItems = useAppStore((s) => s.readItems)
  const mcqSelections = useAppStore((s) => s.mcqSelections)
  const itemEngagement = useAppStore((s) => s.itemEngagement)
  const totalEngagementMs = useAppStore((s) => s.totalEngagementMs)
  const reviews = useRevisionStore((s) => s.reviews)

  useEffect(() => {
    restoreSession()
  }, [restoreSession])

  useEffect(() => {
    if (timer.current) clearTimeout(timer.current)
    timer.current = setTimeout(() => {
      void autoPushIfReady()
    }, DEBOUNCE_MS)
    return () => {
      if (timer.current) clearTimeout(timer.current)
    }
  }, [marks, revealed, readItems, mcqSelections, itemEngagement, totalEngagementMs, reviews])

  useEffect(() => {
    const onHide = () => {
      void autoPushIfReady()
    }
    const onUnload = () => {
      void autoPushIfReady()
    }
    document.addEventListener('visibilitychange', onHide)
    window.addEventListener('pagehide', onUnload)
    return () => {
      document.removeEventListener('visibilitychange', onHide)
      window.removeEventListener('pagehide', onUnload)
    }
  }, [])
}
