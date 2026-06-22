import { motion } from 'framer-motion'
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
      transition={{ duration: 0.1 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <span className="rounded-md bg-violet-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-violet-700 dark:bg-violet-500/15 dark:text-violet-300">
          {index != null ? `Note ${index}` : 'Clinical Note'}
        </span>
        {item.subtopic && <span className="text-xs clinical-muted">{item.subtopic}</span>}
      </div>

      <h3 className="clinical-serif text-lg font-bold leading-snug md:text-xl">{item.title}</h3>

      <div className="clinical-serif mt-4 whitespace-pre-wrap text-[15px] leading-relaxed text-slate-800 dark:text-zinc-200">
        {item.content}
      </div>

      {item.keyPoints && item.keyPoints.length > 0 && (
        <div className="mt-5 rounded-lg border border-violet-200/60 bg-violet-50/40 p-4 dark:border-violet-500/20 dark:bg-violet-500/5">
          <p className="text-xs font-semibold uppercase text-violet-800 dark:text-violet-300">
            Key clinical points
          </p>
          <ul className="mt-2 space-y-2 text-sm">
            {item.keyPoints.map((point, i) => (
              <li key={i} className="flex gap-2">
                <span className="text-violet-500">•</span>
                <span>{point}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {item.reference && (
        <blockquote className="clinical-serif mt-4 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
          <span className="not-italic font-semibold">Source: </span>
          {item.reference}
        </blockquote>
      )}
    </motion.article>
  )
}
