import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { useAppStore } from '@/store/useAppStore'
import { isStudyDataEmpty } from '@/lib/studyData'
import {
  checkSyncHealth,
  isSyncConfigured,
  loginCloudAccount,
  pushCloudAccount,
  registerCloudAccount,
} from '@/lib/syncApi'
import {
  authHash,
  decryptStudyData,
  displayUserId,
  encryptStudyData,
  validatePassword,
  validateUserId,
} from '@/lib/syncCrypto'

interface SyncState {
  userId: string | null
  /** SHA-256 auth token for API calls — not the encryption password. */
  authToken: string | null
  lastSyncedAt: number | null
  cloudUpdatedAt: number | null
  lastError: string | null
  syncing: boolean
  serverOnline: boolean | null

  register: (userId: string, password: string) => Promise<void>
  login: (userId: string, password: string) => Promise<void>
  logout: () => void
  pushNow: () => Promise<void>
  restoreSession: () => Promise<void>
  checkServer: () => Promise<void>
}

async function encryptCurrent(password: string) {
  const data = useAppStore.getState().exportStudyData()
  const blob = await encryptStudyData(password, data)
  return { blob, updatedAt: Date.now() }
}

export const useSyncStore = create<SyncState>()(
  persist(
    (set, get) => ({
      userId: null,
      authToken: null,
      lastSyncedAt: null,
      cloudUpdatedAt: null,
      lastError: null,
      syncing: false,
      serverOnline: null,

      checkServer: async () => {
        if (!isSyncConfigured()) {
          set({ serverOnline: false })
          return
        }
        set({ serverOnline: await checkSyncHealth() })
      },

      register: async (userId, password) => {
        const idErr = validateUserId(userId)
        if (idErr) throw new Error(idErr)
        const pwErr = validatePassword(password)
        if (pwErr) throw new Error(pwErr)
        if (!isSyncConfigured()) throw new Error('Cloud sync is not available on this site yet.')

        set({ syncing: true, lastError: null })
        try {
          const id = displayUserId(userId)
          const auth = await authHash(id, password)
          const { blob, updatedAt } = await encryptCurrent(password)
          const result = await registerCloudAccount(id, auth, blob, updatedAt)
          if (!result.ok) throw new Error(result.error)

          set({
            userId: id,
            authToken: auth,
            lastSyncedAt: updatedAt,
            cloudUpdatedAt: updatedAt,
            syncing: false,
            serverOnline: true,
          })
          cacheSyncPassword(password)
        } catch (e) {
          const msg = e instanceof Error ? e.message : 'Registration failed.'
          set({ syncing: false, lastError: msg })
          throw e
        }
      },

      login: async (userId, password) => {
        const idErr = validateUserId(userId)
        if (idErr) throw new Error(idErr)
        const pwErr = validatePassword(password)
        if (pwErr) throw new Error(pwErr)
        if (!isSyncConfigured()) throw new Error('Cloud sync is not available on this site yet.')

        set({ syncing: true, lastError: null })
        try {
          const id = displayUserId(userId)
          const auth = await authHash(id, password)
          const result = await loginCloudAccount(id, auth)
          if (!result.ok) throw new Error(result.error)

          const local = useAppStore.getState().exportStudyData()
          const localEmpty = isStudyDataEmpty(local)
          const cloudNewer = result.record.updatedAt > (get().lastSyncedAt ?? 0)

          if (localEmpty || cloudNewer) {
            const data = await decryptStudyData(password, result.record)
            useAppStore.getState().importStudyData(data, localEmpty ? 'replace' : 'merge')
          } else if (!isStudyDataEmpty(local)) {
            const { blob, updatedAt } = await encryptCurrent(password)
            const push = await pushCloudAccount(id, auth, blob, updatedAt)
            if (push.ok) {
              set({ lastSyncedAt: push.updatedAt, cloudUpdatedAt: push.updatedAt })
            }
          }

          set({
            userId: id,
            authToken: auth,
            cloudUpdatedAt: result.record.updatedAt,
            lastSyncedAt: get().lastSyncedAt ?? result.record.updatedAt,
            syncing: false,
            serverOnline: true,
          })
          cacheSyncPassword(password)
        } catch (e) {
          const msg = e instanceof Error ? e.message : 'Sign-in failed.'
          set({ syncing: false, lastError: msg })
          throw e
        }
      },

      logout: () => {
        clearSyncPassword()
        set({
          userId: null,
          authToken: null,
          lastError: null,
        })
      },

      pushNow: async () => {
        const { userId, authToken } = get()
        const password = getCachedSyncPassword()
        if (!userId || !authToken) throw new Error('Sign in to sync.')
        if (!password) throw new Error('Sign in again with your password to sync.')
        if (!isSyncConfigured()) throw new Error('Cloud sync is not configured.')

        set({ syncing: true, lastError: null })
        try {
          const { blob, updatedAt } = await encryptCurrent(password)
          const result = await pushCloudAccount(userId, authToken, blob, updatedAt)
          if (!result.ok) throw new Error(result.error)

          set({
            syncing: false,
            lastSyncedAt: result.updatedAt,
            cloudUpdatedAt: result.updatedAt,
            serverOnline: true,
          })
        } catch (e) {
          const msg = e instanceof Error ? e.message : 'Sync failed.'
          set({ syncing: false, lastError: msg })
          throw e
        }
      },

      restoreSession: async () => {
        await get().checkServer()
        const password = getCachedSyncPassword()
        if (!get().userId || !get().authToken || !password) return
        await autoPushIfReady()
      },
    }),
    {
      name: 'h22-sync-account',
      partialize: (s) => ({
        userId: s.userId,
        authToken: s.authToken,
        lastSyncedAt: s.lastSyncedAt,
        cloudUpdatedAt: s.cloudUpdatedAt,
      }),
    },
  ),
)

/** Password kept in sessionStorage for auto-sync (cleared when browser data is wiped). */
const PWD_KEY = 'h22-sync-pwd-session'

export function cacheSyncPassword(password: string) {
  try {
    sessionStorage.setItem(PWD_KEY, password)
  } catch {
    // private mode / quota
  }
}

export function getCachedSyncPassword(): string | null {
  try {
    return sessionStorage.getItem(PWD_KEY)
  } catch {
    return null
  }
}

export function clearSyncPassword() {
  try {
    sessionStorage.removeItem(PWD_KEY)
  } catch {
    // ignore
  }
}

export async function autoPushIfReady() {
  const { userId, authToken, syncing } = useSyncStore.getState()
  const password = getCachedSyncPassword()
  if (!userId || !authToken || syncing || !password) return

  const data = useAppStore.getState().exportStudyData()
  if (isStudyDataEmpty(data)) return

  useSyncStore.setState({ syncing: true })
  try {
    const blob = await encryptStudyData(password, data)
    const updatedAt = Date.now()
    const result = await pushCloudAccount(userId, authToken, blob, updatedAt)
    if (result.ok) {
      useSyncStore.setState({
        syncing: false,
        lastSyncedAt: result.updatedAt,
        cloudUpdatedAt: result.updatedAt,
        lastError: null,
        serverOnline: true,
      })
    } else {
      useSyncStore.setState({ syncing: false, lastError: result.error })
    }
  } catch {
    useSyncStore.setState({ syncing: false })
  }
}
