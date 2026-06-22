import { motion } from 'framer-motion'
import type { AssertionReasonItem, ShortAnswerItem, TrueFalseItem, WhyHowItem } from '@/lib/types'
import { AR_OPTIONS } from '@/lib/constants'
import { AnswerReveal } from '@/components/question/AnswerReveal'

function ItemShell({
  badge,
  subtopic,
  title,
  children,
  footer,
}: {
  badge: string
  subtopic?: string
  title?: string
  children: React.ReactNode
  footer?: React.ReactNode
}) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.1 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <span className="rounded-md bg-slate-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-slate-700 dark:bg-zinc-800 dark:text-zinc-300">
          {badge}
        </span>
        {subtopic && <span className="text-xs clinical-muted">{subtopic}</span>}
      </div>
      {title && (
        <h3 className="clinical-serif text-base font-medium leading-relaxed md:text-lg">{title}</h3>
      )}
      <div className="clinical-serif mt-3 text-[15px] leading-relaxed">{children}</div>
      {footer}
    </motion.article>
  )
}

export function TrueFalseContent({
  item,
  index,
  revealed,
  onToggleReveal,
}: {
  item: TrueFalseItem
  index?: number
  revealed: boolean
  onToggleReveal: () => void
}) {
  return (
    <ItemShell
      badge={index != null ? `True / False ${index}` : 'True / False'}
      subtopic={item.subtopic}
      title={item.statement}
      footer={
        <AnswerReveal revealed={revealed} onToggle={onToggleReveal} className="mt-4">
          <p className="font-semibold">
            Correct:{' '}
            <span className={item.correctAnswer ? 'text-emerald-600' : 'text-red-500'}>
              {item.correctAnswer ? 'True' : 'False'}
            </span>
          </p>
          {item.explanation && <p className="mt-2">{item.explanation}</p>}
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </AnswerReveal>
      }
    >
      <span />
    </ItemShell>
  )
}

export function AssertionReasonContent({
  item,
  index,
  revealed,
  onToggleReveal,
}: {
  item: AssertionReasonItem
  index?: number
  revealed: boolean
  onToggleReveal: () => void
}) {
  return (
    <ItemShell
      badge={index != null ? `Assertion–Reason ${index}` : 'Assertion–Reason'}
      subtopic={item.subtopic}
      footer={
        <AnswerReveal revealed={revealed} onToggle={onToggleReveal} className="mt-4">
          <p className="font-semibold text-emerald-700 dark:text-emerald-400">
            {AR_OPTIONS[item.correctOption]}
          </p>
          {item.explanation && <p className="mt-2">{item.explanation}</p>}
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </AnswerReveal>
      }
    >
      <div className="space-y-3">
        <div className="rounded-lg clinical-border p-3 text-sm">
          <p className="text-xs font-semibold uppercase clinical-muted">Assertion (A)</p>
          <p className="mt-1">{item.assertion}</p>
        </div>
        <div className="rounded-lg clinical-border p-3 text-sm">
          <p className="text-xs font-semibold uppercase clinical-muted">Reason (R)</p>
          <p className="mt-1">{item.reason}</p>
        </div>
      </div>
    </ItemShell>
  )
}

export function WhyHowContent({ item, index }: { item: WhyHowItem; index?: number }) {
  const label = item.type === 'why' ? 'Why' : 'How'
  return (
    <ItemShell
      badge={index != null ? `${label} ${index}` : label}
      subtopic={item.subtopic}
      title={item.question}
      footer={
        item.reference ? (
          <blockquote className="clinical-serif mt-4 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
            {item.reference}
          </blockquote>
        ) : undefined
      }
    >
      <div className="rounded-lg border border-blue-200/50 bg-blue-50/40 p-4 dark:border-blue-500/20 dark:bg-blue-500/5">
        <p className="text-xs font-semibold uppercase text-blue-800 dark:text-blue-300">Answer</p>
        <p className="mt-2 whitespace-pre-wrap">{item.answer}</p>
      </div>
      {item.keyPoints && item.keyPoints.length > 0 && (
        <ul className="mt-4 space-y-2 text-sm">
          {item.keyPoints.map((point, i) => (
            <li key={i} className="flex gap-2">
              <span className="text-blue-500">•</span>
              <span>{point}</span>
            </li>
          ))}
        </ul>
      )}
    </ItemShell>
  )
}

export function ShortAnswerContent({
  item,
  index,
  revealed,
  onToggleReveal,
}: {
  item: ShortAnswerItem
  index?: number
  revealed: boolean
  onToggleReveal: () => void
}) {
  const modelAnswer =
    item.answer || (item as ShortAnswerItem & { modelAnswer?: string }).modelAnswer || ''

  return (
    <ItemShell
      badge={index != null ? `Short Answer ${index}` : 'Short Answer'}
      subtopic={item.subtopic}
      title={item.question}
      footer={
        <AnswerReveal
          revealed={revealed}
          onToggle={onToggleReveal}
          label="Reveal model answer"
          className="mt-4"
        >
          <p className="whitespace-pre-wrap">{modelAnswer}</p>
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </AnswerReveal>
      }
    >
      <p className="text-sm clinical-muted">Think through your answer, then reveal the model response.</p>
    </ItemShell>
  )
}
