import { useEffect } from 'react'
import { useAppStore } from '@/store/useAppStore'

function isTypingTarget(target: EventTarget | null) {
  if (!(target instanceof HTMLElement)) return false
  const tag = target.tagName
  return tag === 'INPUT' || tag === 'TEXTAREA' || target.isContentEditable
}

export function useKeyboardShortcuts() {
  const goNextChapter = useAppStore((s) => s.goNextChapter)
  const goPrevChapter = useAppStore((s) => s.goPrevChapter)
  const currentChapterId = useAppStore((s) => s.currentChapterId)

  useEffect(() => {
    const onKeyDown = (e: KeyboardEvent) => {
      if (isTypingTarget(e.target)) return
      if (!currentChapterId) return

      if (e.key === 'ArrowRight') {
        e.preventDefault()
        goNextChapter()
      }
      if (e.key === 'ArrowLeft') {
        e.preventDefault()
        goPrevChapter()
      }
    }

    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [goNextChapter, goPrevChapter, currentChapterId])
}
