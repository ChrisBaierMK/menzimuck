# menzimuck.ro — Baier Solutions SRL

Site static (HTML/CSS, ~40 linii JS). Structură tip spacex.com: panouri full-bleed, text jos-stânga, nav subțire, butoane conturate.

## Deploy
Drag-and-drop folderul (sau zip-ul) în Netlify → site nou "menzimuck". Apoi: Domain settings → add menzimuck.ro; Forms → enable notifications pe e-mail pentru formularul "oferta".

## Fișiere
- `build.py` — TOATE datele (modele, specificații, domenii, accesorii, texte, telefon, e-mail). Editezi, rulezi `python3 build.py`, se regenerează paginile.
- `css/site.css` — stil. `DESIGN.md` — regulile de design.
- `images/` — 32 fotografii oficiale Menzi Muck AG + `logo.svg` (vectorul original). Hero = fotografia M545x pe traseul conductei la răsărit (`images/m545x-2.jpg`, `HERO_IMG` în build.py). Filmul 4K (225 MB) nu se mai încarcă: dacă vrei film peste poză, cere de la Rüthi un cut 1080p de ~10 MB, pune-l ca `images/hero.mp4` și setează `HERO_VIDEO = "/images/hero.mp4"`. Header: logo Menzi Muck negativ (`images/logo-neg.svg`) + logo Baier Solutions (`images/baier-solutions.svg`) + „Importator oficial România și Republica Moldova”.

## De confirmat înainte de lansare
1. Garanția (corectat 17.10.2026): 24 luni / 1.500 ore, oricare intervine prima; extensie la cerere contra cost la 36 luni, max. 2.000 ore.
2. E-mail de contact: christoph@baiersolutions.ro — schimbă dacă faci info@menzimuck.ro.
3. Confirmarea scrisă de la Menzi Muck AG pentru marcă + fotografii pe menzimuck.ro (footer-ul deja spune "folosite cu acordul acesteia").
