#!/usr/bin/env python3
# menzimuck.ro — static site generator. Edit data below, run: python3 build.py
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = "+40 723 675 581"
PHONE_HREF = "tel:+40723675581"
EMAIL = "christoph@baiersolutions.ro"
COMPANY = "Baier Solutions SRL"
# Hero: the M545x "pipeline at sunrise" photo. HERO_VIDEO = None shows the photo only;
# set it to a video URL (e.g. "/images/hero.mp4" once Rüthi sends a ~10 MB 1080p cut) and the
# film fades in over the photo. Menzi Muck's 4K image film (225 MB, too heavy to stream) is:
# https://menzimuck.com/wp-content/uploads/2023/09/Menzi%20Muck_Imagefilm_V3_4K.mp4
HERO_VIDEO = None
HERO_IMG = "m545x-2.jpg"
HERO_ALT = "Menzi Muck M545x pe traseul unei conducte, la răsărit"

def esc(s): return html.escape(s, quote=True)

HEAD = """<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="Menzi Muck România">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimg}">
<meta property="og:type" content="{ogtype}">
<meta name="twitter:card" content="summary_large_image">
{jsonld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Menzi Muck România — Baier Solutions, importator oficial România și Republica Moldova">
      <img class="mm" src="/images/logo-neg.svg" alt="Menzi Muck" width="92" height="36">
      <img class="bs" src="/images/baier-solutions.svg" alt="Baier Solutions" width="80" height="30">
      <span class="by">Importator oficial<b>România și Republica Moldova</b></span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">Meniu</button>
    <ul id="menu">
      <li><a href="/#modele"{c_modele}>Modele</a></li>
      <li><a href="/excavator-paianjen/"{c_ghid}>Excavator păianjen</a></li>
      <li><a href="/#domenii">Domenii</a></li>
      <li><a href="/#versatilitate">Versatilitate</a></li>
      <li><a href="/ghid/">Ghid</a></li>
      <li><a href="/blog/"{c_blog}>Blog</a></li>
      <li><a href="/#despre">Despre</a></li>
    </ul>
    <a class="cta" href="/#contact">Cere ofertă</a>
  </div>
</header>
"""

FOOT = f"""
<footer>
  <div class="wrap">
    <div>{COMPANY} · Hărman, Brașov · CIF RO33270728</div>
    <ul>
      <li><a href="/excavator-paianjen/">Excavator păianjen</a></li>
      <li><a href="/m5x.html">M5x</a></li><li><a href="/m4x.html">M4x</a></li><li><a href="/m2.html">M2</a></li><li><a href="/a20-a25.html">A20 / A25</a></li>
      <li><a href="/ghid/">Ghid</a></li>
      <li><a href="/blog/">Blog</a></li>
    </ul>
    <ul>
      <li><a href="{PHONE_HREF}">{PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="https://menzimuck.com" rel="noopener">menzimuck.com</a></li>
      <li><a href="https://baiersolutions.ro" rel="noopener">baiersolutions.ro</a></li>
    </ul>
    <div class="legal">© 2026 {COMPANY}, importator oficial Menzi Muck AG (Rüthi, Elveția) pentru România și Republica Moldova. Menzi Muck® este marcă înregistrată a Menzi Muck AG; fotografiile și materialele video sunt proprietatea Menzi Muck AG și sunt folosite cu acordul acesteia. Datele tehnice sunt orientative — configurația finală și prețul se stabilesc prin ofertă.</div>
  </div>
</footer>
<script>
(function(){{var n=document.getElementById('nav');function s(){{n.classList.toggle('solid',window.scrollY>40)}}addEventListener('scroll',s,{{passive:true}});s();
var v=document.querySelector('.hero video');if(v){{v.addEventListener('canplay',function(){{v.classList.add('ready')}});if(matchMedia('(prefers-reduced-motion: reduce)').matches||(navigator.connection&&navigator.connection.saveData)){{v.remove()}}else{{v.play().catch(function(){{}})}}}}
var r=document.querySelector('.rail');document.querySelectorAll('[data-rail]').forEach(function(b){{b.addEventListener('click',function(){{r.scrollBy({{left:(b.dataset.rail==='next'?1:-1)*Math.min(r.clientWidth*.8,460),behavior:'smooth'}})}})}});
}})();
</script>
</body>
</html>
"""

# ---------------- DATA (source: menzimuck.com, Oct 2026) ----------------
SERIES = [
 dict(slug="m5x", name="M5x", kg="de la 12.400 kg", tagline="Clasa grea pentru pante extreme", hero="m545x-2.jpg", gallery=["m545x.jpg","m545x-3.jpg","m525x-2.jpg"],
  lead="Seria M5x lucrează în siguranță pe pante de până la 45° în linia de cădere și 30° în linia de nivel, cu șasiul patentat Menzi Muck pe bază X. Ecartamentul se deschide până la 6 metri — o stabilitate pe care un excavator clasic de 13 tone nu o are. Motor Deutz de 156 CP, hidraulică load-sensing Rexroth, intervale de service de 500 de ore.",
  tech=[("Motor","Deutz turbo diesel, 4 cilindri — 115 kW / 156 CP"),("Cilindree","4.038 cm³"),("Instalație electrică","24 V"),("Demaror","4,0 kW"),("Interval service","500 h"),("Sistem hidraulic","Load Sensing by Rexroth"),("Pompă de lucru","290 l/min · 300 bar"),("Pompă deplasare","210 l/min · 400 bar"),("Powerline (opțional)","220 l/min"),("Viteză de rotire","până la 10 rot/min")],
  models=[
   dict(code="M545x", kg="de la 13.500 kg", img="m545x.jpg", feats=["Transmisie continuă Vx-Drive by Menzi, până la 15 km/h","Sprijin paralel P-Vation by Menzi","Patru roți de aceeași mărime, lățime până la 800 mm","Suporturi de pantă față și/sau spate (opțional)"]),
   dict(code="M535x", kg="de la 13.000 kg", img="m535x.jpg", feats=["Transmisie continuă Vx-Drive by Menzi, până la 11 km/h","Sprijin paralel P-Vation by Menzi","Reglare hidraulică a înălțimii roților directoare","Sprijin telescopic hidraulic"]),
   dict(code="M525x", kg="de la 12.400 kg", img="m525x.jpg", feats=["Transmisie continuă Vx-Drive by Menzi, până la 15 km/h","Două punți detașabile cu roți de rulare","Sprijin telescopic hidraulic"]),
  ]),
 dict(slug="m4x", name="M4x", kg="de la 10.600 kg", tagline="Forță mare, greutate mică", hero="m4x.jpg", gallery=["m4x-2.jpg","m4x-3.jpg","hero.jpg"],
  lead="Șasiul patentat pe bază X al seriei M4x combină stabilitate, mobilitate și un centru de greutate optimizat. Reglarea paralelă a roților pe orizontală și pe verticală ține mașina stabilă pe orice teren. Cilindrul de braț montat sus ridică forța de împingere — esențială la un pășitor — la peste 200 % față de generația anterioară. Motor Deutz de 143 CP, hidraulică I-Control by Menzi Muck.",
  tech=[("Motor","Deutz turbo diesel, 4 cilindri — 105 kW / 143 CP"),("Cilindree","3.621 cm³"),("Instalație electrică","24 V"),("Demaror","4,0 kW"),("Interval service","500 h"),("Sistem hidraulic","I-Control by Menzi Muck"),("Pompă de lucru","260 l/min · 300 bar"),("Pompă deplasare","180 l/min · 400 bar"),("Powerline (opțional)","150 l/min"),("Viteză de rotire","până la 10 rot/min")],
  models=[
   dict(code="M445x", kg="de la 11.500 kg", img="m4x.jpg", feats=["Tracțiune integrală hidrostatică Menzi H-Drive","Sprijin paralel P-Vation by Menzi Muck","Patru roți de aceeași mărime, lățime până la 710 mm","Suporturi de pantă față și/sau spate (opțional)"]),
   dict(code="M435x", kg="de la 11.400 kg", img="m4x-2.jpg", feats=["Tracțiune integrală hidrostatică Menzi H-Drive","Sprijin paralel P-Vation by Menzi","Reglare hidraulică a înălțimii roților directoare","Sprijin telescopic hidraulic"]),
   dict(code="M425x", kg="de la 10.600 kg", img="m4x-3.jpg", feats=["Transmisie hidrostatică Menzi","Două punți detașabile cu roți de rulare","Sprijin telescopic hidraulic"]),
  ]),
 dict(slug="m2", name="M2", kg="de la 7.100 kg", tagline="Se demontează și zboară", hero="m220-3.jpg", gallery=["m220.jpg","m220-2.jpg","dsc.jpg"],
  lead="M2 se descompune în câțiva pași în pachete pentru transport cu elicopterul, telecabina sau macaraua — dispozitive ajutătoare integrate fac demontarea rapidă pe teren. Este alternativa economică pentru lucrări unde nu ajunge niciun alt utilaj: albii de râu, versanți, trasee de cablu, zone fără drum de acces. Motor Deutz de 75 CP conform celor mai noi norme de emisii.",
  tech=[("Motor","Deutz turbo diesel, 4 cilindri — 55 kW / 75 CP"),("Cilindree","2.900 cm³"),("Instalație electrică","12 V"),("Interval service","500 h"),("Sistem hidraulic","Load Sensing by Rexroth"),("Pompă de lucru","230 l/min · 280 bar"),("Pompă deplasare","60 l/min · 250 bar"),("Viteză de rotire","până la 9 rot/min")],
  models=[
   dict(code="M220", kg="de la 7.100 kg", img="m220.jpg", feats=["Transmisie în două trepte cu direcție paralelă autoreglabilă","Două punți detașabile cu roți de rulare","Sprijin telescopic hidraulic","Demontabil pentru transport cu elicopter / telecabină / macara"]),
  ]),
 dict(slug="a20-a25", name="A20 / A25", kg="de la 2.000 kg", tagline="Ușor, dar merge peste tot", hero="a20.jpg", gallery=["a20-2.jpg","a25.jpg","a20.jpg"],
  lead="Cu o greutate de la 2 tone, A20 și A25 ajung practic pe orice teren și, ca și M2, se pretează transportului cu elicopterul. Două punți detașabile cu roți de rulare și sprijin telescopic mecanic. Pentru grădinărit, întreținere de maluri, intervenții în spații înguste și lucrări unde un utilaj mare nu încape.",
  tech=None,
  models=[
   dict(code="A20", kg="de la 2.000 kg", img="a20.jpg", feats=["Tracțiune hidrostatică pe cele două roți mari, până la 2,6 km/h","Două punți detașabile cu roți de rulare","Sprijin telescopic mecanic"],
        tech=[("Motor","Diesel Kubota — 15,8 kW / 21 CP"),("Cilindree","1.123 cm³"),("Instalație electrică","12 V"),("Demaror","1,0 kW"),("Rază minimă de rotire","1.750 mm"),("Viteză de rotire","9 rot/min")]),
   dict(code="A25", kg="de la 2.300 kg", img="a25.jpg", feats=["Tracțiune hidrostatică pe cele două roți mari, până la 2,6 km/h","Două punți detașabile cu roți de rulare","Sprijin telescopic mecanic"],
        tech=[("Motor","Diesel Kubota — 18,5 kW / 25 CP"),("Cilindree","1.305 cm³"),("Instalație electrică","12 V"),("Demaror","1,0 kW"),("Rază minimă de rotire","1.790 mm"),("Viteză de rotire","9 rot/min")]),
  ]),
]

DOMAINS = [
 dict(t="Construcții și fundații speciale", img="hero.jpg",
  p="Taluzuri, drumuri de munte, fundații pe versant, lucrări de consolidare. Un Menzi Muck stă orizontal acolo unde un excavator pe șenile nu poate fi nici măcar adus.",
  li=["Fundații speciale pe pantă","Drumuri și platforme în zone montane","Consolidări de versanți și ziduri de sprijin"]),
 dict(t="Hidro și amenajări de albii", img="m535x-2.jpg",
  p="Lucrează din albia râului, de pe mal sau de pe un dig. Picioarele se reglează independent, mașina stă în apă fără să-și piardă stabilitatea, brațul ajunge unde nu ajunge nimeni.",
  li=["Regularizări de albii și apărări de mal","Baraje, microhidrocentrale, prize de apă","Intervenții după inundații"]),
 dict(t="Forestier", img="forest-2.jpg",
  p="Exploatare pe pantă cu cap harvester, mulcher forestier sau graifer-fierăstrău. Drumuri forestiere, curățare de parcele, lucrări în zone fără acces pentru utilaj greu.",
  li=["Cap harvester Konrad, MVD Greifersäge","Mulcher forestier Seppi, freză de cioate FSI","Drumuri forestiere și platforme de depozitare"]),
 dict(t="Utilități și infrastructură", img="m525x-2.jpg",
  p="Trasee de cablu, conducte și stâlpi în zone inaccesibile: munte, pădure, pantă. M2 și A20/A25 se demontează și zboară cu elicopterul direct la punctul de lucru.",
  li=["Trasee de cablu electric și fibră optică","Conducte de apă și gaz pe teren accidentat","Fundații pentru stâlpi și instalații de telecabină"]),
 dict(t="Feroviar", img="m545x-3.jpg",
  p="Întreținerea taluzurilor și a șanțurilor de-a lungul căii ferate, defrișări de vegetație, lucrări la rambleu — fără a bloca linia și fără utilaj feroviar specializat.",
  li=["Curățare de vegetație și taluzuri","Șanțuri și drenaje de-a lungul liniei","Intervenții la alunecări de teren"]),
 dict(t="Municipal și spații verzi", img="a25.jpg",
  p="Întreținere de pante, maluri și spații verzi, lucrări de grădinărit peisagistic, demolări controlate în spații înguste și intervenții de urgență după dezastre naturale.",
  li=["Întreținere pante și maluri de lac","Peisagistică și amenajări cu A20 / A25","Intervenții la dezastre naturale"]),
]

ATTACH = [
 dict(t="Cupe", s="Cupă de săpat, cupă pentru tiltrotator, cupă de humus (și hidraulică), cupă de sortare — proiectate și fabricate la Menzi Muck.", img="a20-2.jpg"),
 dict(t="Graifere", s="Graifer universal pentru piatră, buștean și materiale în vrac, construit în casă pentru forțele unui excavator păianjen.", img="m4x-3.jpg"),
 dict(t="Tiltrotatoare și cuple rapide", s="Tiltrotator Oilquick sau Rototilt, cap rotativ Powertilt, cuplă rapidă hidraulică — schimbi accesoriul fără să cobori din cabină.", img="rototilt.jpg"),
 dict(t="Trolii", s="Troliu de cablu pentru lucrări pe pante extreme, extragere de buștean și asigurarea mașinii.", img="winch.jpg"),
 dict(t="Demolare și excavare", s="Ciocan hidraulic și sisteme de demolare — Powerline până la 220 l/min alimentează accesorii pe care un excavator clasic nu le poate susține.", img="m220-3.jpg"),
 dict(t="Municipal și forestier", s="Cap harvester, mulcher forestier, freză de cioate, graifer-fierăstrău — un singur utilaj pentru întreaga lucrare.", img="forest.jpg"),
]

def img(name, alt="", cls="", lazy=True, attrs=""):
    l = ' loading="lazy"' if lazy else ''
    c = f' class="{cls}"' if cls else ""
    a = f' {attrs}' if attrs else ""
    return f'<img src="/images/{name}" alt="{esc(alt)}"{c}{l}{a}>'

def spec_table(rows, caption="Date tehnice"):
    tr = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k,v in rows)
    return f'<table class="spec"><caption>{caption}</caption>{tr}</table>'

def series_nav(active):
    a = "".join(f'<a href="/{s["slug"]}.html"{" aria-current=page" if s["slug"]==active else ""}>Menzi Muck {esc(s["name"])}</a>' for s in SERIES)
    return f'<nav class="series-nav">{a}</nav>'

BASE = "https://menzimuck.ro"   # switch to https://menzimuck.ro once that domain is live at ROTLD
ORG = {"@type":"Organization","@id":BASE+"/#org","name":COMPANY,"alternateName":"Menzi Muck România","url":BASE+"/",
       "logo":BASE+"/images/logo.svg","telephone":PHONE,"email":EMAIL,"vatID":"RO33270728",
       "address":{"@type":"PostalAddress","addressLocality":"Hărman","addressRegion":"Brașov","addressCountry":"RO"},
       "areaServed":["RO","MD"],"knowsLanguage":["ro","de","en"],
       "brand":{"@type":"Brand","name":"Menzi Muck"},"sameAs":["https://menzimuck.com"]}
import json as _json
def ld(*objs):
    return "".join('<script type="application/ld+json">'+_json.dumps({"@context":"https://schema.org",**o},ensure_ascii=False)+'</script>' for o in objs)
def crumbs(*items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}
def page_head(title, desc, c_modele="", path="/", jsonld="", ogimg=None, ogtype="website", c_ghid="", c_blog=""):
    return HEAD.format(title=esc(title), desc=esc(desc), c_modele=c_modele, c_ghid=c_ghid, c_blog=c_blog, canonical=BASE+path,
                       ogimg=BASE+"/images/"+(ogimg or HERO_IMG), ogtype=ogtype, jsonld=jsonld)

# ---------------- INDEX ----------------
def build_index():
    cards = "".join(f"""<a class="card" href="/{s['slug']}.html#{m['code'].lower()}">{img(m['img'],'Menzi Muck '+m['code'],lazy=False)}
  <div class="t"><div class="code">{esc(m['code'])}</div><div class="kg">{esc(m['kg'])}</div><span class="more">Fișa tehnică</span></div></a>""" for s in SERIES for m in s["models"])

    domains = "".join(f"""<article class="domain">
  <div class="img">{img(d['img'], d['t'])}</div>
  <div class="txt"><div class="n">0{i+1}</div><h3>{esc(d['t'])}</h3><p>{esc(d['p'])}</p><ul>{''.join(f'<li>{esc(x)}</li>' for x in d['li'])}</ul></div>
</article>""" for i,d in enumerate(DOMAINS))

    attach = "".join(f"""<a href="/#contact">{img(a['img'], a['t'],lazy=False)}<div class="t"><h3>{esc(a['t'])}</h3><p>{esc(a['s'])}</p></div></a>""" for a in ATTACH)

    hero_video = (f'\n    <video muted loop playsinline preload="metadata" poster="/images/{HERO_IMG}" aria-hidden="true">'
                  f'<source src="{HERO_VIDEO}" type="video/mp4"></video>') if HERO_VIDEO else ""
    p = page_head("Excavator păianjen Menzi Muck | Importator oficial România",
        "Excavatoare păianjen (pășitoare) Menzi Muck: M545x, M445x, M220, A20, A25. Importator oficial pentru România și Republica Moldova — vânzare, livrare, instruire operator, service și piese.",
        path="/", jsonld=ld(ORG,{"@type":"WebSite","name":"Menzi Muck România","url":BASE+"/","inLanguage":"ro","publisher":{"@id":BASE+"/#org"}}))
    p += f"""
<section class="panel hero">
  <div class="media">
    {img(HERO_IMG,HERO_ALT,lazy=False,attrs='fetchpriority="high" width="1920" height="1440"')}{hero_video}
  </div>
  <div class="wrap">
    <div class="label rv">Importator oficial Menzi Muck · România și Republica Moldova</div>
    <h1 class="rv d1">Unde alții se opresc, noi abia începem.</h1>
    <p class="sub rv d2">Excavatoare păianjen elvețiene pentru pante, albii, pădure și tot ce nu poate atinge un utilaj pe șenile. Vânzare, livrare, instruire operator și service în România.</p>
    <div class="btn-row rv d3"><a class="btn solid" href="#modele">Vezi modelele</a><a class="btn" href="#contact">Cere ofertă</a></div>
  </div>
  <div class="scroll-hint" aria-hidden="true"></div>
</section>

<div class="strip"><div class="wrap">
  <div><b>45°</b><span>pantă în linia de cădere</span></div>
  <div><b>2–13,5 t</b><span>de la A20 la M545x</span></div>
  <div><b>1966</b><span>Menzi Muck AG, Rüthi, Elveția</span></div>
  <div><b>290 l/min</b><span>debit hidraulic de lucru</span></div>
</div></div>

<section class="text" id="de-ce">
  <div class="wrap">
    <div><div class="eyebrow">De ce un excavator păianjen</div><h2>Merge unde șenila nu are ce căuta.</h2></div>
    <div>
      <p class="lead">Un Menzi Muck își reglează fiecare roată și fiecare picior separat. Stă orizontal pe un versant, în albia unui râu sau lângă o cale ferată — și lucrează de acolo cu forțe de ridicare și rupere mai mari decât un excavator clasic din aceeași clasă de greutate.</p>
      <p>Șasiul patentat și brațul patentat pun la dispoziție un debit hidraulic mult mai mare pentru accesorii. O singură mașină înlocuiește utilaj greu, schele și, de multe ori, zile de lucru manual.</p>
      <div class="cells">
        <div><h3>Stabilitate</h3><p>Sprijin paralel P-Vation și ecartament reglabil până la 6 m pe M5x. Mașina stă, operatorul lucrează.</p></div>
        <div><h3>Mobilitate</h3><p>Transmisie Vx-Drive sau H-Drive, până la 15 km/h pe drum. M2 și A20/A25 se demontează pentru elicopter.</p></div>
        <div><h3>Hidraulică</h3><p>Până la 290 l/min la 300 bar pe pompa de lucru, Powerline suplimentar până la 220 l/min pentru accesorii.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="panel half" id="pante">
  <div class="media">{img('hero.jpg','Menzi Muck M4x în teren montan')}</div>
  <div class="wrap"><div class="label">Elveția, 1.800 m</div><h2>Unde alții se opresc, noi abia începem.</h2><p class="sub">Sloganul Menzi Muck nu e o figură de stil. Este descrierea exactă a locului de muncă.</p></div>
</section>

<section id="domenii">
  <div class="wrap sec-head"><div class="eyebrow">Domenii de activitate</div><h2>Un utilaj. Șase industrii.</h2><p>Oriunde terenul e prea abrupt, prea moale, prea îngust sau prea departe de drum pentru un excavator clasic.</p></div>
  <div class="domains">{domains}</div>
</section>

<section id="versatilitate">
  <div class="wrap sec-head"><div class="eyebrow">Versatilitate</div><h2>Programul de accesorii al clasei regale.</h2><p>Lucrări diferite cer unelte diferite. Puterea hidraulică a unui Menzi Muck duce și cele mai pretențioase accesorii. Cupele, cuplele rapide și graiferele sunt proiectate și fabricate la Menzi Muck; restul vin de la partenerii lor: Oilquick, Rototilt, Seppi, Konrad, FSI, MVD.</p></div>
  <div class="attach">{attach}</div>
  <div class="wrap hydro">
    <div><b>300 bar</b><span>presiune de lucru</span></div>
    <div><b>220 l/min</b><span>Powerline suplimentar pentru accesorii</span></div>
    <div><b>&gt;200 %</b><span>forță de împingere față de generația anterioară (M4x)</span></div>
  </div>
</section>

<section id="modele">
  <div class="wrap sec-head"><div class="eyebrow">Gama</div><h2>Nouă modele. Patru serii.</h2><p>De la 2 tone la 13,5 tone. Fiecare se configurează la Rüthi pentru lucrarea dumneavoastră.</p></div>
  <div class="rail-ctl"><button type="button" data-rail="prev" aria-label="Înapoi">←</button><button type="button" data-rail="next" aria-label="Înainte">→</button></div>
  <div class="rail">{cards}</div>
</section>

<section class="panel half" id="service">
  <div class="media">{img('used.jpg','Livrare Menzi Muck pe trailer')}</div>
  <div class="wrap"><div class="label">Service &amp; instruire</div><h2>De la vizita pe șantier la prima oră de lucru.</h2></div>
</section>
<section class="text" style="padding-top:72px">
  <div class="wrap" style="grid-template-columns:1fr">
    <div class="steps">
      <div><b>01 · Vizită și calcul</b><p>Venim pe șantier, vedem lucrarea și punem pe hârtie ce model și ce accesorii au sens pentru ea — cu un calcul de cost pe oră.</p></div>
      <div><b>02 · Configurare</b><p>Mașina se configurează la Rüthi exact pentru lucrarea dumneavoastră: roți, sprijin, cuplă rapidă, Powerline, accesorii.</p></div>
      <div><b>03 · Livrare și instruire</b><p>Livrăm în România și instruim operatorii pe mașina dumneavoastră. Garanție de până la 36 de luni / 2.000 de ore.</p></div>
      <div><b>04 · Service și piese</b><p>Piese de schimb originale și tehnicieni instruiți de echipa de ingineri Menzi Muck. Intervale de service la 500 de ore.</p></div>
    </div>
  </div>
</section>

<section class="panel half" id="despre">
  <div class="media">{img('poster.jpg','Rüthi, Elveția')}</div>
  <div class="wrap"><div class="label">Despre</div><h2>60 de ani de pionierat elvețian.</h2><p class="sub">Menzi Muck AG construiește excavatoare păianjen (pășitoare) din 1966 la Rüthi, în estul Elveției, și este liderul mondial al segmentului. Mașinile lucrează pe toate continentele.</p></div>
</section>
<section class="text" style="padding-top:72px">
  <div class="wrap">
    <div>{img('history.jpg','Menzi Muck 1966')}</div>
    <div>
      <p class="lead">{COMPANY} din Hărman, Brașov, este importatorul oficial Menzi Muck AG pentru România.</p>
      <p>Familia Baier vinde și pune în funcțiune mașini Menzi Muck în România de peste 20 de ani — cunoaștem utilajul, cunoaștem terenul și vorbim direct cu fabrica, în germană.</p>
      <p>Nu transportăm mașini pentru demonstrații; vă ducem să vedeți un Menzi Muck acolo unde lucrează deja și venim noi la lucrarea dumneavoastră cu un calcul concret.</p>
    </div>
  </div>
</section>

<section id="ghid">
  <div class="wrap sec-head"><div class="eyebrow">Ghid</div><h2>Tot ce trebuie să știi despre excavatorul păianjen.</h2><p>Preț, alegerea modelului, comparații și lucrări tipice — scrise de importatorul oficial.</p></div>
  <div class="wrap guide-grid">{{GUIDE_CARDS}}</div>
</section>

<!-- blog-latest:start -->
<!-- blog-latest:end -->

<section class="contact" id="contact">
  <div class="wrap">
    <div class="contact-side">
      <div class="eyebrow">Contact</div>
      <h2>Cere o ofertă.</h2>
      <p><b>Telefon</b><a href="{PHONE_HREF}">{PHONE}</a></p>
      <p><b>E-mail</b><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><b>Sediu</b>{COMPANY}<br>Hărman, jud. Brașov, România</p>
      <p><b>Limbi</b>Română · Deutsch · English</p>
    </div>
    <form name="oferta" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/multumim.html">
      <input type="hidden" name="form-name" value="oferta">
      <p hidden><label>Nu completați: <input name="bot-field"></label></p>
      <label>Nume și prenume<input name="nume" required autocomplete="name"></label>
      <label>Firmă<input name="firma" autocomplete="organization"></label>
      <label>Telefon<input name="telefon" type="tel" required autocomplete="tel"></label>
      <label>E-mail<input name="email" type="email" required autocomplete="email"></label>
      <label>Model de interes<select name="model"><option>Nu știu încă — vreau recomandare</option><option>M5x (M525x / M535x / M545x)</option><option>M4x (M425x / M435x / M445x)</option><option>M2 (M220)</option><option>A20 / A25</option><option>Mașină second-hand</option><option>Accesorii / piese</option></select></label>
      <label>Județul lucrării<input name="judet"></label>
      <label class="full">Descrieți lucrarea<textarea name="mesaj" placeholder="Tip de lucrare, pantă, acces, accesorii necesare, termen"></textarea></label>
      <button class="btn solid" type="submit">Trimite cererea</button>
    </form>
  </div>
</section>
""" + FOOT
    p = p.replace("{GUIDE_CARDS}", guide_cards([PILLAR]+ARTICLES[:5]))
    open(os.path.join(OUT,"index.html"),"w").write(p)

# ---------------- SERIES PAGES ----------------
def build_series():
    for s in SERIES:
        blocks = ""
        for m in s["models"]:
            feats = "".join(f"<li>{esc(x)}</li>" for x in m["feats"])
            tech = m.get("tech") or s["tech"]
            blocks += f"""
<article class="model" id="{m['code'].lower()}">
  <div class="wrap">
    <div>{img(m['img'],'Menzi Muck '+m['code'],'pic')}
      <h2>Menzi Muck {esc(m['code'])}</h2>
      <div class="kg">{esc(m['kg'])}</div>
      <ul class="chips">{feats}</ul>
      <a class="btn solid" href="/#contact">Cere ofertă pentru {esc(m['code'])}</a>
    </div>
    <div>{spec_table(tech)}</div>
  </div>
</article>"""
        gallery = "".join(img(g, f"Menzi Muck {s['name']}") for g in s["gallery"])
        codes = ", ".join(m["code"] for m in s["models"])
        prods = [{"@type":"Product","name":"Menzi Muck "+m["code"],"brand":{"@type":"Brand","name":"Menzi Muck"},
                  "manufacturer":{"@type":"Organization","name":"Menzi Muck AG"},"category":"Excavator păianjen",
                  "image":BASE+"/images/"+m["img"],"url":BASE+"/"+s["slug"]+".html#"+m["code"].lower(),
                  "description":f"Excavator păianjen Menzi Muck {m['code']}, {m['kg']}. "+"; ".join(m["feats"])} for m in s["models"]]
        p = page_head(f"Menzi Muck {codes} — excavator păianjen",
            f"Excavator păianjen Menzi Muck {codes}: {s['tagline'].lower()}, {s['kg']}. Date tehnice complete, dotări și ofertă de la importatorul oficial din România.",
            ' aria-current="page"', path="/"+s["slug"]+".html", ogimg=s["hero"], ogtype="product",
            jsonld=ld(crumbs(("Acasă","/"),("Excavator păianjen","/excavator-paianjen/"),("Menzi Muck "+s["name"],"/"+s["slug"]+".html")),*prods))
        p += f"""
<section class="panel">
  <div class="media">{img(s['hero'],'Menzi Muck '+s['name'],lazy=False)}</div>
  <div class="wrap">
    <div class="label rv">Excavator păianjen · Seria {esc(s['name'])}</div>
    <h1 class="rv d1">Menzi Muck {esc(s['name'])}</h1>
    <p class="sub rv d2">{esc(s['kg'])} · {esc(s['tagline'])}</p>
    <div class="btn-row rv d3"><a class="btn solid" href="#{s['models'][0]['code'].lower()}">Date tehnice</a><a class="btn" href="/#contact">Cere ofertă</a></div>
  </div>
</section>
{series_nav(s['slug'])}
<section class="text">
  <div class="wrap">
    <div><div class="eyebrow">Seria {esc(s['name'])}</div><h2>{esc(s['tagline'])}</h2></div>
    <div><p class="lead">{esc(s['lead'])}</p></div>
  </div>
</section>
<div class="gallery">{gallery}</div>
{blocks}
<section class="panel short center">
  <div class="media">{img('slope.jpg','')}</div>
  <div class="wrap"><h2>Vrei să-l vezi lucrând?</h2><p class="sub">Vă ducem la un Menzi Muck în lucru și venim pe șantierul dumneavoastră cu un calcul de cost pe oră pentru lucrarea concretă.</p>
  <p class="sub"><a href="/excavator-paianjen/" style="text-decoration:underline">Ce este un excavator păianjen și cum alegi modelul</a></p>
  <div class="btn-row"><a class="btn solid" href="/#contact">Programează o vizită</a><a class="btn" href="{PHONE_HREF}">{PHONE}</a></div></div>
</section>
""" + FOOT
        open(os.path.join(OUT, f"{s['slug']}.html"),"w").write(p)

def build_thanks():
    p = page_head("Mulțumim | Menzi Muck România", "Cererea a fost trimisă.", path="/multumim.html").replace('content="index,follow,max-image-preview:large"','content="noindex"')
    p += f"""
<section class="panel short center">
  <div class="media">{img('poster.jpg','')}</div>
  <div class="wrap"><div class="label">Cerere trimisă</div><h1>Mulțumim.</h1>
  <p class="sub">Vă sunăm în cel mult o zi lucrătoare. Dacă e urgent: {PHONE}.</p>
  <div class="btn-row"><a class="btn" href="/">Înapoi la site</a></div></div>
</section>
""" + FOOT
    open(os.path.join(OUT,"multumim.html"),"w").write(p)

# ---------------- SEO CONTENT ----------------
from content import PILLAR, ARTICLES, DATE
ALL = {a["slug"]:a for a in ARTICLES}

def art_url(a): return "/excavator-paianjen/" if a["slug"]==PILLAR["slug"] else f"/ghid/{a['slug']}/"

def guide_cards(items):
    return "".join(f"""<a class="gcard" href="{art_url(a)}">{img(a['img'], a['h1'])}<div class="t"><span>{esc(a['kicker'])}</span><h3>{esc(a['h1'])}</h3></div></a>""" for a in items)

def range_table():
    rows="".join(f"<tr><td><a href='/{s['slug']}.html#{m['code'].lower()}'>Menzi Muck {m['code']}</a></td><td>{m['kg']}</td><td>{(m.get('tech') or s['tech'])[0][1]}</td></tr>" for s in SERIES for m in s["models"])
    return f"<table class='data'><thead><tr><th>Model</th><th>Greutate</th><th>Motor</th></tr></thead><tbody>{rows}</tbody></table>"

def build_article(a, is_pillar=False):
    path = art_url(a)
    body = a["body"].replace("{RANGE_TABLE}", range_table())
    trail = [("Acasă","/")] + ([] if is_pillar else [("Ghid","/ghid/")]) + [(a["h1"], path)]
    objs = [crumbs(*trail), {"@type":"Article","headline":a["h1"],"description":a["desc"],"image":BASE+"/images/"+a["img"],
            "datePublished":DATE,"dateModified":DATE,"inLanguage":"ro","mainEntityOfPage":BASE+path,
            "author":{"@id":BASE+"/#org"},"publisher":ORG}]
    faq_html=""
    if a.get("faq"):
        objs.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":ans}} for q,ans in a["faq"]]})
        faq_html = "<h2>Întrebări frecvente</h2>" + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q,ans in a["faq"])
    bc = " / ".join(f'<a href="{u}">{esc(n)}</a>' if i<len(trail)-1 else f"<span>{esc(n)}</span>" for i,(n,u) in enumerate(trail))
    rel = [ALL[r] for r in a.get("related",[]) if r in ALL]
    p = page_head(a["title"], a["desc"], path=path, jsonld=ld(*objs), ogimg=a["img"], ogtype="article",
                  c_ghid=' aria-current="page"' if is_pillar else "")
    p += f"""
<section class="panel short art-hero">
  <div class="media">{img(a['img'], a['h1'], lazy=False)}</div>
  <div class="wrap"><div class="label rv">{esc(a['kicker'])}</div><h1 class="rv d1">{esc(a['h1'])}</h1></div>
</section>
<div class="wrap crumbs">{bc}</div>
<article class="wrap art">
  <div class="prose">{body}{faq_html}
    <p class="byline">Baier Solutions SRL — importator oficial Menzi Muck AG pentru România · actualizat {DATE[8:10]}.{DATE[5:7]}.{DATE[:4]}</p>
  </div>
  <aside class="art-cta">
    <div class="eyebrow">Ofertă</div>
    <h3>Calculul pentru lucrarea ta</h3>
    <p>Model, configurație și cost pe oră — gratuit, de la importatorul oficial.</p>
    <a class="btn solid" href="/#contact">Cere ofertă</a>
    <a class="btn" href="{PHONE_HREF}">{PHONE}</a>
    <ul>{''.join(f'<li><a href="/{s["slug"]}.html">Menzi Muck {esc(s["name"])}</a></li>' for s in SERIES)}</ul>
  </aside>
</article>
<section class="related">
  <div class="wrap sec-head" style="padding-top:64px"><div class="eyebrow">Citește și</div></div>
  <div class="wrap guide-grid">{guide_cards(rel)}</div>
</section>
""" + FOOT
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d,"index.html"),"w").write(p)

def build_hub():
    items=[PILLAR]+ARTICLES
    p = page_head("Ghid excavator păianjen: preț, modele, comparații",
        "Ghiduri practice despre excavatoarele păianjen: cât costă, cum alegi modelul, păianjen vs. șenile, închiriere sau cumpărare, lucrări în albii și în pădure.",
        path="/ghid/", jsonld=ld(crumbs(("Acasă","/"),("Ghid","/ghid/")),
          {"@type":"CollectionPage","name":"Ghid excavator păianjen","url":BASE+"/ghid/","hasPart":[{"@type":"Article","headline":a["h1"],"url":BASE+art_url(a)} for a in items]}))
    p += f"""
<section class="panel short art-hero">
  <div class="media">{img('forest-2.jpg','Ghid excavator păianjen', lazy=False)}</div>
  <div class="wrap"><div class="label rv">Ghid</div><h1 class="rv d1">Ghidul excavatorului păianjen</h1></div>
</section>
<div class="wrap guide-grid" style="padding:64px 0 120px">{guide_cards(items)}</div>
""" + FOOT
    os.makedirs(os.path.join(OUT,"ghid"),exist_ok=True)
    open(os.path.join(OUT,"ghid","index.html"),"w").write(p)

def build_sitemap():
    urls=[("/","1.0"),("/excavator-paianjen/","0.9")]+[("/"+s["slug"]+".html","0.9") for s in SERIES]+[("/ghid/","0.6")]+[(art_url(a),"0.7") for a in ARTICLES]
    x='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod><priority>{pr}</priority></url>\n" for u,pr in urls)+"</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(x)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nDisallow: /multumim.html\n\nSitemap: {BASE}/sitemap.xml\n")

if __name__ == "__main__":
    build_index(); build_series(); build_thanks()
    build_article(PILLAR, is_pillar=True)
    for a in ARTICLES: build_article(a)
    build_hub(); build_sitemap()
    print("built: index.html, " + ", ".join(s['slug']+".html" for s in SERIES) + ", multumim.html")
