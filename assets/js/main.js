(function(){
  const config = window.SUNNY_DAY_CONFIG || {};
  const path = location.pathname;
  const isHR = path.includes('/hr/');
  const current = path.split('/').pop() || 'index.html';
  const nav = isHR ? [
    ['Početna','index.html'],
    ['Apartmani','apartments.html'],
    ['Doživljaji','experience.html'],
    ['Galerija','gallery.html'],
    ['Lokacija','location.html'],
    ['Kontakt','contact.html']
  ] : [
    ['Home','index.html'],
    ['Apartments','apartments.html'],
    ['Experience','experience.html'],
    ['Gallery','gallery.html'],
    ['Location','location.html'],
    ['Contact','contact.html']
  ];
  const copy = isHR ? {
    sub:'Apartmani • Pelješac', whatsapp:'WhatsApp', check:'Provjeri dostupnost', call:'Nazovi', inquiry:'Upit', quick:'Brzi linkovi', exp:'Doživljaji', contact:'Kontakt',
    desc:'Moderni apartmani s pogledom na more, bazenom i izvrsnom lokacijom za istraživanje Orebića, Korčule i Pelješca.',
    korcula:'Stari grad Korčula', mljet:'Mljet i slana jezera', ston:'Stonske zidine i solana', viganj:'Viganj i plaže', rights:'Sva prava pridržana.', privacy:'Pravila privatnosti', terms:'Uvjeti korištenja', direct:'Izravni boravak sa stilom'
  } : {
    sub:'Apartments • Pelješac', whatsapp:'WhatsApp', check:'Check availability', call:'Call', inquiry:'Inquiry', quick:'Quick links', exp:'Experiences', contact:'Contact',
    desc:'Mediterranean apartments with sea views, pool access and a calm base for exploring Orebić, Korčula and the Pelješac peninsula.',
    korcula:'Korčula Old Town', mljet:'Mljet salt lakes', ston:'Ston walls & salt pans', viganj:'Viganj & beaches', rights:'All rights reserved.', privacy:'Privacy Policy', terms:'Terms & Conditions', direct:'Direct stays with style'
  };
  const header = document.getElementById('site-header');
  const footer = document.getElementById('site-footer');
  const phoneHref = `tel:${(config.phone || '').replace(/\s+/g,'')}`;
  const whatsappHref = config.whatsapp ? `https://wa.me/${config.whatsapp}` : '#';
  const enTarget = isHR ? `../${current}` : current;
  const hrTarget = isHR ? current : `hr/${current}`;
  const langSwitch = `<span class="lang-switch"><a class="${isHR?'':'is-active'}" href="${enTarget}" hreflang="en">EN</a><a class="${isHR?'is-active':''}" href="${hrTarget}" hreflang="hr">HR</a></span>`;
  if (header) {
    header.innerHTML = `
      <header class="site-header">
        <div class="container nav-wrap">
          <a class="brand" href="index.html" aria-label="Sunny Day Orebić">
            <span class="brand__mark"><img src="${isHR?'../':''}assets/images/sun-mark.svg" alt="" width="22" height="22"></span>
            <span><span class="brand__name">Sunny Day Orebić</span><span class="brand__sub">${copy.sub}</span></span>
          </a>
          <nav class="nav-links" aria-label="Main navigation">${nav.map(([label,href])=>`<a class="${href===current?'is-active':''}" href="${href}">${label}</a>`).join('')}</nav>
          <div class="nav-cta">
            ${langSwitch}
            <a class="nav-contact" href="${phoneHref}">${config.phone||''}</a>
            <a class="btn btn--ghost" href="${whatsappHref}" target="_blank" rel="noreferrer">${copy.whatsapp}</a>
            <button class="nav-toggle" type="button" aria-label="Menu">☰</button>
          </div>
          <div class="nav-panel" hidden>
            <nav class="nav-links" aria-label="Mobile navigation">${nav.map(([label,href])=>`<a class="${href===current?'is-active':''}" href="${href}">${label}</a>`).join('')}</nav>
            ${langSwitch}
            <a class="nav-contact" href="${phoneHref}">${config.phone||''}</a>
            <div style="margin-top:1rem;display:flex;gap:.75rem;flex-wrap:wrap;"><a class="btn btn--primary" href="contact.html">${copy.check}</a><a class="btn btn--ghost" href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a></div>
          </div>
        </div>
      </header>`;
    const siteHeader=header.querySelector('.site-header'), navToggle=header.querySelector('.nav-toggle'), navPanel=header.querySelector('.nav-panel');
    if(navToggle&&navPanel&&siteHeader){navToggle.addEventListener('click',()=>{siteHeader.classList.toggle('is-open');const o=siteHeader.classList.contains('is-open');navPanel.hidden=!o;});}
  }
  if (footer) {
    footer.innerHTML = `<footer class="footer"><div class="container"><div class="footer-grid">
      <div><div class="brand" style="margin-bottom:1rem;"><span class="brand__mark"><img src="${isHR?'../':''}assets/images/sun-mark.svg" alt="" width="22" height="22"></span><span><span class="brand__name" style="font-size:1.7rem;">Sunny Day Orebić</span><span class="brand__sub">${copy.direct}</span></span></div><p>${copy.desc}</p></div>
      <div><h4>${copy.quick}</h4><div class="footer-links">${nav.map(([label,href])=>`<a href="${href}">${label}</a>`).join('')}</div></div>
      <div><h4>${copy.exp}</h4><div class="footer-links"><a href="korcula.html">${copy.korcula}</a><a href="mljet.html">${copy.mljet}</a><a href="ston.html">${copy.ston}</a><a href="viganj.html">${copy.viganj}</a></div></div>
      <div><h4>${copy.contact}</h4><div class="footer-links"><a href="${phoneHref}">${config.phone||''}</a><a href="mailto:${config.email||''}">${config.email||''}</a><a href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a><small>${isHR ? (config.address||'').replace('Croatia','Hrvatska') : (config.address||'')}</small></div></div>
      </div><div class="footer-bottom"><small>© <span id="year"></span> Sunny Day Orebić. ${copy.rights}</small><small><a href="privacy-policy.html">${copy.privacy}</a> • <a href="terms.html">${copy.terms}</a></small></div></div></footer>`;
  }
  const mobileCta=document.getElementById('mobile-cta');
  if(mobileCta) mobileCta.innerHTML=`<div class="mobile-cta__bar"><a href="contact.html">${copy.inquiry}</a><a href="${phoneHref}">${copy.call}</a><a href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a></div>`;
  const onScroll=()=>document.body.classList.toggle('is-scrolled',window.scrollY>20);onScroll();window.addEventListener('scroll',onScroll,{passive:true});
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting) entry.target.classList.add('is-visible');}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
  document.querySelectorAll('.js-phone-link').forEach(a=>a.href=phoneHref);document.querySelectorAll('.js-email-link').forEach(a=>a.href=`mailto:${config.email||''}`);document.querySelectorAll('.js-whatsapp-link').forEach(a=>a.href=whatsappHref);const year=document.getElementById('year');if(year)year.textContent=new Date().getFullYear();
})();