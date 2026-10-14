# Blog — how it works

The blog pages under `/blog/` are generated from the shared Supabase store (`blog_posts`), never edited by hand.

- `node scripts/build-blog.mjs --site <menzimuck|baiersolutions> --src . --out .` regenerates `blog/`, merges the blog URLs
  into `sitemap.xml`, writes `blog/feed.xml`, `blog/latest.json`, and fills the block between
  `<!-- blog-latest:start -->` and `<!-- blog-latest:end -->` in `index.html` with the three latest posts.
- Netlify runs it on every deploy (`netlify.toml`) and the Supabase trigger `blog_posts_notify_build` pings the
  site's build hook whenever a post is published or changed, so new posts appear by themselves.
- Environment variables (set in Netlify → Site configuration → Environment variables): `BLOG_SITE`, `SUPABASE_URL`,
  `SUPABASE_KEY` (publishable key; row-level security exposes only published posts).
- Templates: `templates/<site>.mjs` — the blog reuses the site's own header, footer and CSS (read from `index.html`
  at build time), so a change to the site's navigation is picked up automatically.
- Routing: baiersolutions.ro carries every post; menzi-muck.ro only posts tagged `menzi-muck`. Posts shown on both
  carry `rel=canonical` to menzi-muck.ro.
