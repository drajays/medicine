import { useEffect, useState } from 'react'
import { Cloud, CloudOff, Loader2, LogIn, LogOut, RefreshCw, UserPlus } from 'lucide-react'
import { isSyncConfigured } from '@/lib/syncApi'
import { isStudyDataEmpty } from '@/lib/studyData'
import { useAppStore } from '@/store/useAppStore'
import { useSyncStore } from '@/stores/syncStore'
import { cn } from '@/lib/utils'

function formatWhen(ts: number | null): string {
  if (!ts) return 'Never'
  return new Date(ts).toLocaleString()
}

export function StudyAccountPanel() {
  const exportStudyData = useAppStore((s) => s.exportStudyData)
  const userId = useSyncStore((s) => s.userId)
  const lastSyncedAt = useSyncStore((s) => s.lastSyncedAt)
  const lastError = useSyncStore((s) => s.lastError)
  const syncing = useSyncStore((s) => s.syncing)
  const serverOnline = useSyncStore((s) => s.serverOnline)
  const register = useSyncStore((s) => s.register)
  const login = useSyncStore((s) => s.login)
  const logout = useSyncStore((s) => s.logout)
  const pushNow = useSyncStore((s) => s.pushNow)
  const checkServer = useSyncStore((s) => s.checkServer)

  const [mode, setMode] = useState<'login' | 'register'>('login')
  const [formUser, setFormUser] = useState('')
  const [formPass, setFormPass] = useState('')
  const [formPass2, setFormPass2] = useState('')
  const [busy, setBusy] = useState(false)
  const [formError, setFormError] = useState<string | null>(null)

  const configured = isSyncConfigured()

  useEffect(() => {
    checkServer()
  }, [checkServer])

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setFormError(null)
    if (mode === 'register' && formPass !== formPass2) {
      setFormError('Passwords do not match.')
      return
    }
    setBusy(true)
    try {
      if (mode === 'register') await register(formUser, formPass)
      else await login(formUser, formPass)
      setFormPass('')
      setFormPass2('')
    } catch (err) {
      setFormError(err instanceof Error ? err.message : 'Request failed.')
    } finally {
      setBusy(false)
    }
  }

  const onSync = async () => {
    setFormError(null)
    setBusy(true)
    try {
      await pushNow()
    } catch (err) {
      setFormError(err instanceof Error ? err.message : 'Sync failed.')
    } finally {
      setBusy(false)
    }
  }

  const hasLocalData = !isStudyDataEmpty(exportStudyData())

  return (
    <section className="clinical-card border-l-4 border-l-sky-500 p-5 md:p-6">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="flex items-center gap-2 text-sky-700 dark:text-sky-300">
            <Cloud className="h-4 w-4" />
            <p className="text-xs font-bold uppercase tracking-wider">Study account</p>
          </div>
          <p className="mt-1 max-w-xl text-xs leading-relaxed clinical-muted">
            One-time User ID + password. Progress, revision stats, mock-test activity, and marks are
            encrypted and backed up to the cloud — restore after reinstall by signing in.
          </p>
        </div>
        {configured && (
          <span
            className={cn(
              'rounded-full px-2.5 py-1 text-[10px] font-semibold uppercase',
              serverOnline
                ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-200'
                : 'bg-amber-100 text-amber-800 dark:bg-amber-950/50 dark:text-amber-200',
            )}
          >
            {serverOnline === null ? 'Checking…' : serverOnline ? 'Cloud online' : 'Cloud offline'}
          </span>
        )}
      </div>

      {!configured && (
        <p className="mt-4 rounded-lg bg-amber-50 px-3 py-2 text-xs text-amber-900 dark:bg-amber-950/40 dark:text-amber-100">
          Cloud sync is not enabled on this deployment yet. Use JSON export in the feedback panel as
          a manual backup until the sync server is configured.
        </p>
      )}

      {configured && userId ? (
        <div className="mt-4 space-y-3">
          <div className="flex flex-wrap items-center gap-2 text-sm">
            <span className="font-semibold">Signed in as</span>
            <code className="rounded bg-slate-100 px-2 py-0.5 text-xs dark:bg-zinc-800">{userId}</code>
          </div>
          <p className="text-xs clinical-muted">Last synced: {formatWhen(lastSyncedAt)}</p>
          {(lastError || formError) && (
            <p className="text-xs text-red-600 dark:text-red-400">{formError ?? lastError}</p>
          )}
          <div className="flex flex-wrap gap-2">
            <button
              type="button"
              onClick={onSync}
              disabled={busy || syncing}
              className="inline-flex items-center gap-1.5 rounded-lg bg-sky-600 px-3 py-2 text-xs font-semibold text-white hover:bg-sky-700 disabled:opacity-50"
            >
              {syncing || busy ? (
                <Loader2 className="h-3.5 w-3.5 animate-spin" />
              ) : (
                <RefreshCw className="h-3.5 w-3.5" />
              )}
              Sync now
            </button>
            <button
              type="button"
              onClick={() => {
                logout()
                setFormUser(userId)
              }}
              className="inline-flex items-center gap-1.5 rounded-lg border clinical-border px-3 py-2 text-xs font-semibold hover:bg-slate-50 dark:hover:bg-zinc-800"
            >
              <LogOut className="h-3.5 w-3.5" />
              Sign out
            </button>
          </div>
        </div>
      ) : configured ? (
        <form onSubmit={onSubmit} className="mt-4 space-y-3">
          <div className="flex gap-2">
            <button
              type="button"
              onClick={() => setMode('login')}
              className={cn(
                'rounded-lg px-3 py-1.5 text-xs font-semibold',
                mode === 'login'
                  ? 'bg-sky-600 text-white'
                  : 'border clinical-border clinical-muted',
              )}
            >
              <LogIn className="mr-1 inline h-3.5 w-3.5" />
              Sign in
            </button>
            <button
              type="button"
              onClick={() => setMode('register')}
              className={cn(
                'rounded-lg px-3 py-1.5 text-xs font-semibold',
                mode === 'register'
                  ? 'bg-sky-600 text-white'
                  : 'border clinical-border clinical-muted',
              )}
            >
              <UserPlus className="mr-1 inline h-3.5 w-3.5" />
              Register
            </button>
          </div>

          {mode === 'register' && hasLocalData && (
            <p className="text-xs text-sky-800 dark:text-sky-200">
              Your current progress on this device will be uploaded as the first cloud backup.
            </p>
          )}

          <div className="grid gap-3 sm:grid-cols-2">
            <label className="block text-xs">
              <span className="font-medium">User ID</span>
              <input
                value={formUser}
                onChange={(e) => setFormUser(e.target.value)}
                className="mt-1 w-full rounded-lg border clinical-border bg-transparent px-3 py-2 text-sm"
                placeholder="e.g. resident_ajay"
                autoComplete="username"
                required
              />
            </label>
            <label className="block text-xs">
              <span className="font-medium">Password</span>
              <input
                type="password"
                value={formPass}
                onChange={(e) => setFormPass(e.target.value)}
                className="mt-1 w-full rounded-lg border clinical-border bg-transparent px-3 py-2 text-sm"
                autoComplete={mode === 'register' ? 'new-password' : 'current-password'}
                required
              />
            </label>
          </div>

          {mode === 'register' && (
            <label className="block text-xs sm:max-w-[calc(50%-0.375rem)]">
              <span className="font-medium">Confirm password</span>
              <input
                type="password"
                value={formPass2}
                onChange={(e) => setFormPass2(e.target.value)}
                className="mt-1 w-full rounded-lg border clinical-border bg-transparent px-3 py-2 text-sm"
                autoComplete="new-password"
                required
              />
            </label>
          )}

          {(formError || lastError) && (
            <p className="flex items-center gap-1.5 text-xs text-red-600 dark:text-red-400">
              <CloudOff className="h-3.5 w-3.5" />
              {formError ?? lastError}
            </p>
          )}

          <button
            type="submit"
            disabled={busy || syncing}
            className="rounded-lg bg-sky-600 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-700 disabled:opacity-50"
          >
            {busy ? 'Please wait…' : mode === 'register' ? 'Create account & back up' : 'Sign in & restore'}
          </button>
        </form>
      ) : null}
    </section>
  )
}
