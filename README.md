# medicine

Harrison's Principles of Internal Medicine (22nd ed.) — clinical Q-bank & notes web app.

Clinically-focused MCQs (diagnosis, management & treatment), chapter notes, true/false,
and assertion–reason questions — each linked to the source text. Endocrinology first.

## Launch (GitHub Pages)

Settings → Pages → Branch: `main` → `/ (root)`.

Live: **https://drajays.github.io/medicine/**

The production site is the **React UI** built from `web/` and deployed to the repo root
(`index.html` + `assets/`). The legacy vanilla app is preserved in `legacy/`.

### Deploy UI updates

```bash
cd web
npm install
npm run deploy    # build + copy dist → repo root
git add index.html assets/ legacy/ web/
git commit -m "Deploy React UI"
git push origin main
```

### Local development

```bash
cd web
npm run dev       # http://localhost:5173/medicine/
```

Dev server proxies `/medicine/data/*` to the repo `data/` folder.
