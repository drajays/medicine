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

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

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
        const showCorrect = revealed && isCorrect
        const showWrong = revealed && isSelected && !isCorrect

        return (
          <motion.button
            key={index}
            type="button"
            role="radio"
            aria-checked={isSelected}
            disabled={revealed}
            onClick={() => onSelect(index)}
            whileTap={revealed ? undefined : { scale: 0.99 }}
            transition={{ duration: 0.08 }}
            className={cn(
              'flex w-full items-start gap-3 rounded-xl border px-4 py-3.5 text-left text-[15px] leading-relaxed transition-colors duration-150',
              'clinical-border',
              !revealed &&
                'hover:border-[var(--color-clinical-accent)]/50 hover:bg-slate-50 dark:hover:bg-zinc-800/40',
              isSelected && !revealed && 'border-blue-400 bg-blue-50/70 dark:border-blue-500/40 dark:bg-blue-500/10',
              showCorrect && 'border-emerald-500/70 bg-emerald-50 dark:bg-emerald-500/10',
              showWrong && 'border-red-400/70 bg-red-50 dark:bg-red-500/10',
              revealed && !showCorrect && !showWrong && 'opacity-60',
            )}
          >
            <motion.span
              animate={
                showCorrect ? { scale: [1, 1.18, 1] } : showWrong ? { x: [0, -3, 3, -2, 0] } : {}
              }
              transition={{ duration: 0.3 }}
              className={cn(
                'mt-px flex h-7 w-7 shrink-0 items-center justify-center rounded-lg text-xs font-bold',
                'bg-slate-100 text-slate-600 dark:bg-zinc-800 dark:text-zinc-300',
                isSelected && !revealed && 'bg-blue-600 text-white',
                showCorrect && 'bg-emerald-600 text-white',
                showWrong && 'bg-red-500 text-white',
              )}
            >
              {showCorrect ? (
                <Check className="h-4 w-4" />
              ) : showWrong ? (
                <X className="h-4 w-4" />
              ) : (
                LETTERS[index] ?? index + 1
              )}
            </motion.span>
            <span className="flex-1 pt-0.5">{option}</span>
          </motion.button>
        )
      })}
      {!revealed && (
        <p className="pt-1 text-xs clinical-muted">Select the single best answer.</p>
      )}
    </div>
  )
}
