import { buildStudyExport, type StudyDataPayload } from '@/lib/studyData'

const PBKDF2_ITERATIONS = 120_000
const SALT_BYTES = 16
const IV_BYTES = 12

function bytesToBase64(bytes: Uint8Array): string {
  let s = ''
  for (const b of bytes) s += String.fromCharCode(b)
  return btoa(s)
}

function base64ToBytes(b64: string): Uint8Array {
  const bin = atob(b64)
  const out = new Uint8Array(bin.length)
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i)
  return out
}

function normalizeUserId(raw: string): string {
  return raw.trim().toLowerCase().replace(/[^a-z0-9_]/g, '')
}

export function validateUserId(userId: string): string | null {
  const id = normalizeUserId(userId)
  if (id.length < 3) return 'User ID must be at least 3 characters (letters, numbers, underscore).'
  if (id.length > 32) return 'User ID must be 32 characters or fewer.'
  return null
}

export function validatePassword(password: string): string | null {
  if (password.length < 6) return 'Password must be at least 6 characters.'
  if (password.length > 128) return 'Password is too long.'
  return null
}

/** Server-side auth token — never sent to decrypt; password stays client-only for encryption. */
export async function authHash(userId: string, password: string): Promise<string> {
  const id = normalizeUserId(userId)
  const data = new TextEncoder().encode(`${id}:${password}`)
  const digest = await crypto.subtle.digest('SHA-256', data)
  return bytesToBase64(new Uint8Array(digest))
}

export function displayUserId(userId: string): string {
  return normalizeUserId(userId)
}

function toArrayBuffer(bytes: Uint8Array): ArrayBuffer {
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer
}

async function deriveKey(password: string, salt: Uint8Array): Promise<CryptoKey> {
  const base = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(password),
    'PBKDF2',
    false,
    ['deriveKey'],
  )
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt: toArrayBuffer(salt), iterations: PBKDF2_ITERATIONS, hash: 'SHA-256' },
    base,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt', 'decrypt'],
  )
}

export interface EncryptedStudyBlob {
  encSalt: string
  iv: string
  ciphertext: string
}

export async function encryptStudyData(
  password: string,
  data: StudyDataPayload,
): Promise<EncryptedStudyBlob> {
  const salt = crypto.getRandomValues(new Uint8Array(SALT_BYTES))
  const iv = crypto.getRandomValues(new Uint8Array(IV_BYTES))
  const key = await deriveKey(password, salt)
  const plain = new TextEncoder().encode(JSON.stringify(buildStudyExport(data)))
  const encrypted = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv: toArrayBuffer(iv) },
    key,
    plain,
  )
  return {
    encSalt: bytesToBase64(salt),
    iv: bytesToBase64(iv),
    ciphertext: bytesToBase64(new Uint8Array(encrypted)),
  }
}

export async function decryptStudyData(
  password: string,
  blob: EncryptedStudyBlob,
): Promise<StudyDataPayload> {
  const key = await deriveKey(password, base64ToBytes(blob.encSalt))
  const ivBytes = base64ToBytes(blob.iv)
  const cipherBytes = base64ToBytes(blob.ciphertext)
  const decrypted = await crypto.subtle.decrypt(
    { name: 'AES-GCM', iv: toArrayBuffer(ivBytes) },
    key,
    toArrayBuffer(cipherBytes),
  )
  const json = JSON.parse(new TextDecoder().decode(decrypted)) as {
    data?: StudyDataPayload
  }
  if (!json.data || typeof json.data !== 'object') {
    throw new Error('Cloud backup is corrupted or was created with a different password.')
  }
  return json.data
}
