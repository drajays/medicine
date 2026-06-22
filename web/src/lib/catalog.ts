import type { NavEntry, RawCatalog } from '@/lib/types'

function readyFile(
  entry: { status?: string; file?: string | null },
): entry is { status: string; file: string } {
  return entry.status === 'ready' && Boolean(entry.file)
}

export function buildNavEntries(catalog: RawCatalog): NavEntry[] {
  const entries: NavEntry[] = []

  for (const topic of catalog.hotTopics?.topics ?? []) {
    if (!readyFile(topic)) continue
    entries.push({
      id: topic.id,
      title: topic.title,
      subtitle: topic.subtitle ?? topic.category ?? 'Hot Topic',
      sectionTitle: catalog.hotTopics?.title ?? 'Hot Topics',
      file: topic.file,
      kind: 'hot_topic',
    })
  }

  for (const report of catalog.caseReports?.reports ?? []) {
    if (!readyFile(report)) continue
    entries.push({
      id: report.id,
      title: report.title,
      subtitle: report.subtitle ?? report.category ?? 'Case Report',
      sectionTitle: catalog.caseReports?.title ?? 'Case Reports',
      file: report.file,
      kind: 'case_report',
    })
  }

  for (const trial of catalog.trials?.entries ?? []) {
    if (!readyFile(trial)) continue
    entries.push({
      id: trial.id,
      title: trial.title,
      subtitle: trial.subtitle ?? trial.category ?? 'Clinical Trial',
      sectionTitle: catalog.trials?.title ?? 'Trials',
      file: trial.file,
      kind: 'trial',
    })
  }

  for (const section of catalog.sections ?? []) {
    for (const chapter of section.chapters ?? []) {
      if (!readyFile(chapter)) continue
      entries.push({
        id: chapter.id,
        title: chapter.title,
        subtitle: `Ch. ${chapter.no ?? '—'} · ${section.name}`,
        sectionTitle: section.name,
        file: chapter.file,
        kind: 'harrison',
      })
    }
  }

  return entries
}
