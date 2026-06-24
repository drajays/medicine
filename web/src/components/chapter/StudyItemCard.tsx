import { useAppStore } from '@/store/useAppStore'
import { ItemFeedback } from '@/components/chapter/ItemFeedback'
import { NoteContent } from '@/components/question/NoteContent'
import { McqContent } from '@/components/question/McqContent'
import {
  AssertionReasonContent,
  ShortAnswerContent,
  TrueFalseContent,
  WhyHowContent,
} from '@/components/question/GenericStudyContent'
import type { StudyItem } from '@/lib/types'

export function StudyItemCard({ item, index }: { item: StudyItem; index: number }) {
  const revealed = useAppStore((s) => s.revealed)
  const mcqSelections = useAppStore((s) => s.mcqSelections)
  const toggleReveal = useAppStore((s) => s.toggleReveal)
  const selectMcqOption = useAppStore((s) => s.selectMcqOption)

  const isRevealed = Boolean(revealed[item.id])
  const toggle = () => toggleReveal(item.id)

  return (
    <div id={`item-${item.id}`} className="scroll-mt-24">
      {item.type === 'note' ? (
        <NoteContent item={item} index={index} />
      ) : item.type === 'mcq' ? (
        <McqContent
          item={item}
          index={index}
          revealed={isRevealed}
          selected={mcqSelections[item.id] ?? null}
          onToggleReveal={toggle}
          onSelect={(opt) => selectMcqOption(item.id, opt)}
        />
      ) : item.type === 'true_false' ? (
        <TrueFalseContent item={item} index={index} revealed={isRevealed} onToggleReveal={toggle} />
      ) : item.type === 'assertion_reason' ? (
        <AssertionReasonContent
          item={item}
          index={index}
          revealed={isRevealed}
          onToggleReveal={toggle}
        />
      ) : item.type === 'why' || item.type === 'how' ? (
        <WhyHowContent item={item} index={index} />
      ) : item.type === 'shortanswer' ? (
        <ShortAnswerContent
          item={item}
          index={index}
          revealed={isRevealed}
          onToggleReveal={toggle}
        />
      ) : null}
      <ItemFeedback item={item} />
    </div>
  )
}
