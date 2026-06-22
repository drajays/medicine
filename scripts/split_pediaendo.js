#!/usr/bin/env node
'use strict';

/**
 * Pediaendo OCR split pipeline:
 *   node scripts/split_pediaendo.js split    — JSON → per-chapter content.md + pages.json + _manifest.json
 *   node scripts/split_pediaendo.js images   — download imgs/, rewrite paths in content.md + pages.json
 *   node scripts/split_pediaendo.js all      — split + images
 *   node scripts/split_pediaendo.js index    — write pediaendo_app/data/index.json from _manifest.json
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const SOURCE_DIR = '/Users/dr.ajayshukla/Downloads/pediaendo';
const PEDIAENDO_APP = '/Users/dr.ajayshukla/pediaendo_app';
const MONO_JSON = path.join(SOURCE_DIR, 'endoped.pdf_by_PaddleOCR-VL-1.6.json');
const CHAPTERS_DIR = path.join(SOURCE_DIR, 'chapters');
const MANIFEST_PATH = path.join(CHAPTERS_DIR, '_manifest.json');
const SOURCE_FILE = 'endoped.pdf_by_PaddleOCR-VL-1.6.json';

const BOOKS = [
  {
    slug: 'clinical_rounds',
    title: 'Clinical Rounds in Endocrinology Vol II - Pediatric Endocrinology',
    startPage: 0,
    endPage: 471,
    titleMode: 'toc',
    toc: [
      'Disorders of Growth and Development: Clinical Perspectives',
      'Disorders of Growth and Development: Diagnosis and Treatment',
      'Thyroid Disorders in Children',
      "Childhood Cushing's Syndrome",
      'Rickets–Osteomalacia',
      'Precocious Puberty',
      'Delayed Puberty',
      'Turner Syndrome',
      'Disorders of Sex Development',
      'Congenital Adrenal Hyperplasia',
      'Multiple Endocrine Neoplasia',
      'Diabetes in the Young',
    ],
  },
  {
    slug: 'practical_guide',
    title: 'Pediatric Endocrinology: A Practical Clinical Guide (2024)',
    startPage: 472,
    endPage: 1574,
    titleMode: 'heading',
  },
  {
    slug: 'diagnostic_protocols',
    title: 'Diagnostic Protocols in Endocrinology (2024)',
    startPage: 1575,
    endPage: 1691,
    titleMode: 'section',
  },
];

const BOOK_META = {
  clinical_rounds: {
    section: 'Clinical Rounds — Pediatric Endocrinology',
    authors: 'Anil Bhansali, Anuradha Aggarwal, Girish Parthan, Yashpal Gogate',
    prefix: 'cr',
  },
  practical_guide: {
    section: 'Practical Clinical Guide (2024)',
    authors: 'Sally Radovick, Madhusmita Misra',
    prefix: 'pg',
  },
  diagnostic_protocols: {
    section: 'Diagnostic Protocols (2024)',
    authors: 'Sanjay Bhadada, Liza Das, Rimesh Pal',
    prefix: 'dp',
  },
};

const CHAPTER_START_RE = /^##\s+(\d+)\.1\s+(.+)$/m;
const IMG_CONCURRENCY = 8;
const IMG_RETRIES = 3;

function fileSlug(title) {
  return title
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '')
    .toLowerCase()
    .slice(0, 60);
}

function chapterFolder(chapterNo, title) {
  return `${String(chapterNo).padStart(3, '0')}_${fileSlug(title)}`;
}

function pageText(page) {
  const md = page?.markdown;
  if (!md) return '';
  if (typeof md === 'string') return md;
  return md.text || '';
}

function pageImages(page) {
  const md = page?.markdown;
  if (!md || typeof md !== 'object') return {};
  return md.images || {};
}

function detectChapterStarts(pages, book) {
  const starts = [];
  for (let i = book.startPage; i <= book.endPage; i++) {
    const text = pageText(pages[i]);
    const m = text.match(CHAPTER_START_RE);
    if (!m) continue;
    const ch = parseInt(m[1], 10);
    if (starts.length && starts[starts.length - 1].chapterNo === ch) continue;
    starts.push({ chapterNo: ch, pageStart: i, sectionTitle: m[2].trim() });
  }
  return starts;
}

function extractHeadingTitle(pages, pageIdx, lookback = 4) {
  const min = Math.max(0, pageIdx - lookback);
  for (let i = pageIdx; i >= min; i--) {
    for (const line of pageText(pages[i]).split('\n')) {
      const m = line.trim().match(/^#\s+(.+)$/);
      if (!m) continue;
      const title = m[1].trim();
      if (title === 'Contents' || title.length < 5) continue;
      if (/^\d+\./.test(title) || title.includes('?')) continue;
      return title;
    }
  }
  return null;
}

function resolveChapterTitle(book, chapterNo, sectionTitle, pages, pageStart) {
  if (book.titleMode === 'toc' && book.toc[chapterNo - 1]) {
    return book.toc[chapterNo - 1];
  }
  if (book.titleMode === 'heading') {
    return extractHeadingTitle(pages, pageStart) || sectionTitle;
  }
  return sectionTitle;
}

function countImagesInSlice(pages, start, end) {
  let n = 0;
  for (let i = start; i <= end; i++) {
    n += Object.keys(pageImages(pages[i])).length;
  }
  return n;
}

function buildContentMd(book, chapter, pages) {
  const parts = [
    `# Chapter ${chapter.chapterNo}: ${chapter.chapterTitle}`,
    '',
    `*${book.title}*`,
    '',
    `Source pages: ${chapter.pageStart}–${chapter.pageEnd} (0-based index in ${SOURCE_FILE})`,
    '',
  ];
  for (let i = chapter.pageStart; i <= chapter.pageEnd; i++) {
    const text = pageText(pages[i]).trim();
    if (text) parts.push(text);
  }
  return parts.join('\n\n').trim() + '\n';
}

function buildPagesJson(book, chapter, pages) {
  const slice = [];
  for (let i = chapter.pageStart; i <= chapter.pageEnd; i++) {
    slice.push({ pageIndex: i, ...pages[i] });
  }
  return {
    book: book.slug,
    bookTitle: book.title,
    chapterNo: chapter.chapterNo,
    chapterTitle: chapter.chapterTitle,
    folder: chapter.folder,
    sourceFile: SOURCE_FILE,
    pageStart: chapter.pageStart,
    pageEnd: chapter.pageEnd,
    pageCount: chapter.pageEnd - chapter.pageStart + 1,
    pages: slice,
  };
}

function writeSlice(book, bookDir, label, chapterNo, chapterTitle, pageStart, pageEnd, pages) {
  const folder = chapterNo === 0
    ? '000_front_matter'
    : chapterFolder(chapterNo, chapterTitle);
  const chapter = {
    chapterNo,
    chapterTitle: chapterNo === 0 ? 'Front Matter' : chapterTitle,
    pageStart,
    pageEnd,
    folder,
    imageCount: countImagesInSlice(pages, pageStart, pageEnd),
  };
  const dir = path.join(bookDir, folder);
  fs.mkdirSync(dir, { recursive: true });
  const contentMd = chapterNo === 0
    ? (() => {
        const parts = [`# Front Matter`, '', `*${book.title}*`, '', `Source pages: ${pageStart}–${pageEnd}`, ''];
        for (let i = pageStart; i <= pageEnd; i++) {
          const text = pageText(pages[i]).trim();
          if (text) parts.push(text);
        }
        return parts.join('\n\n').trim() + '\n';
      })()
    : buildContentMd(book, chapter, pages);
  const pagesJson = buildPagesJson(book, chapter, pages);
  fs.writeFileSync(path.join(dir, 'content.md'), contentMd);
  fs.writeFileSync(path.join(dir, 'pages.json'), JSON.stringify(pagesJson, null, 2));
  return {
    book: book.slug,
    bookTitle: book.title,
    chapterNo,
    chapterTitle: chapter.chapterTitle,
    folder,
    path: path.relative(SOURCE_DIR, dir),
    pageStart,
    pageEnd,
    pageCount: pageEnd - pageStart + 1,
    imageCount: chapter.imageCount,
  };
}

function splitMonolith() {
  if (!fs.existsSync(MONO_JSON)) throw new Error('Missing ' + MONO_JSON);
  console.log('Loading', MONO_JSON);
  const pages = JSON.parse(fs.readFileSync(MONO_JSON, 'utf8'));
  console.log(`Loaded ${pages.length} pages`);

  fs.mkdirSync(CHAPTERS_DIR, { recursive: true });
  const manifest = { generated: new Date().toISOString(), sourceFile: SOURCE_FILE, books: [], entries: [] };

  for (const book of BOOKS) {
    const bookDir = path.join(CHAPTERS_DIR, book.slug);
    fs.mkdirSync(bookDir, { recursive: true });

    const starts = detectChapterStarts(pages, book);
    if (!starts.length) throw new Error(`No chapters detected for ${book.slug}`);

    const bookEntries = [];

    if (starts[0].pageStart > book.startPage) {
      bookEntries.push(writeSlice(
        book, bookDir, 'front', 0, 'Front Matter',
        book.startPage, starts[0].pageStart - 1, pages
      ));
    }

    for (let idx = 0; idx < starts.length; idx++) {
      const start = starts[idx];
      const pageEnd = idx + 1 < starts.length ? starts[idx + 1].pageStart - 1 : book.endPage;
      const title = resolveChapterTitle(book, start.chapterNo, start.sectionTitle, pages, start.pageStart);
      bookEntries.push(writeSlice(
        book, bookDir, 'chapter', start.chapterNo, title,
        start.pageStart, pageEnd, pages
      ));
    }

    manifest.books.push({
      slug: book.slug,
      title: book.title,
      startPage: book.startPage,
      endPage: book.endPage,
      chapterCount: starts.length,
      frontMatter: starts[0].pageStart > book.startPage,
    });
    manifest.entries.push(...bookEntries);
    console.log(`${book.slug}: ${bookEntries.length} folders (${starts.length} chapters)`);
  }

  fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2));
  console.log(`Wrote ${manifest.entries.length} entries → ${MANIFEST_PATH}`);
  return manifest;
}

function loadManifest() {
  if (!fs.existsSync(MANIFEST_PATH)) return splitMonolith();
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
}

function imgBasename(key) {
  return path.basename(key.replace(/^imgs\//, ''));
}

function downloadUrl(url, dest) {
  return new Promise((resolve, reject) => {
    const proto = url.startsWith('https') ? https : http;
    const req = proto.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 split_pediaendo/1.0' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        downloadUrl(res.headers.location, dest).then(resolve).catch(reject);
        return;
      }
      if (res.statusCode !== 200) {
        res.resume();
        reject(new Error(`HTTP ${res.statusCode} for ${url}`));
        return;
      }
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(dest, Buffer.concat(chunks));
        resolve(dest);
      });
    });
    req.on('error', reject);
    req.setTimeout(30000, () => {
      req.destroy(new Error('timeout'));
    });
  });
}

async function downloadWithRetry(url, dest) {
  for (let attempt = 1; attempt <= IMG_RETRIES; attempt++) {
    try {
      await downloadUrl(url, dest);
      return;
    } catch (err) {
      if (attempt === IMG_RETRIES) throw err;
      await new Promise((r) => setTimeout(r, 500 * attempt));
    }
  }
}

async function mapPool(items, limit, fn) {
  const results = [];
  let i = 0;
  async function worker() {
    while (i < items.length) {
      const idx = i++;
      results[idx] = await fn(items[idx], idx);
    }
  }
  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, worker));
  return results;
}

function collectChapterImages(chapterDir) {
  const pagesPath = path.join(chapterDir, 'pages.json');
  if (!fs.existsSync(pagesPath)) return [];
  const data = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
  const tasks = [];
  const seen = new Set();
  for (const page of data.pages) {
    const images = page.markdown?.images || {};
    for (const [key, url] of Object.entries(images)) {
      if (!url || seen.has(url)) continue;
      seen.add(url);
      const basename = imgBasename(key);
      tasks.push({ key, url, basename, localRel: `imgs/${basename}` });
    }
  }
  return tasks;
}

async function processChapterImages(entry) {
  const chapterDir = path.join(SOURCE_DIR, entry.path);
  const imgsDir = path.join(chapterDir, 'imgs');
  fs.mkdirSync(imgsDir, { recursive: true });

  const tasks = collectChapterImages(chapterDir);
  if (!tasks.length) return { downloaded: 0, skipped: 0, failed: 0 };

  let downloaded = 0;
  let skipped = 0;
  let failed = 0;
  const urlToLocal = {};

  await mapPool(tasks, IMG_CONCURRENCY, async (task) => {
    const dest = path.join(imgsDir, task.basename);
    urlToLocal[task.url] = task.localRel;
    urlToLocal[task.key] = task.localRel;
    if (fs.existsSync(dest) && fs.statSync(dest).size > 0) {
      skipped++;
      return;
    }
    try {
      await downloadWithRetry(task.url, dest);
      downloaded++;
    } catch (err) {
      failed++;
      console.error(`  FAIL ${task.basename}: ${err.message}`);
    }
  });

  let contentMd = fs.readFileSync(path.join(chapterDir, 'content.md'), 'utf8');
  for (const task of tasks) {
    if (task.url) contentMd = contentMd.split(task.url).join(task.localRel);
    contentMd = contentMd.split(task.key).join(task.localRel);
    contentMd = contentMd.split(`imgs/${task.basename}`).join(task.localRel);
  }
  fs.writeFileSync(path.join(chapterDir, 'content.md'), contentMd);

  const pagesPath = path.join(chapterDir, 'pages.json');
  const data = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
  const localImages = {};
  for (const task of tasks) {
    localImages[task.key] = task.localRel;
  }
  data.localImages = localImages;
  for (const page of data.pages) {
    if (!page.markdown?.images) continue;
    const stripped = {};
    for (const [key] of Object.entries(page.markdown.images)) {
      stripped[key] = localImages[key] || `imgs/${imgBasename(key)}`;
    }
    page.markdown.images = stripped;
  }
  fs.writeFileSync(pagesPath, JSON.stringify(data, null, 2));

  return { downloaded, skipped, failed };
}

function chapterId(bookSlug, chapterNo) {
  const meta = BOOK_META[bookSlug];
  return `${meta.prefix}-${String(chapterNo).padStart(3, '0')}`;
}

function generateAppIndex(appDir = PEDIAENDO_APP) {
  const manifest = loadManifest();
  const sections = manifest.books.map((book) => {
    const meta = BOOK_META[book.slug];
    const chapters = manifest.entries
      .filter((e) => e.book === book.slug && e.chapterNo > 0)
      .map((e) => {
        const id = chapterId(book.slug, e.chapterNo);
        const slug = fileSlug(e.chapterTitle);
        return {
          id,
          no: String(e.chapterNo),
          title: e.chapterTitle,
          file: null,
          status: 'pending',
          sourcePath: e.path + '/content.md',
          sourceFolder: e.path,
          imageCount: e.imageCount,
        };
      });
    return { name: meta.section, chapters };
  });

  const index = {
    title: "Pediatric Endocrinology — Clinical Q-Bank & Notes",
    sourceRoot: path.join(SOURCE_DIR, 'chapters'),
    generatedFrom: path.relative(SOURCE_DIR, MANIFEST_PATH),
    sections,
  };

  const dataDir = path.join(appDir, 'data');
  fs.mkdirSync(dataDir, { recursive: true });
  const outPath = path.join(dataDir, 'index.json');
  fs.writeFileSync(outPath, JSON.stringify(index, null, 2) + '\n');
  const total = sections.reduce((n, s) => n + s.chapters.length, 0);
  console.log(`Wrote ${total} chapter entries → ${outPath}`);
  return index;
}

async function downloadImages() {
  const manifest = loadManifest();
  let totalDl = 0;
  let totalSkip = 0;
  let totalFail = 0;

  for (const entry of manifest.entries) {
    if (!entry.imageCount) continue;
    process.stdout.write(`${entry.path} (${entry.imageCount} refs)... `);
    const stats = await processChapterImages(entry);
    totalDl += stats.downloaded;
    totalSkip += stats.skipped;
    totalFail += stats.failed;
    console.log(`dl=${stats.downloaded} skip=${stats.skipped} fail=${stats.failed}`);
  }

  console.log(`Images done: downloaded=${totalDl} skipped=${totalSkip} failed=${totalFail}`);
  if (totalFail > 0) process.exitCode = 1;
}

async function main() {
  const cmd = process.argv[2] || 'all';
  if (cmd === 'split') {
    splitMonolith();
  } else if (cmd === 'images') {
    await downloadImages();
  } else if (cmd === 'all') {
    splitMonolith();
    await downloadImages();
  } else if (cmd === 'index') {
    generateAppIndex();
  } else {
    console.error('Usage: node scripts/split_pediaendo.js [split|images|all|index]');
    process.exit(1);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
