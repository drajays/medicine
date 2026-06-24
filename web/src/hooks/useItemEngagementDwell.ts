import { useEffect, useRef, type RefObject } from 'react'
import { useAppStore } from '@/store/useAppStore'
import { DWELL_TICK_MS, isItemEngaged } from '@/lib/studyProgress'

/**
 * After an item is engaged, credit bounded dwell time only while it stays
 * ≥50% visible and the document tab is active. Scrolling past without
 * engaging awards nothing.
 */
export function useItemEngagementDwell(itemId: string, rootRef: RefObject<HTMLElement | null>) {
  const creditDwell = useAppStore((s) => s.creditItemDwell)
  const engaged = useAppStore((s) =>
    isItemEngaged(itemId, {
      revealed: s.revealed,
      readItems: s.readItems,
      mcqSelections: s.mcqSelections,
      marks: s.marks,
    }),
  )

  const dwellAccrued = useRef(0)
  const visible = useRef(false)

  useEffect(() => {
    dwellAccrued.current = 0
  }, [itemId])

  useEffect(() => {
    if (!engaged) return
    const el = rootRef.current
    if (!el) return

    const observer = new IntersectionObserver(
      ([entry]) => {
        visible.current = entry.isIntersecting && entry.intersectionRatio >= 0.5
      },
      { threshold: [0, 0.5, 1] },
    )
    observer.observe(el)
    return () => observer.disconnect()
  }, [engaged, itemId, rootRef])

  useEffect(() => {
    if (!engaged) return

    const tick = () => {
      if (!visible.current || document.visibilityState !== 'visible') return
      const added = creditDwell(itemId, DWELL_TICK_MS, dwellAccrued.current)
      dwellAccrued.current += added
    }

    const id = window.setInterval(tick, DWELL_TICK_MS)
    return () => window.clearInterval(id)
  }, [engaged, itemId, creditDwell])
}
