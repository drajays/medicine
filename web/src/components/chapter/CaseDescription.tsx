import type { ChapterData } from '@/lib/types'

export function CaseDescription({ chapter }: { chapter: ChapterData }) {
  const p = chapter.patient
  if (!chapter.caseDescription && !p) return null

  return (
    <section className="clinical-card mt-4 p-5 md:p-6">
      <div className="mb-3 text-xs font-bold uppercase tracking-wide text-teal-700 dark:text-teal-300">
        Case Description
      </div>
      {p && (p.age || p.sex || p.chiefComplaint) && (
        <div className="mb-4 grid gap-2 text-sm sm:grid-cols-2">
          {p.age != null && (
            <div>
              <span className="text-xs font-semibold uppercase clinical-muted">Age</span>
              <p>{p.age}</p>
            </div>
          )}
          {p.sex && (
            <div>
              <span className="text-xs font-semibold uppercase clinical-muted">Sex</span>
              <p>{p.sex}</p>
            </div>
          )}
          {p.chiefComplaint && (
            <div className="sm:col-span-2">
              <span className="text-xs font-semibold uppercase clinical-muted">Chief complaint</span>
              <p>{p.chiefComplaint}</p>
            </div>
          )}
          {p.pmh?.length ? (
            <div className="sm:col-span-2">
              <span className="text-xs font-semibold uppercase clinical-muted">PMH</span>
              <p>{p.pmh.join('; ')}</p>
            </div>
          ) : null}
          {p.medications?.length ? (
            <div className="sm:col-span-2">
              <span className="text-xs font-semibold uppercase clinical-muted">Medications</span>
              <p>{p.medications.join('; ')}</p>
            </div>
          ) : null}
        </div>
      )}
      {chapter.caseDescription && (
        <div className="clinical-serif whitespace-pre-wrap text-[15px] leading-relaxed">
          {chapter.caseDescription}
        </div>
      )}
      {chapter.keyFindings?.length ? (
        <div className="mt-4">
          <p className="text-xs font-semibold uppercase clinical-muted">Key findings</p>
          <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
            {chapter.keyFindings.map((f, i) => (
              <li key={i}>{f}</li>
            ))}
          </ul>
        </div>
      ) : null}
      {chapter.finalDiagnosis && (
        <div className="mt-4 rounded-lg border border-teal-200/60 bg-teal-50/50 p-3 dark:border-teal-500/20 dark:bg-teal-950/20">
          <p className="text-xs font-semibold uppercase clinical-muted">Final diagnosis</p>
          <p className="mt-1 text-sm font-medium">{chapter.finalDiagnosis}</p>
        </div>
      )}
      {chapter.learningObjectives?.length ? (
        <div className="mt-4">
          <p className="text-xs font-semibold uppercase clinical-muted">Learning objectives</p>
          <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
            {chapter.learningObjectives.map((o, i) => (
              <li key={i}>{o}</li>
            ))}
          </ul>
        </div>
      ) : null}
    </section>
  )
}
