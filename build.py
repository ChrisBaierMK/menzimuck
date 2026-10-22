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
def B(ro, en): return f'<span data-ro>{ro}</span><span data-en>{en}</span>'
def kgB(kg): return B(kg, kg.replace("de la", "from").replace(".", ","))  # "de la 13.500 kg" -> "from 13,500 kg"

# Injected into FOOT: remembers the RO/EN choice and toggles the <body> class.
LANG_JS = """
(function(){
  var b=document.body,btns=document.querySelectorAll('[data-lang]');
  function set(l){b.className='lang-'+l;document.documentElement.lang=l;
    btns.forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.lang===l))});
    try{localStorage.setItem('lang',l)}catch(e){}}
  btns.forEach(function(x){x.addEventListener('click',function(){set(x.dataset.lang)})});
  var s=null;try{s=localStorage.getItem('lang')}catch(e){}
  if(s==='en')set('en');
})();
"""

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
<body class="lang-ro">
<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Menzi Muck România — Baier Solutions, importator oficial România și Republica Moldova">
      <img class="mm" src="/images/logo-neg.svg" alt="Menzi Muck" width="92" height="36">
      <img class="bs" src="/images/baier-solutions.svg" alt="Baier Solutions" width="80" height="30">
      <span class="by"><span data-ro>Importator oficial<b>România și Republica Moldova</b></span><span data-en>Official importer<b>Romania &amp; Republic of Moldova</b></span></span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))"><span data-ro>Meniu</span><span data-en>Menu</span></button>
    <ul id="menu">
      <li><a href="/#modele"{c_modele}><span data-ro>Modele</span><span data-en>Models</span></a></li>
      <li><a href="/excavator-paianjen/"{c_ghid}><span data-ro>Excavator păianjen</span><span data-en>Spider excavator</span></a></li>
      <li><a href="/#domenii"><span data-ro>Domenii</span><span data-en>Applications</span></a></li>
      <li><a href="/#versatilitate"><span data-ro>Versatilitate</span><span data-en>Attachments</span></a></li>
      <li><a href="/ghid/"><span data-ro>Ghid</span><span data-en>Guide</span></a></li>
      <li><a href="/blog/"{c_blog}>Blog</a></li>
      <li><a href="/#despre"><span data-ro>Despre</span><span data-en>About</span></a></li>
    </ul>
    <div class="lang" role="group" aria-label="Limbă / Language"><button type="button" data-lang="ro" aria-pressed="true">RO</button><button type="button" data-lang="en" aria-pressed="false">EN</button></div>
    <a class="cta" href="/#contact"><span data-ro>Cere ofertă</span><span data-en>Get a quote</span></a>
  </div>
</header>
"""

FOOT = f"""
<footer>
  <div class="wrap">
    <div>{COMPANY} · Hărman, Brașov · CIF RO33270728</div>
    <ul>
      <li><a href="/excavator-paianjen/"><span data-ro>Excavator păianjen</span><span data-en>Spider excavator</span></a></li>
      <li><a href="/m5x.html">M5x</a></li><li><a href="/m4x.html">M4x</a></li><li><a href="/m2.html">M2</a></li><li><a href="/a20-a25.html">A20 / A25</a></li>
      <li><a href="/ghid/"><span data-ro>Ghid</span><span data-en>Guide</span></a></li>
      <li><a href="/blog/">Blog</a></li>
    </ul>
    <ul>
      <li><a href="{PHONE_HREF}">{PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="https://menzimuck.ro">menzimuck.ro</a></li>
      <li><a href="https://menzimuck.com" rel="noopener">menzimuck.com</a></li>
      <li><a href="https://baiersolutions.ro" rel="noopener">baiersolutions.ro</a></li>
    </ul>
    <div class="legal"><span data-ro>© 2026 {COMPANY}, importator oficial Menzi Muck AG (Rüthi, Elveția) pentru România și Republica Moldova. Menzi Muck® este marcă înregistrată a Menzi Muck AG; fotografiile și materialele video sunt proprietatea Menzi Muck AG și sunt folosite cu acordul acesteia. Datele tehnice sunt orientative — configurația finală și prețul se stabilesc prin ofertă.</span><span data-en>© 2026 {COMPANY}, official importer of Menzi Muck AG (Rüthi, Switzerland) for Romania and the Republic of Moldova. Menzi Muck® is a registered trademark of Menzi Muck AG; the photos and videos are the property of Menzi Muck AG and are used with its consent. Technical data is indicative — the final configuration and price are set by quote.</span></div>
  </div>
</footer>
<script>{LANG_JS}</script>
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
  tech=[("Motor","Deutz turbo diesel, 4 cilindri — 115 kW / 156 CP"),("Cilindree","4.038 cm³"),("Instalație electrică","24 V"),("Demaror","4,0 kW"),("Interval service","500 h"),("Sistem hidraulic","Load Sensing by Rexroth"),("Pompă de lucru","290 l/min · 300 bar"),("Pompă deplasare","210 l/min · 400 bar"),("Powerline (opțional)","220 l/min · max. 350 bar"),("Viteză de rotire","până la 10 rot/min")],
  extra=[
   ("Pompă Powerline pentru accesorii","Powerline pump for attachments",
    "Alimentare prioritară cu până la 220 l/min și maximum 350 bar. Debitul și presiunea se selectează din display. Furtun hidraulic: tur 1 țol, retur 1 ¼ țol.",
    "Priority feed of up to 220 l/min and a maximum of 350 bar. Flow and pressure are selected on the display. Hydraulic hose: 1 inch supply, 1 ¼ inch return."),
   ("Moduri de direcție","Steering modes",
    "Direcție pe puntea față, direcție pe puntea spate, direcție integrală pe patru roți și mers în crab.",
    "Front-axle steering, rear-axle steering, four-wheel steering and crab steering."),
   ("Mod lanțuri","Chain mode",
    "Cu lanțuri montate, protecția la coliziune se asigură prin activarea electrică a modului pentru lanțuri forestiere sau de zăpadă.",
    "With chains fitted, collision protection is ensured by electrically switching on forestry or snow-chain mode."),
   ("Tracțiune maximă","Maximum traction",
    "Blocajul hidraulic de diferențial asigură tracțiune maximă pe teren alunecos sau moale. Se activează manual, pentru și mai multă putere în modul off-road.",
    "The hydraulic differential lock ensures maximum traction on slippery or soft ground. It can be engaged manually for even more performance in off-road mode."),
   ("„Nu se poate” nu există","There's no such thing as “can't”",
    "Pe pante de până la 100 % (45°), în apă de până la 2,2 m adâncime sau în mlaștină adâncă, la munte sau în pădure — M5x are foarte puține limite. Șasiul flexibil se adaptează oricărui teren; în construcții, M5x depășește posibilitățile unui excavator pe șenile cu aceeași putere hidraulică.",
    "On slopes up to 100 % (45°), in water up to 2.2 m deep or in deep mud, in the mountains or in the forest — the M5x has very few limits. The flexible chassis adapts to any ground; in construction it goes beyond what a tracked excavator with the same hydraulic power can do."),
   ("Purtător pentru foraj, pădure și cale ferată","Carrier for drilling, forestry and rail",
    "M5x este un purtător excelent pentru diferite sisteme de foraj și pentru accesorii mari consumatoare de putere, municipale sau forestiere. În pădure lucrează ca harvester pe pante abrupte — în doborâturi de vânt, rărituri țintite sau tăieri rase. Ca excavator rutier-feroviar, Menzi Muck are avantaje enorme pe și lângă calea ferată.",
    "The M5x is an excellent carrier for various drilling systems and for power-hungry municipal or forestry attachments. In the forest it works as a steep-slope harvester — in windthrow, selective thinning or clear-cutting. As a road-rail excavator, the Menzi Muck has huge advantages on and beside the track."),
  ],
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
 dict(t="Construcții și fundații speciale", te="Construction & special foundations", img="hero.jpg",
  p="Taluzuri, drumuri de munte, fundații pe versant, lucrări de consolidare. Un Menzi Muck stă orizontal acolo unde un excavator pe șenile nu poate fi nici măcar adus.",
  pe="Embankments, mountain roads, hillside foundations, reinforcement works. A Menzi Muck stands level where a tracked excavator can't even be brought in.",
  li=["Fundații speciale pe pantă","Drumuri și platforme în zone montane","Consolidări de versanți și ziduri de sprijin"],
  lie=["Special foundations on slopes","Roads and platforms in mountain areas","Slope reinforcement and retaining walls"]),
 dict(t="Hidro și amenajări de albii", te="Hydro & river works", img="m535x-2.jpg",
  p="Lucrează din albia râului, de pe mal sau de pe un dig. Picioarele se reglează independent, mașina stă în apă fără să-și piardă stabilitatea, brațul ajunge unde nu ajunge nimeni.",
  pe="It works from the riverbed, the bank or a dike. The legs adjust independently, the machine stands in water without losing its stability, the boom reaches where nothing else can.",
  li=["Regularizări de albii și apărări de mal","Baraje, microhidrocentrale, prize de apă","Intervenții după inundații"],
  lie=["River regulation and bank protection","Dams, micro-hydro plants, water intakes","Post-flood interventions"]),
 dict(t="Forestier", te="Forestry", img="forest-2.jpg",
  p="Exploatare pe pantă cu procesor forestier, mulcher forestier sau graifer-fierăstrău. Drumuri forestiere, curățare de parcele, lucrări în zone fără acces pentru utilaj greu.",
  pe="Slope harvesting with a forestry processor, forestry mulcher or saw-grapple. Forest roads, clearing plots, work in areas with no access for heavy equipment.",
  li=["Procesor forestier Konrad, graifer-fierăstrău MVD","Mulcher forestier Seppi, freză de cioate FSI","Drumuri forestiere și platforme de depozitare"],
  lie=["Konrad forestry processor, MVD saw-grapple","Seppi forestry mulcher, FSI stump cutter","Forest roads and storage platforms"]),
 dict(t="Utilități și infrastructură", te="Utilities & infrastructure", img="m525x-2.jpg",
  p="Trasee de cablu, conducte și stâlpi în zone inaccesibile: munte, pădure, pantă. M2 și A20/A25 se demontează și zboară cu elicopterul direct la punctul de lucru.",
  pe="Cable routes, pipelines and poles in inaccessible areas: mountain, forest, slope. The M2 and A20/A25 break down and fly in by helicopter straight to the work point.",
  li=["Trasee de cablu electric și fibră optică","Conducte de apă și gaz pe teren accidentat","Fundații pentru stâlpi și instalații de telecabină"],
  lie=["Power and fibre-optic cable routes","Water and gas pipelines on rough terrain","Foundations for poles and cable-car installations"]),
 dict(t="Feroviar", te="Railway", img="m545x-3.jpg",
  p="Întreținerea taluzurilor și a șanțurilor de-a lungul căii ferate, defrișări de vegetație, lucrări la rambleu — fără a bloca linia și fără utilaj feroviar specializat.",
  pe="Maintaining embankments and ditches along the railway, vegetation clearing, embankment works — without blocking the line and without specialised rail equipment.",
  li=["Curățare de vegetație și taluzuri","Șanțuri și drenaje de-a lungul liniei","Intervenții la alunecări de teren"],
  lie=["Vegetation and embankment clearing","Ditches and drainage along the line","Landslide interventions"]),
 dict(t="Municipal și spații verzi", te="Municipal & green spaces", img="a25.jpg",
  p="Întreținere de pante, maluri și spații verzi, lucrări de grădinărit peisagistic, demolări controlate în spații înguste și intervenții de urgență după dezastre naturale.",
  pe="Maintenance of slopes, banks and green spaces, landscape gardening, controlled demolition in tight spaces and emergency response after natural disasters.",
  li=["Întreținere pante și maluri de lac","Peisagistică și amenajări cu A20 / A25","Intervenții la dezastre naturale"],
  lie=["Slope and lakeshore maintenance","Landscaping with the A20 / A25","Natural-disaster response"]),
]

ATTACH = [
 dict(t="Cupe", te="Buckets", s="Cupă de săpat, cupă pentru tiltrotator, cupă de humus (și hidraulică), cupă de sortare — proiectate și fabricate la Menzi Muck.", se="Digging bucket, tiltrotator bucket, humus bucket (also hydraulic), sorting bucket — designed and built at Menzi Muck.", img="a20-2.jpg"),
 dict(t="Graifere", te="Grapples", s="Graifer universal pentru piatră, buștean și materiale în vrac, construit în casă pentru forțele unui excavator păianjen.", se="Universal grapple for stone, logs and bulk materials, built in-house for the forces of a spider excavator.", img="m4x-3.jpg"),
 dict(t="Tiltrotatoare și cuple rapide", te="Tiltrotators & quick couplers", s="Tiltrotator Oilquick sau Rototilt, cap rotativ Powertilt, cuplă rapidă hidraulică — schimbi accesoriul fără să cobori din cabină.", se="Oilquick or Rototilt tiltrotator, Powertilt rotating head, hydraulic quick coupler — change the attachment without leaving the cab.", img="rototilt.jpg"),
 dict(t="Trolii", te="Winches", s="Troliu de cablu pentru lucrări pe pante extreme, extragere de buștean și asigurarea mașinii.", se="Cable winch for work on extreme slopes, log extraction and securing the machine.", img="winch.jpg"),
 dict(t="Demolare și excavare", te="Demolition & excavation", s="Ciocan hidraulic și sisteme de demolare — Powerline până la 220 l/min alimentează accesorii pe care un excavator clasic nu le poate susține.", se="Hydraulic hammer and demolition systems — a Powerline circuit up to 220 l/min feeds attachments a conventional excavator can't support.", img="m220-3.jpg"),
 dict(t="Municipal și forestier", te="Municipal & forestry", s="Procesor forestier Konrad, mulcher forestier, freză de cioate, graifer-fierăstrău — un singur utilaj pentru întreaga lucrare.", se="Konrad forestry processor, forestry mulcher, stump cutter, saw-grapple — one machine for the whole job.", img="forest.jpg"),
]

# ---------------- EN translations for model-page copy (RO source string -> EN) ----------------
TR = {
 # taglines
 "Clasa grea pentru pante extreme":"Heavy class for extreme slopes",
 "Forță mare, greutate mică":"Big force, low weight",
 "Se demontează și zboară":"Breaks down and flies",
 "Ușor, dar merge peste tot":"Light, but goes anywhere",
 # leads
 "Seria M5x lucrează în siguranță pe pante de până la 45° în linia de cădere și 30° în linia de nivel, cu șasiul patentat Menzi Muck pe bază X. Ecartamentul se deschide până la 6 metri — o stabilitate pe care un excavator clasic de 13 tone nu o are. Motor Deutz de 156 CP, hidraulică load-sensing Rexroth, intervale de service de 500 de ore.":"The M5x series works safely on slopes up to 45° in the fall line and 30° across it, on Menzi Muck's patented X-base chassis. The track gauge opens up to 6 metres — stability a conventional 13-tonne excavator simply doesn't have. 156 hp Deutz engine, Rexroth load-sensing hydraulics, 500-hour service intervals.",
 "Șasiul patentat pe bază X al seriei M4x combină stabilitate, mobilitate și un centru de greutate optimizat. Reglarea paralelă a roților pe orizontală și pe verticală ține mașina stabilă pe orice teren. Cilindrul de braț montat sus ridică forța de împingere — esențială la un pășitor — la peste 200 % față de generația anterioară. Motor Deutz de 143 CP, hidraulică I-Control by Menzi Muck.":"The M4x series' patented X-base chassis combines stability, mobility and an optimised centre of gravity. Parallel wheel adjustment, horizontal and vertical, keeps the machine steady on any terrain. The high-mounted boom cylinder raises breakout force — essential on a walking excavator — to over 200% versus the previous generation. 143 hp Deutz engine, I-Control hydraulics by Menzi Muck.",
 "M2 se descompune în câțiva pași în pachete pentru transport cu elicopterul, telecabina sau macaraua — dispozitive ajutătoare integrate fac demontarea rapidă pe teren. Este alternativa economică pentru lucrări unde nu ajunge niciun alt utilaj: albii de râu, versanți, trasee de cablu, zone fără drum de acces. Motor Deutz de 75 CP conform celor mai noi norme de emisii.":"The M2 breaks down in a few steps into packages for transport by helicopter, cable car or crane — integrated aids make dismantling quick on site. It's the economical choice for jobs no other machine can reach: riverbeds, hillsides, cable routes, areas with no access road. 75 hp Deutz engine meeting the latest emission standards.",
 "Cu o greutate de la 2 tone, A20 și A25 ajung practic pe orice teren și, ca și M2, se pretează transportului cu elicopterul. Două punți detașabile cu roți de rulare și sprijin telescopic mecanic. Pentru grădinărit, întreținere de maluri, intervenții în spații înguste și lucrări unde un utilaj mare nu încape.":"Weighing from 2 tonnes, the A20 and A25 reach practically any terrain and, like the M2, suit helicopter transport. Two detachable axles with road wheels and mechanical telescopic support. For gardening, bank maintenance, work in tight spaces and jobs where a large machine won't fit.",
 # feats
 "Transmisie continuă Vx-Drive by Menzi, până la 15 km/h":"Continuous Vx-Drive transmission by Menzi, up to 15 km/h",
 "Transmisie continuă Vx-Drive by Menzi, până la 11 km/h":"Continuous Vx-Drive transmission by Menzi, up to 11 km/h",
 "Sprijin paralel P-Vation by Menzi":"P-Vation parallel support by Menzi",
 "Sprijin paralel P-Vation by Menzi Muck":"P-Vation parallel support by Menzi Muck",
 "Patru roți de aceeași mărime, lățime până la 800 mm":"Four equal-size wheels, up to 800 mm wide",
 "Patru roți de aceeași mărime, lățime până la 710 mm":"Four equal-size wheels, up to 710 mm wide",
 "Suporturi de pantă față și/sau spate (opțional)":"Front and/or rear slope supports (optional)",
 "Reglare hidraulică a înălțimii roților directoare":"Hydraulic height adjustment of the steering wheels",
 "Sprijin telescopic hidraulic":"Hydraulic telescopic support",
 "Două punți detașabile cu roți de rulare":"Two detachable axles with road wheels",
 "Tracțiune integrală hidrostatică Menzi H-Drive":"Menzi H-Drive hydrostatic all-wheel drive",
 "Transmisie hidrostatică Menzi":"Menzi hydrostatic transmission",
 "Transmisie în două trepte cu direcție paralelă autoreglabilă":"Two-speed transmission with self-adjusting parallel steering",
 "Demontabil pentru transport cu elicopter / telecabină / macara":"Dismantles for helicopter / cable-car / crane transport",
 "Tracțiune hidrostatică pe cele două roți mari, până la 2,6 km/h":"Hydrostatic drive on the two large wheels, up to 2.6 km/h",
 "Sprijin telescopic mecanic":"Mechanical telescopic support",
}
def tr(s): return TR.get(s, s)

# Spec-table: translate the labels; values keep their numbers, with the few RO words swapped.
TECH_LABELS = {"Motor":"Engine","Cilindree":"Displacement","Instalație electrică":"Electrical system",
 "Demaror":"Starter","Interval service":"Service interval","Sistem hidraulic":"Hydraulic system",
 "Pompă de lucru":"Work pump","Pompă deplasare":"Travel pump","Powerline (opțional)":"Powerline (optional)",
 "Viteză de rotire":"Slewing speed","Rază minimă de rotire":"Min. turning radius"}
def tech_en(v):
    return (v.replace("până la","up to").replace("rot/min","rpm").replace("cilindri","cyl.")
             .replace(" CP"," hp").replace("Diesel Kubota","Kubota diesel"))

def img(name, alt="", cls="", lazy=True, attrs=""):
    l = ' loading="lazy"' if lazy else ''
    c = f' class="{cls}"' if cls else ""
    a = f' {attrs}' if attrs else ""
    return f'<img src="/images/{name}" alt="{esc(alt)}"{c}{l}{a}>'

def spec_table(rows, caption_ro="Date tehnice", caption_en="Technical data"):
    rr = "".join(f"<tr><th>{B(k, TECH_LABELS.get(k,k))}</th><td>{B(v, tech_en(v))}</td></tr>" for k,v in rows)
    return f'<table class="spec"><caption>{B(caption_ro, caption_en)}</caption>{rr}</table>'

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
  <div class="t"><div class="code">{esc(m['code'])}</div><div class="kg">{kgB(m['kg'])}</div><span class="more">{B('Fișa tehnică','Specs')}</span></div></a>""" for s in SERIES for m in s["models"])

    domains = "".join(f"""<article class="domain">
  <div class="img">{img(d['img'], d['t'])}</div>
  <div class="txt"><div class="n">0{i+1}</div><h3>{B(d['t'], d['te'])}</h3><p>{B(d['p'], d['pe'])}</p><ul>{''.join(f'<li>{B(x, xe)}</li>' for x,xe in zip(d['li'], d['lie']))}</ul></div>
</article>""" for i,d in enumerate(DOMAINS))

    attach = "".join(f"""<a href="/#contact">{img(a['img'], a['t'],lazy=False)}<div class="t"><h3>{B(a['t'], a['te'])}</h3><p>{B(a['s'], a['se'])}</p></div></a>""" for a in ATTACH)

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
    <div class="label rv"><span data-ro>Importator oficial Menzi Muck · România și Republica Moldova</span><span data-en>Official Menzi Muck importer · Romania &amp; Republic of Moldova</span></div>
    <h1 class="rv d1"><span data-ro>Unde alții se opresc, noi abia începem.</span><span data-en>Where others stop, we're just getting started.</span></h1>
    <p class="sub rv d2"><span data-ro>Excavatoare păianjen elvețiene pentru pante, albii, pădure și tot ce nu poate atinge un utilaj pe șenile. Vânzare, livrare, instruire operator și service în România.</span><span data-en>Swiss spider excavators for slopes, riverbeds, forests and everything a tracked machine can't reach. Sales, delivery, operator training and service in Romania.</span></p>
    <div class="btn-row rv d3"><a class="btn solid" href="#modele"><span data-ro>Vezi modelele</span><span data-en>See the models</span></a><a class="btn" href="#contact"><span data-ro>Cere ofertă</span><span data-en>Get a quote</span></a></div>
  </div>
  <div class="scroll-hint" aria-hidden="true"></div>
</section>

<div class="strip"><div class="wrap">
  <div><b>45°</b><span><span data-ro>pantă în linia de cădere</span><span data-en>slope in the fall line</span></span></div>
  <div><b>2–13,5 t</b><span><span data-ro>de la A20 la M545x</span><span data-en>from A20 to M545x</span></span></div>
  <div><b>1966</b><span><span data-ro>Menzi Muck AG, Rüthi, Elveția</span><span data-en>Menzi Muck AG, Rüthi, Switzerland</span></span></div>
  <div><b>290 l/min</b><span><span data-ro>debit hidraulic de lucru</span><span data-en>working hydraulic flow</span></span></div>
</div></div>

<section class="text" id="de-ce">
  <div class="wrap">
    <div><div class="eyebrow"><span data-ro>De ce un excavator păianjen</span><span data-en>Why a spider excavator</span></div><h2><span data-ro>Merge unde șenila nu are ce căuta.</span><span data-en>It works where tracks have no business.</span></h2></div>
    <div>
      <p class="lead"><span data-ro>Un Menzi Muck își reglează fiecare roată și fiecare picior separat. Stă orizontal pe un versant, în albia unui râu sau lângă o cale ferată — și lucrează de acolo cu forțe de ridicare și rupere mai mari decât un excavator clasic din aceeași clasă de greutate.</span><span data-en>A Menzi Muck adjusts every wheel and every leg independently. It stands level on a hillside, in a riverbed or beside a railway — and works from there with lifting and breakout forces greater than a conventional excavator in the same weight class.</span></p>
      <p><span data-ro>Șasiul patentat și brațul patentat pun la dispoziție un debit hidraulic mult mai mare pentru accesorii. O singură mașină înlocuiește utilaj greu, schele și, de multe ori, zile de lucru manual.</span><span data-en>The patented chassis and boom deliver far greater hydraulic flow for attachments. A single machine replaces heavy equipment, scaffolding and, often, days of manual labour.</span></p>
      <div class="cells">
        <div><h3><span data-ro>Stabilitate</span><span data-en>Stability</span></h3><p><span data-ro>Sprijin paralel P-Vation și ecartament reglabil până la 6 m pe M5x. Mașina stă, operatorul lucrează.</span><span data-en>P-Vation parallel support and a track gauge adjustable up to 6 m on the M5x. The machine stays put, the operator works.</span></p></div>
        <div><h3><span data-ro>Mobilitate</span><span data-en>Mobility</span></h3><p><span data-ro>Transmisie Vx-Drive sau H-Drive, până la 15 km/h pe drum. M2 și A20/A25 se demontează pentru elicopter.</span><span data-en>Vx-Drive or H-Drive transmission, up to 15 km/h on the road. The M2 and A20/A25 break down for helicopter transport.</span></p></div>
        <div><h3><span data-ro>Hidraulică</span><span data-en>Hydraulics</span></h3><p><span data-ro>Până la 290 l/min la 300 bar pe pompa de lucru, plus pompă Powerline cu alimentare prioritară — până la 220 l/min și 350 bar — pentru accesorii.</span><span data-en>Up to 290 l/min at 300 bar on the work pump, plus a priority-fed Powerline pump — up to 220 l/min and 350 bar — for attachments.</span></p></div>
      </div>
    </div>
  </div>
</section>

<section class="panel half" id="pante">
  <div class="media">{img('hero.jpg','Menzi Muck M4x în teren montan')}</div>
  <div class="wrap"><div class="label"><span data-ro>Elveția, 1.800 m</span><span data-en>Switzerland, 1,800 m</span></div><h2><span data-ro>Unde alții se opresc, noi abia începem.</span><span data-en>Where others stop, we're just getting started.</span></h2><p class="sub"><span data-ro>Sloganul Menzi Muck nu e o figură de stil. Este descrierea exactă a locului de muncă.</span><span data-en>The Menzi Muck slogan isn't a figure of speech. It's an exact description of the job site.</span></p></div>
</section>

<section id="domenii">
  <div class="wrap sec-head"><div class="eyebrow"><span data-ro>Domenii de activitate</span><span data-en>Applications</span></div><h2><span data-ro>Un utilaj. Șase industrii.</span><span data-en>One machine. Six industries.</span></h2><p><span data-ro>Oriunde terenul e prea abrupt, prea moale, prea îngust sau prea departe de drum pentru un excavator clasic.</span><span data-en>Wherever the ground is too steep, too soft, too narrow or too far from the road for a conventional excavator.</span></p></div>
  <div class="domains">{domains}</div>
</section>

<section id="versatilitate">
  <div class="wrap sec-head"><div class="eyebrow"><span data-ro>Versatilitate</span><span data-en>Attachments</span></div><h2><span data-ro>Programul de accesorii al clasei regale.</span><span data-en>The attachment programme of the royal class.</span></h2><p><span data-ro>Lucrări diferite cer unelte diferite. Puterea hidraulică a unui Menzi Muck duce și cele mai pretențioase accesorii. Cupele, cuplele rapide și graiferele sunt proiectate și fabricate la Menzi Muck; restul vin de la partenerii lor: Oilquick, Rototilt, Seppi, Konrad, FSI, MVD — și multe alte accesorii, inclusiv pentru foraj. Fiecare accesoriu se adaptează la utilaj după cerința clientului: cu fixare directă la braț, pe cuple hidraulice rapide, pe rotatoare sau chiar pe diferite sisteme de tiltrotatoare.</span><span data-en>Different jobs call for different tools. A Menzi Muck's hydraulic power drives even the most demanding attachments. Buckets, quick couplers and grapples are designed and built by Menzi Muck; the rest come from their partners: Oilquick, Rototilt, Seppi, Konrad, FSI, MVD — and many other attachments, including for drilling. Each attachment is adapted to the machine to the customer's requirements: mounted directly on the arm, on hydraulic quick couplers, on rotators or even on different tiltrotator systems.</span></p></div>
  <div class="attach">{attach}</div>
  <div class="wrap hydro">
    <div><b>300 bar</b><span><span data-ro>presiune de lucru</span><span data-en>working pressure</span></span></div>
    <div><b>220 l/min · 350 bar</b><span><span data-ro>pompă Powerline suplimentară pentru accesorii (M5x)</span><span data-en>extra Powerline pump for attachments (M5x)</span></span></div>
    <div><b>&gt;200 %</b><span><span data-ro>forță de împingere față de generația anterioară (M4x)</span><span data-en>more breakout force than the previous generation (M4x)</span></span></div>
  </div>
  <div class="wrap hydro-note"><p><span data-ro>Powerline cu alimentare prioritară: până la 220 l/min și maximum 350 bar. Debitul și presiunea se selectează din display. Furtun hidraulic: tur 1 țol, retur 1 ¼ țol.</span><span data-en>Priority-fed Powerline: up to 220 l/min and a maximum of 350 bar. Flow and pressure are selected on the display. Hydraulic hose: 1 inch supply, 1 ¼ inch return.</span></p></div>
</section>

<section id="modele">
  <div class="wrap sec-head"><div class="eyebrow"><span data-ro>Gama</span><span data-en>The range</span></div><h2><span data-ro>Nouă modele. Patru serii.</span><span data-en>Nine models. Four series.</span></h2><p><span data-ro>De la 2 tone la 13,5 tone. Fiecare se configurează la Rüthi pentru lucrarea dumneavoastră.</span><span data-en>From 2 tonnes to 13.5 tonnes. Each one is configured at Rüthi for your job.</span></p></div>
  <div class="rail-ctl"><button type="button" data-rail="prev" aria-label="Înapoi">←</button><button type="button" data-rail="next" aria-label="Înainte">→</button></div>
  <div class="rail">{cards}</div>
</section>

<section class="panel half" id="service">
  <div class="media">{img('used.jpg','Livrare Menzi Muck pe trailer')}</div>
  <div class="wrap"><div class="label"><span data-ro>Service &amp; instruire</span><span data-en>Service &amp; training</span></div><h2><span data-ro>De la vizita pe șantier la prima oră de lucru.</span><span data-en>From the site visit to the first hour of work.</span></h2></div>
</section>
<section class="text" style="padding-top:72px">
  <div class="wrap" style="grid-template-columns:1fr">
    <div class="steps">
      <div><b>01 · <span data-ro>Vizită pe șantier</span><span data-en>Site visit</span></b><p><span data-ro>Venim pe șantier, vedem lucrarea și punem pe hârtie ce model și ce accesorii au sens pentru ea.</span><span data-en>We come to the site, look at the job and put on paper which model and attachments make sense for it.</span></p></div>
      <div><b>02 · <span data-ro>Configurare</span><span data-en>Configuration</span></b><p><span data-ro>Mașina se configurează la Rüthi exact pentru lucrarea dumneavoastră: roți, sprijin, cuplă rapidă, Powerline, accesorii.</span><span data-en>The machine is configured at Rüthi exactly for your job: wheels, support, quick coupler, Powerline, attachments.</span></p></div>
      <div><b>03 · <span data-ro>Livrare și instruire</span><span data-en>Delivery &amp; training</span></b><p><span data-ro>Livrăm în România și instruim operatorii pe mașina dumneavoastră. Garanție 24 de luni sau 1.500 de ore de funcționare, oricare intervine prima. La cerere, extensie la 36 de luni contra cost, fără a depăși 2.000 de ore.</span><span data-en>We deliver across Romania and train your operators on your machine. Warranty of 24 months or 1,500 operating hours, whichever comes first. On request, an extension to 36 months at extra cost, not exceeding 2,000 hours.</span></p></div>
      <div><b>04 · <span data-ro>Service și piese</span><span data-en>Service &amp; parts</span></b><p><span data-ro>Piese de schimb originale și tehnicieni instruiți de echipa de ingineri Menzi Muck. Intervale de service la 500 de ore.</span><span data-en>Original spare parts and technicians trained by the Menzi Muck engineering team. Service intervals at 500 hours.</span></p></div>
    </div>
  </div>
</section>

<section class="panel half" id="despre">
  <div class="media">{img('poster.jpg','Rüthi, Elveția')}</div>
  <div class="wrap"><div class="label"><span data-ro>Despre</span><span data-en>About</span></div><h2><span data-ro>60 de ani de pionierat elvețian.</span><span data-en>60 years of Swiss pioneering.</span></h2><p class="sub"><span data-ro>Menzi Muck AG construiește excavatoare păianjen (pășitoare) din 1966 la Rüthi, în estul Elveției, și este liderul mondial al segmentului. Mașinile lucrează pe toate continentele.</span><span data-en>Menzi Muck AG has built spider (walking) excavators since 1966 in Rüthi, eastern Switzerland, and is the world leader in the segment. The machines work on every continent.</span></p></div>
</section>
<section class="text" style="padding-top:72px">
  <div class="wrap">
    <div>{img('history.jpg','Menzi Muck 1966')}</div>
    <div>
      <p class="lead"><span data-ro>{COMPANY} din Hărman, Brașov, este importatorul oficial Menzi Muck AG pentru România.</span><span data-en>{COMPANY} in Hărman, Brașov, is the official Menzi Muck AG importer for Romania.</span></p>
      <p><span data-ro>Familia Baier vinde și pune în funcțiune mașini Menzi Muck în România de peste 20 de ani — cunoaștem utilajul, cunoaștem terenul și vorbim direct cu fabrica, în germană.</span><span data-en>The Baier family has sold and commissioned Menzi Muck machines in Romania for over 20 years — we know the machine, we know the terrain and we speak directly with the factory, in German.</span></p>
      <p><span data-ro>Nu transportăm mașini pentru demonstrații; vă ducem să vedeți un Menzi Muck acolo unde lucrează deja și venim noi la lucrarea dumneavoastră să stabilim modelul și configurația potrivite.</span><span data-en>We don't truck machines around for demos; we take you to see a Menzi Muck already at work and come to your site to settle the right model and configuration.</span></p>
    </div>
  </div>
</section>

<section id="ghid">
  <div class="wrap sec-head"><div class="eyebrow"><span data-ro>Ghid</span><span data-en>Guide</span></div><h2><span data-ro>Tot ce trebuie să știi despre excavatorul păianjen.</span><span data-en>Everything you need to know about the spider excavator.</span></h2><p><span data-ro>Preț, alegerea modelului, comparații și lucrări tipice — scrise de importatorul oficial.</span><span data-en>Price, choosing the model, comparisons and typical jobs — written by the official importer.</span></p></div>
  <div class="wrap guide-grid">{{GUIDE_CARDS}}</div>
</section>

<!-- blog-latest:start -->
<!-- blog-latest:end -->

<section class="contact" id="contact">
  <div class="wrap">
    <div class="contact-side">
      <div class="eyebrow">Contact</div>
      <h2><span data-ro>Cere o ofertă.</span><span data-en>Request a quote.</span></h2>
      <p><b><span data-ro>Telefon</span><span data-en>Phone</span></b><a href="{PHONE_HREF}">{PHONE}</a></p>
      <p><b>E-mail</b><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><b><span data-ro>Sediu</span><span data-en>Office</span></b>{COMPANY}<br><span data-ro>Hărman, jud. Brașov, România</span><span data-en>Hărman, Brașov County, Romania</span></p>
      <p><b><span data-ro>Limbi</span><span data-en>Languages</span></b>Română · Deutsch · English</p>
    </div>
    <form name="oferta" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/multumim.html">
      <input type="hidden" name="form-name" value="oferta">
      <p hidden><label>Nu completați: <input name="bot-field"></label></p>
      <label><span data-ro>Nume și prenume</span><span data-en>Full name</span><input name="nume" required autocomplete="name"></label>
      <label><span data-ro>Firmă</span><span data-en>Company</span><input name="firma" autocomplete="organization"></label>
      <label><span data-ro>Telefon</span><span data-en>Phone</span><input name="telefon" type="tel" required autocomplete="tel"></label>
      <label>E-mail<input name="email" type="email" required autocomplete="email"></label>
      <label><span data-ro>Model de interes</span><span data-en>Model of interest</span><select name="model"><option>Nu știu / Not sure — recomandare</option><option>M5x (M525x / M535x / M545x)</option><option>M4x (M425x / M435x / M445x)</option><option>M2 (M220)</option><option>A20 / A25</option><option>Accesorii / parts</option></select></label>
      <label><span data-ro>Județul lucrării</span><span data-en>Work county</span><input name="judet"></label>
      <label class="full"><span data-ro>Descrieți lucrarea</span><span data-en>Describe the job</span><textarea name="mesaj" placeholder="Tip lucrare, pantă, acces, accesorii, termen"></textarea></label>
      <button class="btn solid" type="submit"><span data-ro>Trimite cererea</span><span data-en>Send request</span></button>
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
            feats = "".join(f"<li>{B(x, tr(x))}</li>" for x in m["feats"])
            tech = m.get("tech") or s["tech"]
            code = esc(m['code'])
            blocks += f"""
<article class="model" id="{m['code'].lower()}">
  <div class="wrap">
    <div>{img(m['img'],'Menzi Muck '+m['code'],'pic')}
      <h2>Menzi Muck {code}</h2>
      <div class="kg">{kgB(m['kg'])}</div>
      <ul class="chips">{feats}</ul>
      <a class="btn solid" href="/#contact">{B('Cere ofertă pentru '+code, 'Request a quote for '+code)}</a>
    </div>
    <div>{spec_table(tech)}</div>
  </div>
</article>"""
        gallery = "".join(img(g, f"Menzi Muck {s['name']}") for g in s["gallery"])
        extra = ""
        if s.get("extra"):
            cells = "".join(f"<div><h3>{B(t, te)}</h3><p>{B(x, xe)}</p></div>" for t, te, x, xe in s["extra"])
            extra = f"""<section class="text" style="padding-top:0">
  <div class="wrap">
    <div><div class="eyebrow">{B('Dotări', 'Features')}</div><h2>{B('Ce mai poate '+esc(s['name']), 'What else the '+esc(s['name'])+' can do')}</h2></div>
    <div class="cells two">{cells}</div>
  </div>
</section>"""
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
    <div class="label rv">{B('Excavator păianjen · Seria '+esc(s['name']), 'Spider excavator · '+esc(s['name'])+' series')}</div>
    <h1 class="rv d1">Menzi Muck {esc(s['name'])}</h1>
    <p class="sub rv d2">{kgB(s['kg'])} · {B(s['tagline'], tr(s['tagline']))}</p>
    <div class="btn-row rv d3"><a class="btn solid" href="#{s['models'][0]['code'].lower()}">{B('Date tehnice','Technical data')}</a><a class="btn" href="/#contact">{B('Cere ofertă','Get a quote')}</a></div>
  </div>
</section>
{series_nav(s['slug'])}
<section class="text">
  <div class="wrap">
    <div><div class="eyebrow">{B('Seria '+esc(s['name']), esc(s['name'])+' series')}</div><h2>{B(s['tagline'], tr(s['tagline']))}</h2></div>
    <div><p class="lead">{B(s['lead'], tr(s['lead']))}</p></div>
  </div>
</section>
{extra}
<div class="gallery">{gallery}</div>
{blocks}
<section class="panel short center">
  <div class="media">{img('slope.jpg','')}</div>
  <div class="wrap"><h2>{B('Vrei să-l vezi lucrând?','Want to see it working?')}</h2><p class="sub">{B('Vă ducem la un Menzi Muck în lucru și venim pe șantierul dumneavoastră să stabilim modelul și accesoriile potrivite pentru lucrare.','We take you to a Menzi Muck at work and come to your site to settle the right model and attachments for the job.')}</p>
  <p class="sub"><a href="/excavator-paianjen/" style="text-decoration:underline">{B('Ce este un excavator păianjen și cum alegi modelul','What a spider excavator is and how to choose the model')}</a></p>
  <div class="btn-row"><a class="btn solid" href="/#contact">{B('Programează o vizită','Book a visit')}</a><a class="btn" href="{PHONE_HREF}">{PHONE}</a></div></div>
</section>
""" + FOOT
        open(os.path.join(OUT, f"{s['slug']}.html"),"w").write(p)

def build_thanks():
    p = page_head("Mulțumim | Menzi Muck România", "Cererea a fost trimisă.", path="/multumim.html").replace('content="index,follow,max-image-preview:large"','content="noindex"')
    p += f"""
<section class="panel short center">
  <div class="media">{img('poster.jpg','')}</div>
  <div class="wrap"><div class="label">{B('Cerere trimisă','Request sent')}</div><h1>{B('Mulțumim.','Thank you.')}</h1>
  <p class="sub">{B('Vă sunăm în cel mult o zi lucrătoare. Dacă e urgent: '+PHONE+'.','We will call you within one working day. If it is urgent: '+PHONE+'.')}</p>
  <div class="btn-row"><a class="btn" href="/">{B('Înapoi la site','Back to site')}</a></div></div>
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
    <h3>Oferta pentru lucrarea ta</h3>
    <p>Model, configurație și accesorii — gratuit, de la importatorul oficial.</p>
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
