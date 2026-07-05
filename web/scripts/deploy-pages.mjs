import { cpSync, mkdirSync, readdirSync, rmSync, statSync } from 'fs'
import { resolve, join } from 'path'
import { fileURLToPath } from 'url'
import { execSync } from 'child_process'

const __dirname = fileURLToPath(new URL('.', import.meta.url))
const webRoot = resolve(__dirname, '..')
const repoRoot = resolve(webRoot, '..')
const distDir = resolve(webRoot, 'dist')

try {
  execSync('node scripts/generate-content-log.mjs', { cwd: repoRoot, stdio: 'inherit' })
} catch {
  console.warn('content_log.json generation skipped (non-fatal)')
}

function copyDir(src, dest) {
  mkdirSync(dest, { recursive: true })
  for (const entry of readdirSync(src)) {
    const from = join(src, entry)
    const to = join(dest, entry)
    if (statSync(from).isDirectory()) copyDir(from, to)
    else cpSync(from, to)
  }
}

if (!statSync(distDir).isDirectory()) {
  console.error('Run npm run build first — dist/ not found')
  process.exit(1)
}

// Archive legacy vanilla app, then remove from root
const legacyDir = resolve(repoRoot, 'legacy')
mkdirSync(legacyDir, { recursive: true })
for (const file of ['app.js', 'styles.css']) {
  const src = resolve(repoRoot, file)
  const dest = resolve(legacyDir, file)
  try {
    if (statSync(src).isFile()) {
      cpSync(src, dest)
      rmSync(src)
    }
  } catch {
    /* already moved */
  }
}

// Deploy Vite build to Pages root
cpSync(resolve(distDir, 'index.html'), resolve(repoRoot, 'index.html'))
const assetsDest = resolve(repoRoot, 'assets')
mkdirSync(assetsDest, { recursive: true })
// Remove prior Vite hashed bundles only (keep other static assets)
for (const entry of readdirSync(assetsDest)) {
  if (/^index-[A-Za-z0-9_-]+\.(js|css)$/.test(entry)) {
    rmSync(join(assetsDest, entry))
  }
}
copyDir(resolve(distDir, 'assets'), assetsDest)

// Copy static public assets (favicon, PWA service worker + manifest, icons).
for (const file of ['favicon.svg', 'icons.svg', 'sw.js', 'manifest.webmanifest']) {
  const src = resolve(distDir, file)
  try {
    cpSync(src, resolve(repoRoot, file))
  } catch {
    /* optional */
  }
}

console.log('Deployed web/dist → repo root (index.html + assets/ + sw.js + manifest)')
