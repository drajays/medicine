import { Check, BookOpen } from 'lucide-react'
import { cn } from '@/lib/utils'

export function MarkReadButton({
  read,
  onMarkRead,
}: {
  read: boolean
  onMarkRead: () => void
}) {
  if (read) {
    return (
      <div className="mt-4 inline-flex items-center gap-1.5 rounded-full bg-emerald-100 px-3 py-1 text-xs font-semibold text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-200">
        <Check className="h-3.5 w-3.5" />
        Marked as read
      </div>
    )
  }

  return (
    <button
      type="button"
      onClick={onMarkRead}
      className={cn(
        'mt-4 inline-flex items-center gap-2 rounded-lg border clinical-border px-3 py-2 text-xs font-semibold',
        'transition-colors hover:bg-slate-50 dark:hover:bg-zinc-800',
      )}
    >
      <BookOpen className="h-3.5 w-3.5" />
      Mark as read
    </button>
  )
}
