
(() => {
  const isEN = location.pathname.includes('/en/');
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
  const href = (name) => name;
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
