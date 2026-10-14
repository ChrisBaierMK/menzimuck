// menzi-muck.ro blog template — mirrors the site's own /ghid/ article pages (build.py), reusing /css/site.css.
export const site = {
  key: 'menzimuck', name: 'Menzi Muck România', baseUrl: 'https://menzi-muck.ro', lang: 'ro',
  blogTitle: 'Blog Menzi Muck România', blogH1: 'Blog: Menzi Muck în lume și în România',
  blogDescription: 'Noutăți Menzi Muck din toată lumea, explicate pentru șantierele din România: modele noi, lucrări pe pante și în albii, târguri, service și finanțare.',
  blogHero: '/images/slope.jpg', ogImage: 'https://menzi-muck.ro/images/m545x-2.jpg',
  phone: '+40 723 675 581', phoneHref: 'tel:+40723675581', email: 'christoph@baiersolutions.ro',
  indexTags: true, onlyTags: ['menzi-muck'],
  nofollow: /mascus|machineryzone|machinerypark|machineryline|olx\.ro/,
  fonts: '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">',
  org: { '@type': 'Organization', '@id': 'https://menzi-muck.ro/#org', name: 'Baier Solutions SRL', alternateName: 'Menzi Muck România', url: 'https://menzi-muck.ro/', logo: 'https://menzi-muck.ro/images/logo.svg', telephone: '+40 723 675 581', email: 'christoph@baiersolutions.ro', vatID: 'RO33270728', address: { '@type': 'PostalAddress', addressLocality: 'Hărman', addressRegion: 'Brașov', addressCountry: 'RO' }, areaServed: ['RO', 'MD'], knowsLanguage: ['ro', 'de', 'en'], brand: { '@type': 'Brand', name: 'Menzi Muck' }, sameAs: ['https://menzimuck.com', 'https://baiersolutions.ro'] },
};

// Fallbacks used only when the site's index.html cannot be read.
export const fallbackHeader = `<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Menzi Muck România — Baier Solutions, importator oficial România și Republica Moldova">
      <img class="mm" src="/images/logo-neg.svg" alt="Menzi Muck" width="92" height="36">
      <img class="bs" src="/images/baier-solutions.svg" alt="Baier Solutions" width="80" height="30">
      <span class="by">Importator oficial<b>România și Republica Moldova</b></span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">Meniu</button>
    <ul id="menu">
      <li><a href="/#modele">Modele</a></li>
      <li><a href="/excavator-paianjen/">Excavator păianjen</a></li>
      <li><a href="/#domenii">Domenii</a></li>
      <li><a href="/ghid/">Ghid</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/#despre">Despre</a></li>
    </ul>
    <a class="cta" href="/#contact">Cere ofertă</a>
  </div>
</header>`;
export const fallbackFooter = `<footer>
  <div class="wrap">
    <div>Baier Solutions SRL · Hărman, Brașov · CIF RO33270728</div>
    <ul><li><a href="/excavator-paianjen/">Excavator păianjen</a></li><li><a href="/m5x.html">M5x</a></li><li><a href="/m4x.html">M4x</a></li><li><a href="/m2.html">M2</a></li><li><a href="/a20-a25.html">A20 / A25</a></li><li><a href="/ghid/">Ghid</a></li><li><a href="/blog/">Blog</a></li></ul>
    <ul><li><a href="tel:+40723675581">+40 723 675 581</a></li><li><a href="mailto:christoph@baiersolutions.ro">christoph@baiersolutions.ro</a></li><li><a href="https://menzimuck.com" rel="noopener">menzimuck.com</a></li></ul>
    <div class="legal">© 2026 Baier Solutions SRL, importator oficial Menzi Muck AG (Rüthi, Elveția) pentru România și Republica Moldova. Menzi Muck® este marcă înregistrată a Menzi Muck AG; fotografiile și materialele video sunt proprietatea Menzi Muck AG și sunt folosite cu acordul acesteia.</div>
  </div>
</footer>`;
export const footerScript = `<script>(function(){var n=document.getElementById('nav');if(!n)return;function s(){n.classList.toggle('solid',window.scrollY>40)}addEventListener('scroll',s,{passive:true});s();})();</script>`;

export const extraCss = `.prose figure{margin:28px 0 8px}.prose figure img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}.prose figcaption{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);padding-top:10px}.prose .credit{font-size:13px;color:var(--ink-3);margin:-2px 0 24px}.prose figure+.credit{margin-top:4px}
.post-meta{display:flex;gap:18px;flex-wrap:wrap;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-2);margin:0 0 28px}
.post-tags{display:flex;gap:8px;flex-wrap:wrap;margin:40px 0 0}.post-tags a{font-size:11px;letter-spacing:.16em;text-transform:uppercase;border:1px solid var(--line);padding:6px 10px}.post-tags a:hover{border-color:#fff}
.origin{font-size:13px;color:var(--ink-3);margin-top:24px;padding-top:16px;border-top:1px solid var(--line)}.origin a{color:#fff;text-decoration:underline}
.gcard .d{display:block;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3);margin-bottom:6px}
.pager{display:flex;justify-content:center;gap:8px;padding:8px 0 96px}.pager a,.pager span{font-size:12px;letter-spacing:.14em;padding:12px 16px;border:1px solid var(--line)}.pager a:hover,.pager span[aria-current]{border-color:#fff}
.sec-blog{padding:0 0 24px}`;

export function head({ title, description, canonical, ogImage, ogType, jsonld, noindex }) {
  return `<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${description}">
<meta name="robots" content="${noindex ? 'noindex,follow' : 'index,follow,max-image-preview:large'}">
<link rel="canonical" href="${canonical}">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="Menzi Muck România">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${ogImage}">
<meta property="og:type" content="${ogType}">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Blog Menzi Muck România" href="https://menzi-muck.ro/blog/feed.xml">
${jsonld}
${site.fonts}
<link rel="stylesheet" href="/css/site.css">
<link rel="stylesheet" href="/blog/blog.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
</head>
<body>
`;
}

export function card(p, h) {
  return `<a class="gcard" href="/blog/${p.slug}/">${h.img(p.cover_image_url, p.cover_image_alt || p.title, 720, 'loading="lazy"')}<div class="t"><span class="d">${h.dateRo(p.published_at)}${p.tags?.[0] ? ' · ' + h.esc(p.tags[0].replace(/-/g, ' ')) : ''}</span><h3>${h.esc(p.title)}</h3></div></a>`;
}

export function listPage({ posts, title, h1, description, eyebrow, page, pages, pathFor, hero }, h) {
  const pager = pages > 1 ? `<nav class="wrap pager" aria-label="Pagini">${Array.from({ length: pages }, (_, i) => i + 1).map(n => n === page ? `<span aria-current="page">${n}</span>` : `<a href="${pathFor(n)}">${n}</a>`).join('')}</nav>` : '';
  return `
<section class="panel short art-hero">
  <div class="media"><img src="${hero}" alt="${h.esc(h1)}"></div>
  <div class="wrap"><div class="label rv">${h.esc(eyebrow)}</div><h1 class="rv d1">${h.esc(h1)}</h1></div>
</section>
<div class="wrap sec-blog"><p class="crumbs" style="padding:24px 0 0"><a href="/">Acasă</a> / <span>Blog</span></p><p style="max-width:64ch;color:var(--ink-2);margin:18px 0 0">${h.esc(description)}</p></div>
<div class="wrap guide-grid" style="padding:40px 0 ${pages > 1 ? '40px' : '120px'}">${posts.map(p => card(p, h)).join('')}</div>
${pager}`;
}

export function postPage({ p, bodyHtml, canonical, isSecondary, related, canonicalHost }, h) {
  const faq = (p.faq || []).length ? `<h2>Întrebări frecvente</h2>${p.faq.map(f => `<details><summary>${h.esc(f.q)}</summary><p>${h.esc(f.a)}</p></details>`).join('')}` : '';
  const d = new Date(p.published_at);
  return `
<section class="panel short art-hero">
  <div class="media">${h.img(p.cover_image_url, p.cover_image_alt || p.title, 1600, 'fetchpriority="high"')}</div>
  <div class="wrap"><div class="label rv">${h.esc((p.tags || [])[0]?.replace(/-/g, ' ') || 'Blog')}</div><h1 class="rv d1">${h.esc(p.title)}</h1></div>
</section>
<div class="wrap crumbs"><a href="/">Acasă</a> / <a href="/blog/">Blog</a> / <span>${h.esc(p.title)}</span></div>
<article class="wrap art">
  <div class="prose">
    <div class="post-meta"><time datetime="${h.esc(p.published_at)}">${h.dateRo(p.published_at)}</time><span>${h.readMin(p.body_md)} min de citit</span><span>${h.esc(p.author || 'Baier Solutions')}</span></div>
    ${p.excerpt ? `<p class="lead">${h.esc(p.excerpt)}</p>` : ''}
    ${bodyHtml}
    ${faq}
    ${(p.tags || []).length ? `<div class="post-tags">${p.tags.map(t => `<a href="/blog/tag/${h.esc(t)}/">${h.esc(t.replace(/-/g, ' '))}</a>`).join('')}</div>` : ''}
    ${isSecondary ? `<p class="origin">Publicat original pe <a href="${h.esc(canonical)}">${h.esc(canonicalHost)}</a>.</p>` : ''}
    <p class="byline">Baier Solutions SRL — importator oficial Menzi Muck AG pentru România · publicat ${String(d.getUTCDate()).padStart(2, '0')}.${String(d.getUTCMonth() + 1).padStart(2, '0')}.${d.getUTCFullYear()}</p>
  </div>
  <aside class="art-cta">
    <div class="eyebrow">Ofertă</div>
    <h3>Calculul pentru lucrarea ta</h3>
    <p>O oră la dumneavoastră pe șantier, cu omul de utilaje: drum tehnologic contra mașină, pe cifrele lui.</p>
    <a class="btn solid" href="/#contact">Cere ofertă</a>
    <a class="btn" href="${site.phoneHref}">${site.phone}</a>
    <ul><li><a href="/excavator-paianjen/">Excavator păianjen</a></li><li><a href="/m5x.html">Menzi Muck M5x</a></li><li><a href="/m4x.html">Menzi Muck M4x</a></li><li><a href="/m2.html">Menzi Muck M2</a></li><li><a href="/a20-a25.html">Menzi Muck A20 / A25</a></li><li><a href="/ghid/">Ghid</a></li></ul>
  </aside>
</article>
${related.length ? `<section class="related"><div class="wrap sec-head" style="padding-top:64px"><div class="eyebrow">Citește și</div></div><div class="wrap guide-grid">${related.map(r => card(r, h)).join('')}</div></section>` : '<div style="height:64px"></div>'}
`;
}

// Static block injected into index.html between <!-- blog-latest --> markers.
export function latestBlock(posts, h) {
  return `<section id="blog">
  <div class="wrap sec-head"><div class="eyebrow">Blog</div><h2>Menzi Muck în lume și în România.</h2><p>Modele noi, lucrări pe pante și în albii, târguri — povestite pentru antreprenorii de aici. <a href="/blog/" style="text-decoration:underline">Toate articolele</a>.</p></div>
  <div class="wrap guide-grid">${posts.slice(0, 3).map(p => card(p, h)).join('')}</div>
</section>`;
}
