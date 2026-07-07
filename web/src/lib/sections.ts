import type { HeaderKind, NavRow } from '@/lib/types'

export interface LandingItem {
  id: string
  title: string
  subtitle: string
  /** Sub-section label (Harrison section name / trial subsection), if any. */
  group?: string
  /** External href — present for calculator and imaging atlas entries. */
  href?: string
}

export interface LandingSection {
  key: string
  kind: HeaderKind
  title: string
  subtitle?: string
  count: number
  items: LandingItem[]
}

/** Header kinds that begin a new top-level section on the landing page. */
const TOP_LEVEL: HeaderKind[] = [
  'hot_topics',
  'case_reports',
  'pediatric_endo',
  'sub_apps',
  'stories',
  'calculators',
  'imaging_resources',
  'trials',
  'harrison_banner',
]

/**
 * Collapse the flat nav rows into the handful of top-level sections shown as
 * tabs on the landing page. Sub-headers (trial subsections, Harrison sections)
 * become `group` labels on the items they precede.
 */
export function buildSections(rows: NavRow[]): LandingSection[] {
  const sections: LandingSection[] = []
  let current: LandingSection | null = null
  let currentGroup: string | undefined

  for (const row of rows) {
    if (row.type === 'header') {
      if (TOP_LEVEL.includes(row.headerKind)) {
        current = {
          key: row.id,
          kind: row.headerKind,
          title: row.title,
          subtitle: row.subtitle,
          count: row.count ?? 0,
          items: [],
        }
        currentGroup = undefined
        sections.push(current)
      } else {
        currentGroup = row.title
      }
      continue
    }
    if (!current) continue
    if (row.type === 'entry') {
      current.items.push({
        id: row.entry.id,
        title: row.entry.title,
        subtitle: row.entry.subtitle,
        group: currentGroup,
      })
    } else if (row.type === 'calculator' || row.type === 'imaging' || row.type === 'sub_app') {
      current.items.push({
        id: row.id,
        title: row.title,
        subtitle: row.subtitle,
        group: currentGroup,
        href: row.href,
      })
    }
  }

  for (const section of sections) {
    if (!section.count) section.count = section.items.length
  }
  return sections.filter((s) => s.items.length)
}
