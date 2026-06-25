export const AR_OPTIONS = [
  'Both A and R are true, and R is the correct explanation of A',
  'Both A and R are true, but R is NOT the correct explanation of A',
  'A is true, but R is false',
  'A is false, but R is true',
  'Both A and R are false',
] as const

export const DATA_BASE = `${import.meta.env.BASE_URL}data/`

/** Cloud sync API (Cloudflare Worker). Set at build time via VITE_SYNC_API_URL. */
export const SYNC_API_URL = (
  (import.meta.env.VITE_SYNC_API_URL as string | undefined) ?? ''
).replace(/\/$/, '')

/** GitHub repo (owner/name) where content flags are filed as issues. */
export const FLAG_REPO = 'drajays/medicine'
