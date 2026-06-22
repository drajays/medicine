import { motion } from 'framer-motion'
import type { AssertionReasonItem, ShortAnswerItem, TrueFalseItem, WhyHowItem } from '@/lib/types'
import { AR_OPTIONS } from '@/lib/constants'
import { AnswerReveal } from '@/components/question/AnswerReveal'
import { cn } from '@/lib/utils'

function StudyShell({
  badge,
  subtopic,
  title,
  children,
  revealed,
  onToggleReveal,
  revealContent,
  revealLabel = 'Reveal Answer',
}: {
  badge: string
  subtopic?: string
  title: string
  children: React.ReactNode
  revealed: boolean
  onToggleReveal: () => void
  revealContent: React.ReactNode
  revealLabel?: string
}) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.12 }}
      className="clinical-card p-6 md:p-8"
    >
      <div className="mb-4 flex items-center gap-2">
        <span className="rounded-md bg-slate-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-slate-700 dark:bg-zinc-800 dark:text-zinc-300">
          {badge}
        </span>
        {subtopic && <span className="text-xs clinical-muted">{subtopic}</span>}
      </div>
      <h2 className="clinical-serif text-lg font-medium leading-relaxed md:text-xl">{title}</h2>
      <div className="clinical-serif mt-4 text-[15px] leading-relaxed">{children}</div>
      <AnswerReveal revealed={revealed} onToggle={onToggleReveal} label={revealLabel}>
        {revealContent}
      </AnswerReveal>
    </motion.article>
  )
}

export function TrueFalseContent({
  item,
  revealed,
  onToggleReveal,
}: {
  item: TrueFalseItem
  revealed: boolean
  onToggleReveal: () => void
}) {
  return (
    <StudyShell
      badge="True / False"
      subtopic={item.subtopic}
      title={item.statement}
      revealed={revealed}
      onToggleReveal={onToggleReveal}
      revealContent={
        <>
          <p className="font-semibold">
            Correct answer:{' '}
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
        </>
      }
    >
      <span />
    </StudyShell>
  )
}

export function AssertionReasonContent({
  item,
  revealed,
  onToggleReveal,
}: {
  item: AssertionReasonItem
  revealed: boolean
  onToggleReveal: () => void
}) {
  return (
    <StudyShell
      badge="Assertion–Reason"
      subtopic={item.subtopic}
      title="Evaluate the assertion and reason"
      revealed={revealed}
      onToggleReveal={onToggleReveal}
      revealContent={
        <>
          <p className="font-semibold text-emerald-700 dark:text-emerald-400">
            {AR_OPTIONS[item.correctOption]}
          </p>
          {item.explanation && <p className="mt-2">{item.explanation}</p>}
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </>
      }
    >
      <div className="space-y-4">
        <div className="rounded-lg clinical-border p-4">
          <p className="text-xs font-semibold uppercase clinical-muted">Assertion (A)</p>
          <p className="mt-1">{item.assertion}</p>
        </div>
        <div className="rounded-lg clinical-border p-4">
          <p className="text-xs font-semibold uppercase clinical-muted">Reason (R)</p>
          <p className="mt-1">{item.reason}</p>
        </div>
        {revealed && (
          <ol className="space-y-2 text-sm">
            {AR_OPTIONS.map((opt, i) => (
              <li
                key={i}
                className={cn(
                  'rounded-lg px-3 py-2 clinical-border',
                  i === item.correctOption && 'border-emerald-500/50 bg-emerald-50 dark:bg-emerald-500/10',
                )}
              >
                {opt}
              </li>
            ))}
          </ol>
        )}
      </div>
    </StudyShell>
  )
}

export function WhyHowContent({
  item,
  revealed,
  onToggleReveal,
}: {
  item: WhyHowItem
  revealed: boolean
  onToggleReveal: () => void
}) {
  const badge = item.type === 'why' ? 'Why' : 'How'
  return (
    <StudyShell
      badge={badge}
      subtopic={item.subtopic}
      title={item.question}
      revealed={revealed}
      onToggleReveal={onToggleReveal}
      revealContent={
        <>
          <p>{item.answer}</p>
          {item.keyPoints && item.keyPoints.length > 0 && (
            <ul className="mt-3 space-y-2">
              {item.keyPoints.map((point, i) => (
                <li key={i} className="flex gap-2">
                  <span className="text-blue-500">•</span>
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          )}
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </>
      }
    >
      <span />
    </StudyShell>
  )
}

export function ShortAnswerContent({
  item,
  revealed,
  onToggleReveal,
}: {
  item: ShortAnswerItem
  revealed: boolean
  onToggleReveal: () => void
}) {
  return (
    <StudyShell
      badge="Short Answer"
      subtopic={item.subtopic}
      title={item.question}
      revealed={revealed}
      onToggleReveal={onToggleReveal}
      revealContent={
        <>
          <p>{item.answer}</p>
          {item.reference && (
            <blockquote className="mt-3 border-l-2 border-blue-400/50 pl-3 text-sm italic clinical-muted">
              {item.reference}
            </blockquote>
          )}
        </>
      }
    >
      <span />
    </StudyShell>
  )
}
