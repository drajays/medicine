import { useState } from 'react'
import { Flag, Star } from 'lucide-react'
import { useAppStore, type FeedbackCtx } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import type { StudyItem } from '@/lib/types'

export function itemLabel(item: StudyItem): string {
  const raw =
    (item as { title?: string }).title ??
    (item as { stem?: string }).stem ??
    (item as { statement?: string }).statement ??
    (item as { assertion?: string }).assertion ??
    (item as { question?: string }).question ??
    ''
  return raw.length > 90 ? raw.slice(0, 90) + '…' : raw
}

/**
 * Per-item local feedback: a 1-5 star quality rating and a flag (with optional
 * comment). Everything is stored locally and surfaced via the Feedback panel's
 * "copy as text" export — no network/token needed for personal use.
 */
export function ItemFeedback({ item }: { item: StudyItem }) {
  const rating = useAppStore((s) => s.ratings[item.id] ?? 0)
  const flagged = useAppStore((s) => item.id in s.flags)
  const flagComment = useAppStore((s) => s.flags[item.id] ?? '')
  const rateItem = useAppStore((s) => s.rateItem)
  const flagItem = useAppStore((s) => s.flagItem)
  const chapterId = useAppStore((s) => s.currentChapterId)
  const chapterTitle = useAppStore((s) => s.getCurrentChapter()?.title ?? '')
  const [hover, setHover] = useState(0)

  const ctx = (): FeedbackCtx => ({
    chapterId: chapterId ?? '?',
    chapterTitle,
    label: itemLabel(item),
    type: item.type,
  })

  const onFlag = () => {
    if (flagged) {
      flagItem(item.id, null)
      return
    }
    const comment = window.prompt('What is wrong with this item? (optional)', flagComment) ?? ''
    flagItem(item.id, comment, ctx())
  }

  return (
    <div className="mt-2 flex items-center justify-end gap-3 px-1 text-xs clinical-muted">
      <div className="flex items-center gap-0.5" role="radiogroup" aria-label="Rate this item 1 to 5">
        {[1, 2, 3, 4, 5].map((n) => (
          <button
            key={n}
            type="button"
            aria-label={`${n} star${n > 1 ? 's' : ''}`}
            aria-pressed={rating === n}
            onMouseEnter={() => setHover(n)}
            onMouseLeave={() => setHover(0)}
            onFocus={() => setHover(n)}
            onBlur={() => setHover(0)}
            onClick={() => rateItem(item.id, rating === n ? 0 : n, ctx())}
            className="p-0.5 transition-transform hover:scale-110"
          >
            <Star
              className={cn(
                'h-3.5 w-3.5',
                (hover || rating) >= n
                  ? 'fill-amber-400 text-amber-400'
                  : 'text-slate-300 dark:text-zinc-600',
              )}
            />
          </button>
        ))}
      </div>
      <button
        type="button"
        onClick={onFlag}
        title={flagged ? 'Flagged — click to unflag' : 'Flag a problem (saved locally)'}
        className={cn(
          'inline-flex items-center gap-1 rounded-md border px-2 py-1 font-medium clinical-border',
          flagged
            ? 'border-red-300 bg-red-50 text-red-600 dark:border-red-500/40 dark:bg-red-500/10 dark:text-red-300'
            : 'hover:border-red-300 hover:text-red-600 dark:hover:border-red-500/40 dark:hover:text-red-400',
        )}
      >
        <Flag className={cn('h-3 w-3', flagged && 'fill-current')} />
        {flagged ? 'Flagged' : 'Flag'}
      </button>
    </div>
  )
}
