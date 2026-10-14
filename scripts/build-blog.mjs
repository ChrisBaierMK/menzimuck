#!/usr/bin/env node
/**
 * build-blog.mjs — renders the shared Supabase blog store into static pages for ONE site,
 * using that site's own header, footer and CSS (extracted from its index.html at build time).
 *
 *   node scripts/build-blog.mjs --site menzimuck --src . --out .          (in place: blog/ next to the site files)
 *   node scripts/build-blog.mjs --site baiersolutions --src . --out dist  (copy site → dist, then build the blog there)
 *   add --from seed-posts to build offline from JSON files instead of Supabase
 *
 * Env: BLOG_SITE, SUPABASE_URL, SUPABASE_KEY (publishable key), NO_IMAGE_CDN=1 to link images directly.
 * Writes: blog/index.html, blog/page/N/, blog/<slug>/, blog/tag/<tag>/ (menzimuck only), blog/feed.xml,
 *   blog/latest.json, blog/blog.css (+ blog/site-base.css on baiersolutions), merges blog URLs into sitemap.xml,
 *   adds the Sitemap line to robots.txt if missing, and fills the <!-- blog-latest:start/end --> block in index.html.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const args = Object.fromEntries(process.argv.slice(2).map((a, i, all) => a.startsWith('--') ? [a.slice(2), all[i + 1] && !all[i + 1].startsWith('--') ? all[i + 1] : true] : []).filter(Boolean));

const SITE = String(args.site || process.env.BLOG_SITE || '').trim();
const SRC = path.resolve(root, String(args.src || '.'));
const OUT = path.resolve(root, String(args.out || '.'));
const FROM = args.from ? path.resolve(root, String(args.from)) : null;
const PER_PAGE = 12;

if (!['menzimuck', 'baiersolutions'].includes(SITE)) { console.error(`--site must be menzimuck or baiersolutions (got "${SITE}")`); process.exit(1); }
const T = await import(`../templates/${SITE}.mjs`);
const site = T.site;

// ---------- data ----------
async function loadPosts() {
  if (FROM) {
    const posts = fs.readdirSync(FROM).filter(f => f.endsWith('.json')).map(f => JSON.parse(fs.readFileSync(path.join(FROM, f), 'utf8')))
      .map(p => ({ published_at: new Date().toISOString(), updated_at: new Date().toISOString(), status: 'published', ...p }));
    return { posts, siteRows: [{ key: 'menzimuck', base_url: 'https://menzi-muck.ro' }, { key: 'baiersolutions', base_url: 'https://baiersolutions.ro' }] };
  }
  const url = process.env.SUPABASE_URL, key = process.env.SUPABASE_KEY;
  if (!url || !key) { console.error('SUPABASE_URL and SUPABASE_KEY are required (or use --from <dir>)'); process.exit(1); }
  const h = { apikey: key, Authorization: `Bearer ${key}` };
  const q = `${url}/rest/v1/blog_posts?select=*&status=eq.published&sites=cs.{${SITE}}&order=published_at.desc&limit=1000`;
  const [pr, sr] = await Promise.all([fetch(q, { headers: h }), fetch(`${url}/rest/v1/blog_sites?select=key,base_url`, { headers: h })]);
  if (!pr.ok) throw new Error(`posts fetch failed: ${pr.status} ${await pr.text()}`);
  if (!sr.ok) throw new Error(`sites fetch failed: ${sr.status} ${await sr.text()}`);
  return { posts: await pr.json(), siteRows: await sr.json() };
}

// ---------- helpers (passed to templates as `h`) ----------
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const months = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie'];
const dateRo = iso => { const d = new Date(iso); return `${d.getUTCDate()} ${months[d.getUTCMonth()]} ${d.getUTCFullYear()}`; };
const words = md => md.replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/[#*_>`]/g, '').split(/\s+/).filter(Boolean).length;
const readMin = md => Math.max(1, Math.round(words(md) / 200));
// Local photos live in /media/blog/<name>-640.webp and -1200.webp; serve the small one to phones and cards.
const local = u => /^\/media\/blog\/.+-(640|1200)\.webp$/.test(u || '');
// Real pixel size of local WebP photos, so width/height attributes keep the true ratio.
const sizeCache = new Map();
function webpSize(u) {
  if (sizeCache.has(u)) return sizeCache.get(u);
  let r = null;
  try {
    const b = fs.readFileSync(path.join(SRC, u.replace(/^\//, '')));
    const t = b.toString('ascii', 12, 16);
    if (t === 'VP8X') r = [1 + b.readUIntLE(24, 3), 1 + b.readUIntLE(27, 3)];
    else if (t === 'VP8 ') r = [b.readUInt16LE(26) & 0x3fff, b.readUInt16LE(28) & 0x3fff];
    else if (t === 'VP8L') { const v = b.readUInt32LE(21); r = [(v & 0x3fff) + 1, ((v >> 14) & 0x3fff) + 1]; }
  } catch {}
  sizeCache.set(u, r); return r;
}
const img = (u, alt, w = 1200, extra = '') => {
  if (!u) return '';
  if (local(u)) {
    const base = u.replace(/-(640|1200)\.webp$/, '');
    const src = w <= 720 ? `${base}-640.webp` : `${base}-1200.webp`;
    const sizes = w <= 720 ? '(max-width: 760px) 100vw, 400px' : '(max-width: 760px) 100vw, 760px';
    const d = webpSize(src) || webpSize(u);
    const dims = d ? `width="${d[0]}" height="${d[1]}"` : '';
    return `<img src="${esc(src)}" srcset="${esc(base)}-640.webp 640w, ${esc(base)}-1200.webp 1200w" sizes="${sizes}" alt="${esc(alt)}" ${dims} decoding="async" ${extra}>`;
  }
  return `<img src="${esc(u)}" alt="${esc(alt)}" decoding="async" ${extra}>`;
};
const absolute = (base, p) => base.replace(/\/$/, '') + p;
const write = (rel, content) => { const f = path.join(OUT, rel); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, content); };
const h = { esc, dateRo, readMin, img };

function renderMarkdown(md) {
  const renderer = new marked.Renderer();
  // marked v12 passes (href, title, text); v13+ passes a token object — support both
  const tok = (a, title, text) => (a && typeof a === 'object') ? a : { href: a, title, text };
  renderer.image = (a, b, c) => { const { href, text } = tok(a, b, c); return `<figure>${img(href, text, 1200, 'loading="lazy"')}<figcaption>${esc(text)}</figcaption></figure>`; };
  renderer.link = (a, b, c) => { const { href, title, text } = tok(a, b, c);
    const ext = /^https?:\/\//.test(href) && !href.startsWith(site.baseUrl);
    const rel = site.nofollow.test(href) ? ' rel="nofollow noopener"' : (ext ? ' rel="noopener"' : '');
    return `<a href="${esc(href)}"${title ? ` title="${esc(title)}"` : ''}${ext ? ` target="_blank"${rel}` : ''}>${text}</a>`;
  };
  let html = marked.parse(md, { renderer, gfm: true, breaks: false });
  html = html.replace(/<\/figure>\s*<p><em>(Foto:[^<]*)<\/em><\/p>/g, '</figure><p class="credit">$1</p>');
  return html;
}

// ---------- the site's own chrome ----------
const indexPath = path.join(SRC, 'index.html');
const indexHtml = fs.existsSync(indexPath) ? fs.readFileSync(indexPath, 'utf8') : '';
function extract(re, fallback) { const m = indexHtml.match(re); return m ? m[0] : fallback; }
let header = extract(/<header[\s\S]*?<\/header>/, T.fallbackHeader);
let footer = extract(/<footer[\s\S]*?<\/footer>/, T.fallbackFooter);
// make home-page-relative links and assets absolute so they work under /blog/...
const absolutize = s => s.replace(/href="#/g, 'href="/#').replace(/(src|href)="(img|images|fonts|css)\//g, '$1="/$2/');
header = absolutize(header); footer = absolutize(footer);
// mark the Blog link as current
header = header.replace(/<a href="\/blog\/"(?![^>]*aria-current)/, '<a href="/blog/" aria-current="page"');
if (!/href="\/blog\/"/.test(header)) console.warn(`[${SITE}] note: index.html header has no /blog/ link yet`);

let siteBaseCss = null;
if (SITE === 'baiersolutions') {
  const m = indexHtml.match(/<style>([\s\S]*?)<\/style>/);
  siteBaseCss = (m ? m[1] : '').replace(/url\((['"]?)fonts\//g, 'url($1/fonts/');
}

function shell({ title, description, canonical, ogImage, ogType = 'website', jsonld = [], noindex = false, body }) {
  const ld = jsonld.map(o => `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', ...o })}</script>`).join('');
  return T.head({ title: esc(title), description: esc(description), canonical: esc(canonical), ogImage: esc(ogImage || site.ogImage), ogType, jsonld: ld, noindex })
    + header + '\n' + body + '\n' + footer + '\n' + T.footerScript + '\n</body>\n</html>\n';
}

// ---------- pages ----------
function listPage({ posts, title, h1, description, eyebrow, canonicalPath, page = 1, pages = 1, pathFor, noindex = false, hero }) {
  const body = T.listPage({ posts, title, h1, description, eyebrow, page, pages, pathFor, hero }, h);
  const jsonld = [{ '@type': 'Blog', name: site.blogTitle, url: absolute(site.baseUrl, canonicalPath), description, publisher: site.org,
    blogPost: posts.slice(0, 10).map(p => ({ '@type': 'BlogPosting', headline: p.title, url: absolute(site.baseUrl, `/blog/${p.slug}/`), datePublished: p.published_at })) }];
  return shell({ title: page > 1 ? `${title} — pagina ${page}` : title, description, canonical: absolute(site.baseUrl, canonicalPath), noindex: noindex || page > 1, jsonld, body });
}

function postPage(p, all, siteRows) {
  const pathP = `/blog/${p.slug}/`;
  const canonicalBase = (siteRows.find(s => s.key === p.canonical_site) || {}).base_url || site.baseUrl;
  const canonical = absolute(canonicalBase, pathP);
  const isSecondary = p.canonical_site !== site.key;
  const bodyHtml = renderMarkdown(p.body_md);
  const related = all.filter(o => o.slug !== p.slug).map(o => ({ o, n: (o.tags || []).filter(t => (p.tags || []).includes(t)).length })).filter(x => x.n > 0).sort((a, b) => b.n - a.n).slice(0, 3).map(x => x.o);
  const jsonld = [
    { '@type': 'BreadcrumbList', itemListElement: [{ '@type': 'ListItem', position: 1, name: 'Acasă', item: site.baseUrl + '/' }, { '@type': 'ListItem', position: 2, name: 'Blog', item: absolute(site.baseUrl, '/blog/') }, { '@type': 'ListItem', position: 3, name: p.title, item: absolute(site.baseUrl, pathP) }] },
    { '@type': 'Article', headline: p.seo_title || p.title, description: p.meta_description, image: p.cover_image_url || undefined, datePublished: p.published_at, dateModified: p.updated_at || p.published_at, inLanguage: p.lang || 'ro', mainEntityOfPage: canonical, author: { '@id': site.org['@id'] }, publisher: site.org, keywords: [p.primary_keyword, ...(p.secondary_keywords || [])].filter(Boolean).join(', ') }
  ];
  if ((p.faq || []).length) jsonld.push({ '@type': 'FAQPage', mainEntity: p.faq.map(f => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })) });
  const body = T.postPage({ p, bodyHtml, canonical, isSecondary, related, canonicalHost: canonicalBase.replace(/^https?:\/\//, '') }, h);
  return shell({ title: p.seo_title || p.title, description: p.meta_description || p.excerpt || '', canonical, ogImage: p.cover_image_url, ogType: 'article', jsonld, body });
}

function feed(posts) {
  const items = posts.slice(0, 20).map(p => `<item><title>${esc(p.title)}</title><link>${esc(absolute(site.baseUrl, `/blog/${p.slug}/`))}</link><guid isPermaLink="true">${esc(absolute(site.baseUrl, `/blog/${p.slug}/`))}</guid><pubDate>${new Date(p.published_at).toUTCString()}</pubDate><description>${esc(p.excerpt || p.meta_description || '')}</description>${(p.tags || []).map(t => `<category>${esc(t)}</category>`).join('')}</item>`).join('\n');
  return `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>${esc(site.blogTitle)}</title><link>${esc(absolute(site.baseUrl, '/blog/'))}</link><description>${esc(site.blogDescription)}</description><language>ro</language><lastBuildDate>${new Date().toUTCString()}</lastBuildDate>\n${items}\n</channel></rss>\n`;
}

function mergeSitemap(posts, tags) {
  const url = (loc, lastmod, pri) => `  <url><loc>${esc(loc)}</loc>${lastmod ? `<lastmod>${new Date(lastmod).toISOString().slice(0, 10)}</lastmod>` : ''}<priority>${pri}</priority></url>`;
  const entries = [url(absolute(site.baseUrl, '/blog/'), posts[0]?.updated_at, '0.8'),
    ...posts.filter(p => p.canonical_site === site.key).map(p => url(absolute(site.baseUrl, `/blog/${p.slug}/`), p.updated_at || p.published_at, '0.7')),
    ...(site.indexTags ? tags.map(t => url(absolute(site.baseUrl, `/blog/tag/${t}/`), null, '0.4')) : [])];
  const f = path.join(OUT, 'sitemap.xml');
  if (fs.existsSync(f)) {
    let x = fs.readFileSync(f, 'utf8').replace(/\s*<url><loc>[^<]*\/blog\/[^<]*<\/loc>.*?<\/url>/g, '');
    x = x.replace(/\s*<\/urlset>/, `\n${entries.join('\n')}\n</urlset>`);
    fs.writeFileSync(f, x);
  } else {
    write('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${url(site.baseUrl + '/', null, '1.0')}\n${entries.join('\n')}\n</urlset>\n`);
  }
}

function injectLatest(posts) {
  const f = path.join(OUT, 'index.html');
  if (!fs.existsSync(f)) return false;
  const x = fs.readFileSync(f, 'utf8');
  const re = /<!-- blog-latest:start -->[\s\S]*?<!-- blog-latest:end -->/;
  if (!re.test(x)) { console.warn(`[${SITE}] index.html has no <!-- blog-latest:start/end --> markers; home block not injected`); return false; }
  fs.writeFileSync(f, x.replace(re, `<!-- blog-latest:start -->\n${T.latestBlock(posts, h)}\n<!-- blog-latest:end -->`));
  return true;
}

function copySite() {
  if (SRC === OUT) return;
  const skip = new Set(['node_modules', 'dist', '.git', '.netlify', 'scripts', 'templates', 'seed-posts', 'snippets', 'package.json', 'package-lock.json', 'README-blog.md', '.gitignore', '_tmp-claude', '__pycache__', '_versions']);
  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(OUT, { recursive: true });
  for (const entry of fs.readdirSync(SRC)) {
    if (skip.has(entry) || entry.startsWith('deploy-') || entry.endsWith('.tgz')) continue;
    fs.cpSync(path.join(SRC, entry), path.join(OUT, entry), { recursive: true });
  }
}

async function main() {
  const t0 = Date.now();
  const { posts: raw, siteRows } = await loadPosts();
  let posts = raw.filter(p => (p.sites || []).includes(site.key) && p.status === 'published');
  if (site.onlyTags) posts = posts.filter(p => (p.tags || []).some(t => site.onlyTags.includes(t)));
  posts.sort((a, b) => new Date(b.published_at) - new Date(a.published_at));
  copySite();
  fs.rmSync(path.join(OUT, 'blog'), { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, 'blog'), { recursive: true });
  write('blog/blog.css', T.extraCss);
  if (siteBaseCss) write('blog/site-base.css', siteBaseCss);

  const pages = Math.max(1, Math.ceil(posts.length / PER_PAGE));
  for (let n = 1; n <= pages; n++) {
    write(n === 1 ? 'blog/index.html' : `blog/page/${n}/index.html`, listPage({ posts: posts.slice((n - 1) * PER_PAGE, n * PER_PAGE), title: site.blogTitle, h1: site.blogH1, description: site.blogDescription, eyebrow: 'Blog', hero: site.blogHero,
      canonicalPath: n === 1 ? '/blog/' : `/blog/page/${n}/`, page: n, pages, pathFor: k => k === 1 ? '/blog/' : `/blog/page/${k}/` }));
  }
  for (const p of posts) write(`blog/${p.slug}/index.html`, postPage(p, posts, siteRows));
  const tags = site.indexTags ? [...new Set(posts.flatMap(p => p.tags || []))].sort() : [];
  for (const t of tags) {
    const tp = posts.filter(p => (p.tags || []).includes(t));
    write(`blog/tag/${t}/index.html`, listPage({ posts: tp, title: `${t.replace(/-/g, ' ')} — ${site.blogTitle}`, h1: t.replace(/-/g, ' '), description: `Articole despre ${t.replace(/-/g, ' ')} pe ${site.name}.`, eyebrow: 'Etichetă', hero: site.blogHero, canonicalPath: `/blog/tag/${t}/`, pathFor: () => `/blog/tag/${t}/` }));
  }
  write('blog/feed.xml', feed(posts));
  write('blog/latest.json', JSON.stringify(posts.slice(0, 3).map(p => ({ title: p.title, url: `/blog/${p.slug}/`, excerpt: p.excerpt || p.meta_description || '', cover: p.cover_image_url, alt: p.cover_image_alt, date: p.published_at }))));
  mergeSitemap(posts, tags);
  const robots = path.join(OUT, 'robots.txt');
  const sm = `Sitemap: ${absolute(site.baseUrl, '/sitemap.xml')}`;
  if (!fs.existsSync(robots)) write('robots.txt', `User-agent: *\nAllow: /\n\n${sm}\n`);
  else if (!fs.readFileSync(robots, 'utf8').includes('Sitemap:')) fs.appendFileSync(robots, `\n${sm}\n`);
  const injected = injectLatest(posts);
  console.log(`[${site.key}] ${posts.length} posts, ${tags.length} tag pages, ${pages} index page(s), home block ${injected ? 'injected' : 'skipped'} → ${OUT} in ${Date.now() - t0} ms`);
}

main().catch(e => { console.error(e); process.exit(1); });
