// baiersolutions.ro blog template — reuses the home page's header, footer, fonts and tokens (extracted at build time).
export const site = {
  key: 'baiersolutions', name: 'Baier Solutions', baseUrl: 'https://baiersolutions.ro', lang: 'ro',
  blogTitle: 'Blog Baier Solutions', blogH1: 'Blog',
  blogDescription: 'Noutăți de la Baier Solutions: excavatoare Menzi Muck, evenimente MK1930, campanii de marketing, skateparkuri — și ce înseamnă fiecare pentru clienții din România.',
  ogImage: 'https://baiersolutions.ro/img/hero-pano-1920.webp',
  phone: '+40 723 675 581', phoneHref: 'tel:+40723675581', email: 'christoph@baiersolutions.ro',
  indexTags: false, onlyTags: null,
  nofollow: /mascus|machineryzone|machinerypark|machineryline|olx\.ro/,
  org: { '@type': 'LocalBusiness', '@id': 'https://baiersolutions.ro/#business', name: 'Baier Solutions', legalName: 'Baier Solutions SRL', url: 'https://baiersolutions.ro/', image: 'https://baiersolutions.ro/img/hero-pano-1920.webp', telephone: '+40 723 675 581', email: 'christoph@baiersolutions.ro', address: { '@type': 'PostalAddress', addressLocality: 'Hărman', addressRegion: 'Brașov', addressCountry: 'RO' }, sameAs: ['https://menzimuck.ro', 'https://mk1930.ro', 'https://actioncloud.co'] },
};

export const fallbackHeader = `<header id="hdr">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Baier Solutions"><img src="/img/logo-wordmark-white.svg" alt="Baier Solutions" width="2060" height="556"></a>
    <ul>
      <li><a href="/#utilaje">Excavatoare</a></li><li><a href="/#evenimente">Evenimente</a></li><li><a href="/#marketing">Marketing</a></li><li><a href="/#skateparkuri">Skateparkuri</a></li><li><a href="/blog/" class="on">Blog</a></li><li><a href="/#contact">Contact</a></li>
    </ul>
    <div class="nr"><a class="btn" href="/#contact">Scrie-ne</a></div>
  </div>
</header>`;
export const fallbackFooter = `<footer><div class="wrap"><a class="brand" href="/" aria-label="Baier Solutions"><img src="/img/logo-lockup-white.svg" alt="Baier Solutions" style="height:64px" width="2060" height="776"></a><span>© ${new Date().getFullYear()} Baier Solutions SRL, Hărman, Brașov · CUI RO33270728</span><span>Calitatea unui atelier german, viteza unui start-up, grija unei afaceri de familie.</span></div></footer>`;
export const footerScript = `<script>(function(){var y=document.getElementById('y');if(y)y.textContent=new Date().getFullYear();var h=document.getElementById('hdr');if(!h)return;function s(){h.classList.toggle('solid',window.scrollY>24)}addEventListener('scroll',s,{passive:true});s();var b=document.getElementById('menubtn');if(b){b.addEventListener('click',function(){var o=h.classList.toggle('open');b.setAttribute('aria-expanded',o)})}})();</script>`;

// Blog-only styles on top of the home page's inline CSS (served as /blog/site-base.css).
export const extraCss = `body.blog{padding-top:64px}body.blog .lang{display:none}
.bwrap{max-width:1120px;margin:0 auto;padding:0 var(--g)}.bnarrow{max-width:760px;margin:0 auto;padding:0 var(--g)}
.bhero{padding:clamp(40px,6vw,72px) 0 24px;border-bottom:1px solid var(--line)}.bhero .k{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--cyan);font-weight:600;margin-bottom:12px}.bhero h1{font-size:clamp(34px,5vw,58px);max-width:18ch}.bhero p{color:var(--muted);max-width:60ch;margin-top:14px;font-size:18px}
.bgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;padding:36px 0 64px}
.bcard{display:flex;flex-direction:column;text-decoration:none;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:hidden;transition:transform .2s,border-color .2s}.bcard:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.4)}
.bcard img{width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;display:block}.bcard .t{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}.bcard .k{font-size:12px;color:var(--muted);letter-spacing:.06em}.bcard h3{font-size:18px;font-weight:600;line-height:1.3}.bcard p{color:var(--muted);font-size:15px;line-height:1.5}.bcard .k.b{margin-top:auto;padding-top:8px}
.crumbs{font-size:13px;color:var(--muted);padding:28px 0 16px}.crumbs a{text-decoration:none}.crumbs a:hover{color:#fff}
.post h1{font-size:clamp(32px,4.6vw,52px);max-width:22ch;margin:6px 0 14px}.post .lead{font-size:20px;color:#d4d4d4;line-height:1.5;margin:0 0 18px}
.pmeta{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--muted);margin:0 0 26px}
.cover{margin:0 0 32px;border-radius:8px;overflow:hidden;background:#000}.cover img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block}.cover figcaption,.prose figcaption{font-size:12px;color:var(--muted);padding:8px 2px 0}
.prose{font-size:18px;line-height:1.7;color:#e4e4e7}.prose h2{font-size:clamp(23px,2.6vw,30px);margin:44px 0 14px;line-height:1.15}.prose h3{font-size:20px;margin:30px 0 10px}.prose p{margin:0 0 18px}.prose ul,.prose ol{padding-left:1.3em;margin:0 0 18px}.prose li{margin:0 0 6px}
.prose a{color:#fff;text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(34,211,238,.6)}.prose a:hover{text-decoration-color:var(--cyan)}
.prose figure{margin:28px 0 6px}.prose figure img{width:100%;height:auto;border-radius:8px;display:block}.prose .credit{font-size:13px;color:var(--muted);margin:0 0 22px}.prose strong{font-weight:600;color:#fff}
.prose details{border-top:1px solid var(--line);padding:14px 0}.prose details:last-of-type{border-bottom:1px solid var(--line)}.prose summary{cursor:pointer;font-weight:600;color:#fff}.prose details p{margin:10px 0 0;color:var(--muted)}
.ctabox{margin:44px 0 0;padding:24px 26px;border:1px solid var(--line);border-left:3px solid var(--cyan);border-radius:8px;background:var(--panel)}.ctabox h2{font-size:22px;margin:0 0 8px}.ctabox p{color:var(--muted);margin:0 0 16px}
.origin{font-size:13px;color:var(--muted);margin:28px 0 0;padding-top:14px;border-top:1px solid var(--line)}.origin a{color:#fff}
.ptags{display:flex;gap:8px;flex-wrap:wrap;margin:36px 0 0}.ptags span{font-size:12px;letter-spacing:.06em;border:1px solid var(--line);border-radius:999px;padding:5px 11px;color:var(--muted)}
.related{border-top:1px solid var(--line);margin-top:48px;padding-top:36px}.related h2{font-size:22px;margin:0}
.pager{display:flex;justify-content:center;gap:8px;padding:0 0 64px}.pager a,.pager span{font-size:14px;padding:10px 14px;border:1px solid var(--line);border-radius:6px;text-decoration:none}.pager span[aria-current]{border-color:var(--cyan);color:var(--cyan)}
@media (prefers-reduced-motion:no-preference){.rise{opacity:0;transform:translateY(10px);animation:rise .5s cubic-bezier(.2,.7,.2,1) forwards}.rise:nth-child(2){animation-delay:.06s}.rise:nth-child(3){animation-delay:.12s}.rise:nth-child(4){animation-delay:.18s}@keyframes rise{to{opacity:1;transform:none}}}`;

export function head({ title, description, canonical, ogImage, ogType, jsonld, noindex }) {
  return `<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${title}</title>
<meta name="description" content="${description}">
<link rel="canonical" href="${canonical}">
<meta name="robots" content="${noindex ? 'noindex, follow' : 'index, follow, max-image-preview:large'}">
<meta property="og:type" content="${ogType}">
<meta property="og:site_name" content="Baier Solutions">
<meta property="og:locale" content="ro_RO">
<meta property="og:url" content="${canonical}">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:image" content="${ogImage}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A0A0B">
<link rel="alternate" type="application/rss+xml" title="Blog Baier Solutions" href="https://baiersolutions.ro/blog/feed.xml">
${jsonld}
<link rel="icon" href="/img/app-icon.svg" type="image/svg+xml">
<link rel="icon" href="/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="stylesheet" href="/blog/site-base.css">
<link rel="stylesheet" href="/blog/blog.css">
</head>
<body class="lang-ro blog">
`;
}

export function card(p, h) {
  return `<a class="bcard rise" href="/blog/${p.slug}/">${h.img(p.cover_image_url, p.cover_image_alt || p.title, 720, 'loading="lazy"')}<div class="t"><span class="k">${h.esc((p.tags || [])[0]?.replace(/-/g, ' ') || 'Blog')}</span><h3>${h.esc(p.title)}</h3><p>${h.esc(p.excerpt || p.meta_description || '')}</p><span class="k b">${h.dateRo(p.published_at)} · ${h.readMin(p.body_md)} min</span></div></a>`;
}

export function listPage({ posts, title, h1, description, eyebrow, page, pages, pathFor }, h) {
  const pager = pages > 1 ? `<nav class="pager" aria-label="Pagini">${Array.from({ length: pages }, (_, i) => i + 1).map(n => n === page ? `<span aria-current="page">${n}</span>` : `<a href="${pathFor(n)}">${n}</a>`).join('')}</nav>` : '';
  return `<main>
<section class="bhero"><div class="bwrap"><div class="k">${h.esc(eyebrow)}</div><h1>${h.esc(h1)}</h1><p>${h.esc(description)}</p></div></section>
<section class="bwrap"><div class="bgrid">${posts.map(p => card(p, h)).join('')}</div>${pager}</section>
</main>`;
}

export function postPage({ p, bodyHtml, canonical, isSecondary, related, canonicalHost }, h) {
  const faq = (p.faq || []).length ? `<h2>Întrebări frecvente</h2>${p.faq.map(f => `<details><summary>${h.esc(f.q)}</summary><p>${h.esc(f.a)}</p></details>`).join('')}` : '';
  return `<main>
<article class="post">
<div class="bnarrow">
  <nav class="crumbs" aria-label="Navigare"><a href="/">Baier Solutions</a> › <a href="/blog/">Blog</a> › <span>${h.esc(p.title)}</span></nav>
  <div class="bhero" style="padding:0 0 22px;border:0"><div class="k">${h.esc((p.tags || [])[0]?.replace(/-/g, ' ') || 'Blog')}</div><h1>${h.esc(p.title)}</h1>${p.excerpt ? `<p class="lead">${h.esc(p.excerpt)}</p>` : ''}</div>
  <div class="pmeta"><span>${h.esc(p.author || 'Baier Solutions')}</span><time datetime="${h.esc(p.published_at)}">${h.dateRo(p.published_at)}</time><span>${h.readMin(p.body_md)} min de citit</span></div>
  ${p.cover_image_url ? `<figure class="cover">${h.img(p.cover_image_url, p.cover_image_alt || p.title, 1400, 'fetchpriority="high" decoding="async"')}<figcaption>${h.esc(p.cover_image_alt || '')}${p.images?.[0]?.credit ? ` · Foto: ${h.esc(p.images[0].credit)}` : ''}</figcaption></figure>` : ''}
  <div class="prose">${bodyHtml}${faq}</div>
  ${(p.tags || []).length ? `<div class="ptags">${p.tags.map(t => `<span>${h.esc(t.replace(/-/g, ' '))}</span>`).join('')}</div>` : ''}
  <aside class="ctabox"><h2>Un proiect pe care nimeni nu vrea să îl ia?</h2><p>Utilaje, evenimente, marketing, skateparkuri: scrieți-ne două rânduri și revenim cu un plan.</p><a class="btn" href="/#contact">Scrie-ne</a></aside>
  ${isSecondary ? `<p class="origin">Publicat original pe <a href="${h.esc(canonical)}">${h.esc(canonicalHost)}</a>.</p>` : ''}
</div>
${related.length ? `<section class="related"><div class="bwrap"><h2>Citiți și</h2><div class="bgrid">${related.map(r => card(r, h)).join('')}</div></div></section>` : ''}
</article>
</main>`;
}

export function latestBlock(posts, h) {
  return `<section class="bl" id="blog">
  <div class="wrap">
    <div class="bl-head"><span class="bl-k">Blog</span><h2>Din blog</h2><p>Menzi Muck în lume și în România, evenimente, marketing — povestite scurt. <a href="/blog/">Toate articolele</a>.</p></div>
    <div class="bl-grid">${posts.slice(0, 3).map(p => `<a class="bl-card" href="/blog/${p.slug}/">${h.img(p.cover_image_url, p.cover_image_alt || p.title, 720, 'loading="lazy"')}<span class="bl-t"><span class="bl-d">${h.dateRo(p.published_at)}</span><span class="bl-h">${h.esc(p.title)}</span></span></a>`).join('')}</div>
  </div>
</section>`;
}
