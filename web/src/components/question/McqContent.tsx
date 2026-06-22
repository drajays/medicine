import { motion } from 'framer-motion'
import type { McqItem } from '@/lib/types'
import { McqOptions } from '@/components/question/McqOptions'
import { AnswerReveal } from '@/components/question/AnswerReveal'

interface McqContentProps {
  item: McqItem
  revealed: boolean
  selected: number | null
  onToggleReveal: () => void
  onSelect: (index: number) => void
}

export function McqContent({
  item,
  revealed,
  selected,
  onToggleReveal,
  onSelect,
}: McqContentProps) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-4 flex items-center gap-2">
        <span className="rounded-md bg-blue-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-blue-700 dark:bg-blue-500/15 dark:text-blue-300">
          MCQ
        </span>
        {item.subtopic && (
          <span className="text-xs clinical-muted">{item.subtopic}</span>
        )}
      </div>

      <p className="clinical-serif text-lg font-medium leading-relaxed md:text-xl">
        {item.stem}
      </p>

      <McqOptions
        options={item.options}
        selected={selected}
        correctOption={item.correctOption}
        revealed={revealed}
        onSelect={onSelect}
      />

      <AnswerReveal revealed={revealed} onToggle={onToggleReveal}>
        {item.explanation && <p>{item.explanation}</p>}
        {item.reference && (
          <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
            {item.reference}
          </blockquote>
        )}
      </AnswerReveal>
    </motion.article>
  )
}
