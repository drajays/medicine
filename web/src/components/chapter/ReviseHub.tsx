import { useMemo, useState, type ReactNode } from 'react'
import { ChevronRight, RotateCw } from 'lucide-react'
import { useAppStore } from '@/store/useAppStore'
import { cn } from '@/lib/utils'
import { progressOf, reviseListFromMarks, type ReviseEntry } from '@/lib/studyMarks'

type HubFilter = 'all' | 'revise' | 'doubt' | 'tough'

const FILTERS: Array<{ id: HubFilter; label: string }> = [
  { id: 'all', label: 'All' },
  { id: 'revise', label: 'To revise' },
  { id: 'doubt', label: 'Doubt' },
  { id: 'tough', label: 'Tough' },
]

function matches(entry: ReviseEntry, f: HubFilter): boolean {
  const m = entry.mark
  if (f === 'all') return true
  if (f === 'revise') return m.action === 'revise'
  if (f === 'doubt') return m.status === 'doubt'
  if (f === 'tough') return m.difficulty === 'tough'
  return true
}

/**
 * A computed cross-chapter view of everything the learner flagged for revision
 * (Action=Revise or Status=Doubt), grouped by chapter. Uses the context stored
 * on each mark, so it needs no chapter fetches. Not a catalog HeaderKind — it is
 * rendered directly by the landing page's "Revise" pill.
 */
export function ReviseHub() {
  const marks = useAppStore((s) => s.marks)
  const selectItem = useAppStore((s) => s.selectItem)
  const [filter, setFilter] = useState<HubFilter>('all')

  const groups = useMemo(() => {
    const list = reviseListFromMarks(marks).filter((e) => matches(e, filter))
    const byChapter = new Map<string, { title: string; entries: ReviseEntry[] }>()
    for (const e of list) {
      const key = e.mark.chapterId ?? 'unknown'
      const title = e.mark.chapterTitle ?? 'Other'
      if (!byChapter.has(key)) byChapter.set(key, { title, entries: [] })
      byChapter.get(key)!.entries.push(e)
    }
    return [...byChapter.entries()].map(([id, g]) => ({ id, ...g }))
  }, [marks, filter])

  const total = groups.reduce((n, g) => n + g.entries.length, 0)

  if (!reviseListFromMarks(marks).length) {
    return (
      <div className="clinical-card p-8 text-center">
        <h2 className="text-lg font-semibold">Nothing to revise yet</h2>
        <p className="clinical-serif mt-2 text-[15px] leading-relaxed clinical-muted">
          Open any chapter and mark items <strong>Revise</strong> or <strong>Doubt</strong> using
          the “Marks” bar under each item. They’ll collect here for quick revision across the whole
          portal.
        </p>
      </div>
    )
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-center gap-2">
        {FILTERS.map((f) => (
          <button
            key={f.id}
            type="button"
            onClick={() => setFilter(f.id)}
            className={cn(
              'rounded-full border px-3 py-1 text-xs font-semibold transition-colors',
              filter === f.id
                ? 'border-amber-500 bg-amber-500 text-white'
                : 'clinical-border clinical-muted hover:text-slate-900 dark:hover:text-zinc-100',
            )}
          >
            {f.label}
          </button>
        ))}
        <span className="ml-auto text-xs clinical-muted tabular-nums">{total} items</span>
      </div>

      {groups.map((g) => (
        <div key={g.id}>
          <p className="mb-2 px-1 text-[11px] font-bold uppercase tracking-wider clinical-muted">
            {g.title} · {g.entries.length}
          </p>
          <div className="space-y-2">
            {g.entries.map((e) => {
              const m = e.mark
              return (
                <button
                  key={e.itemId}
                  type="button"
                  onClick={() => selectItem(g.id, e.itemId)}
                  className="clinical-card group flex w-full items-center gap-3 border-l-[3px] border-l-amber-500 p-3 text-left transition-all duration-150 hover:-translate-y-0.5 hover:shadow-md"
                >
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{m.label || e.itemId}</p>
                    <div className="mt-1 flex flex-wrap items-center gap-1.5 text-[10px] font-semibold">
                      {m.action === 'revise' && <Tag color="amber">Revise</Tag>}
                      {m.status === 'doubt' && <Tag color="red">Doubt</Tag>}
                      {m.difficulty === 'tough' && <Tag color="violet">Tough</Tag>}
                      {m.confidence === 'guessed' && <Tag color="slate">Guessed</Tag>}
                      {m.errorType === 'concept' && <Tag color="slate">Concept gap</Tag>}
                      <span className="clinical-muted">·</span>
                      <span className="clinical-muted uppercase">{progressOf(m)}</span>
                      {m.timesRevised > 0 && (
                        <span className="inline-flex items-center gap-0.5 clinical-muted">
                          <RotateCw className="h-2.5 w-2.5" />×{m.timesRevised}
                        </span>
                      )}
                    </div>
                  </div>
                  <ChevronRight className="h-4 w-4 shrink-0 clinical-muted transition-transform group-hover:translate-x-0.5" />
                </button>
              )
            })}
          </div>
        </div>
      ))}
    </div>
  )
}

const TAG_STYLE: Record<string, string> = {
  amber: 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-200',
  red: 'bg-red-100 text-red-700 dark:bg-red-950/50 dark:text-red-300',
  violet: 'bg-violet-100 text-violet-800 dark:bg-violet-950/50 dark:text-violet-200',
  slate: 'bg-slate-100 text-slate-600 dark:bg-zinc-800 dark:text-zinc-300',
}

function Tag({ color, children }: { color: string; children: ReactNode }) {
  return (
    <span className={cn('rounded-full px-1.5 py-0.5 uppercase tracking-wide', TAG_STYLE[color])}>
      {children}
    </span>
  )
}
