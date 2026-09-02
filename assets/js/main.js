
(function(){
  const config = window.SUNNY_DAY_CONFIG || {};
  const current = location.pathname.split('/').pop() || 'index.html';
  const nav = [
    ['Home','index.html'],
    ['Apartments','apartments.html'],
    ['Experience','experience.html'],
    ['Gallery','gallery.html'],
    ['Location','location.html'],
    ['Contact','contact.html']
  ];
  const header = document.getElementById('site-header');
  const footer = document.getElementById('site-footer');
  const phoneHref = `tel:${(config.phone || '').replace(/\s+/g,'')}`;
  const whatsappHref = config.whatsapp ? `https://wa.me/${config.whatsapp}` : '#';
  if (header) {
    header.innerHTML = `
      <header class="site-header">
        <div class="container nav-wrap">
          <a class="brand" href="index.html" aria-label="Sunny Day Orebić home">
            <span class="brand__mark"><img src="assets/images/sun-mark.svg" alt="" width="22" height="22"></span>
            <span>
              <span class="brand__name">Sunny Day Orebić</span>
              <span class="brand__sub">Apartments • Pelješac</span>
            </span>
          </a>
          <nav class="nav-links" aria-label="Main navigation">
            ${nav.map(([label, href]) => `<a class="${href === current ? 'is-active' : ''}" href="${href}">${label}</a>`).join('')}
          </nav>
          <div class="nav-cta">
            <a class="nav-contact" href="${phoneHref}">${config.phone || ''}</a>
            <a class="btn btn--ghost" href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a>
            <button class="nav-toggle" type="button" aria-label="Open menu">☰</button>
          </div>
          <div class="nav-panel" hidden>
            <nav class="nav-links" aria-label="Mobile navigation">
              ${nav.map(([label, href]) => `<a class="${href === current ? 'is-active' : ''}" href="${href}">${label}</a>`).join('')}
            </nav>
            <a class="nav-contact" href="${phoneHref}">${config.phone || ''}</a>
            <div style="margin-top:1rem;display:flex;gap:.75rem;flex-wrap:wrap;">
              <a class="btn btn--primary" href="contact.html">Check availability</a>
              <a class="btn btn--ghost" href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a>
            </div>
          </div>
        </div>
      </header>`;
    const siteHeader = header.querySelector('.site-header');
    const navToggle = header.querySelector('.nav-toggle');
    const navPanel = header.querySelector('.nav-panel');
    if (navToggle && navPanel && siteHeader) {
      navToggle.addEventListener('click', ()=> {
        siteHeader.classList.toggle('is-open');
        const isOpen = siteHeader.classList.contains('is-open');
        navPanel.hidden = !isOpen;
      });
    }
  }
  if (footer) {
    footer.innerHTML = `
      <footer class="footer">
        <div class="container">
          <div class="footer-grid">
            <div>
              <div class="brand" style="margin-bottom:1rem;">
                <span class="brand__mark"><img src="assets/images/sun-mark.svg" alt="" width="22" height="22"></span>
                <span>
                  <span class="brand__name" style="font-size:1.7rem;">Sunny Day Orebić</span>
                  <span class="brand__sub">Direct stays with style</span>
                </span>
              </div>
              <p>Mediterranean apartments with sea views, pool access and a calm base for exploring Orebić, Korčula and the Pelješac peninsula.</p>
            </div>
            <div>
              <h4>Quick links</h4>
              <div class="footer-links">
                ${nav.map(([label, href]) => `<a href="${href}">${label}</a>`).join('')}
              </div>
            </div>
            <div>
              <h4>Experiences</h4>
              <div class="footer-links">
                <a href="korcula.html">Korčula Old Town</a>
                <a href="mljet.html">Mljet salt lakes</a>
                <a href="ston.html">Ston walls & salt pans</a>
                <a href="viganj.html">Viganj & beaches</a>
              </div>
            </div>
            <div>
              <h4>Contact</h4>
              <div class="footer-links">
                <a href="${phoneHref}">${config.phone || ''}</a>
                <a href="mailto:${config.email || ''}">${config.email || ''}</a>
                <a href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a>
                <small>${config.address || ''}</small>
              </div>
            </div>
          </div>
          <div class="footer-bottom">
            <small>© <span id="year"></span> Sunny Day Orebić. All rights reserved.</small>
            <small><a href="privacy-policy.html">Privacy Policy</a> • <a href="terms.html">Terms & Conditions</a></small>
          </div>
        </div>
      </footer>`;
  }
  const mobileCta = document.getElementById('mobile-cta');
  if (mobileCta) {
    mobileCta.innerHTML = `
      <div class="mobile-cta__bar">
        <a href="contact.html">Inquiry</a>
        <a href="${phoneHref}">Call</a>
        <a href="${whatsappHref}" target="_blank" rel="noreferrer">WhatsApp</a>
      </div>`;
  }
  const onScroll = () => document.body.classList.toggle('is-scrolled', window.scrollY > 20);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('is-visible');
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  document.querySelectorAll('.js-phone-link').forEach(a => a.href = phoneHref);
  document.querySelectorAll('.js-email-link').forEach(a => a.href = `mailto:${config.email || ''}`);
  document.querySelectorAll('.js-whatsapp-link').forEach(a => a.href = whatsappHref);
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
