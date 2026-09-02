from pathlib import Path
import html

ROOT = Path('/mnt/data/sunnyday-majestic-style')

CSS = r'''
:root{
  --bg:#0d0d12;
  --surface:#14141c;
  --surface-2:#1a1a23;
  --surface-3:#20202a;
  --gold:#d3aa62;
  --gold-2:#f0cf8b;
  --text:#f5f4f1;
  --muted:#aaa8b0;
  --line:rgba(255,255,255,.09);
  --gold-line:rgba(211,170,98,.34);
  --shadow:0 24px 70px rgba(0,0,0,.38);
  --radius:7px;
  --max:1180px;
  --serif:"Cormorant Garamond",Georgia,serif;
  --sans:"Manrope","Inter",Arial,sans-serif;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);line-height:1.65}a{color:inherit;text-decoration:none}img{display:block;max-width:100%}button,input,select,textarea{font:inherit}.container{width:min(calc(100% - 40px),var(--max));margin:auto}.section{padding:86px 0}.section--tight{padding:58px 0}.section--alt{background:#111118}.section--raised{background:linear-gradient(180deg,#13131b,#0f0f15)}
.eyebrow{margin:0 0 10px;text-transform:uppercase;letter-spacing:.22em;color:var(--gold);font-weight:700;font-size:11px}.section-title{font:600 clamp(38px,5vw,58px)/.96 var(--serif);margin:0;color:var(--text)}.section-title em{font-style:normal;color:var(--gold-2)}.section-lead{max-width:720px;color:var(--muted);margin:16px auto 0}.center{text-align:center}.rule{width:72px;height:1px;background:var(--gold);margin:20px auto 0;opacity:.8}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 24px;border:1px solid var(--gold);border-radius:2px;text-transform:uppercase;letter-spacing:.08em;font-size:12px;font-weight:800;transition:.28s ease;cursor:pointer}.btn--gold{background:var(--gold);color:#121014}.btn--gold:hover{background:var(--gold-2);border-color:var(--gold-2);transform:translateY(-2px)}.btn--outline{color:var(--text);background:rgba(12,12,17,.35)}.btn--outline:hover{background:rgba(211,170,98,.13);transform:translateY(-2px)}.text-link{display:inline-flex;gap:8px;align-items:center;color:var(--gold-2);font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:800}.text-link:hover span{transform:translateX(4px)}.text-link span{transition:.25s}
/* header */
.site-header{position:fixed;z-index:90;top:0;left:0;right:0;height:82px;display:flex;align-items:center;background:linear-gradient(180deg,rgba(7,7,10,.75),rgba(7,7,10,.18),transparent);transition:.3s}.site-header.scrolled{height:70px;background:rgba(10,10,14,.92);backdrop-filter:blur(15px);border-bottom:1px solid var(--line)}.nav{display:grid;grid-template-columns:220px 1fr 220px;align-items:center;gap:24px}.brand{display:flex;align-items:center;gap:12px}.brand-mark{width:42px;height:42px;border:1px solid var(--gold);display:grid;place-items:center;color:var(--gold-2);font:700 17px/1 var(--serif);transform:rotate(45deg)}.brand-mark span{transform:rotate(-45deg)}.brand-text strong{display:block;font:600 20px/1 var(--serif);letter-spacing:.08em}.brand-text small{display:block;color:var(--gold);font-size:8px;text-transform:uppercase;letter-spacing:.28em;margin-top:5px}.nav-links{display:flex;justify-content:center;gap:25px}.nav-links a{color:#dddbe0;font-size:12px;font-weight:700;position:relative}.nav-links a:after{content:"";position:absolute;left:50%;bottom:-8px;width:0;height:1px;background:var(--gold);transition:.25s;transform:translateX(-50%)}.nav-links a:hover:after,.nav-links a.active:after{width:100%}.nav-actions{display:flex;align-items:center;justify-content:flex-end;gap:11px}.lang{font-size:11px;color:var(--muted);font-weight:800;letter-spacing:.08em}.lang strong{color:var(--gold)}.nav-toggle{display:none;width:44px;height:44px;border:1px solid var(--line);background:#17171f;color:#fff}.mobile-panel{display:none}
/* hero */
.hero{min-height:760px;height:100svh;max-height:980px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden}.hero-media{position:absolute;inset:0}.hero-media img{width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(.8) contrast(1.04)}.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(7,7,10,.68),rgba(7,7,10,.30) 47%,rgba(7,7,10,.48)),linear-gradient(180deg,rgba(7,7,10,.12),rgba(7,7,10,.28) 54%,#0d0d12 100%)}.hero-content{position:relative;z-index:2;text-align:center;max-width:850px;padding-top:70px}.hero-kicker{font:500 clamp(31px,4vw,48px)/1 var(--serif);margin:0 0 3px;color:#f4f1ea}.hero h1{font:600 clamp(53px,8.2vw,91px)/.88 var(--serif);margin:0;color:var(--gold-2);text-shadow:0 7px 35px rgba(0,0,0,.35)}.hero p{max-width:640px;margin:23px auto;color:#e7e5e6;font-size:15px}.hero-actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:27px}.scroll-cue{position:absolute;bottom:28px;z-index:3;left:50%;transform:translateX(-50%);color:#d8d3c9;font-size:9px;text-transform:uppercase;letter-spacing:.3em;display:grid;justify-items:center;gap:8px}.scroll-cue i{display:block;width:1px;height:32px;background:linear-gradient(var(--gold),transparent)}
/* cards */
.card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.lux-card{background:var(--surface-2);border:1px solid var(--line);box-shadow:var(--shadow);overflow:hidden;transition:.3s;position:relative}.lux-card:hover{transform:translateY(-6px);border-color:var(--gold-line)}.lux-card-media{aspect-ratio:1.28;overflow:hidden;position:relative}.lux-card-media:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(10,10,14,.55))}.lux-card-media img{width:100%;height:100%;object-fit:cover;transition:.7s}.lux-card:hover img{transform:scale(1.045)}.lux-card-body{padding:22px 22px 24px;text-align:center}.lux-card h3{font:600 28px/1 var(--serif);margin:0 0 9px}.lux-card p{font-size:12px;color:var(--muted);margin:0 0 15px}.lux-card-meta{font-size:9px;text-transform:uppercase;letter-spacing:.18em;color:var(--gold);margin-bottom:8px}
/* quick inquiry */
.quick-wrap{padding:36px 0 44px}.quick{display:grid;grid-template-columns:1.4fr repeat(3,1fr) auto;gap:12px;align-items:end;background:#121219;border:1px solid var(--line);padding:22px 24px;box-shadow:var(--shadow)}.quick h3{font:600 30px/1 var(--serif);margin:0 0 7px}.quick p{margin:0;color:var(--muted);font-size:11px}.field label{display:block;color:#85838b;font-size:8px;text-transform:uppercase;letter-spacing:.17em;margin-bottom:6px}.field input,.field select,.form input,.form select,.form textarea{width:100%;background:#1a1a22;border:1px solid rgba(255,255,255,.08);color:#f4f2ee;min-height:48px;padding:12px 14px;border-radius:1px;outline:none}.field input:focus,.field select:focus,.form input:focus,.form select:focus,.form textarea:focus{border-color:var(--gold)}
/* feature icons */
.feature-row{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.feature{padding:30px 20px;text-align:center;border-right:1px solid var(--line)}.feature:last-child{border-right:0}.feature-icon{width:48px;height:48px;margin:0 auto 10px;display:grid;place-items:center;border:1px solid var(--gold-line);color:var(--gold-2);font-size:20px;border-radius:50%}.feature h4{font:600 20px/1 var(--serif);margin:5px 0}.feature p{color:var(--muted);font-size:10px;margin:0}
/* visual split */
.split{display:grid;grid-template-columns:1.12fr .88fr;gap:48px;align-items:center}.split.reverse{grid-template-columns:.88fr 1.12fr}.split-media{position:relative}.split-media img{width:100%;height:560px;object-fit:cover}.split-media:after{content:"";position:absolute;inset:14px -14px -14px 14px;border:1px solid var(--gold-line);z-index:-1}.split-copy h2{font:600 clamp(42px,5vw,64px)/.9 var(--serif);margin:0 0 18px}.split-copy p{color:var(--muted);max-width:540px}.bullets{display:grid;gap:11px;margin:24px 0 30px}.bullets div{display:grid;grid-template-columns:18px 1fr;gap:9px;color:#cac8ce;font-size:13px}.bullets b{color:var(--gold)}
/* mosaic */
.mosaic{display:grid;grid-template-columns:1.05fr .95fr .95fr;grid-template-rows:270px 270px;gap:10px}.mosaic figure{margin:0;position:relative;overflow:hidden;background:#1a1a22}.mosaic figure:first-child{grid-row:1/3}.mosaic img{width:100%;height:100%;object-fit:cover;transition:.7s}.mosaic figure:hover img{transform:scale(1.04)}.mosaic figcaption{position:absolute;left:18px;bottom:14px;color:#fff;font:600 22px/1 var(--serif);text-shadow:0 3px 12px #000}.mosaic figure:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(0,0,0,.55));pointer-events:none}.mosaic figcaption{z-index:2}
/* destination */
.dest-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.dest{min-height:235px;background:linear-gradient(145deg,#181820,#111118);border:1px solid var(--line);padding:26px;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden}.dest:before{content:"";position:absolute;width:180px;height:180px;border:1px solid var(--gold-line);border-radius:50%;right:-70px;top:-70px}.dest span{color:var(--gold);font-size:9px;text-transform:uppercase;letter-spacing:.18em}.dest h3{font:600 31px/1 var(--serif);margin:7px 0 9px}.dest p{color:var(--muted);font-size:11px;margin:0 0 15px}
/* page hero */
.page-hero{height:520px;position:relative;display:flex;align-items:flex-end;padding-bottom:65px;overflow:hidden}.page-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.76)}.page-hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,8,.25),#0d0d12 100%)}.page-hero-content{position:relative;z-index:2}.crumbs{font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:#b5b0aa;margin-bottom:14px}.crumbs a{color:var(--gold)}.page-hero h1{font:600 clamp(48px,7vw,78px)/.9 var(--serif);margin:0;max-width:800px}.page-hero p{max-width:650px;color:#c2c0c5}
/* forms */
.contact-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:22px}.form,.contact-box{background:#14141c;border:1px solid var(--line);padding:28px}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.form label{display:block;color:#98959e;font-size:9px;text-transform:uppercase;letter-spacing:.14em;margin-bottom:14px}.form label span{display:block;margin-bottom:7px}.form textarea{min-height:140px;resize:vertical}.form-status{min-height:20px;color:var(--gold-2);font-size:12px;margin-top:10px}.contact-box h3{font:600 31px/1 var(--serif);margin-top:0}.contact-item{padding:14px 0;border-bottom:1px solid var(--line)}.contact-item small{display:block;color:var(--gold);text-transform:uppercase;letter-spacing:.14em;font-size:8px}.contact-item a,.contact-item span{font-size:13px;color:#dddbe0}.map{width:100%;height:400px;border:0;filter:grayscale(1) contrast(.9) invert(.9);opacity:.78}
/* details */
.amenities{display:grid;grid-template-columns:repeat(2,1fr);gap:11px;margin:24px 0}.amenity{border:1px solid var(--line);padding:13px;color:#c6c4c9;font-size:12px;background:#13131a}.amenity b{color:var(--gold);margin-right:8px}.gallery-columns{columns:3 290px;column-gap:12px}.gallery-columns figure{margin:0 0 12px;break-inside:avoid;overflow:hidden;border:1px solid var(--line)}.gallery-columns img{width:100%;transition:.5s}.gallery-columns figure:hover img{transform:scale(1.025)}.legal{max-width:860px}.legal h2{font:600 32px/1 var(--serif);color:var(--gold-2)}.legal p,.legal li{color:#b9b7be}
/* footer */
.footer{padding:58px 0 28px;background:#09090d;border-top:1px solid var(--line)}.footer-grid{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px}.footer h4{font:600 20px/1 var(--serif);margin:0 0 15px}.footer a,.footer p,.footer small{color:#95929b;font-size:11px}.footer-links{display:grid;gap:9px}.footer-bottom{border-top:1px solid var(--line);margin-top:32px;padding-top:18px;display:flex;justify-content:space-between;gap:20px}.footer-brand{font:600 29px/1 var(--serif);color:#fff}.footer-brand span{color:var(--gold)}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .75s ease,transform .75s ease}.reveal.visible{opacity:1;transform:none}
@media(max-width:1050px){.nav{grid-template-columns:1fr auto}.nav-links{display:none}.nav-actions .btn{display:none}.nav-toggle{display:block}.mobile-panel{position:absolute;top:70px;left:20px;right:20px;background:#101016;border:1px solid var(--line);padding:18px;box-shadow:var(--shadow)}.mobile-panel.open{display:grid;gap:14px}.mobile-panel a{font-size:13px}.card-grid,.dest-grid{grid-template-columns:repeat(2,1fr)}.quick{grid-template-columns:1fr 1fr}.quick-intro{grid-column:1/-1}.quick .btn{width:100%}.split,.split.reverse,.contact-grid{grid-template-columns:1fr}.split-media img{height:440px}.footer-grid{grid-template-columns:1fr 1fr}.feature-row{grid-template-columns:repeat(2,1fr)}.feature:nth-child(2){border-right:0}.feature:nth-child(-n+2){border-bottom:1px solid var(--line)}}
@media(max-width:690px){.container{width:min(calc(100% - 28px),var(--max))}.section{padding:64px 0}.site-header{height:70px}.brand-text strong{font-size:17px}.brand-mark{width:36px;height:36px}.nav-actions .lang{display:none}.hero{min-height:700px}.hero h1{font-size:51px}.hero-kicker{font-size:30px}.hero p{font-size:13px}.card-grid,.dest-grid,.quick,.feature-row,.form-grid,.footer-grid{grid-template-columns:1fr}.feature{border-right:0;border-bottom:1px solid var(--line)}.feature:last-child{border-bottom:0}.quick{padding:18px}.mosaic{grid-template-columns:1fr;grid-template-rows:none}.mosaic figure,.mosaic figure:first-child{height:260px;grid-row:auto}.split-media img{height:340px}.footer-bottom{flex-direction:column}.page-hero{height:460px}.gallery-columns{columns:1}.amenities{grid-template-columns:1fr}}
'''

JS = r'''
(() => {
  const isEN = location.pathname.includes('/en/');
  const base = isEN ? '../' : '';
  const page = location.pathname.split('/').pop() || 'index.html';
  const t = isEN ? {
    home:'Home', apartments:'Apartments', experience:'Experience', gallery:'Gallery', location:'Location', contact:'Contact', inquiry:'Check availability',
    sub:'Luxury Apartments • Orebić', quick:'Quick links', explore:'Explore', legal:'Legal', privacy:'Privacy Policy', terms:'Terms & Conditions',
    phone:'+385 91 730 6770', email:'info@sunnydayorebic.com', address:'Ul. Bana Josipa Jelačića 82, 20250 Orebić, Croatia'
  } : {
    home:'Naslovna', apartments:'Apartmani', experience:'Doživljaji', gallery:'Galerija', location:'Lokacija', contact:'Kontakt', inquiry:'Provjeri dostupnost',
    sub:'Luksuzni apartmani • Orebić', quick:'Brzi linkovi', explore:'Istražite', legal:'Pravno', privacy:'Pravila privatnosti', terms:'Uvjeti korištenja',
    phone:'+385 91 730 6770', email:'info@sunnydayorebic.com', address:'Ul. Bana Josipa Jelačića 82, 20250 Orebić, Hrvatska'
  };
  const href = (name) => base + name;
  const nav = [
    [t.home,'index.html'],[t.apartments,'apartments.html'],[t.experience,'experience.html'],[t.gallery,'gallery.html'],[t.location,'location.html'],[t.contact,'contact.html']
  ];
  const header = document.getElementById('site-header');
  if(header){
    header.innerHTML = `<header class="site-header"><div class="container nav">
      <a class="brand" href="${href('index.html')}"><span class="brand-mark"><span>SD</span></span><span class="brand-text"><strong>Sunny Day Orebić</strong><small>${t.sub}</small></span></a>
      <nav class="nav-links">${nav.map(([label,file])=>`<a class="${page===file?'active':''}" href="${href(file)}">${label}</a>`).join('')}</nav>
      <div class="nav-actions"><span class="lang">${isEN?`<a href="../${page}">HR</a> / <strong>EN</strong>`:`<strong>HR</strong> / <a href="en/${page}">EN</a>`}</span><a class="btn btn--outline" href="${href('contact.html')}">${t.inquiry}</a><button class="nav-toggle" aria-label="Menu">☰</button></div>
      <div class="mobile-panel">${nav.map(([label,file])=>`<a href="${href(file)}">${label}</a>`).join('')}<a href="${href('contact.html')}" style="color:var(--gold)">${t.inquiry}</a>${isEN?`<a href="../${page}">HRVATSKI</a>`:`<a href="en/${page}">ENGLISH</a>`}</div>
    </div></header>`;
    const h=header.querySelector('.site-header');
    const toggle=header.querySelector('.nav-toggle');
    const panel=header.querySelector('.mobile-panel');
    toggle?.addEventListener('click',()=>panel.classList.toggle('open'));
    const scroll=()=>h.classList.toggle('scrolled',scrollY>25);scroll();addEventListener('scroll',scroll,{passive:true});
  }
  const footer=document.getElementById('site-footer');
  if(footer){footer.innerHTML=`<footer class="footer"><div class="container"><div class="footer-grid">
    <div><div class="footer-brand">Sunny Day <span>Orebić</span></div><p>${isEN?'A refined base for sea-view stays, poolside days and discovering the Pelješac peninsula.':'Elegantna baza za boravak uz more, opuštanje uz bazen i otkrivanje Pelješca.'}</p></div>
    <div><h4>${t.quick}</h4><div class="footer-links">${nav.slice(0,4).map(([l,f])=>`<a href="${href(f)}">${l}</a>`).join('')}</div></div>
    <div><h4>${t.explore}</h4><div class="footer-links"><a href="${href('korcula.html')}">Korčula</a><a href="${href('mljet.html')}">Mljet</a><a href="${href('ston.html')}">Ston</a><a href="${href('viganj.html')}">Viganj</a></div></div>
    <div><h4>${t.contact}</h4><div class="footer-links"><a href="tel:+385917306770">${t.phone}</a><a href="mailto:${t.email}">${t.email}</a><small>${t.address}</small></div></div>
    </div><div class="footer-bottom"><small>© ${new Date().getFullYear()} Sunny Day Orebić</small><small><a href="${href('privacy-policy.html')}">${t.privacy}</a> • <a href="${href('terms.html')}">${t.terms}</a></small></div></div></footer>`}
  const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.1});document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
  document.querySelectorAll('.quick-form').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(form);const q=new URLSearchParams();for(const [k,v] of d.entries())if(v)q.set(k,v);location.href=href('contact.html')+'?'+q.toString()}));
  const qs=new URLSearchParams(location.search);['arrival','departure','guests'].forEach(n=>{const el=document.querySelector(`[name="${n}"]`);if(el&&qs.get(n))el.value=qs.get(n)});
  document.querySelectorAll('input[type="date"]').forEach(el=>el.min=new Date().toISOString().slice(0,10));
})();
'''

FORM_JS = r'''
(() => {
  const config = window.SUNNY_DAY_CONFIG || {};
  document.querySelectorAll('.js-contact-form').forEach(form => {
    const status = form.querySelector('.form-status');
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const key = config.web3formsAccessKey;
      if (!key || key === 'YOUR_WEB3FORMS_ACCESS_KEY') {
        status.textContent = document.documentElement.lang === 'hr' ? 'Prije objave unesite Web3Forms access key u assets/js/site-config.js.' : 'Add your Web3Forms access key in assets/js/site-config.js before publishing.';
        return;
      }
      const fd = new FormData(form); fd.set('access_key', key);
      const btn=form.querySelector('button[type="submit"]'); btn.disabled=true; status.textContent='...';
      try{const r=await fetch('https://api.web3forms.com/submit',{method:'POST',body:fd});const j=await r.json();if(j.success){form.reset();status.textContent=document.documentElement.lang==='hr'?'Hvala! Upit je uspješno poslan.':'Thank you! Your inquiry was sent.'}else status.textContent=j.message||'Error';}
      catch(err){status.textContent=document.documentElement.lang==='hr'?'Slanje trenutno nije uspjelo.':'Unable to send right now.'}finally{btn.disabled=false}
    });
  });
})();
'''

CONFIG = """window.SUNNY_DAY_CONFIG={web3formsAccessKey:'YOUR_WEB3FORMS_ACCESS_KEY'};\n"""

(ROOT/'assets/css/style.css').write_text(CSS)
(ROOT/'assets/js/main.js').write_text(JS)
(ROOT/'assets/js/forms.js').write_text(FORM_JS)
(ROOT/'assets/js/site-config.js').write_text(CONFIG)

# shared data
experiences = [
 ('korcula.html','Korčula','Stari grad, šetnja uz more i lagani otočni dan.'),
 ('mljet.html','Mljet','Nacionalni park, slana jezera i mirniji ritam prirode.'),
 ('ston.html','Ston','Povijesne zidine, solana i autentični Pelješac.'),
 ('viganj.html','Viganj','Plaže, vjetar, more i opuštena atmosfera.'),
 ('bacina-lakes.html','Baćinska jezera','Drugačiji krajolik za miran jednodnevni izlet.'),
 ('kravica-waterfalls.html','Kravica','Veći dnevni izlet za goste koji žele prirodnu atrakciju.')]
experiences_en = [
 ('korcula.html','Korčula','Old-town lanes, waterfront walks and an easy island day.'),
 ('mljet.html','Mljet','National park scenery, salt lakes and a slower nature rhythm.'),
 ('ston.html','Ston','Historic walls, salt pans and authentic Pelješac atmosphere.'),
 ('viganj.html','Viganj','Beaches, wind, sea and a relaxed coastal mood.'),
 ('bacina-lakes.html','Baćina Lakes','A quieter freshwater landscape for a scenic day out.'),
 ('kravica-waterfalls.html','Kravica','A bigger day trip for guests looking for dramatic nature.')]


def head(title, desc, lang='hr', base=''):
  return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#0d0d12"><link rel="icon" href="{base}assets/images/favicon.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="{base}assets/css/style.css"><script defer src="{base}assets/js/site-config.js"></script><script defer src="{base}assets/js/main.js"></script><script defer src="{base}assets/js/forms.js"></script></head><body><div id="site-header"></div>'''

def end(): return '<div id="site-footer"></div></body></html>'

def hero(img, kicker, title, desc, lang='hr', base=''):
  contact = 'contact.html'
  apartments = 'apartments.html'
  return f'''<section class="hero"><div class="hero-media"><img src="{base}{img}" alt="Sunny Day Orebić"></div><div class="container hero-content reveal"><p class="hero-kicker">{kicker}</p><h1>{title}</h1><p>{desc}</p><div class="hero-actions"><a class="btn btn--gold" href="{contact}">{'PROVJERI DOSTUPNOST' if lang=='hr' else 'CHECK AVAILABILITY'}</a><a class="btn btn--outline" href="{apartments}">{'POGLEDAJ APARTMANE' if lang=='hr' else 'VIEW APARTMENTS'}</a></div></div><div class="scroll-cue"><span>{'SKROLAJ' if lang=='hr' else 'SCROLL'}</span><i></i></div></section>'''

def pagehero(img,title,desc,crumb,lang='hr',base=''):
  return f'''<section class="page-hero"><img src="{base}{img}" alt=""><div class="container page-hero-content reveal"><div class="crumbs"><a href="index.html">{'Naslovna' if lang=='hr' else 'Home'}</a> / {crumb}</div><h1>{title}</h1><p>{desc}</p></div></section>'''

def quick(lang='hr'):
  if lang=='hr':
    return '''<section class="quick-wrap"><div class="container"><form class="quick quick-form reveal"><div class="quick-intro"><h3>Brza provjera termina</h3><p>Odaberite datume i broj gostiju — ne rezervirate online, nego šaljete upit vlasniku.</p></div><div class="field"><label>Dolazak</label><input type="date" name="arrival" required></div><div class="field"><label>Odlazak</label><input type="date" name="departure" required></div><div class="field"><label>Gosti</label><select name="guests" required><option value="">Odaberite</option><option>1 gost</option><option>2 gosta</option><option>3 gosta</option><option>4 gosta</option><option>5 gostiju</option><option>6+ gostiju</option></select></div><button class="btn btn--gold" type="submit">POŠALJI UPIT</button></form></div></section>'''
  return '''<section class="quick-wrap"><div class="container"><form class="quick quick-form reveal"><div class="quick-intro"><h3>Quick availability check</h3><p>Choose your dates and guests — this sends an inquiry, not an online booking.</p></div><div class="field"><label>Arrival</label><input type="date" name="arrival" required></div><div class="field"><label>Departure</label><input type="date" name="departure" required></div><div class="field"><label>Guests</label><select name="guests" required><option value="">Select</option><option>1 guest</option><option>2 guests</option><option>3 guests</option><option>4 guests</option><option>5 guests</option><option>6+ guests</option></select></div><button class="btn btn--gold" type="submit">SEND INQUIRY</button></form></div></section>'''

def contact_form(lang='hr'):
  if lang=='hr':
    labels=('Ime i prezime','E-mail','Telefon','Broj gostiju','Datum dolaska','Datum odlaska','Poruka','Pošalji upit')
    guestopts=''.join(f'<option>{x}</option>' for x in ['1 gost','2 gosta','3 gosta','4 gosta','5 gostiju','6+ gostiju'])
  else:
    labels=('Full name','Email','Phone','Guests','Arrival date','Departure date','Message','Send inquiry')
    guestopts=''.join(f'<option>{x}</option>' for x in ['1 guest','2 guests','3 guests','4 guests','5 guests','6+ guests'])
  return f'''<form class="form js-contact-form reveal"><div class="form-grid"><label><span>{labels[0]}</span><input name="name" required></label><label><span>{labels[1]}</span><input type="email" name="email" required></label><label><span>{labels[2]}</span><input type="tel" name="phone" placeholder="+385 ..." required></label><label><span>{labels[3]}</span><select name="guests" required><option value="">—</option>{guestopts}</select></label><label><span>{labels[4]}</span><input type="date" name="arrival" required></label><label><span>{labels[5]}</span><input type="date" name="departure" required></label></div><label><span>{labels[6]}</span><textarea name="message"></textarea></label><input type="hidden" name="subject" value="Sunny Day Orebić - Availability inquiry"><button class="btn btn--gold" type="submit">{labels[7]}</button><div class="form-status"></div></form>'''

# HR HOME
home_hr = head('Sunny Day Orebić | Luksuzni apartmani u Orebiću','Premium apartmani u Orebiću s bazenom, modernim interijerom i izravnim upitom za dostupnost.')
home_hr += hero('assets/images/living-dining-large-window.avif','Dobro došli u','Luksuz, mir &amp; Jadran','Moderni apartmani u Orebiću predstavljeni u tamnijem, elegantnom boutique stilu — s naglaskom na fotografije, atmosferu i izravan kontakt.','hr')
home_hr += '''<main><section class="section section--alt"><div class="container center reveal"><p class="eyebrow">Sunny Day Orebić</p><h2 class="section-title">Smještaj koji izgleda <em>vrijedno vašeg odmora.</em></h2><p class="section-lead">Novi dizajn odbacuje generičan turistički izgled i preuzima ozbiljniji hotelski smjer: tamne površine, zlatni detalji, jasne sekcije i snažne stvarne fotografije objekta.</p><div class="rule"></div></div></section>
<section class="section section--raised"><div class="container"><div class="center reveal" style="margin-bottom:32px"><p class="eyebrow">Smještaj & doživljaj</p><h2 class="section-title">Odaberite svoj <em>Sunny Day</em></h2></div><div class="card-grid">
<article class="lux-card reveal"><div class="lux-card-media"><img src="assets/images/living-dining-roundtable.avif" alt="Apartman s pogledom na more"></div><div class="lux-card-body"><div class="lux-card-meta">Pogled na more • moderan interijer</div><h3>Apartman s pogledom na more</h3><p>Svijetao interijer, privatni vanjski prostor i atmosfera stvorena za sporiji ritam odmora.</p><a class="text-link" href="apartment-sea-view.html">Pogledaj apartman <span>→</span></a></div></article>
<article class="lux-card reveal"><div class="lux-card-media"><img src="assets/images/bedroom-double-soft.avif" alt="Apartman s dvije spavaće sobe"></div><div class="lux-card-body"><div class="lux-card-meta">Prostran raspored • obiteljski boravak</div><h3>Apartman s dvije spavaće sobe</h3><p>Više prostora za parove, obitelji i goste koji žele udobnost tijekom duljeg boravka.</p><a class="text-link" href="apartment-two-bedroom.html">Pogledaj apartman <span>→</span></a></div></article>
<article class="lux-card reveal"><div class="lux-card-media"><img src="assets/images/pool-loungers-day.avif" alt="Bazen i terasa"></div><div class="lux-card-body"><div class="lux-card-meta">Bazen • terasa • odmor</div><h3>Bazen & vanjski prostor</h3><p>Dio iskustva koji najbrže stvara želju za boravkom — sunce, ležaljke i opušteni mediteranski dani.</p><a class="text-link" href="gallery.html">Otvori galeriju <span>→</span></a></div></article>
</div></div></section>'''
home_hr += quick('hr')
home_hr += '''<section class="section section--alt"><div class="container feature-row reveal"><div class="feature"><div class="feature-icon">✦</div><h4>Pogled na more</h4><p>Vizual koji odmah prodaje osjećaj lokacije.</p></div><div class="feature"><div class="feature-icon">◉</div><h4>Bazen</h4><p>Opuštanje uz bazen kao važan dio boravka.</p></div><div class="feature"><div class="feature-icon">◇</div><h4>Moderan interijer</h4><p>Čiste linije, svjetlo i udobni prostori.</p></div><div class="feature"><div class="feature-icon">⌖</div><h4>Orebić</h4><p>Odlična baza za Pelješac i Korčulu.</p></div></div></section>
<section class="section"><div class="container split"><div class="split-media reveal"><img src="assets/images/terrace-sofa-view.avif" alt="Terasa Sunny Day Orebić"></div><div class="split-copy reveal"><p class="eyebrow">Premium dojam bez pretjerivanja</p><h2>Više boutique hotel, manje <em>klasični apartmanski web.</em></h2><p>Fotografije dobivaju dominantnu ulogu, tekst je kraći i precizniji, a korisnik uvijek vidi sljedeći logičan korak — apartman, galeriju, lokaciju ili upit za termin.</p><div class="bullets"><div><b>01</b><span>Velike stvarne fotografije bez nepotrebnog ponavljanja.</span></div><div><b>02</b><span>Tamna luksuzna paleta bez krem pozadina.</span></div><div><b>03</b><span>Suptilne animacije umjesto napadnih 3D efekata.</span></div></div><a class="btn btn--outline" href="gallery.html">POGLEDAJ GALERIJU</a></div></div></section>
<section class="section section--raised"><div class="container"><div class="center reveal" style="margin-bottom:30px"><p class="eyebrow">Fotografije koje prodaju osjećaj</p><h2 class="section-title">Prostor, detalji &amp; <em>atmosfera.</em></h2></div><div class="mosaic reveal"><figure><img src="assets/images/pool-wide-day.avif" alt="Bazen"><figcaption>Bazen</figcaption></figure><figure><img src="assets/images/kitchen-dining-openplan.avif" alt="Kuhinja"><figcaption>Interijer</figcaption></figure><figure><img src="assets/images/terrace-lounger-sea.avif" alt="Terasa"><figcaption>Terasa</figcaption></figure><figure><img src="assets/images/bedroom-sea-view.avif" alt="Spavaća soba"><figcaption>Udobnost</figcaption></figure><figure><img src="assets/images/exterior-night-landscape.avif" alt="Objekt noću"><figcaption>Večernji ugođaj</figcaption></figure></div></div></section>
<section class="section section--alt"><div class="container"><div class="center reveal" style="margin-bottom:30px"><p class="eyebrow">Istražite okolicu</p><h2 class="section-title">Jedan boravak. <em>Mnogo razloga za ostati.</em></h2><p class="section-lead">Posebne podstranice vode goste prema mjestima i izletima u okolici, bez zatrpavanja naslovnice.</p></div><div class="dest-grid">'''
for f,n,d in experiences:
  home_hr += f'<article class="dest reveal"><span>Izlet iz Orebića</span><h3>{n}</h3><p>{d}</p><a class="text-link" href="{f}">Istraži <span>→</span></a></article>'
home_hr += '''</div></div></section></main>''' + end()
(ROOT/'index.html').write_text(home_hr)

# EN HOME
home_en = head('Sunny Day Orebić | Luxury Apartments in Orebić','Premium apartments in Orebić with pool, modern interiors and direct availability inquiries.','en','../')
home_en += hero('../assets/images/living-dining-large-window.avif','Welcome to','Luxury, calm &amp; the Adriatic','Modern apartments in Orebić presented with a darker boutique-hotel aesthetic — focused on real photography, atmosphere and direct contact.','en','')
home_en += '''<main><section class="section section--alt"><div class="container center reveal"><p class="eyebrow">Sunny Day Orebić</p><h2 class="section-title">A stay that feels <em>worth your holiday.</em></h2><p class="section-lead">The new direction drops the generic rental look and moves toward a refined hotel aesthetic: dark surfaces, gold accents, clear structure and strong real property photography.</p><div class="rule"></div></div></section>
<section class="section section--raised"><div class="container"><div class="center reveal" style="margin-bottom:32px"><p class="eyebrow">Stay & experience</p><h2 class="section-title">Choose your <em>Sunny Day</em></h2></div><div class="card-grid">
<article class="lux-card reveal"><div class="lux-card-media"><img src="../assets/images/living-dining-roundtable.avif" alt="Sea view apartment"></div><div class="lux-card-body"><div class="lux-card-meta">Sea view • modern interior</div><h3>Sea View Apartment</h3><p>Bright interiors, outdoor space and an atmosphere designed for slower Mediterranean days.</p><a class="text-link" href="apartment-sea-view.html">View apartment <span>→</span></a></div></article>
<article class="lux-card reveal"><div class="lux-card-media"><img src="../assets/images/bedroom-double-soft.avif" alt="Two bedroom apartment"></div><div class="lux-card-body"><div class="lux-card-meta">Spacious layout • family stay</div><h3>Two-Bedroom Apartment</h3><p>More space for couples, families and guests who value comfort during a longer stay.</p><a class="text-link" href="apartment-two-bedroom.html">View apartment <span>→</span></a></div></article>
<article class="lux-card reveal"><div class="lux-card-media"><img src="../assets/images/pool-loungers-day.avif" alt="Pool and terrace"></div><div class="lux-card-body"><div class="lux-card-meta">Pool • terrace • relaxation</div><h3>Pool & Outdoor Living</h3><p>Sun, loungers and relaxed poolside moments that make the property feel like a complete holiday experience.</p><a class="text-link" href="gallery.html">Open gallery <span>→</span></a></div></article>
</div></div></section>'''
home_en += quick('en')
home_en += '''<section class="section section--alt"><div class="container feature-row reveal"><div class="feature"><div class="feature-icon">✦</div><h4>Sea views</h4><p>A strong visual reason to choose the location.</p></div><div class="feature"><div class="feature-icon">◉</div><h4>Swimming pool</h4><p>Poolside relaxation as part of the stay.</p></div><div class="feature"><div class="feature-icon">◇</div><h4>Modern interiors</h4><p>Clean lines, light and comfortable spaces.</p></div><div class="feature"><div class="feature-icon">⌖</div><h4>Orebić</h4><p>A great base for Pelješac and Korčula.</p></div></div></section>
<section class="section"><div class="container split"><div class="split-media reveal"><img src="../assets/images/terrace-sofa-view.avif" alt="Sunny Day terrace"></div><div class="split-copy reveal"><p class="eyebrow">Premium without excess</p><h2>More boutique hotel, less <em>generic apartment website.</em></h2><p>Photography takes the lead, copy is shorter and more confident, and every section gives the guest a clear next move: explore an apartment, see the gallery, check the location or send an inquiry.</p><div class="bullets"><div><b>01</b><span>Large real property photos without needless repetition.</span></div><div><b>02</b><span>Dark luxury palette with no cream backgrounds.</span></div><div><b>03</b><span>Subtle motion instead of distracting 3D effects.</span></div></div><a class="btn btn--outline" href="gallery.html">VIEW GALLERY</a></div></div></section>
<section class="section section--raised"><div class="container"><div class="center reveal" style="margin-bottom:30px"><p class="eyebrow">Photography that sells the mood</p><h2 class="section-title">Space, detail &amp; <em>atmosphere.</em></h2></div><div class="mosaic reveal"><figure><img src="../assets/images/pool-wide-day.avif" alt="Pool"><figcaption>Pool</figcaption></figure><figure><img src="../assets/images/kitchen-dining-openplan.avif" alt="Kitchen"><figcaption>Interior</figcaption></figure><figure><img src="../assets/images/terrace-lounger-sea.avif" alt="Terrace"><figcaption>Terrace</figcaption></figure><figure><img src="../assets/images/bedroom-sea-view.avif" alt="Bedroom"><figcaption>Comfort</figcaption></figure><figure><img src="../assets/images/exterior-night-landscape.avif" alt="Evening exterior"><figcaption>Evening mood</figcaption></figure></div></div></section>
<section class="section section--alt"><div class="container"><div class="center reveal" style="margin-bottom:30px"><p class="eyebrow">Explore nearby</p><h2 class="section-title">One stay. <em>More reasons to linger.</em></h2><p class="section-lead">Dedicated subpages introduce nearby places and day trips without crowding the homepage.</p></div><div class="dest-grid">'''
for f,n,d in experiences_en:
  home_en += f'<article class="dest reveal"><span>Day trip from Orebić</span><h3>{n}</h3><p>{d}</p><a class="text-link" href="{f}">Explore <span>→</span></a></article>'
home_en += '</div></div></section></main>'+end()
(ROOT/'en/index.html').write_text(home_en)

# Generic pages generator
apt_data_hr=[
 ('apartment-sea-view.html','Apartman s pogledom na more','Svijetao, moderan prostor s vanjskim dijelom i snažnim osjećajem jadranskog odmora.','assets/images/living-dining-roundtable.avif',['Pogled na more i okolinu','Moderan dnevni prostor','Opremljena kuhinja','Klimatizacija','Wi‑Fi','Privatna kupaonica'],['assets/images/living-dining-roundtable.avif','assets/images/terrace-sofa-view.avif','assets/images/kitchen-dining-openplan.avif','assets/images/bedroom-double.avif','assets/images/bathroom-basin.avif']),
 ('apartment-two-bedroom.html','Apartman s dvije spavaće sobe','Prostraniji raspored za obitelji, parove i goste koji žele više privatnosti i udobnosti.','assets/images/bedroom-double-soft.avif',['Dvije spavaće sobe','Prostrani dnevni dio','Terasa / vanjski prostor','Opremljena kuhinja','Klimatizacija','Wi‑Fi'],['assets/images/bedroom-double-soft.avif','assets/images/bedroom-twins.avif','assets/images/living-dining-sea.avif','assets/images/terrace-sofa-day.avif','assets/images/bathroom-laundry.avif'])]
apt_data_en=[
 ('apartment-sea-view.html','Sea View Apartment','A bright modern space with outdoor living and a strong Adriatic holiday atmosphere.','../assets/images/living-dining-roundtable.avif',['Sea and surrounding views','Modern living area','Equipped kitchen','Air conditioning','Wi‑Fi','Private bathroom'],['../assets/images/living-dining-roundtable.avif','../assets/images/terrace-sofa-view.avif','../assets/images/kitchen-dining-openplan.avif','../assets/images/bedroom-double.avif','../assets/images/bathroom-basin.avif']),
 ('apartment-two-bedroom.html','Two-Bedroom Apartment','A roomier layout for families, couples and guests who value extra privacy and comfort.','../assets/images/bedroom-double-soft.avif',['Two bedrooms','Spacious living area','Terrace / outdoor area','Equipped kitchen','Air conditioning','Wi‑Fi'],['../assets/images/bedroom-double-soft.avif','../assets/images/bedroom-twins.avif','../assets/images/living-dining-sea.avif','../assets/images/terrace-sofa-day.avif','../assets/images/bathroom-laundry.avif'])]

def apartment_page(data,lang='hr'):
  f,title,desc,heroimg,amen,imgs=data
  base='' if lang=='hr' else '../'
  page=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(heroimg,title,desc,'Apartmani' if lang=='hr' else 'Apartments',lang,'')
  page+='<main><section class="section"><div class="container split"><div class="split-copy reveal"><p class="eyebrow">'+('Detalji apartmana' if lang=='hr' else 'Apartment details')+'</p><h2>'+('Udobnost bez vizualne gužve.' if lang=='hr' else 'Comfort without visual clutter.')+'</h2><p>'+desc+'</p><div class="amenities">'+''.join(f'<div class="amenity"><b>✓</b>{x}</div>' for x in amen)+'</div><a class="btn btn--gold" href="contact.html">'+('PROVJERI DOSTUPNOST' if lang=='hr' else 'CHECK AVAILABILITY')+'</a></div><div class="split-media reveal"><img src="'+imgs[1]+'" alt=""></div></div></section><section class="section section--raised"><div class="container"><div class="center reveal" style="margin-bottom:28px"><p class="eyebrow">Galerija</p><h2 class="section-title">'+('Pogledajte prostor izbliza.' if lang=='hr' else 'See the space up close.')+'</h2></div><div class="gallery-columns">'+''.join(f'<figure class="reveal"><img src="{i}" alt="{title}"></figure>' for i in imgs)+'</div></div></section>'+quick(lang)+'</main>'+end()
  return page
for d in apt_data_hr:(ROOT/d[0]).write_text(apartment_page(d,'hr'))
for d in apt_data_en:(ROOT/'en'/d[0]).write_text(apartment_page(d,'en'))

# Apartments overview
for lang,base,out in [('hr','',ROOT/'apartments.html'),('en','../',ROOT/'en/apartments.html')]:
  hr=lang=='hr'; title='Apartmani' if hr else 'Apartments'; desc='Odaberite smještaj i pošaljite izravan upit za željene datume.' if hr else 'Choose your stay and send a direct inquiry for your preferred dates.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/terrace-sofa-glass.avif',title,desc,title,lang,'')
  p+='<main><section class="section section--raised"><div class="container"><div class="card-grid">'
  cards=[('assets/images/living-dining-roundtable.avif','Apartman s pogledom na more','apartment-sea-view.html','Moderan interijer, vanjski prostor i jadranski ugođaj.') ,('assets/images/bedroom-double-soft.avif','Apartman s dvije spavaće sobe','apartment-two-bedroom.html','Više prostora za obitelji i dulji boravak.'),('assets/images/pool-loungers-day.avif','Bazen & terasa','gallery.html','Sunčani vanjski prostor kao dio premium iskustva.')] if hr else [('assets/images/living-dining-roundtable.avif','Sea View Apartment','apartment-sea-view.html','Modern interior, outdoor living and an Adriatic mood.'),('assets/images/bedroom-double-soft.avif','Two-Bedroom Apartment','apartment-two-bedroom.html','More space for families and longer stays.'),('assets/images/pool-loungers-day.avif','Pool & Terrace','gallery.html','Sunny outdoor space as part of the premium experience.')]
  for img,n,f,d in cards:
    p+=f'<article class="lux-card reveal"><div class="lux-card-media"><img src="{base}{img}" alt="{n}"></div><div class="lux-card-body"><h3>{n}</h3><p>{d}</p><a class="text-link" href="{f}">{"Pogledaj" if hr else "View"} <span>→</span></a></div></article>'
  p+='</div></div></section>'+quick(lang)+'</main>'+end();out.write_text(p)

# gallery
imgs=['pool-wide-day.avif','terrace-sofa-view.avif','living-dining-roundtable.avif','bedroom-double-soft.avif','kitchen-dining-openplan.avif','pool-fruit-detail.avif','terrace-lounger-sea.avif','bedroom-sea-view.avif','exterior-night-front.avif','living-dining-sea.avif','bathroom-basin.avif','exterior-front-flowers.avif','pool-waterline.avif','terrace-sofa-glass.avif','exterior-night-landscape.avif']
for lang,base,out in [('hr','',ROOT/'gallery.html'),('en','../',ROOT/'en/gallery.html')]:
  hr=lang=='hr';title='Galerija' if hr else 'Gallery';desc='Pažljivo odabrane fotografije objekta, apartmana, bazena i terasa.' if hr else 'A curated selection of the property, apartments, pool and terraces.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/exterior-night-front.avif',title,desc,title,lang,'')
  p+='<main><section class="section"><div class="container gallery-columns">'+''.join(f'<figure class="reveal"><img src="{base}assets/images/{i}" alt="Sunny Day Orebić"></figure>' for i in imgs)+'</div></section>'+quick(lang)+'</main>'+end();out.write_text(p)

# experience overview and destination pages
for lang,base,out,exp in [('hr','',ROOT/'experience.html',experiences),('en','../',ROOT/'en/experience.html',experiences_en)]:
  hr=lang=='hr';title='Doživljaji & izleti' if hr else 'Experiences & Day Trips';desc='Ideje za izlete i mjesta koja gosti mogu otkriti tijekom boravka u Orebiću.' if hr else 'Ideas for places and day trips guests can discover while staying in Orebić.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/orebic-harbor-twilight.avif',title,desc,title,lang,'')
  p+='<main><section class="section section--alt"><div class="container dest-grid">'+''.join(f'<article class="dest reveal"><span>{"Izlet iz Orebića" if hr else "Day trip from Orebić"}</span><h3>{n}</h3><p>{d}</p><a class="text-link" href="{f}">{"Istraži" if hr else "Explore"} <span>→</span></a></article>' for f,n,d in exp)+'</div></section>'+quick(lang)+'</main>'+end();out.write_text(p)

# destination detail, uses Orebić contextual imagery but does not claim it is destination photo
for lang,base,exp in [('hr','',experiences),('en','../',experiences_en)]:
  hr=lang=='hr';heroimg=base+'assets/images/orebic-harbor-day.avif'
  tips_hr='Ovu podstranicu koristimo kao inspiraciju za planiranje izleta. Prije polaska preporučuje se provjeriti aktualne vozne redove, ulaznice i uvjete putovanja.'
  tips_en='This page is intended as trip inspiration. Before setting out, guests should check current timetables, tickets and travel conditions.'
  for f,n,d in exp:
    desc=d
    p=head(f'{n} | Sunny Day Orebić',desc,lang,base)+pagehero(heroimg,n,desc,'Doživljaji' if hr else 'Experiences',lang,'')
    p+='<main><section class="section"><div class="container split"><div class="split-media reveal"><img src="'+base+'assets/images/view-aerial-sea.avif" alt="Pelješac i Jadran"></div><div class="split-copy reveal"><p class="eyebrow">'+('Ideja za izlet' if hr else 'Day-trip idea')+'</p><h2>'+('Još jedan razlog za dulji boravak u Orebiću.' if hr else 'Another reason to stay longer in Orebić.')+'</h2><p>'+d+'</p><div class="bullets"><div><b>01</b><span>'+('Planirajte izlet prema vremenu i sezoni.' if hr else 'Plan around the weather and season.')+'</span></div><div><b>02</b><span>'+('Ostavite dovoljno vremena za opušten povratak.' if hr else 'Leave enough time for a relaxed return.')+'</span></div><div><b>03</b><span>'+('Kombinirajte izlet s lokalnom gastronomijom.' if hr else 'Pair the trip with local food and wine.')+'</span></div></div></div></div></section><section class="section section--alt"><div class="container legal reveal"><h2>'+('Praktična napomena' if hr else 'Practical note')+'</h2><p>'+(tips_hr if hr else tips_en)+'</p></div></section>'+quick(lang)+'</main>'+end()
    (ROOT/f if hr else ROOT/'en'/f).write_text(p)

# location
for lang,base,out in [('hr','',ROOT/'location.html'),('en','../',ROOT/'en/location.html')]:
  hr=lang=='hr';title='Lokacija' if hr else 'Location';desc='Sunny Day Orebić nalazi se u Orebiću, na Pelješcu, s dobrim polazištem za more, grad i izlete.' if hr else 'Sunny Day Orebić is located in Orebić on the Pelješac peninsula, well placed for the sea, town and day trips.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/view-aerial-coast.avif',title,desc,title,lang,'')
  p+='<main><section class="section"><div class="container split"><div class="split-copy reveal"><p class="eyebrow">Orebić • Pelješac</p><h2>'+('Baza za more, Korčulu i Pelješac.' if hr else 'A base for the sea, Korčula and Pelješac.')+'</h2><p>'+desc+'</p><div class="bullets"><div><b>01</b><span>'+('Blizina svakodnevnih sadržaja i obale.' if hr else 'Convenient access to the coast and everyday essentials.')+'</span></div><div><b>02</b><span>'+('Jednostavno polazište za okolne izlete.' if hr else 'An easy starting point for nearby trips.')+'</span></div><div><b>03</b><span>'+('Mirniji smještaj uz dobru povezanost.' if hr else 'A calmer stay with useful connections.')+'</span></div></div></div><div class="split-media reveal"><img src="'+base+'assets/images/orebic-harbor-day.avif" alt="Orebić"></div></div></section><section class="section section--alt"><div class="container"><iframe class="map" loading="lazy" src="https://www.google.com/maps?q=Ul.%20Bana%20Josipa%20Jela%C4%8Di%C4%87a%2082,%2020250%20Orebi%C4%87,%20Croatia&output=embed"></iframe></div></section>'+quick(lang)+'</main>'+end();out.write_text(p)

# contact
for lang,base,out in [('hr','',ROOT/'contact.html'),('en','../',ROOT/'en/contact.html')]:
  hr=lang=='hr';title='Kontakt & dostupnost' if hr else 'Contact & Availability';desc='Pošaljite datume, broj gostiju i kontakt podatke kako bi vlasnik provjerio dostupnost.' if hr else 'Send your dates, guest count and contact details so the owner can check availability.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/terrace-sofa-view.avif',title,desc,title,lang,'')
  p+='<main><section class="section"><div class="container contact-grid">'+contact_form(lang)+f'''<aside class="contact-box reveal"><p class="eyebrow">{'Izravni kontakt' if hr else 'Direct contact'}</p><h3>{'Bez online bookinga. Samo jednostavan upit.' if hr else 'No online booking. Just a simple inquiry.'}</h3><div class="contact-item"><small>{'Telefon' if hr else 'Phone'}</small><a href="tel:+385917306770">+385 91 730 6770</a></div><div class="contact-item"><small>E-mail</small><a href="mailto:info@sunnydayorebic.com">info@sunnydayorebic.com</a></div><div class="contact-item"><small>{'Adresa' if hr else 'Address'}</small><span>Ul. Bana Josipa Jelačića 82, 20250 Orebić</span></div><div class="contact-item"><small>WhatsApp</small><a href="https://wa.me/385917306770" target="_blank" rel="noreferrer">{'Otvori razgovor' if hr else 'Open chat'}</a></div></aside></div></section></main>'''+end();out.write_text(p)

# about optional
for lang,base,out in [('hr','',ROOT/'about.html'),('en','../',ROOT/'en/about.html')]:
  hr=lang=='hr';title='O Sunny Day Orebiću' if hr else 'About Sunny Day Orebić';desc='Moderan smještaj u Orebiću predstavljen kroz premium boutique-hotel vizualni smjer.' if hr else 'Modern accommodation in Orebić presented through a refined boutique-hotel visual direction.'
  p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/exterior-aerial-building.avif',title,desc,title,lang,'')
  p+='<main><section class="section"><div class="container split"><div class="split-media reveal"><img src="'+base+'assets/images/exterior-front-flowers.avif" alt="Sunny Day Orebić"></div><div class="split-copy reveal"><p class="eyebrow">Sunny Day Orebić</p><h2>'+('Moderni odmor predstavljen ozbiljnije i elegantnije.' if hr else 'A modern stay presented with more confidence and elegance.')+'</h2><p>'+desc+'</p></div></div></section>'+quick(lang)+'</main>'+end();out.write_text(p)

# legal
for lang,base in [('hr',''),('en','../')]:
  hr=lang=='hr'
  for file,title in [('privacy-policy.html','Pravila privatnosti' if hr else 'Privacy Policy'),('terms.html','Uvjeti korištenja' if hr else 'Terms & Conditions')]:
    desc=('Predložak pravne stranice koji prije objave treba uskladiti s konačnim podacima vlasnika.' if hr else 'A legal-page template to be updated with the owner’s final approved information before publishing.')
    p=head(f'{title} | Sunny Day Orebić',desc,lang,base)+pagehero(base+'assets/images/exterior-night-aerial.avif',title,desc,title,lang,'')
    p+='<main><section class="section"><div class="container legal reveal"><h2>'+('Važna napomena' if hr else 'Important note')+'</h2><p>'+desc+'</p><p>'+('Stranica je dizajnerski pripremljena, ali pravni tekst treba zamijeniti konačnim sadržajem klijenta prije produkcijske objave.' if hr else 'The page is visually prepared, but the legal copy should be replaced with the client’s final wording before production launch.')+'</p></div></section></main>'+end();(ROOT/file if hr else ROOT/'en'/file).write_text(p)

# redirects and robots
(ROOT/'_redirects').write_text('''/apartman-s-pogledom-na-more/ /apartment-sea-view.html 301\n/apartman-s-dvije-spavace-sobe/ /apartment-two-bedroom.html 301\n/smjestaj-orebic/ /apartments.html 301\n/galerija-apartmani-orebic/ /gallery.html 301\n/mjesta-u-blizini/ /experience.html 301\n/kontakt-sunny-day-orebic/ /contact.html 301\n/o-nama-sunny-day-apartmani/ /about.html 301\n''')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://www.sunnydayorebic.com/sitemap.xml\n')
# sitemap
pages=['index.html','apartments.html','apartment-sea-view.html','apartment-two-bedroom.html','gallery.html','experience.html','location.html','contact.html','about.html']+[x[0] for x in experiences]
urls=''.join(f'<url><loc>https://www.sunnydayorebic.com/{p}</loc></url>' for p in pages)+''.join(f'<url><loc>https://www.sunnydayorebic.com/en/{p}</loc></url>' for p in pages)
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
(ROOT/'README.txt').write_text('''SUNNY DAY OREBIĆ — NEW DARK LUXURY REDESIGN\n\nSmjer: inspiriran referentnim Majestic Hotel Pinterest vizualom, ali prilagođen Sunny Day Orebiću i stvarnim fotografijama objekta.\n\nStruktura:\n- HR je glavni jezik (root)\n- EN je u /en/\n- 2 stvarna glavna tipa apartmana s postojećeg weba\n- galerija, lokacija, kontakt, iskustva/izleti i legalne podstranice\n- quick availability forma NE rezervira online; vodi na kontakt/upit\n\nKontakt forma:\n- u assets/js/site-config.js zamijeni YOUR_WEB3FORMS_ACCESS_KEY stvarnim Web3Forms ključem\n\nCloudflare Pages:\n- bez build command-a\n- output: root projekta\n\nNapomena:\n- Pravne tekstove zamijeniti finalnim tekstom vlasnika prije objave.\n''')
print('built', len(list(ROOT.rglob('*.html'))), 'html files')
