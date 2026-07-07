import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'path'
import fs from 'fs'
import path from 'path'

function serveRepoData(): Plugin {
  const dataDir = resolve(__dirname, '..', 'data')
  const repoRoot = resolve(__dirname, '..', '..')
  const staticDirs = ['calculators', 'imaging'] as const

  return {
    name: 'serve-repo-data',
    configureServer(server) {
      server.middlewares.use('/medicine/data', (req, res, next) => {
        const rel = (req.url ?? '/index.json').replace(/^\//, '').split('?')[0]
        const filePath = path.join(dataDir, rel)
        if (!filePath.startsWith(dataDir) || !fs.existsSync(filePath)) {
          next()
          return
        }
        res.setHeader('Content-Type', 'application/json')
        fs.createReadStream(filePath).pipe(res)
      })

      for (const dir of staticDirs) {
        const root = path.join(repoRoot, dir)
        server.middlewares.use(`/medicine/${dir}`, (req, res, next) => {
          const rel = (req.url ?? '/').replace(/^\//, '').split('?')[0]
          const filePath = path.join(root, rel)
          if (!filePath.startsWith(root) || !fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
            next()
            return
          }
          res.setHeader('Content-Type', rel.endsWith('.html') ? 'text/html' : 'application/octet-stream')
          fs.createReadStream(filePath).pipe(res)
        })
      }
    },
  }
}

export default defineConfig({
  base: '/medicine/',
  plugins: [react(), tailwindcss(), serveRepoData()],
  resolve: {
    alias: { '@': resolve(__dirname, 'src') },
  },
})
