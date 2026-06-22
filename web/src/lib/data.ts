import { DATA_BASE } from '@/lib/constants'

export async function fetchJSON<T>(path: string): Promise<T> {
  const url = path.startsWith('http') ? path : `${DATA_BASE}${path}`
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Failed to load ${url}`)
  return res.json() as Promise<T>
}
