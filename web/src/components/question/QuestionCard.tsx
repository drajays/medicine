import { useAppStore } from '@/store/useAppStore'
import { QuestionSkeleton } from '@/components/ui/Skeleton'
import { NoteContent } from '@/components/question/NoteContent'
import { McqContent } from '@/components/question/McqContent'
import {
  AssertionReasonContent,
  ShortAnswerContent,
  TrueFalseContent,
  WhyHowContent,
} from '@/components/question/GenericStudyContent'
import { SwipeArea } from '@/hooks/useSwipeGesture'

export function QuestionCard() {
  const chapterLoading = useAppStore((s) => s.chapterLoading)
  const item = useAppStore((s) => s.getCurrentItem())
  const revealed = useAppStore((s) => s.revealed)
  const mcqSelections = useAppStore((s) => s.mcqSelections)
  const toggleReveal = useAppStore((s) => s.toggleReveal)
  const selectMcqOption = useAppStore((s) => s.selectMcqOption)
  const goNext = useAppStore((s) => s.goNext)
  const goPrev = useAppStore((s) => s.goPrev)
  const currentChapterId = useAppStore((s) => s.currentChapterId)

  if (!currentChapterId) {
    return (
      <div className="mx-auto max-w-2xl px-4 py-12 md:py-20">
        <div className="clinical-card p-8 text-center">
          <h2 className="text-xl font-semibold">Welcome to Harrison&apos;s 22e</h2>
          <p className="clinical-serif mt-3 text-[15px] leading-relaxed clinical-muted">
            Select a chapter from the sidebar or press{' '}
            <kbd className="rounded border px-1.5 py-0.5 text-xs">⌘K</kbd> to search.
            Navigate questions with arrow keys; press space to reveal answers.
          </p>
          <div className="mt-8 grid gap-3 text-left sm:grid-cols-3">
            {[
              { k: '⌘K', v: 'Command palette' },
              { k: '← →', v: 'Prev / Next' },
              { k: 'Space', v: 'Reveal answer' },
            ].map((hint) => (
              <div key={hint.k} className="rounded-lg clinical-border p-4">
                <kbd className="text-sm font-semibold">{hint.k}</kbd>
                <p className="mt-1 text-xs clinical-muted">{hint.v}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  if (chapterLoading || !item) {
    return <QuestionSkeleton />
  }

  const isRevealed = Boolean(revealed[item.id])
  const toggle = () => toggleReveal(item.id)

  return (
    <SwipeArea
      className="mx-auto max-w-3xl px-4 py-4 md:px-8 md:py-6"
      onSwipeLeft={goNext}
      onSwipeRight={goPrev}
    >
      {item.type === 'note' ? (
        <NoteContent item={item} revealed={isRevealed} onToggleReveal={toggle} />
      ) : item.type === 'mcq' ? (
        <McqContent
          item={item}
          revealed={isRevealed}
          selected={mcqSelections[item.id] ?? null}
          onToggleReveal={toggle}
          onSelect={(index) => selectMcqOption(item.id, index)}
        />
      ) : item.type === 'true_false' ? (
        <TrueFalseContent item={item} revealed={isRevealed} onToggleReveal={toggle} />
      ) : item.type === 'assertion_reason' ? (
        <AssertionReasonContent item={item} revealed={isRevealed} onToggleReveal={toggle} />
      ) : item.type === 'why' || item.type === 'how' ? (
        <WhyHowContent item={item} revealed={isRevealed} onToggleReveal={toggle} />
      ) : item.type === 'shortanswer' ? (
        <ShortAnswerContent item={item} revealed={isRevealed} onToggleReveal={toggle} />
      ) : null}
    </SwipeArea>
  )
}
