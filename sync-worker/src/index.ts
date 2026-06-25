export interface Env {
  STUDY_KV: KVNamespace
}

interface StoredRecord {
  authHash: string
  encSalt: string
  iv: string
  ciphertext: string
  updatedAt: number
}

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
}

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS },
  })
}

function normalizeUserId(raw: string): string | null {
  const id = raw.trim().toLowerCase().replace(/[^a-z0-9_]/g, '')
  if (id.length < 3 || id.length > 32) return null
  return id
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: CORS })
    }

    const url = new URL(request.url)

    if (url.pathname === '/health') {
      return json({ ok: true })
    }

    if (url.pathname === '/api/v1/register' && request.method === 'POST') {
      const body = (await request.json()) as Record<string, unknown>
      const userId = normalizeUserId(String(body.userId ?? ''))
      if (!userId) return json({ error: 'Invalid user ID.' }, 400)
      if (!body.authHash || !body.encSalt || !body.iv || !body.ciphertext) {
        return json({ error: 'Missing backup fields.' }, 400)
      }

      const key = `user:${userId}`
      const existing = await env.STUDY_KV.get(key)
      if (existing) return json({ error: 'User ID already exists.' }, 409)

      const record: StoredRecord = {
        authHash: String(body.authHash),
        encSalt: String(body.encSalt),
        iv: String(body.iv),
        ciphertext: String(body.ciphertext),
        updatedAt: Number(body.updatedAt) || Date.now(),
      }
      await env.STUDY_KV.put(key, JSON.stringify(record))
      return json({ ok: true })
    }

    if (url.pathname === '/api/v1/login' && request.method === 'POST') {
      const body = (await request.json()) as Record<string, unknown>
      const userId = normalizeUserId(String(body.userId ?? ''))
      if (!userId) return json({ error: 'Invalid user ID.' }, 400)

      const raw = await env.STUDY_KV.get(`user:${userId}`)
      if (!raw) return json({ error: 'User not found.' }, 404)

      const record = JSON.parse(raw) as StoredRecord
      if (record.authHash !== String(body.authHash ?? '')) {
        return json({ error: 'Incorrect password.' }, 401)
      }

      return json({
        encSalt: record.encSalt,
        iv: record.iv,
        ciphertext: record.ciphertext,
        updatedAt: record.updatedAt,
      })
    }

    if (url.pathname === '/api/v1/sync' && request.method === 'PUT') {
      const body = (await request.json()) as Record<string, unknown>
      const userId = normalizeUserId(String(body.userId ?? ''))
      if (!userId) return json({ error: 'Invalid user ID.' }, 400)

      const raw = await env.STUDY_KV.get(`user:${userId}`)
      if (!raw) return json({ error: 'User not found.' }, 404)

      const existing = JSON.parse(raw) as StoredRecord
      if (existing.authHash !== String(body.authHash ?? '')) {
        return json({ error: 'Unauthorized.' }, 401)
      }

      const incomingAt = Number(body.updatedAt) || Date.now()
      const record: StoredRecord = {
        authHash: existing.authHash,
        encSalt: String(body.encSalt),
        iv: String(body.iv),
        ciphertext: String(body.ciphertext),
        updatedAt: Math.max(incomingAt, existing.updatedAt),
      }
      await env.STUDY_KV.put(`user:${userId}`, JSON.stringify(record))
      return json({ ok: true, updatedAt: record.updatedAt })
    }

    return json({ error: 'Not found.' }, 404)
  },
}
