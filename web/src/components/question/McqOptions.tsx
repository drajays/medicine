import { motion } from 'framer-motion'
import { Check, X } from 'lucide-react'
import { cn } from '@/lib/utils'

interface McqOptionsProps {
  options: string[]
  selected: number | null
  correctOption: number
  revealed: boolean
  onSelect: (index: number) => void
}

export function McqOptions({
  options,
  selected,
  correctOption,
  revealed,
  onSelect,
}: McqOptionsProps) {
  return (
    <div className="mt-5 space-y-2" role="radiogroup" aria-label="Answer options">
      {options.map((option, index) => {
        const isSelected = selected === index
        const isCorrect = index === correctOption
        const showResult = revealed && (isSelected || isCorrect)

        return (
          <motion.button
            key={index}
            type="button"
            role="radio"
            aria-checked={isSelected}
            onClick={() => onSelect(index)}
            whileTap={{ scale: 0.995 }}
            transition={{ duration: 0.08 }}
            className={cn(
              'flex w-full items-start gap-3 rounded-xl px-4 py-3.5 text-left text-sm clinical-border transition-colors duration-100',
              'hover:border-blue-300 hover:bg-slate-50 dark:hover:border-blue-500/30 dark:hover:bg-zinc-800/40',
              isSelected && !revealed && 'border-blue-400 bg-blue-50/70 dark:border-blue-500/40 dark:bg-blue-500/10',
              showResult && isCorrect && 'border-emerald-500/60 bg-emerald-50 dark:bg-emerald-500/10',
              showResult && isSelected && !isCorrect && 'border-red-400/60 bg-red-50 dark:bg-red-500/10',
            )}
          >
            <span
              className={cn(
                'mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-md text-xs font-semibold',
                'bg-slate-100 text-slate-600 dark:bg-zinc-800 dark:text-zinc-300',
                isSelected && 'bg-blue-600 text-white',
                showResult && isCorrect && 'bg-emerald-600 text-white',
                showResult && isSelected && !isCorrect && 'bg-red-500 text-white',
              )}
            >
              {index + 1}
            </span>
            <span className="flex-1 leading-relaxed">{option}</span>
            {showResult && isCorrect && <Check className="mt-0.5 h-4 w-4 shrink-0 text-emerald-600" />}
            {showResult && isSelected && !isCorrect && <X className="mt-0.5 h-4 w-4 shrink-0 text-red-500" />}
          </motion.button>
        )
      })}
      <p className="pt-1 text-xs clinical-muted">
        Keys <kbd className="rounded border px-1">1</kbd>–<kbd className="rounded border px-1">4</kbd> select options
      </p>
    </div>
  )
}
