import { motion } from 'framer-motion'
import type { NoteItem } from '@/lib/types'
import { AnswerReveal } from '@/components/question/AnswerReveal'

interface NoteContentProps {
  item: NoteItem
  revealed: boolean
  onToggleReveal: () => void
}

export function NoteContent({ item, revealed, onToggleReveal }: NoteContentProps) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-4 flex items-center gap-2">
        <span className="rounded-md bg-violet-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-violet-700 dark:bg-violet-500/15 dark:text-violet-300">
          Clinical Note
        </span>
        {item.subtopic && (
          <span className="text-xs clinical-muted">{item.subtopic}</span>
        )}
      </div>

      <h2 className="clinical-serif text-xl font-bold leading-snug md:text-2xl">
        {item.title}
      </h2>

      <div className="clinical-serif mt-5 whitespace-pre-wrap text-[15px] leading-relaxed clinical-muted">
        {item.content}
      </div>

      <AnswerReveal revealed={revealed} onToggle={onToggleReveal} label="Reveal Key Points">
        {item.keyPoints && item.keyPoints.length > 0 ? (
          <ul className="space-y-2">
            {item.keyPoints.map((point, i) => (
              <li key={i} className="flex gap-2">
                <span className="text-blue-500">•</span>
                <span>{point}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p>No key points available.</p>
        )}
        {item.reference && (
          <blockquote className="mt-4 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
            {item.reference}
          </blockquote>
        )}
      </AnswerReveal>
    </motion.article>
  )
}
