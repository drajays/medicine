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
  section?: string
  chapterNo?: string
  volume?: number
  items: StudyItem[]
}

export interface NavEntry {
  id: string
  title: string
  subtitle: string
  sectionTitle: string
  file: string
  kind: 'harrison' | 'hot_topic' | 'case_report' | 'trial'
}

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
    reports: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string | null
      status: string
    }>
  }
  trials?: {
    title?: string
    entries: Array<{
      id: string
      title: string
      subtitle?: string
      category?: string
      file: string | null
      status: string
    }>
  }
}

export interface SearchResult {
  id: string
  kind: 'chapter' | 'item'
  label: string
  subtitle: string
  chapterId: string
  itemIndex?: number
}
