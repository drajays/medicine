import type { HeaderKind, NavEntry, NavRow, RawCatalog } from '@/lib/types'

function readyFile(
  entry: { status?: string; file?: string | null },
): entry is { status: string; file: string } {
  return entry.status === 'ready' && Boolean(entry.file)
}

function pushHeader(
  rows: NavRow[],
  id: string,
  title: string,
  headerKind: HeaderKind,
  opts?: { subtitle?: string; count?: number },
) {
  rows.push({
    type: 'header',
    id,
    title,
    headerKind,
    subtitle: opts?.subtitle,
    count: opts?.count,
  })
}

export function buildNavEntries(catalog: RawCatalog): NavEntry[] {
  return buildNavRows(catalog)
    .filter((row): row is NavRow & { type: 'entry' } => row.type === 'entry')
    .map((row) => row.entry)
}

export function buildNavRows(catalog: RawCatalog): NavRow[] {
  const rows: NavRow[] = []

  const hotTopics = (catalog.hotTopics?.topics ?? []).filter(readyFile)
  if (hotTopics.length) {
    pushHeader(rows, 'hdr-hot-topics', catalog.hotTopics?.title ?? 'Hot Topics', 'hot_topics', {
      subtitle: catalog.hotTopics?.description,
      count: hotTopics.length,
    })
    for (const topic of hotTopics) {
      rows.push({
        type: 'entry',
        entry: {
          id: topic.id,
          title: topic.title,
          subtitle: topic.subtitle ?? topic.category ?? 'Hot Topic',
          sectionTitle: catalog.hotTopics?.title ?? 'Hot Topics',
          file: topic.file as string,
          kind: 'hot_topic',
        },
      })
    }
  }

  const caseReports = (catalog.caseReports?.reports ?? []).filter(readyFile)
  if (caseReports.length) {
    pushHeader(rows, 'hdr-case-reports', catalog.caseReports?.title ?? 'Case Reports', 'case_reports', {
      subtitle: catalog.caseReports?.description,
      count: caseReports.length,
    })
    for (const report of caseReports) {
      rows.push({
        type: 'entry',
        entry: {
          id: report.id,
          title: report.title,
          subtitle: report.subtitle ?? report.category ?? 'Case Report',
          sectionTitle: catalog.caseReports?.title ?? 'Case Reports',
          file: report.file as string,
          kind: 'case_report',
        },
      })
    }
  }

  const pedEndo = (catalog.pediatricEndo?.chapters ?? []).filter(readyFile)
  if (pedEndo.length) {
    pushHeader(
      rows,
      'hdr-pediatric-endo',
      catalog.pediatricEndo?.title ?? 'Pediatric Endocrinology',
      'pediatric_endo',
      {
        subtitle: catalog.pediatricEndo?.description,
        count: pedEndo.length,
      },
    )
    for (const chapter of pedEndo) {
      rows.push({
        type: 'entry',
        entry: {
          id: chapter.id,
          title: chapter.title,
          subtitle: chapter.subtitle ?? `Ch. ${chapter.no ?? '—'}`,
          sectionTitle: catalog.pediatricEndo?.title ?? 'Pediatric Endocrinology',
          file: chapter.file as string,
          kind: 'harrison',
        },
      })
    }
  }

  const stories = (catalog.stories?.entries ?? []).filter(readyFile)
  if (stories.length) {
    pushHeader(rows, 'hdr-stories', catalog.stories?.title ?? 'Stories', 'stories', {
      subtitle: catalog.stories?.description,
      count: stories.length,
    })
    for (const story of stories) {
      rows.push({
        type: 'entry',
        entry: {
          id: story.id,
          title: story.title,
          subtitle: story.subtitle ?? story.category ?? 'Story',
          sectionTitle: catalog.stories?.title ?? 'Stories',
          file: story.file as string,
          kind: 'story',
        },
      })
    }
  }

  const calculators = (catalog.calculators?.entries ?? []).filter(readyFile)
  if (calculators.length) {
    pushHeader(rows, 'hdr-calculators', catalog.calculators?.title ?? 'Calculators', 'calculators', {
      subtitle: catalog.calculators?.description,
      count: calculators.length,
    })
    for (const calc of calculators) {
      rows.push({
        type: 'calculator',
        id: calc.id,
        title: calc.title,
        subtitle: calc.subtitle ?? calc.category ?? 'Calculator',
        href: `calculators/${calc.file}`,
      })
    }
  }

  const imaging = (catalog.imagingResources?.entries ?? []).filter(readyFile)
  if (imaging.length) {
    pushHeader(
      rows,
      'hdr-imaging',
      catalog.imagingResources?.title ?? 'Imaging & Atlases',
      'imaging_resources',
      {
        subtitle: catalog.imagingResources?.description,
        count: imaging.length,
      },
    )
    for (const atlas of imaging) {
      rows.push({
        type: 'imaging',
        id: atlas.id,
        title: atlas.title,
        subtitle: atlas.subtitle ?? atlas.category ?? 'Imaging Atlas',
        href: `imaging/${atlas.file}`,
      })
    }
  }

  const trials = (catalog.trials?.entries ?? []).filter(readyFile)
  if (trials.length) {
    pushHeader(rows, 'hdr-trials', catalog.trials?.title ?? 'Clinical Trials', 'trials', {
      subtitle: catalog.trials?.description,
      count: trials.length,
    })

    const subsections = catalog.trials?.subsections ?? []
    const grouped = new Map<string, typeof trials>()
    for (const trial of trials) {
      const key = trial.subsection ?? 'general'
      if (!grouped.has(key)) grouped.set(key, [])
      grouped.get(key)!.push(trial)
    }

    for (const [key, items] of grouped) {
      const sub = subsections.find((s) => s.id === key)
      pushHeader(rows, `hdr-trial-${key}`, sub?.title ?? key.toUpperCase(), 'trial_sub', {
        subtitle: sub?.description,
        count: items.length,
      })
      for (const trial of items) {
        rows.push({
          type: 'entry',
          entry: {
            id: trial.id,
            title: trial.title,
            subtitle: trial.subtitle ?? trial.category ?? 'Trial',
            sectionTitle: catalog.trials?.title ?? 'Trials',
            file: trial.file as string,
            kind: 'trial',
          },
        })
      }
    }
  }

  const harrisonSections = catalog.sections ?? []
  const harrisonReady = harrisonSections.flatMap((s) =>
    (s.chapters ?? []).filter(readyFile).map((ch) => ({ section: s, chapter: ch })),
  )
  if (harrisonReady.length) {
    pushHeader(rows, 'hdr-harrison', "Harrison's 22e Chapters", 'harrison_banner', {
      subtitle: 'Principles of Internal Medicine, 22nd ed.',
      count: harrisonReady.length,
    })

    for (const section of harrisonSections) {
      const chapters = (section.chapters ?? []).filter(readyFile)
      if (!chapters.length) continue
      pushHeader(rows, `hdr-section-${section.name}`, section.name, 'harrison_section', {
        count: chapters.length,
      })
      for (const chapter of chapters) {
        rows.push({
          type: 'entry',
          entry: {
            id: chapter.id,
            title: chapter.title,
            subtitle: `Ch. ${chapter.no ?? '—'}`,
            sectionTitle: section.name,
            file: chapter.file as string,
            kind: 'harrison',
          },
        })
      }
    }
  }

  return rows
}

export function navRowHeight(row: NavRow): number {
  if (row.type === 'header') {
    if (row.headerKind === 'trial_sub') return 36
    if (row.headerKind === 'harrison_section') return 38
    return 54
  }
  if (row.type === 'calculator') return 58
  if (row.type === 'imaging') return 58
  return 66
}
