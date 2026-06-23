import { motion } from 'framer-motion'
import type { CSSProperties } from 'react'
import type { NoteItem } from '@/lib/types'

interface NoteContentProps {
  item: NoteItem
  index?: number
}

export function NoteContent({ item, index }: NoteContentProps) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      style={{ '--block-accent': '#8b5cf6' } as CSSProperties}
      className="clinical-card study-block p-6 md:p-8"
    >
      <div className="mb-2.5 flex flex-wrap items-baseline gap-x-3 gap-y-1">
        <span className="eyebrow text-violet-700 dark:text-violet-300">
          {index != null ? `Note ${index}` : 'Clinical Note'}
        </span>
        {item.subtopic && <span className="text-xs clinical-muted">{item.subtopic}</span>}
      </div>

      <h3 className="text-xl font-semibold leading-snug md:text-[1.6rem]">{item.title}</h3>

      <div className="reading-prose mt-4 whitespace-pre-wrap text-slate-800 dark:text-zinc-200">
        {item.content}
      </div>

      {item.keyPoints && item.keyPoints.length > 0 && (
        <div className="mt-6 rounded-xl border border-violet-200/60 bg-violet-50/40 p-4 md:p-5 dark:border-violet-500/20 dark:bg-violet-500/5">
          <p className="eyebrow text-violet-800 dark:text-violet-300">Key clinical points</p>
          <ul className="mt-3 space-y-2.5 text-[15px] leading-relaxed">
            {item.keyPoints.map((point, i) => (
              <li key={i} className="flex gap-2.5">
                <span aria-hidden className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-violet-500" />
                <span>{point}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {item.reference && (
        <blockquote className="reading-prose mt-5 border-l-2 border-[var(--color-clinical-accent)]/40 pl-3.5 text-sm italic clinical-muted">
          <span className="not-italic font-semibold">Source: </span>
          {item.reference}
        </blockquote>
      )}
    </motion.article>
  )
}
