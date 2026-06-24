import { useMemo, useState } from 'react'
import { Copy, Star, Trash2, X } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface Row {
  id: string
  rating: number
  flag: string | null
  chapterId: string
  chapterTitle: string
  label: string
  type: string
}

function buildText(rows: Row[]): string {
  const flagged = rows.filter((r) => r.flag !== null)
  const rated = rows.filter((r) => r.rating > 0)
  const lines: string[] = ['# Study portal feedback', '']
  if (flagged.length) {
    lines.push(`## Flagged (${flagged.length})`)
    for (const r of flagged) {
      lines.push(
        `- [${r.chapterId}] ${r.id} (${r.type})${r.rating ? ` — ${r.rating}/5` : ''}: ${r.label}` +
          (r.flag ? `\n    → ${r.flag}` : ''),
      )
    }
    lines.push('')
  }
  if (rated.length) {
    lines.push(`## Rated (${rated.length})`)
    for (const r of [...rated].sort((a, b) => b.rating - a.rating)) {
      lines.push(`- ${r.rating}/5  [${r.chapterId}] ${r.id} (${r.type}): ${r.label}`)
    }
  }
  return lines.join('\n')
}

export function FeedbackPanel({ open, onClose }: { open: boolean; onClose: () => void }) {
  const ratings = useAppStore((s) => s.ratings)
  const flags = useAppStore((s) => s.flags)
  const ctx = useAppStore((s) => s.feedbackCtx)
  const clearFeedback = useAppStore((s) => s.clearFeedback)
  const [copied, setCopied] = useState(false)

  const rows = useMemo<Row[]>(() => {
    const ids = new Set([...Object.keys(ratings), ...Object.keys(flags)])
    return [...ids]
      .map((id) => {
        const c = ctx[id]
        return {
          id,
          rating: ratings[id] ?? 0,
          flag: id in flags ? flags[id] : null,
          chapterId: c?.chapterId ?? '?',
          chapterTitle: c?.chapterTitle ?? '',
          label: c?.label ?? '',
          type: c?.type ?? '',
        }
      })
      .sort((a, b) => Number(b.flag !== null) - Number(a.flag !== null) || b.rating - a.rating)
  }, [ratings, flags, ctx])

  if (!open) return null

  const text = buildText(rows)
  const copy = async () => {
    try {
      await navigator.clipboard.writeText(text)
      setCopied(true)
      setTimeout(() => setCopied(false), 1500)
    } catch {
      /* clipboard blocked — the textarea below is selectable as a fallback */
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <button
        type="button"
        aria-label="Close"
        onClick={onClose}
        className="absolute inset-0 bg-black/40 backdrop-blur-sm"
      />
      <div className="relative z-10 flex max-h-[85vh] w-full max-w-2xl flex-col overflow-hidden rounded-xl border clinical-border bg-[var(--color-clinical-card-light)] shadow-xl dark:bg-[var(--color-clinical-card-dark)]">
        <div className="flex items-center justify-between border-b clinical-border px-4 py-3">
          <h2 className="text-sm font-semibold">
            My feedback{' '}
            <span className="clinical-muted">
              ({rows.filter((r) => r.flag !== null).length} flagged, {rows.filter((r) => r.rating > 0).length} rated)
            </span>
          </h2>
          <button type="button" onClick={onClose} aria-label="Close" className="clinical-muted">
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="min-h-0 flex-1 overflow-y-auto px-4 py-3">
          {rows.length === 0 ? (
            <p className="py-8 text-center text-sm clinical-muted">
              No feedback yet. Rate items with the stars or flag a problem, and it will collect here.
            </p>
          ) : (
            <ul className="space-y-2">
              {rows.map((r) => (
                <li
                  key={r.id}
                  className={cn(
                    'rounded-lg border p-3 text-sm clinical-border',
                    r.flag !== null && 'border-red-300/70 bg-red-50/50 dark:border-red-500/30 dark:bg-red-500/10',
                  )}
                >
                  <div className="flex items-center gap-2">
                    {r.flag !== null && (
                      <span className="rounded bg-red-100 px-1.5 py-0.5 text-[10px] font-bold uppercase text-red-700 dark:bg-red-500/20 dark:text-red-300">
                        Flag
                      </span>
                    )}
                    {r.rating > 0 && (
                      <span className="flex items-center gap-0.5 text-amber-500">
                        {r.rating}
                        <Star className="h-3 w-3 fill-current" />
                      </span>
                    )}
                    <span className="font-mono text-xs clinical-muted">{r.id}</span>
                  </div>
                  {r.label && <p className="mt-1 line-clamp-2">{r.label}</p>}
                  {r.flag ? <p className="mt-1 text-xs text-red-600 dark:text-red-300">→ {r.flag}</p> : null}
                  <p className="mt-1 text-[11px] clinical-muted">
                    {r.chapterTitle || r.chapterId}
                  </p>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="flex items-center justify-between gap-2 border-t clinical-border px-4 py-3">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => {
              if (window.confirm('Clear all your ratings and flags?')) clearFeedback()
            }}
            disabled={rows.length === 0}
            className="text-red-600 dark:text-red-400"
          >
            <Trash2 className="h-3.5 w-3.5" />
            Clear all
          </Button>
          <Button variant="accent" size="sm" onClick={copy} disabled={rows.length === 0}>
            <Copy className="h-3.5 w-3.5" />
            {copied ? 'Copied!' : 'Copy as text'}
          </Button>
        </div>
      </div>
    </div>
  )
}
