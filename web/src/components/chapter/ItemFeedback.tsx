import { useState } from 'react'
import { Flag, Star, ThumbsUp } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { FLAG_REPO } from '@/lib/constants'
import { cn } from '@/lib/utils'
import type { StudyItem } from '@/lib/types'

/**
 * Per-item feedback recorded in git without any token: a 1-5 star rating (stored
 * locally for the reader) plus one "send to repo" button that opens a pre-filled
 * GitHub issue. The label follows the rating — 4-5 stars files a `content-quality`
 * endorsement, anything else files a `content-flag` problem report — so the
 * author can review flagged vs high-quality items by simply filtering issues.
 */
export function ItemFeedback({ item }: { item: StudyItem }) {
  const rating = useAppStore((s) => s.ratings[item.id] ?? 0)
  const rateItem = useAppStore((s) => s.rateItem)
  const chapterId = useAppStore((s) => s.currentChapterId)
  const chapterTitle = useAppStore((s) => s.getCurrentChapter()?.title ?? '')
  const [hover, setHover] = useState(0)

  const isEndorse = rating >= 4

  const submit = () => {
    const label = isEndorse ? 'content-quality' : 'content-flag'
    const title = `${isEndorse ? 'High-quality' : 'Flag'}: ${item.id}`
    const prompt = isEndorse
      ? '**Why is this high-quality?** (optional):'
      : '**What is wrong / what should change?** (fact, pitfall, missing detail, source):'
    const body = [
      `**Item:** \`${item.id}\` (${item.type})`,
      `**Chapter:** \`${chapterId ?? '?'}\` — ${chapterTitle}`,
      rating ? `**Reviewer rating:** ${rating}/5` : '',
      '',
      prompt,
      '',
      '',
      ...(isEndorse ? [] : ['**Suggested correction / high-quality source:**', '', '']),
      '---',
      '_Submitted from the study portal._',
    ]
      .filter((l) => l !== '')
      .join('\n')
    const url = `https://github.com/${FLAG_REPO}/issues/new?labels=${label}&title=${encodeURIComponent(
      title,
    )}&body=${encodeURIComponent(body)}`
    window.open(url, '_blank', 'noopener,noreferrer')
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
            onClick={() => rateItem(item.id, rating === n ? 0 : n)}
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
        onClick={submit}
        title={
          isEndorse
            ? 'Mark high-quality (opens a GitHub issue, no login content needed beyond GitHub)'
            : 'Flag a problem (opens a GitHub issue)'
        }
        className={cn(
          'inline-flex items-center gap-1 rounded-md border px-2 py-1 font-medium clinical-border',
          isEndorse
            ? 'hover:border-emerald-300 hover:text-emerald-600 dark:hover:border-emerald-500/40 dark:hover:text-emerald-400'
            : 'hover:border-red-300 hover:text-red-600 dark:hover:border-red-500/40 dark:hover:text-red-400',
        )}
      >
        {isEndorse ? (
          <>
            <ThumbsUp className="h-3 w-3" /> Endorse
          </>
        ) : (
          <>
            <Flag className="h-3 w-3" /> Flag
          </>
        )}
      </button>
    </div>
  )
}
