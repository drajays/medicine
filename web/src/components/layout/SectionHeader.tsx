import { cn } from '@/lib/utils'
import type { HeaderKind, NavEntry } from '@/lib/types'

const HEADER_THEME: Record<
  HeaderKind,
  { wrap: string; title: string; meta: string; icon: string }
> = {
  hot_topics: {
    icon: '🔥',
    wrap: 'bg-gradient-to-r from-amber-100/90 to-orange-50 border-l-[3px] border-l-amber-500 dark:from-amber-950/50 dark:to-orange-950/25 dark:border-l-amber-400',
    title: 'text-amber-950 dark:text-amber-50',
    meta: 'text-amber-800/80 dark:text-amber-200/70',
  },
  case_reports: {
    icon: '📋',
    wrap: 'bg-gradient-to-r from-teal-100/90 to-emerald-50 border-l-[3px] border-l-teal-600 dark:from-teal-950/50 dark:to-emerald-950/25 dark:border-l-teal-400',
    title: 'text-teal-950 dark:text-teal-50',
    meta: 'text-teal-800/80 dark:text-teal-200/70',
  },
  pediatric_endo: {
    icon: '🧒',
    wrap: 'bg-gradient-to-r from-green-100/90 to-emerald-50 border-l-[3px] border-l-green-600 dark:from-green-950/50 dark:to-emerald-950/25 dark:border-l-green-400',
    title: 'text-green-950 dark:text-green-50',
    meta: 'text-green-800/80 dark:text-green-200/70',
  },
  stories: {
    icon: '💬',
    wrap: 'bg-gradient-to-r from-rose-100/90 to-pink-50 border-l-[3px] border-l-rose-500 dark:from-rose-950/50 dark:to-pink-950/25 dark:border-l-rose-400',
    title: 'text-rose-950 dark:text-rose-50',
    meta: 'text-rose-800/80 dark:text-rose-200/70',
  },
  calculators: {
    icon: '🧮',
    wrap: 'bg-gradient-to-r from-violet-100/90 to-purple-50 border-l-[3px] border-l-violet-600 dark:from-violet-950/50 dark:to-purple-950/25 dark:border-l-violet-400',
    title: 'text-violet-950 dark:text-violet-50',
    meta: 'text-violet-800/80 dark:text-violet-200/70',
  },
  imaging_resources: {
    icon: '🩻',
    wrap: 'bg-gradient-to-r from-cyan-100/90 to-sky-50 border-l-[3px] border-l-cyan-600 dark:from-cyan-950/50 dark:to-sky-950/25 dark:border-l-cyan-400',
    title: 'text-cyan-950 dark:text-cyan-50',
    meta: 'text-cyan-800/80 dark:text-cyan-200/70',
  },
  trials: {
    icon: '📊',
    wrap: 'bg-gradient-to-r from-blue-100/90 to-sky-50 border-l-[3px] border-l-blue-600 dark:from-blue-950/50 dark:to-sky-950/25 dark:border-l-blue-400',
    title: 'text-blue-950 dark:text-blue-50',
    meta: 'text-blue-800/80 dark:text-blue-200/70',
  },
  trial_sub: {
    icon: '›',
    wrap: 'bg-blue-50/70 border-l-[3px] border-l-blue-400/70 dark:bg-blue-950/20 dark:border-l-blue-500/50',
    title: 'text-blue-900 dark:text-blue-100',
    meta: 'text-blue-700/75 dark:text-blue-300/70',
  },
  harrison_banner: {
    icon: '📖',
    wrap: 'bg-gradient-to-r from-slate-200/90 to-zinc-100 border-l-[3px] border-l-slate-700 dark:from-slate-800/80 dark:to-zinc-900/60 dark:border-l-slate-400',
    title: 'text-slate-900 dark:text-slate-50',
    meta: 'text-slate-700/85 dark:text-slate-300/75',
  },
  harrison_section: {
    icon: '§',
    wrap: 'bg-gradient-to-r from-indigo-100/80 to-indigo-50/60 border-l-[3px] border-l-indigo-600 dark:from-indigo-950/45 dark:to-indigo-950/20 dark:border-l-indigo-400',
    title: 'text-indigo-950 dark:text-indigo-50',
    meta: 'text-indigo-800/75 dark:text-indigo-200/65',
  },
}

interface SectionHeaderProps {
  kind: HeaderKind
  title: string
  subtitle?: string
  count?: number
}

export function SectionHeader({ kind, title, subtitle, count }: SectionHeaderProps) {
  const theme = HEADER_THEME[kind]
  const isSub = kind === 'trial_sub' || kind === 'harrison_section'

  return (
    <div
      className={cn(
        'mx-1 flex items-start gap-2 rounded-lg px-3',
        theme.wrap,
        isSub ? 'ml-2 py-1.5' : 'py-2.5',
      )}
    >
      <span
        className={cn('shrink-0 leading-none', isSub ? 'text-sm opacity-70' : 'text-base')}
        aria-hidden
      >
        {theme.icon}
      </span>
      <div className="min-w-0 flex-1">
        <div className="flex items-baseline justify-between gap-2">
          <p
            className={cn(
              'font-semibold leading-snug',
              theme.title,
              isSub ? 'text-[11px] uppercase tracking-wide' : 'text-[13px]',
            )}
          >
            {title}
          </p>
          {count != null && (
            <span className={cn('shrink-0 text-[10px] font-semibold tabular-nums', theme.meta)}>
              {count}
            </span>
          )}
        </div>
        {subtitle && !isSub && (
          <p className={cn('mt-0.5 line-clamp-2 text-[10px] leading-snug', theme.meta)}>
            {subtitle}
          </p>
        )}
      </div>
    </div>
  )
}

export function entryKindAccent(kind: NavEntry['kind'] | 'calculator' | 'imaging') {
  switch (kind) {
    case 'hot_topic':
      return 'border-l-2 border-l-amber-400/60'
    case 'case_report':
      return 'border-l-2 border-l-teal-500/60'
    case 'trial':
      return 'border-l-2 border-l-blue-500/60'
    case 'story':
      return 'border-l-2 border-l-rose-500/60'
    case 'harrison':
      return 'border-l-2 border-l-indigo-500/50'
    case 'calculator':
      return 'border-l-2 border-l-violet-500/60'
    case 'imaging':
      return 'border-l-2 border-l-cyan-500/60'
    default:
      return ''
  }
}
