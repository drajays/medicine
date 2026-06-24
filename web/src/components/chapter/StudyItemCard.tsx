import { useRef } from 'react'
import { useAppStore } from '@/store/useAppStore'
import { ItemFeedback } from '@/components/chapter/ItemFeedback'
import { MarkReadButton } from '@/components/chapter/MarkReadButton'
import { StudyMarks } from '@/components/chapter/StudyMarks'
import { NoteContent } from '@/components/question/NoteContent'
import { McqContent } from '@/components/question/McqContent'
import {
  AssertionReasonContent,
  ShortAnswerContent,
  TrueFalseContent,
  WhyHowContent,
} from '@/components/question/GenericStudyContent'
import { useItemEngagementDwell } from '@/hooks/useItemEngagementDwell'
import { isItemEngaged, itemRequiresExplicitRead } from '@/lib/studyProgress'
import type { StudyItem } from '@/lib/types'

export function StudyItemCard({ item, index }: { item: StudyItem; index: number }) {
  const rootRef = useRef<HTMLDivElement>(null)
  const revealed = useAppStore((s) => s.revealed)
  const readItems = useAppStore((s) => s.readItems)
  const mcqSelections = useAppStore((s) => s.mcqSelections)
  const marks = useAppStore((s) => s.marks)
  const toggleReveal = useAppStore((s) => s.toggleReveal)
  const selectMcqOption = useAppStore((s) => s.selectMcqOption)
  const markItemRead = useAppStore((s) => s.markItemRead)

  const isRevealed = Boolean(revealed[item.id])
  const isRead = Boolean(readItems[item.id])
  const toggle = () => toggleReveal(item.id)
  const needsRead = itemRequiresExplicitRead(item.type)
  const engaged = isItemEngaged(item.id, { revealed, readItems, mcqSelections, marks })

  useItemEngagementDwell(item.id, rootRef)

  return (
    <div ref={rootRef} id={`item-${item.id}`} className="scroll-mt-24">
      {item.type === 'note' ? (
        <>
          <NoteContent item={item} index={index} />
          {needsRead && (
            <div className="px-1">
              <MarkReadButton read={isRead || engaged} onMarkRead={() => markItemRead(item.id)} />
            </div>
          )}
        </>
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
        <>
          <WhyHowContent item={item} index={index} />
          {needsRead && (
            <div className="px-1">
              <MarkReadButton read={isRead || engaged} onMarkRead={() => markItemRead(item.id)} />
            </div>
          )}
        </>
      ) : item.type === 'shortanswer' ? (
        <ShortAnswerContent
          item={item}
          index={index}
          revealed={isRevealed}
          onToggleReveal={toggle}
        />
      ) : null}
      <StudyMarks item={item} />
      <ItemFeedback item={item} />
    </div>
  )
}
