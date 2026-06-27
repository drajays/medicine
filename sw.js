/* Harrison's 22e — offline service worker (hand-rolled, no build deps).
 * Caches the app shell, all data/ JSON, and Google Fonts so the Q-bank works
 * offline. Bump VERSION to invalidate old caches on the next deploy. */
const VERSION = 'v1'
const SHELL_CACHE = `harrison-shell-${VERSION}`
const DATA_CACHE = `harrison-data-${VERSION}`
const FONT_CACHE = `harrison-fonts-${VERSION}`

// sw.js sits at the scope root (e.g. /medicine/sw.js) → BASE = /medicine/
const BASE = new URL('./', self.location).pathname

self.addEventListener('install', (event) => {
  self.skipWaiting()
  // Pre-cache the navigation shell (index.html at the base path).
  event.waitUntil(
    caches
      .open(SHELL_CACHE)
      .then((cache) => cache.add(new Request(BASE, { cache: 'reload' })))
      .catch(() => {}),
  )
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys()
      await Promise.all(
        keys
          .filter((k) => !k.endsWith(VERSION))
          .map((k) => caches.delete(k)),
      )
      await self.clients.claim()
    })(),
  )
})

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName)
  const cached = await cache.match(request)
  if (cached) return cached
  const res = await fetch(request)
  if (res && res.ok) cache.put(request, res.clone())
  return res
}

// Serve cached copy immediately; refresh the cache in the background.
async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName)
  const cached = await cache.match(request)
  const network = fetch(request)
    .then((res) => {
      if (res && res.ok) cache.put(request, res.clone())
      return res
    })
    .catch(() => null)
  return cached || (await network) || new Response('Offline', { status: 503 })
}

async function networkFirstNav(request) {
  const cache = await caches.open(SHELL_CACHE)
  try {
    const res = await fetch(request)
    if (res && res.ok) cache.put(BASE, res.clone())
    return res
  } catch {
    return (await cache.match(BASE)) || (await cache.match(request)) || Response.error()
  }
}

self.addEventListener('fetch', (event) => {
  const request = event.request
  if (request.method !== 'GET') return
  const url = new URL(request.url)

  // Google Fonts (cross-origin) — stale-while-revalidate so type renders offline.
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    event.respondWith(staleWhileRevalidate(request, FONT_CACHE))
    return
  }

  if (url.origin !== self.location.origin) return

  // Content JSON: serve cached instantly, update in the background.
  if (url.pathname.startsWith(BASE + 'data/')) {
    event.respondWith(staleWhileRevalidate(request, DATA_CACHE))
    return
  }

  // Hashed Vite bundles are immutable → cache-first.
  if (url.pathname.startsWith(BASE + 'assets/')) {
    event.respondWith(cacheFirst(request, SHELL_CACHE))
    return
  }

  // SPA navigations: network-first, fall back to the cached shell.
  if (request.mode === 'navigate') {
    event.respondWith(networkFirstNav(request))
    return
  }

  // Everything else same-origin (favicon, icons, manifest, calculators) → cache-first.
  event.respondWith(cacheFirst(request, SHELL_CACHE))
})
