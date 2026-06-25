# Study progress cloud sync

Encrypted backup for progress, revision stats, mock-test activity, and marks.

## Deploy once (maintainer)

```bash
cd sync-worker
npm install
npx wrangler kv namespace create STUDY_KV
# Copy the id into wrangler.toml → [[kv_namespaces]] id = "..."
npm run deploy
```

Note the Worker URL (e.g. `https://medicine-study-sync.<account>.workers.dev`).

## Enable in the web app build

Create `web/.env.production`:

```
VITE_SYNC_API_URL=https://medicine-study-sync.<account>.workers.dev
```

Then `cd web && npm run deploy` and commit the updated root `index.html` + `assets/`.

## Student flow

1. **Progress** tab → **Study account** → **Register** (one-time User ID + password).
2. Study normally — auto-sync every ~45s while signed in.
3. After reinstall / new phone → **Sign in** with the same credentials → progress restores.

Data is **AES-256-GCM encrypted** in the browser; the server only stores ciphertext.
