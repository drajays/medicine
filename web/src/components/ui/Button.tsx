import { forwardRef, type ButtonHTMLAttributes } from 'react'
import { cn } from '@/lib/utils'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'ghost' | 'outline' | 'accent'
  size?: 'sm' | 'md' | 'icon'
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'default', size = 'md', ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={cn(
          'inline-flex items-center justify-center gap-2 rounded-lg font-medium transition-colors duration-100',
          'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500/50',
          'disabled:pointer-events-none disabled:opacity-40',
          size === 'sm' && 'h-8 px-3 text-xs',
          size === 'md' && 'h-9 px-3.5 text-sm',
          size === 'icon' && 'h-9 w-9',
          variant === 'default' &&
            'bg-slate-900 text-white hover:bg-slate-800 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-white',
          variant === 'ghost' &&
            'hover:bg-slate-100 dark:hover:bg-zinc-800/80 text-slate-700 dark:text-zinc-300',
          variant === 'outline' &&
            'clinical-border bg-transparent hover:bg-slate-50 dark:hover:bg-zinc-800/50',
          variant === 'accent' &&
            'bg-blue-600 text-white hover:bg-blue-500',
          className,
        )}
        {...props}
      />
    )
  },
)
Button.displayName = 'Button'
