export type ItemType =
  | 'note'
  | 'mcq'
  | 'true_false'
  | 'assertion_reason'
  | 'why'
  | 'how'
  | 'shortanswer'

export interface McqItem {
  id: string
  type: 'mcq'
  subtopic?: string
  stem: string
  options: string[]
  correctOption: number
  explanation?: string
  reference?: string
}

export interface NoteItem {
  id: string
  type: 'note'
  subtopic?: string
  title: string
  content: string
  keyPoints?: string[]
  reference?: string
}

export interface TrueFalseItem {
  id: string
  type: 'true_false'
  subtopic?: string
  statement: string
  correctAnswer: boolean
  explanation?: string
  reference?: string
}

export interface AssertionReasonItem {
  id: string
  type: 'assertion_reason'
  subtopic?: string
  assertion: string
  reason: string
  correctOption: number
  explanation?: string
  reference?: string
}

export interface WhyHowItem {
  id: string
  type: 'why' | 'how'
  subtopic?: string
  question: string
  answer: string
  keyPoints?: string[]
  reference?: string
}

export interface ShortAnswerItem {
  id: string
  type: 'shortanswer'
  subtopic?: string
  question: string
  answer: string
  reference?: string
}

export type StudyItem =
  | McqItem
  | NoteItem
  | TrueFalseItem
  | AssertionReasonItem
  | WhyHowItem
  | ShortAnswerItem

export interface ChapterData {
  id: string
  title: string
  subtitle?: string
  section?: string
  chapterNo?: string
  volume?: number
  category?: string
  authors?: string
  topicType?: string
  reportType?: string
  trialType?: string
  subsection?: string
  items: StudyItem[]
  patient?: {
    age?: number | string
    sex?: string
    chiefComplaint?: string
    pmh?: string[]
    medications?: string[]
  }
  caseDescription?: string
  keyFindings?: string[]
  finalDiagnosis?: string
  learningObjectives?: string[]
  inclusionCriteria?: string[]
  exclusionCriteria?: string[]
  keyTakeaways?: string[]
  trialDesign?: Record<string, string>
  trialSummary?: {
    headings?: Record<string, string>
    outcomes?: Array<{ definition?: string }>
  }
  relatedChapters?: Array<{ id: string; title: string }>
}

export interface NavEntry {
  id: string
  title: string
  subtitle: string
  sectionTitle: string
  file: string
  kind: 'harrison' | 'hot_topic' | 'case_report' | 'trial' | 'story'
}

export type HeaderKind =
  | 'hot_topics'
  | 'case_reports'
  | 'pediatric_endo'
  | 'stories'
  | 'calculators'
  | 'trials'
  | 'trial_sub'
  | 'harrison_banner'
  | 'harrison_section'

export type NavRow =
  | {
      type: 'header'
      id: string
      title: string
      subtitle?: string
      count?: number
      headerKind: HeaderKind
    }
  | { type: 'entry'; entry: NavEntry }
  | { type: 'calculator'; id: string; title: string; subtitle: string; href: string }

export interface RawCatalog {
  title: string
  sections?: Array<{
    name: string
    chapters: Array<{
      id: string
      no?: string
      title: string
      file: string | null
      status: string
    }>
  }>
  hotTopics?: {
    title?: string
    description?: string
    topics: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string | null
      status: string
    }>
  }
  caseReports?: {
    title?: string
    description?: string
    reports: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string | null
      status: string
    }>
  }
  pediatricEndo?: {
    title?: string
    description?: string
    chapters: Array<{
      id: string
      no?: string
      title: string
      subtitle?: string
      file: string | null
      status: string
    }>
  }
  stories?: {
    title?: string
    description?: string
    entries: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string | null
      status: string
    }>
  }
  calculators?: {
    title?: string
    description?: string
    entries: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string
      status: string
    }>
  }
  trials?: {
    title?: string
    description?: string
    subsections?: Array<{ id: string; title: string; description?: string }>
    entries: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      subsection?: string
      file: string | null
      status: string
    }>
  }
}

/**
 * Per-item study marks: the 7 minimalist toggles + seen/revise counters.
 * Each axis is tri-state (undefined = unset). Stored per item id in the
 * persisted Zustand store, alongside ratings/flags/bookmarks. The chapter
 * context (mirroring FeedbackCtx) lets the Revise Hub aggregate across
 * chapters without re-fetching their JSON.
 */
export interface ItemMark {
  difficulty?: 'tough' | 'easy'
  priority?: 'important' | 'not'
  action?: 'revise' | 'no_revise'
  status?: 'clear' | 'doubt'
  method?: 'logic' | 'rote'
  confidence?: 'knew' | 'guessed' // questions only
  errorType?: 'silly' | 'concept' // questions only
  timesDone: number
  timesRevised: number
  firstSeenAt?: number
  lastSeenAt?: number
  // context for the Revise Hub
  chapterId?: string
  chapterTitle?: string
  label?: string
  itemType?: string
}

/** A subset of ItemMark axes used to filter items within a chapter. */
export interface StudyFilter {
  difficulty?: ItemMark['difficulty']
  priority?: ItemMark['priority']
  action?: ItemMark['action']
  status?: ItemMark['status']
  method?: ItemMark['method']
  confidence?: ItemMark['confidence']
  errorType?: ItemMark['errorType']
  progress?: 'new' | 'done' | 'revised'
}

export interface SearchResult {
  id: string
  kind: 'chapter' | 'item'
  label: string
  subtitle: string
  chapterId: string
  itemId?: string
}
