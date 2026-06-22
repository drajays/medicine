import { motion } from 'framer-motion'
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

export function McqContent({
  item,
  index,
  revealed,
  selected,
  onToggleReveal,
  onSelect,
}: McqContentProps) {
  const stem = item.stem || (item as McqItem & { question?: string }).question || ''

  return (
    <motion.article
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.1 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <span className="rounded-md bg-blue-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-blue-700 dark:bg-blue-500/15 dark:text-blue-300">
          {index != null ? `MCQ ${index}` : 'MCQ'}
        </span>
        {item.subtopic && <span className="text-xs clinical-muted">{item.subtopic}</span>}
      </div>

      <p className="clinical-serif text-base font-medium leading-relaxed md:text-lg">{stem}</p>

      <McqOptions
        options={item.options}
        selected={selected}
        correctOption={item.correctOption}
        revealed={revealed}
        onSelect={onSelect}
      />

      <AnswerReveal revealed={revealed} onToggle={onToggleReveal} className="mt-4">
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
