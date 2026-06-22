import { useEffect } from 'react'
import { useAppStore } from '@/store/useAppStore'

function isTypingTarget(target: EventTarget | null) {
  if (!(target instanceof HTMLElement)) return false
  const tag = target.tagName
  return tag === 'INPUT' || tag === 'TEXTAREA' || target.isContentEditable
}

export function useKeyboardShortcuts() {
  const toggleReveal = useAppStore((s) => s.toggleReveal)
  const goNext = useAppStore((s) => s.goNext)
  const goPrev = useAppStore((s) => s.goPrev)
  const getCurrentItem = useAppStore((s) => s.getCurrentItem)
  const selectMcqOption = useAppStore((s) => s.selectMcqOption)
  const setCommandOpen = useAppStore((s) => s.setCommandOpen)

  useEffect(() => {
    const onKeyDown = (e: KeyboardEvent) => {
      if (isTypingTarget(e.target)) return

      if (e.code === 'Space') {
        e.preventDefault()
        toggleReveal()
        return
      }

      if (e.key === 'ArrowRight') {
        e.preventDefault()
        goNext()
        return
      }

      if (e.key === 'ArrowLeft') {
        e.preventDefault()
        goPrev()
        return
      }

      const item = getCurrentItem()
      if (item?.type === 'mcq' && ['1', '2', '3', '4'].includes(e.key)) {
        e.preventDefault()
        selectMcqOption(item.id, Number(e.key) - 1)
      }
    }

    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [toggleReveal, goNext, goPrev, getCurrentItem, selectMcqOption, setCommandOpen])
}
