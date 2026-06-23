import { motion } from 'framer-motion'
import type { CSSProperties, ReactNode } from 'react'
import type { AssertionReasonItem, ShortAnswerItem, TrueFalseItem, WhyHowItem } from '@/lib/types'
import { AR_OPTIONS } from '@/lib/constants'
import { AnswerReveal } from '@/components/question/AnswerReveal'
import { cn } from '@/lib/utils'

function ItemShell({
  badge,
  subtopic,
  title,
  children,
  footer,
  accent,
  tone,
}: {
  badge: string
  subtopic?: string
  title?: string
  children: ReactNode
  footer?: ReactNode
  accent: string
  tone: string
}) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      style={{ '--block-accent': accent } as CSSProperties}
      className="clinical-card study-block p-6 md:p-8"
    >
      <div className="mb-2.5 flex flex-wrap items-baseline gap-x-3 gap-y-1">
        <span className={cn('eyebrow', tone)}>{badge}</span>
        {subtopic && <span className="text-xs clinical-muted">{subtopic}</span>}
      </div>
      {title && <h3 className="text-lg font-semibold leading-snug md:text-xl">{title}</h3>}
      <div className="mt-3 text-[15px] leading-relaxed">{children}</div>
      {footer}
    </motion.article>
  )
}

function SourceQuote({ children }: { children: ReactNode }) {
  return (
    <blockquote className="reading-prose mt-3 border-l-2 border-[var(--color-clinical-accent)]/40 pl-3.5 text-sm italic clinical-muted">
      {children}
    </blockquote>
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
      accent="#c2872a"
      tone="text-amber-700 dark:text-amber-300"
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
          {item.reference && <SourceQuote>{item.reference}</SourceQuote>}
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
      accent="#6366f1"
      tone="text-indigo-700 dark:text-indigo-300"
      badge={index != null ? `Assertion–Reason ${index}` : 'Assertion–Reason'}
      subtopic={item.subtopic}
      footer={
        <AnswerReveal revealed={revealed} onToggle={onToggleReveal} className="mt-4">
          <p className="font-semibold text-emerald-700 dark:text-emerald-400">
            {AR_OPTIONS[item.correctOption]}
          </p>
          {item.explanation && <p className="mt-2">{item.explanation}</p>}
          {item.reference && <SourceQuote>{item.reference}</SourceQuote>}
        </AnswerReveal>
      }
    >
      <div className="space-y-2.5">
        <div className="rounded-lg clinical-border border p-3.5">
          <p className="eyebrow clinical-muted">Assertion (A)</p>
          <p className="reading-prose mt-1.5 text-[15px]">{item.assertion}</p>
        </div>
        <div className="rounded-lg clinical-border border p-3.5">
          <p className="eyebrow clinical-muted">Reason (R)</p>
          <p className="reading-prose mt-1.5 text-[15px]">{item.reason}</p>
        </div>
      </div>
    </ItemShell>
  )
}

export function WhyHowContent({ item, index }: { item: WhyHowItem; index?: number }) {
  const label = item.type === 'why' ? 'Why' : 'How'
  return (
    <ItemShell
      accent="#0d9488"
      tone="text-teal-700 dark:text-teal-300"
      badge={index != null ? `${label} ${index}` : label}
      subtopic={item.subtopic}
      title={item.question}
      footer={item.reference ? <SourceQuote>{item.reference}</SourceQuote> : undefined}
    >
      <div className="rounded-xl border border-teal-200/60 bg-teal-50/40 p-4 md:p-5 dark:border-teal-500/20 dark:bg-teal-500/5">
        <p className="eyebrow text-teal-800 dark:text-teal-300">Answer</p>
        <p className="reading-prose mt-2 whitespace-pre-wrap">{item.answer}</p>
      </div>
      {item.keyPoints && item.keyPoints.length > 0 && (
        <ul className="mt-4 space-y-2.5 text-[15px] leading-relaxed">
          {item.keyPoints.map((point, i) => (
            <li key={i} className="flex gap-2.5">
              <span aria-hidden className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-teal-500" />
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
      accent="#9a8c72"
      tone="clinical-muted"
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
          <p className="reading-prose whitespace-pre-wrap">{modelAnswer}</p>
          {item.reference && <SourceQuote>{item.reference}</SourceQuote>}
        </AnswerReveal>
      }
    >
      <p className="text-sm clinical-muted">
        Think through your answer, then reveal the model response.
      </p>
    </ItemShell>
  )
}
