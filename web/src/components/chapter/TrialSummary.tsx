import type { ChapterData } from '@/lib/types'

export function TrialSummary({ chapter }: { chapter: ChapterData }) {
  const d = chapter.trialDesign ?? {}
  const h = chapter.trialSummary?.headings ?? {}
  const hasMeta =
    d.year || d.design || d.sampleSize || h.design || h.population || h.intervention

  if (!hasMeta) return null

  const cell = (label: string, value?: string) =>
    value ? (
      <div className="min-w-0">
        <p className="text-[10px] font-semibold uppercase clinical-muted">{label}</p>
        <p className="mt-0.5 text-sm leading-snug">{value}</p>
      </div>
    ) : null

  return (
    <section className="clinical-card mt-4 p-5 md:p-6">
      <div className="mb-3 text-xs font-bold uppercase tracking-wide text-blue-700 dark:text-blue-300">
        Trial Summary
      </div>
      <div className="grid gap-3 sm:grid-cols-2">
        {cell('Year', d.year)}
        {cell('Design', h.design || d.design)}
        {cell('Sample size', d.sampleSize)}
        {cell('Follow-up', h.followUp || d.duration)}
        {cell('Intervention', h.intervention || d.intervention)}
        {cell('Comparator', h.comparator || d.comparator)}
        {cell(
          'Primary endpoint',
          d.primaryEndpoint || chapter.trialSummary?.outcomes?.[0]?.definition,
        )}
        {cell('NCT', h.nct)}
        {cell('Funding', h.funding)}
      </div>
    </section>
  )
}
