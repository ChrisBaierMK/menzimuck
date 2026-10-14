# menzi-muck.ro — SEO plan (14 Oct 2026)

## 1. What the research showed
Source: Google RO autocomplete + live Google RO SERPs, 14 Oct 2026.

| Query | What ranks today | Opportunity |
|---|---|---|
| excavator păianjen / paianjen / tip păianjen | **Only marketplaces**: Machineryline, MachineryZone, OLX, Via-Mobilis, Truck1, Machinerypark. No dealer, no brand page. | **Main target.** A dealer pillar page can take #1–3. |
| excavator pășitor | Zero autocomplete. Nobody searches it. | Secondary term only. Site copy switched to "păianjen". |
| menzi muck (+ m545x, a25, m2, a20, m220, 445, preț, romania, second hand) | menzimuck.com, Machineryline, menzimuck.eu (Czech dealer), **best-tools.ro** (a Romanian site with a Menzi Muck product page) | Model pages now titled with the exact model codes people type. Check who best-tools.ro is — a reseller using the brand. |
| închiriere excavator păianjen | Generic rental sites, one Menzi rental ad on OLX | Almost no supply → article targets it; rental could be a business line. |
| excavator pentru pante abrupte | Nothing relevant; a rental blog says tracked excavators max ~35° | Comparison article owns this angle (35° vs 45°). |
| utilaje forestiere (de vânzare, brașov, second hand) | Broad forestry demand | Forestry article; future: forestry landing page. |
| kaiser (spider/walking excavator, s8, s12), euromach | Competitor brand searches | Comparison article captures them. |

## 2. Implemented (live)
- Terminology: "excavator păianjen" in every title, H1, hero and nav; "pășitor" kept as synonym.
- Pillar page `/excavator-paianjen/` — definition, how it works, uses, full range table, price, rent vs buy, model chooser, 5-question FAQ (FAQPage schema).
- 7 guide articles under `/ghid/`: price 2026 (real market data), păianjen vs șenile, rent vs buy, albii/hidro, forestier, Menzi vs Kaiser vs Euromach, second-hand checklist. Each links to models, pillar, contact, and 3 related articles.
- Model pages titled "Menzi Muck M545x, M535x, M525x — excavator păianjen" (exact autocomplete codes) + Product schema per model.
- Homepage: Organization + WebSite schema, guide section linking 6 articles.
- Every page: canonical, OG/Twitter tags, absolute OG image, robots meta; `/multumim.html` noindex.
- `sitemap.xml` (14 URLs) + `robots.txt`.
- Canonical domain: **menzi-muck.ro**. When menzimuck.ro is fixed at ROTLD: change `BASE` in build.py, rebuild, add menzimuck.ro as primary in Netlify — old URLs 301 automatically.

## 3. Do this week (needs your logins — 30 min total)
1. **Google Search Console** → add property `https://menzi-muck.ro` → verify via *HTML file* (I'll add the file to the site) → submit `sitemap.xml`. Without this, Google may take weeks to find the pages.
2. **Google Business Profile** → "Baier Solutions — Menzi Muck România", category *Construction equipment supplier*, Hărman, phone, website menzi-muck.ro. This is what ranks for "menzi muck românia" on Maps.
3. **Bing Webmaster Tools** → import from Search Console (one click).

## 4. Link building — ranked by value
Rule: every link must come from a real relationship or a real listing. No bought links, no PBNs — in a niche this small, one bad link pattern costs more than ten good links bring.

| # | Target | Why it matters | Ask |
|---|---|---|---|
| 1 | **menzimuck.com dealer locator** (Standorte) | Highest-authority link possible, from the brand itself | Ask Rüthi to list Baier Solutions for Romania with link to menzi-muck.ro |
| 2 | **Machineryline / MachineryZone / Truck1 / Machinerypark dealer profiles** | They own the SERP today — be the dealer inside their pages | Create a dealer profile with website link; list every used/demo machine |
| 3 | **baiersolutions.ro** | Your own site, already live | Menzi Muck domain block links to menzi-muck.ro (I'll add it) |
| 4 | **OLX + Via-Mobilis listings** | Where buyers browse | Each listing ends with "Detalii: menzi-muck.ro" |
| 5 | **RET Utilaje** (existing customer) | Customer link = trust | Ask for a "Menzi Muck prin Baier Solutions" mention + link |
| 6 | **Trade media**: Revista Construcțiilor, Monitorul Construcțiilor, Agro & forestry press | Editorial links | Pitch: "Primul distribuitor dedicat de excavatoare păianjen din România" + photos |
| 7 | **Associations**: ARACO (construction contractors), ASFOR (forestry) | Directory + member pages | Membership or partner listing |
| 8 | **Business directories**: ListaFirme, Daibau.ro, Firme.info, Cylex | Citation consistency for Maps | Same name/address/phone everywhere |
| 9 | **YouTube**: Romanian-language video of a Menzi Muck working (RET's machine) | Video results show on "menzi muck" SERP | Film one job, link site in description |

## 5. Outreach drafts

**To Menzi Muck AG (German)**
> Betreff: Händlereintrag Rumänien – Baier Solutions SRL
>
> Guten Tag,
> wir haben für den rumänischen Markt die Website menzi-muck.ro gestartet (Produktseiten aller Schreitbagger auf Rumänisch, Ratgeber, Anfrageformular). Könnten Sie Baier Solutions SRL im Händlerverzeichnis auf menzimuck.com unter Rumänien mit Link auf https://menzi-muck.ro eintragen?
> Gleichzeitig bitten wir um eine schriftliche Bestätigung, dass wir Logo und Bildmaterial von menzimuck.com auf der Website verwenden dürfen, sowie um eine komprimierte 1080p-Version des Imagefilms.
> Freundliche Grüße, Christoph Baier

**To trade press (Romanian)**
> Subiect: Excavatoarele păianjen Menzi Muck au distribuitor oficial în România
>
> Bună ziua,
> Baier Solutions SRL din Hărman (Brașov) este distribuitorul oficial Menzi Muck AG pentru România — producătorul elvețian care a inventat excavatorul păianjen în 1966. Utilajele lucrează pe pante de până la 45°, în albii și în pădure, unde excavatoarele clasice nu ajung. Am lansat menzi-muck.ro, cu ghiduri practice pentru antreprenori (preț, comparații, lucrări hidrotehnice și forestiere). Vă putem pune la dispoziție fotografii și o vizită la un utilaj în lucru.
> Cu stimă, Christoph Baier, +40 723 675 581

**To RET Utilaje (Romanian)**
> Bună ziua, am lansat menzi-muck.ro. Dacă vă ajută la propriile vânzări, putem prezenta M220-ul vostru ca studiu de caz (cu link către voi), iar voi ne menționați ca furnizor cu link către site. Mulțumesc!

## 6. Next 8 articles (one per week keeps the site growing)
1. Menzi Muck M545x — test complet (target: "menzi muck m545x")
2. Menzi Muck A20 vs A25 (target: "menzi muck a20", "a25")
3. Excavator păianjen pentru microhidrocentrale
4. Transportul unui excavator păianjen: trailer, autorizații, elicopter
5. Accesorii pentru excavator păianjen: tiltrotator, troliu, mulcher
6. Excavator păianjen pentru drumuri forestiere în Carpați
7. Studiu de caz: Menzi Muck M220 la RET Utilaje
8. Finanțare: leasing și fonduri pentru utilaje (AFIR, PNRR) — check open calls first

## 7. How we'll know it works
Search Console after 4–8 weeks: impressions for "excavator păianjen", "menzi muck romania", model codes. Target: top 3 for "excavator păianjen" and #1 for "menzi muck românia" within 3 months — the SERP has no dealer competing, so this is realistic, not hype.
