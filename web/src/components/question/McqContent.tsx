import { motion } from 'framer-motion'
import type { CSSProperties } from 'react'
import type { McqItem } from '@/lib/types'
import { McqOptions } from '@/components/question/McqOptions'
import { AnswerReveal } from '@/components/question/AnswerReveal'

interface McqContentProps {
  item: McqItem
  index?: number
  revealed: boolean
  selected: number | null
  onToggleReveal: () => void
  onSelect: (index: number) => void
}

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

export function McqContent({
  item,
  index,
  revealed,
  selected,
  onToggleReveal,
  onSelect,
}: McqContentProps) {
  const stem = item.stem || (item as McqItem & { question?: string }).question || ''
  const correctLetter = LETTERS[item.correctOption] ?? String(item.correctOption + 1)
  const graded = revealed && selected != null
  const isRight = graded && selected === item.correctOption

  return (
    <motion.article
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      style={{ '--block-accent': '#3b82f6' } as CSSProperties}
      className="clinical-card study-block p-6 md:p-8"
    >
      <div className="mb-2.5 flex flex-wrap items-baseline gap-x-3 gap-y-1">
        <span className="eyebrow text-blue-700 dark:text-blue-300">
          {index != null ? `MCQ ${index}` : 'MCQ'}
        </span>
        {item.subtopic && <span className="text-xs clinical-muted">{item.subtopic}</span>}
      </div>

      <p className="reading-prose text-[1.0625rem] font-medium md:text-[1.15rem]">{stem}</p>

      <McqOptions
        options={item.options}
        selected={selected}
        correctOption={item.correctOption}
        revealed={revealed}
        onSelect={onSelect}
      />

      {graded && (
        <motion.p
          initial={{ opacity: 0, y: 2 }}
          animate={{ opacity: 1, y: 0 }}
          className={cnResult(isRight)}
        >
          {isRight ? 'Correct.' : `Not quite — the answer is ${correctLetter}.`}
        </motion.p>
      )}

      <AnswerReveal revealed={revealed} onToggle={onToggleReveal} className="mt-4">
        {item.explanation && <p>{item.explanation}</p>}
        {item.reference && (
          <blockquote className="mt-3 border-l-2 border-[var(--color-clinical-accent)]/40 pl-3.5 text-sm italic clinical-muted">
            {item.reference}
          </blockquote>
        )}
      </AnswerReveal>
    </motion.article>
  )
}

function cnResult(isRight: boolean) {
  return [
    'mt-3.5 text-sm font-semibold',
    isRight ? 'text-emerald-700 dark:text-emerald-400' : 'text-red-600 dark:text-red-400',
  ].join(' ')
}
