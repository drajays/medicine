import { motion, AnimatePresence } from 'framer-motion'
import { ChevronDown, Lightbulb } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { cn } from '@/lib/utils'

interface AnswerRevealProps {
  revealed: boolean
  onToggle: () => void
  children: React.ReactNode
  label?: string
  className?: string
}

export function AnswerReveal({
  revealed,
  onToggle,
  children,
  label = 'Reveal Answer',
  className,
}: AnswerRevealProps) {
  return (
    <div className={className}>
      <Button
        variant={revealed ? 'outline' : 'accent'}
        onClick={onToggle}
        className="w-full justify-between sm:w-auto"
        aria-expanded={revealed}
      >
        <span className="flex items-center gap-2">
          <Lightbulb className="h-4 w-4" />
          {revealed ? 'Hide Answer' : label}
        </span>
        <ChevronDown
          className={cn('h-4 w-4 transition-transform duration-100', revealed && 'rotate-180')}
        />
      </Button>

      <AnimatePresence initial={false}>
        {revealed && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.12, ease: 'easeOut' }}
            className="overflow-hidden"
          >
            <div className="clinical-serif mt-4 space-y-3 rounded-xl border border-blue-200/60 bg-blue-50/50 p-5 text-[15px] leading-relaxed dark:border-blue-500/20 dark:bg-blue-500/5">
              {children}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <p className="mt-2 hidden text-xs clinical-muted sm:block">
        Click to reveal answer
      </p>
    </div>
  )
}
