import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { X, Eye, Keyboard, Undo2 } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { useRevisionStore } from '@/stores/revisionStore'
import { RPSInspector } from '@/components/RPSInspector'
import { itemMarkLabel } from '@/lib/studyMarks'
import { RECALL_LABELS, type RecallRating, type RevisionStudyItem } from '@/lib/revision-math'
import { REVISION_MODES } from '@/lib/revisionQueue'
import {
  TIME_TO_REVEAL_CAP_MS,
  computeTimeToRevealMs,
  formatTimeToReveal,
} from '@/lib/timeToReveal'
import { cn } from '@/lib/utils'
import type { StudyItem } from '@/lib/types'

const RATING_COLORS: Record<RecallRating, string> = {
  0: 'bg-red-600 hover:bg-red-700',
  1: 'bg-orange-600 hover:bg-orange-700',
  2: 'bg-amber-600 hover:bg-amber-700',
  3: 'bg-lime-600 hover:bg-lime-700',
  4: 'bg-emerald-600 hover:bg-emerald-700',
  5: 'bg-teal-600 hover:bg-teal-700',
}

interface SmartTriageModalProps {
  open: boolean
  onClose: () => void
}

function TriageItemBody({
  item,
  revealed,
}: {
  item: StudyItem
  revealed: boolean
}) {
  if (item.type === 'note') {
    return (
      <div className="space-y-4">
        <h3 className="text-lg font-semibold">{item.title}</h3>
        {revealed ? (
          <div className="clinical-serif space-y-3 text-[15px] leading-relaxed">
            <p>{item.content}</p>
            {item.keyPoints?.length ? (
              <ul className="list-disc space-y-1 pl-5 text-sm">
                {item.keyPoints.map((kp, i) => (
                  <li key={i}>{kp}</li>
                ))}
              </ul>
            ) : null}
          </div>
        ) : (
          <p className="text-sm clinical-muted">Press Space to reveal the note.</p>
        )}
      </div>
    )
  }

  if (item.type === 'mcq') {
    return (
      <div className="space-y-4">
        <p className="clinical-serif text-[15px] leading-relaxed">{item.stem}</p>
        <ol className="space-y-2">
          {item.options.map((opt, i) => (
            <li
              key={i}
              className={cn(
                'rounded-lg border px-3 py-2 text-sm clinical-border',
                revealed && i === item.correctOption && 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/30',
              )}
            >
              <span className="font-semibold tabular-nums">{String.fromCharCode(65 + i)}.</span> {opt}
            </li>
          ))}
        </ol>
        {revealed && (
          <p className="clinical-serif text-sm leading-relaxed clinical-muted">{item.explanation}</p>
        )}
        {!revealed && <p className="text-sm clinical-muted">Press Space to reveal the answer.</p>}
      </div>
    )
  }

  const prompt =
    item.type === 'true_false'
      ? item.statement
      : item.type === 'assertion_reason'
        ? `A: ${item.assertion}\nR: ${item.reason}`
        : item.type === 'why' || item.type === 'how'
          ? item.question
          : item.type === 'shortanswer'
            ? item.question
            : itemMarkLabel(item)

  return (
    <div className="space-y-4">
      <p className="clinical-serif whitespace-pre-wrap text-[15px] leading-relaxed">{prompt}</p>
      {revealed && (
        <div className="clinical-serif rounded-lg bg-slate-50 p-4 text-sm leading-relaxed dark:bg-zinc-900/60">
          {item.type === 'true_false' && (
            <p>
              <strong>{item.correctAnswer ? 'True' : 'False'}</strong> — {item.explanation}
            </p>
          )}
          {item.type === 'assertion_reason' && <p>{item.explanation}</p>}
          {(item.type === 'why' || item.type === 'how') && <p>{item.answer}</p>}
          {item.type === 'shortanswer' && <p>{item.answer}</p>}
        </div>
      )}
      {!revealed && <p className="text-sm clinical-muted">Press Space to reveal the answer.</p>}
    </div>
  )
}

/**
 * One card in the triage session. Owns its own reveal/timer state; the parent
 * remounts it (via a position-based key) when the card changes, so state resets
 * without any synchronising effect. The mount effect only seeds a ref-based
 * "shown at" timestamp — no render-time impurity, no setState-in-effect.
 */
function TriageCard({
  revisionItem,
  contentItem,
  onReveal,
  onRate,
}: {
  revisionItem: RevisionStudyItem
  contentItem: StudyItem
  onReveal: () => void
  onRate: (rating: RecallRating, timeToRevealMs: number) => void
}) {
  const showTimeAfterReveal = useRevisionStore((s) => s.showTimeAfterReveal)
  const getItemBreakdown = useRevisionStore((s) => s.getItemBreakdown)
  const [revealed, setRevealed] = useState(false)
  const [timeToRevealMs, setTimeToRevealMs] = useState<number | null>(null)
  const shownAtRef = useRef(0)

  useEffect(() => {
    shownAtRef.current = Date.now()
  }, [])

  const reveal = useCallback(() => {
    if (revealed) return
    setTimeToRevealMs(computeTimeToRevealMs(shownAtRef.current || Date.now(), Date.now()))
    setRevealed(true)
    onReveal()
  }, [revealed, onReveal])

  const rate = useCallback(
    (rating: RecallRating) => {
      if (!revealed || timeToRevealMs == null) return
      onRate(rating, timeToRevealMs)
    },
    [revealed, timeToRevealMs, onRate],
  )

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === ' ') {
        e.preventDefault()
        reveal()
        return
      }
      if (revealed && /^[0-5]$/.test(e.key)) {
        e.preventDefault()
        rate(Number(e.key) as RecallRating)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [reveal, rate, revealed])

  const breakdown = getItemBreakdown(revisionItem.id)

  return (
    <>
      <div className="clinical-card p-6 md:p-8">
        <div className="mb-4 flex items-center gap-2 text-xs font-semibold uppercase clinical-muted">
          <span>{revisionItem.itemType}</span>
          {revisionItem.tags.map((t) => (
            <span
              key={t}
              className="rounded-full bg-amber-100 px-2 py-0.5 text-[10px] text-amber-800 dark:bg-amber-950/50 dark:text-amber-200"
            >
              {t}
            </span>
          ))}
        </div>
        <TriageItemBody item={contentItem} revealed={revealed} />
        {!revealed && (
          <button
            type="button"
            onClick={reveal}
            className="mt-6 inline-flex items-center gap-2 rounded-lg border clinical-border px-4 py-2 text-sm font-semibold transition-colors hover:bg-slate-50 dark:hover:bg-zinc-800"
          >
            <Eye className="h-4 w-4" />
            Reveal
            <kbd className="rounded border px-1.5 py-0.5 text-[10px] font-normal clinical-muted">
              Space
            </kbd>
          </button>
        )}
        {revealed && showTimeAfterReveal && timeToRevealMs != null && (
          <p className="mt-4 text-xs tabular-nums clinical-muted">
            Time to reveal: {formatTimeToReveal(timeToRevealMs)} (capped at{' '}
            {TIME_TO_REVEAL_CAP_MS / 1000}s)
          </p>
        )}
      </div>

      {breakdown && <RPSInspector breakdown={breakdown} itemId={revisionItem.id} defaultOpen={false} />}

      {revealed && (
        <motion.div
          initial={{ opacity: 0, y: 4 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.12 }}
          className="clinical-card p-4"
        >
          <p className="mb-3 text-xs font-bold uppercase tracking-wider clinical-muted">
            Rate your recall
          </p>
          <div className="grid grid-cols-3 gap-2 sm:grid-cols-6">
            {([0, 1, 2, 3, 4, 5] as RecallRating[]).map((r) => (
              <button
                key={r}
                type="button"
                onClick={() => rate(r)}
                className={cn(
                  'flex flex-col items-center rounded-lg px-2 py-3 text-white transition-transform active:scale-95',
                  RATING_COLORS[r],
                )}
              >
                <span className="text-lg font-bold tabular-nums">{r}</span>
                <span className="mt-0.5 text-[9px] font-semibold uppercase leading-tight">
                  {RECALL_LABELS[r]}
                </span>
              </button>
            ))}
          </div>
          <p className="mt-3 flex items-center gap-1.5 text-[10px] clinical-muted">
            <Keyboard className="h-3 w-3" />
            Keys 0–5 to rate · U to undo · Esc to exit · ratings 0–2 re-queue the card
          </p>
        </motion.div>
      )}
    </>
  )
}

export function SmartTriageModal({ open, onClose }: SmartTriageModalProps) {
  const session = useRevisionStore((s) => s.session)
  const getCurrentSessionItem = useRevisionStore((s) => s.getCurrentSessionItem)
  const recordReview = useRevisionStore((s) => s.recordReview)
  const undoLastReview = useRevisionStore((s) => s.undoLastReview)
  const canUndo = useRevisionStore((s) => s.undoStack.length > 0)
  const endSession = useRevisionStore((s) => s.endSession)
  const showTimeAfterReveal = useRevisionStore((s) => s.showTimeAfterReveal)
  const setShowTimeAfterReveal = useRevisionStore((s) => s.setShowTimeAfterReveal)
  const loadChapter = useAppStore((s) => s.loadChapter)
  const chapters = useAppStore((s) => s.chapters)
  const markRevised = useAppStore((s) => s.markRevised)
  const recordItemReveal = useAppStore((s) => s.recordItemReveal)

  const revisionItem = getCurrentSessionItem()
  const chapterId = revisionItem?.chapterId

  const progress = session
    ? { current: Math.min(session.currentIndex + 1, session.itemIds.length), total: session.itemIds.length }
    : null
  const isComplete = session ? session.currentIndex >= session.itemIds.length : false
  const modeLabel = session
    ? (REVISION_MODES.find((m) => m.preset === session.mode)?.title ?? 'Revision')
    : 'Revision'

  // Ensure the current card's chapter JSON is loaded (store action only — no
  // component setState here, so the content item can be derived during render).
  useEffect(() => {
    if (open && chapterId && !chapters[chapterId]) loadChapter(chapterId)
  }, [open, chapterId, chapters, loadChapter])

  const contentItem = revisionItem
    ? (chapters[revisionItem.chapterId]?.items.find((i) => i.id === revisionItem.id) ?? null)
    : null

  const handleClose = useCallback(() => {
    endSession()
    onClose()
  }, [endSession, onClose])

  const studyCtx = useMemo(
    () =>
      revisionItem
        ? {
            chapterId: revisionItem.chapterId,
            chapterTitle: revisionItem.subject,
            label: revisionItem.title,
            itemType: revisionItem.itemType,
          }
        : undefined,
    [revisionItem],
  )

  const handleReveal = useCallback(() => {
    if (!revisionItem || !contentItem) return
    recordItemReveal(revisionItem.id, {
      ...studyCtx,
      itemType: contentItem.type,
    })
  }, [revisionItem, contentItem, recordItemReveal, studyCtx])

  const handleRate = useCallback(
    (rating: RecallRating, timeToRevealMs: number) => {
      if (!revisionItem) return
      recordReview(revisionItem.id, rating, timeToRevealMs)
      markRevised(revisionItem.id, studyCtx)
    },
    [revisionItem, studyCtx, recordReview, markRevised],
  )

  const handleUndo = useCallback(() => {
    undoLastReview()
  }, [undoLastReview])

  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        handleClose()
        return
      }
      if ((e.key === 'u' || e.key === 'Backspace') && canUndo) {
        e.preventDefault()
        handleUndo()
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [open, canUndo, handleClose, handleUndo])

  if (!open) return null

  return (
    <div className="fixed inset-0 z-50 flex flex-col bg-[var(--color-clinical-bg-light)] dark:bg-[var(--color-clinical-bg-dark)]">
      <header className="flex items-center gap-3 border-b clinical-border px-4 py-3 md:px-6">
        <div className="min-w-0 flex-1">
          <p className="text-xs font-bold uppercase tracking-wider text-amber-700 dark:text-amber-300">
            Revision Mode · {modeLabel}
          </p>
          {revisionItem && (
            <p className="truncate text-sm clinical-muted">
              {revisionItem.subject} · {revisionItem.title}
            </p>
          )}
        </div>
        {progress && (
          <span className="rounded-full bg-slate-100 px-2.5 py-1 text-xs font-semibold tabular-nums dark:bg-zinc-800">
            {isComplete ? 'Done' : `${progress.current} / ${progress.total}`}
          </span>
        )}
        {canUndo && (
          <button
            type="button"
            onClick={handleUndo}
            className="inline-flex items-center gap-1.5 rounded-lg border clinical-border px-2.5 py-1.5 text-xs font-semibold transition-colors hover:bg-slate-100 dark:hover:bg-zinc-800"
            aria-label="Undo last rating"
            title="Undo last rating (U)"
          >
            <Undo2 className="h-3.5 w-3.5" />
            <span className="hidden sm:inline">Undo</span>
          </button>
        )}
        <button
          type="button"
          onClick={handleClose}
          className="rounded-lg p-2 clinical-muted transition-colors hover:bg-slate-100 dark:hover:bg-zinc-800"
          aria-label="Close triage"
        >
          <X className="h-5 w-5" />
        </button>
      </header>

      <div className="flex items-center justify-end gap-2 border-b clinical-border px-4 py-1.5 md:px-6">
        <label className="flex cursor-pointer items-center gap-2 text-[10px] clinical-muted">
          <input
            type="checkbox"
            checked={showTimeAfterReveal}
            onChange={(e) => setShowTimeAfterReveal(e.target.checked)}
            className="rounded border-slate-300"
          />
          Show time after reveal
        </label>
      </div>

      <main className="flex-1 overflow-y-auto px-4 py-6 md:px-8">
        <AnimatePresence mode="wait">
          {isComplete ? (
            <motion.div
              key="complete"
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.16 }}
              className="mx-auto max-w-lg text-center"
            >
              <div className="clinical-card p-10">
                <h2 className="text-xl font-semibold">Session complete</h2>
                <p className="clinical-serif mt-3 text-[15px] clinical-muted">
                  You reviewed {session?.reviewedCount ?? 0} items. Your intervals have been updated.
                </p>
                <button
                  type="button"
                  onClick={handleClose}
                  className="mt-6 rounded-lg bg-amber-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-amber-700"
                >
                  Back to dashboard
                </button>
              </div>
            </motion.div>
          ) : revisionItem && contentItem ? (
            <motion.div
              key={`${session?.currentIndex ?? 0}-${revisionItem.id}`}
              initial={{ opacity: 0, y: 6 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -6 }}
              transition={{ duration: 0.16 }}
              className="mx-auto max-w-2xl space-y-5"
            >
              <TriageCard
                revisionItem={revisionItem}
                contentItem={contentItem}
                onReveal={handleReveal}
                onRate={handleRate}
              />
            </motion.div>
          ) : (
            <motion.p
              key="loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="text-center text-sm clinical-muted"
            >
              Loading item…
            </motion.p>
          )}
        </AnimatePresence>
      </main>
    </div>
  )
}
