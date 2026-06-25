import { SYNC_API_URL } from '@/lib/constants'
import type { EncryptedStudyBlob } from '@/lib/syncCrypto'

export interface CloudRecord extends EncryptedStudyBlob {
  updatedAt: number
}

function apiUrl(path: string): string {
  if (!SYNC_API_URL) throw new Error('Cloud sync is not configured on this deployment.')
  return `${SYNC_API_URL}${path}`
}

async function request<T>(
  path: string,
  init: RequestInit,
): Promise<{ ok: true; data: T } | { ok: false; status: number; error: string }> {
  try {
    const res = await fetch(apiUrl(path), {
      ...init,
      headers: { 'Content-Type': 'application/json', ...(init.headers ?? {}) },
    })
    const body = (await res.json().catch(() => ({}))) as { error?: string }
    if (!res.ok) {
      return { ok: false, status: res.status, error: body.error ?? res.statusText }
    }
    return { ok: true, data: body as T }
  } catch {
    return { ok: false, status: 0, error: 'Could not reach the sync server. Check your connection.' }
  }
}

export function isSyncConfigured(): boolean {
  return Boolean(SYNC_API_URL)
}

export async function checkSyncHealth(): Promise<boolean> {
  if (!SYNC_API_URL) return false
  try {
    const res = await fetch(apiUrl('/health'))
    return res.ok
  } catch {
    return false
  }
}

export async function registerCloudAccount(
  userId: string,
  auth: string,
  blob: EncryptedStudyBlob,
  updatedAt: number,
): Promise<{ ok: true } | { ok: false; error: string }> {
  const result = await request<{ ok: true }>('/api/v1/register', {
    method: 'POST',
    body: JSON.stringify({ userId, authHash: auth, ...blob, updatedAt }),
  })
  if (!result.ok) {
    if (result.status === 409) return { ok: false, error: 'This User ID is already taken.' }
    return { ok: false, error: result.error }
  }
  return { ok: true }
}

export async function loginCloudAccount(
  userId: string,
  auth: string,
): Promise<{ ok: true; record: CloudRecord } | { ok: false; error: string }> {
  const result = await request<CloudRecord>('/api/v1/login', {
    method: 'POST',
    body: JSON.stringify({ userId, authHash: auth }),
  })
  if (!result.ok) {
    if (result.status === 404) return { ok: false, error: 'User ID not found. Register first.' }
    if (result.status === 401) return { ok: false, error: 'Incorrect password.' }
    return { ok: false, error: result.error }
  }
  return { ok: true, record: result.data }
}

export async function pushCloudAccount(
  userId: string,
  auth: string,
  blob: EncryptedStudyBlob,
  updatedAt: number,
): Promise<{ ok: true; updatedAt: number } | { ok: false; error: string }> {
  const result = await request<{ ok: true; updatedAt: number }>('/api/v1/sync', {
    method: 'PUT',
    body: JSON.stringify({ userId, authHash: auth, ...blob, updatedAt }),
  })
  if (!result.ok) {
    if (result.status === 401) return { ok: false, error: 'Session expired — sign in again.' }
    return { ok: false, error: result.error }
  }
  return { ok: true, updatedAt: result.data.updatedAt }
}
