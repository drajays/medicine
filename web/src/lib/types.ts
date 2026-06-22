export type ItemType = 'note' | 'mcq' | 'true_false' | 'assertion_reason'

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

export type StudyItem = McqItem | NoteItem | TrueFalseItem

export interface ChapterData {
  id: string
  volume: number
  chapterNo: string
  title: string
  section: string
  items: StudyItem[]
}

export interface ChapterMeta {
  id: string
  title: string
  section: string
  chapterNo: string
  file: string
  status: 'ready' | 'pending'
  itemCount: number
}

export interface CatalogSection {
  id: string
  title: string
  chapters: ChapterMeta[]
}

export interface Catalog {
  title: string
  sections: CatalogSection[]
}

export interface SearchResult {
  id: string
  kind: 'chapter' | 'item'
  label: string
  subtitle: string
  chapterId: string
  itemIndex?: number
}
