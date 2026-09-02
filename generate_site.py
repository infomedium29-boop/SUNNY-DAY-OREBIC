import os, textwrap, json
project='/mnt/data/sunnyday-redesign'
assets=os.path.join(project,'assets')
os.makedirs(os.path.join(assets,'css'), exist_ok=True)
os.makedirs(os.path.join(assets,'js'), exist_ok=True)

site = {
    'name':'Sunny Day Orebić',
    'tagline':'Mediterranean apartments with sea views, pool and a calm premium stay in the heart of Orebić.',
}

# ---------- Helper functions ----------
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w',encoding='utf-8') as f:
        f.write(content)

base_head = '''
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#111612">
<link rel="icon" href="assets/images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<script src="assets/js/site-config.js" defer></script>
<script src="assets/js/main.js" defer></script>
<script src="assets/js/forms.js" defer></script>
'''

def layout(title, description, body, page_class='', extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<title>{title}</title>
<meta name="description" content="{description}">
{base_head}
{extra_head}
</head>
<body class="{page_class}">
<div id="site-header"></div>
{body}
<div id="site-footer"></div>
<div id="mobile-cta" class="mobile-cta"></div>
</body>
</html>
'''

inquiry_form = '''
<form class="inquiry-form js-inquiry-form reveal" data-form-type="availability">
    <div class="form-grid">
        <label>
            <span>Your name</span>
            <input type="text" name="name" placeholder="Full name" required>
        </label>
        <label>
            <span>Email address</span>
            <input type="email" name="email" placeholder="you@example.com" required>
        </label>
        <label>
            <span>Phone number</span>
            <input type="tel" name="phone" placeholder="+385 ..." required>
        </label>
        <label>
            <span>Guests</span>
            <select name="guests" required>
                <option value="">Select</option>
                <option>1 guest</option>
                <option>2 guests</option>
                <option>3 guests</option>
                <option>4 guests</option>
                <option>5 guests</option>
                <option>6+ guests</option>
            </select>
        </label>
        <label>
            <span>Arrival date</span>
            <input type="date" name="arrival" required>
        </label>
        <label>
            <span>Departure date</span>
            <input type="date" name="departure" required>
        </label>
    </div>
    <label>
        <span>Message</span>
        <textarea name="message" rows="5" placeholder="Tell us which apartment or travel period interests you."></textarea>
    </label>
    <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">
    <input type="hidden" name="subject" value="Sunny Day Orebić - New availability request">
    <input type="hidden" name="from_name" value="Sunny Day Orebić Website">
    <input type="checkbox" name="botcheck" class="hidden-botcheck" tabindex="-1" autocomplete="off">
    <div class="form-actions">
        <button type="submit" class="btn btn--primary">Send inquiry</button>
        <p class="form-note">Fast note: replace the Web3Forms access key in <strong>assets/js/site-config.js</strong> to make the form live after deployment.</p>
    </div>
    <div class="form-status" aria-live="polite"></div>
</form>
'''

quick_cta = '''
<section class="section section--dark cta-band">
    <div class="container cta-band__inner reveal">
        <div>
            <p class="eyebrow">Ready for your stay in Orebić?</p>
            <h2>Send a direct inquiry and get a personal reply.</h2>
            <p>No online booking maze. Just a clean, personal and fast way to check availability.</p>
        </div>
        <div class="cta-band__buttons">
            <a class="btn btn--primary" href="contact.html">Check availability</a>
            <a class="btn btn--ghost-light js-phone-link" href="#">Call us</a>
        </div>
    </div>
</section>
'''

page_intro = '''
<section class="section">
  <div class="container intro intro--narrow reveal">
    <p class="eyebrow">Stay in style</p>
    <h2>Designed for guests who value comfort, calm and a better direct-booking experience.</h2>
    <p>Sunny Day Orebić is presented as a boutique-style apartment stay: elegant visuals, clear information, strong calls to action and enough breathing space to keep visitors exploring the website instead of leaving after the first scroll.</p>
  </div>
</section>
'''

# ---------- CSS ----------
css = r'''
:root {
  --bg: #f5f1e8;
  --bg-soft: #fbf8f2;
  --card: rgba(255,255,255,0.78);
  --card-strong: rgba(255,255,255,0.92);
  --text: #1c231d;
  --muted: #59645a;
  --accent: #b08f4f;
  --accent-dark: #8e723c;
  --line: rgba(28,35,29,0.1);
  --dark: #111612;
  --dark-soft: #1a201b;
  --shadow: 0 25px 60px rgba(17,22,18,0.12);
  --radius: 22px;
  --radius-sm: 16px;
  --max: 1220px;
  --header-h: 86px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Inter', system-ui, sans-serif;
  color: var(--text);
  background: linear-gradient(180deg, #f6f2e9 0%, #fbf8f2 35%, #f6f1e7 100%);
  line-height: 1.65;
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
button, input, select, textarea { font: inherit; }
main { display: block; }
.hidden-botcheck { position: absolute; left: -99999px; opacity: 0; }
.container { width: min(calc(100% - 2rem), var(--max)); margin: 0 auto; }
.section { padding: 6.25rem 0; position: relative; }
.section--soft { background: rgba(255,255,255,0.35); }
.section--dark { background: linear-gradient(180deg, #161d18 0%, #0e130f 100%); color: #f4efe4; }
.eyebrow {
  text-transform: uppercase;
  letter-spacing: .22em;
  font-size: .76rem;
  color: var(--accent);
  margin: 0 0 1rem;
  font-weight: 700;
}
.section h2, .hero h1, .page-banner h1, .split-content h2, .detail-copy h1 {
  font-family: 'Cormorant Garamond', Georgia, serif;
  line-height: .95;
  letter-spacing: -0.02em;
  margin: 0 0 1rem;
}
.section h2 { font-size: clamp(2.45rem, 5vw, 4.35rem); }
.lead {
  font-size: 1.1rem;
  color: var(--muted);
  max-width: 48rem;
}
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .7rem;
  padding: 0.95rem 1.5rem;
  border-radius: 999px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: transform .35s ease, box-shadow .35s ease, background .35s ease, border-color .35s ease;
  font-weight: 600;
}
.btn:hover { transform: translateY(-2px); }
.btn--primary { background: linear-gradient(135deg, #c4a261, var(--accent)); color: #fff; box-shadow: 0 15px 35px rgba(176,143,79,0.28); }
.btn--secondary { background: var(--dark); color: #fff; }
.btn--ghost { border-color: rgba(255,255,255,.28); background: rgba(255,255,255,.08); color: #fff; }
.btn--ghost-dark { border-color: var(--line); background: rgba(255,255,255,.7); }
.btn--ghost-light { border-color: rgba(255,255,255,.24); color: #fff; }
.link-arrow { font-weight: 700; color: var(--accent-dark); display: inline-flex; gap: .45rem; align-items: center; }
#site-header {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 60;
  transition: transform .4s ease;
}
.site-header {
  height: var(--header-h);
  display: flex;
  align-items: center;
  backdrop-filter: blur(16px);
  background: rgba(12,16,13,0.16);
  border-bottom: 1px solid rgba(255,255,255,.08);
}
body.is-scrolled .site-header {
  background: rgba(12,16,13,0.75);
  border-bottom-color: rgba(255,255,255,.12);
}
.nav-wrap { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.brand {
  display: flex; align-items: center; gap: .85rem;
}
.brand__mark {
  width: 40px; height: 40px; border-radius: 50%;
  display: grid; place-items: center;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.14);
}
.brand__name { color: #fff; font-family: 'Cormorant Garamond', serif; font-size: 1.85rem; line-height: .92; }
.brand__sub { color: rgba(255,255,255,.76); font-size: .76rem; text-transform: uppercase; letter-spacing: .22em; }
.nav-links {
  display: flex; align-items: center; gap: 1.5rem;
}
.nav-links a { color: rgba(255,255,255,.84); font-size: .94rem; transition: color .35s ease; }
.nav-links a:hover, .nav-links a.is-active { color: #fff; }
.nav-cta { display: flex; align-items: center; gap: .75rem; }
.nav-contact { color: rgba(255,255,255,.8); font-size: .92rem; white-space: nowrap; }
.nav-toggle { display: none; }
.hero {
  position: relative;
  min-height: 100svh;
  display: flex;
  align-items: end;
  padding: 8.5rem 0 4.5rem;
  overflow: hidden;
  color: #fff;
}
.hero__slides, .hero__overlay, .hero__gradient { position: absolute; inset: 0; }
.hero__slide {
  position: absolute; inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transform: scale(1.08);
  animation: heroFade 18s infinite;
}
.hero__slide:nth-child(2) { animation-delay: 6s; }
.hero__slide:nth-child(3) { animation-delay: 12s; }
@keyframes heroFade {
  0% { opacity: 0; transform: scale(1.08); }
  6% { opacity: 1; }
  28% { opacity: 1; transform: scale(1); }
  34% { opacity: 0; }
  100% { opacity: 0; }
}
.hero__overlay { background: linear-gradient(180deg, rgba(7,10,8,.24), rgba(7,10,8,.55)); }
.hero__gradient { background: radial-gradient(circle at 20% 20%, rgba(255,255,255,.08), transparent 30%), linear-gradient(180deg, rgba(8,11,9,.15), rgba(8,11,9,.6)); }
.hero__content {
  position: relative; z-index: 2;
  width: min(100%, 760px);
}
.hero__kicker {
  display: inline-flex; align-items: center; gap: .55rem;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 999px;
  padding: .55rem .9rem;
  margin-bottom: 1.4rem;
}
.hero h1 { font-size: clamp(4rem, 9vw, 7.2rem); margin-bottom: 1rem; }
.hero p { font-size: clamp(1.05rem, 2vw, 1.22rem); color: rgba(255,255,255,.82); max-width: 40rem; }
.hero__actions { display: flex; flex-wrap: wrap; gap: .9rem; margin-top: 2rem; }
.hero__meta {
  margin-top: 2.4rem;
  display: flex; flex-wrap: wrap; gap: 1rem;
}
.hero__meta-card {
  padding: 1rem 1.1rem;
  border-radius: var(--radius-sm);
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.14);
  min-width: 180px;
}
.hero__meta-card strong { display: block; font-size: .85rem; text-transform: uppercase; letter-spacing: .16em; color: rgba(255,255,255,.7); }
.hero__scroll {
  position: absolute; right: 1.25rem; bottom: 2rem; z-index: 3;
  display: flex; flex-direction: column; align-items: center; gap: .85rem; font-size: .8rem; text-transform: uppercase; letter-spacing: .16em; color: rgba(255,255,255,.78);
}
.hero__scroll-line { width: 1px; height: 88px; background: linear-gradient(180deg, rgba(255,255,255,.18), rgba(255,255,255,.95)); }
.feature-strip {
  margin-top: -2.2rem;
  position: relative;
  z-index: 5;
}
.feature-strip__grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
}
.feature-card {
  padding: 1.35rem 1rem;
  border-radius: 18px;
  text-align: center;
  background: rgba(255,255,255,.92);
  box-shadow: var(--shadow);
  border: 1px solid rgba(17,22,18,.06);
}
.feature-card span:first-child { font-size: 1.8rem; display: block; margin-bottom: .45rem; }
.feature-card strong { display: block; font-size: .94rem; }
.feature-card small { color: var(--muted); }
.intro { text-align: center; }
.intro--narrow { width: min(100%, 860px); margin: 0 auto; }
.grid { display: grid; gap: 1.4rem; }
.grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.card {
  background: var(--card-strong);
  border: 1px solid rgba(17,22,18,.06);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
}
.card__image {
  position: relative;
  overflow: hidden;
  aspect-ratio: 4/3;
}
.card__image img { width: 100%; height: 100%; object-fit: cover; transition: transform .8s ease; }
.card:hover .card__image img { transform: scale(1.04); }
.card__body { padding: 1.45rem; }
.card__meta {
  display: flex; flex-wrap: wrap; gap: .65rem 1rem; margin: .6rem 0 1rem;
  color: var(--muted); font-size: .92rem;
}
.card__title { font-family: 'Cormorant Garamond', serif; font-size: 2rem; margin: 0; line-height: 1.02; }
.story-grid {
  display: grid;
  grid-template-columns: 1.05fr .95fr;
  gap: 1.5rem;
  align-items: stretch;
}
.story-panel {
  position: relative;
  min-height: 620px;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: var(--shadow);
}
.story-panel__media, .story-panel__overlay { position: absolute; inset: 0; }
.story-panel__media img { width: 100%; height: 100%; object-fit: cover; }
.story-panel__overlay { background: linear-gradient(180deg, rgba(9,12,10,.08), rgba(9,12,10,.64)); }
.story-panel__content {
  position: relative; z-index: 2; color: #fff; padding: 2.2rem; display: flex; flex-direction: column; justify-content: end; height: 100%;
}
.story-panel__content h3 { font-family: 'Cormorant Garamond', serif; font-size: clamp(2.4rem, 4vw, 4rem); line-height: .92; margin: 0 0 1rem; }
.story-stack { display: grid; gap: 1.5rem; }
.story-card {
  display: grid; grid-template-columns: 1fr 1.15fr; gap: 1.2rem; align-items: center;
  border-radius: 26px; background: var(--card-strong); box-shadow: var(--shadow); padding: 1rem;
}
.story-card img { width: 100%; height: 100%; object-fit: cover; border-radius: 20px; min-height: 230px; }
.story-card__copy h3 { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; margin: 0 0 .75rem; line-height: 1; }
.apartment-showcase { display: grid; grid-template-columns: .82fr 1.18fr; gap: 1.8rem; align-items: start; }
.apartment-showcase__intro {
  position: sticky; top: calc(var(--header-h) + 2rem);
  align-self: start;
}
.badge-row { display: flex; flex-wrap: wrap; gap: .65rem; margin: 1rem 0 1.5rem; }
.badge {
  display: inline-flex; align-items: center; gap: .4rem;
  background: rgba(176,143,79,.12);
  color: var(--accent-dark);
  padding: .45rem .8rem;
  border-radius: 999px;
  font-size: .9rem;
  font-weight: 600;
}
.metrics {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1.5rem;
}
.metric {
  border-radius: 18px;
  border: 1px solid rgba(17,22,18,.08);
  background: rgba(255,255,255,.72);
  padding: 1rem;
}
.metric strong { display: block; font-size: 1.6rem; }
.experience-cards .card__image { aspect-ratio: 1/1.08; }
.quote-strip {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem;
}
.quote {
  padding: 1.4rem;
  border-radius: 22px;
  background: rgba(255,255,255,.88);
  box-shadow: var(--shadow);
  border: 1px solid rgba(17,22,18,.06);
}
.quote p { margin: .75rem 0 0; color: var(--muted); font-size: .95rem; }
.quote strong { display: block; margin-top: 1.1rem; }
.gallery-grid {
  columns: 3 280px;
  column-gap: 1rem;
}
.gallery-item {
  break-inside: avoid;
  margin-bottom: 1rem;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--shadow);
  background: var(--card-strong);
}
.gallery-item img { width: 100%; height: auto; }
.gallery-caption { padding: .95rem 1rem 1.05rem; color: var(--muted); font-size: .94rem; }
.cta-band__inner {
  display: flex; gap: 2rem; justify-content: space-between; align-items: center;
}
.cta-band__buttons { display: flex; gap: 1rem; flex-wrap: wrap; }
.footer {
  background: #0c110d;
  color: rgba(255,255,255,.82);
  padding: 2.8rem 0 1.2rem;
}
.footer-grid { display: grid; grid-template-columns: 1.25fr .9fr .9fr .9fr; gap: 1.2rem; }
.footer h4 { color: #fff; margin-top: 0; margin-bottom: .9rem; }
.footer small, .footer p, .footer a { color: rgba(255,255,255,.7); }
.footer-links { display: grid; gap: .55rem; }
.footer-bottom { display: flex; justify-content: space-between; gap: 1rem; border-top: 1px solid rgba(255,255,255,.08); margin-top: 1.8rem; padding-top: 1.1rem; font-size: .92rem; }
.page-banner {
  position: relative;
  padding: 10rem 0 4.2rem;
  color: #fff;
  overflow: hidden;
}
.page-banner__bg, .page-banner__overlay { position: absolute; inset: 0; }
.page-banner__bg img { width: 100%; height: 100%; object-fit: cover; }
.page-banner__overlay { background: linear-gradient(180deg, rgba(7,10,8,.26), rgba(7,10,8,.72)); }
.page-banner__content { position: relative; z-index: 2; width: min(100%, 760px); }
.page-banner h1 { font-size: clamp(3.2rem, 7vw, 5.8rem); margin-bottom: .9rem; }
.page-banner p { color: rgba(255,255,255,.82); font-size: 1.1rem; max-width: 42rem; }
.crumbs { display: flex; gap: .55rem; flex-wrap: wrap; color: rgba(255,255,255,.78); margin-bottom: 1rem; font-size: .94rem; }
.split {
  display: grid; grid-template-columns: .95fr 1.05fr; gap: 2rem; align-items: center;
}
.split--reverse { grid-template-columns: 1.05fr .95fr; }
.split-media img { width: 100%; height: 100%; object-fit: cover; border-radius: 28px; box-shadow: var(--shadow); }
.info-box {
  padding: 1.5rem;
  border-radius: 24px;
  background: rgba(255,255,255,.86);
  border: 1px solid rgba(17,22,18,.08);
  box-shadow: var(--shadow);
}
.info-list { display: grid; gap: .85rem; padding: 0; margin: 1rem 0 0; list-style: none; }
.info-list li {
  display: grid; grid-template-columns: 1.2rem 1fr; gap: .75rem; align-items: start;
  color: var(--muted);
}
.amenity-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: .85rem 1.2rem; padding: 0; list-style: none; }
.amenity-grid li, .check-list li { display: flex; gap: .7rem; align-items: start; color: var(--muted); }
.check-list { display: grid; gap: .75rem; padding: 0; list-style: none; margin: 1rem 0 0; }
.stat-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
.stat-card {
  padding: 1.25rem;
  background: rgba(255,255,255,.82);
  border-radius: 20px;
  border: 1px solid rgba(17,22,18,.08);
  box-shadow: var(--shadow);
}
.stat-card strong { display: block; font-size: 2rem; color: var(--text); }
.inquiry-wrap {
  display: grid; grid-template-columns: 1.06fr .94fr; gap: 1.5rem;
}
.inquiry-form, .contact-card {
  background: rgba(255,255,255,.88);
  border: 1px solid rgba(17,22,18,.08);
  border-radius: 28px;
  box-shadow: var(--shadow);
  padding: 1.5rem;
}
.form-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 1rem; }
.inquiry-form label { display: grid; gap: .45rem; margin-bottom: 1rem; color: var(--muted); }
.inquiry-form input, .inquiry-form select, .inquiry-form textarea {
  width: 100%; padding: .95rem 1rem; border-radius: 16px; border: 1px solid rgba(17,22,18,.12); background: rgba(255,255,255,.9); color: var(--text);
}
.inquiry-form input:focus, .inquiry-form select:focus, .inquiry-form textarea:focus { outline: 2px solid rgba(176,143,79,.22); border-color: var(--accent); }
.form-actions { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }
.form-note { margin: 0; font-size: .92rem; color: var(--muted); }
.form-status { min-height: 1.2rem; margin-top: .7rem; font-size: .95rem; color: var(--accent-dark); }
.contact-card h3 { font-family: 'Cormorant Garamond', serif; font-size: 2rem; margin: 0 0 1rem; }
.contact-points { display: grid; gap: .85rem; }
.contact-point { padding: .95rem 1rem; border-radius: 18px; background: rgba(245,241,232,.9); }
.embedded-map { border: 0; width: 100%; min-height: 420px; border-radius: 26px; box-shadow: var(--shadow); }
.listing {
  display: grid; gap: 1rem;
}
.listing__item {
  padding: 1.3rem;
  border-radius: 22px;
  background: rgba(255,255,255,.82);
  border: 1px solid rgba(17,22,18,.08);
  box-shadow: var(--shadow);
}
.tips-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.tip {
  padding: 1.3rem;
  border-radius: 22px;
  background: rgba(255,255,255,.78);
  border: 1px solid rgba(17,22,18,.08);
  box-shadow: var(--shadow);
}
.rich-text h2 { font-size: clamp(2rem,4vw,3.5rem); }
.rich-text p, .rich-text li { color: var(--muted); }
.rich-text ul { padding-left: 1.15rem; }
.mobile-cta {
  position: fixed; left: 1rem; right: 1rem; bottom: 1rem; z-index: 62; display: none;
}
.mobile-cta__bar {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: .6rem; padding: .6rem; border-radius: 18px; background: rgba(12,16,13,.88); backdrop-filter: blur(16px); box-shadow: 0 20px 50px rgba(0,0,0,.24);
}
.mobile-cta__bar a { text-align: center; color: #fff; padding: .85rem .5rem; border-radius: 12px; background: rgba(255,255,255,.08); font-size: .92rem; }
.reveal { opacity: 0; transform: translateY(18px); transition: opacity .8s ease, transform .8s ease; }
.reveal.is-visible { opacity: 1; transform: translateY(0); }
@media (max-width: 1100px) {
  .feature-strip__grid, .grid--4, .quote-strip, .stat-row, .tips-grid { grid-template-columns: repeat(2, 1fr); }
  .story-grid, .apartment-showcase, .split, .inquiry-wrap, .footer-grid { grid-template-columns: 1fr; }
  .apartment-showcase__intro { position: static; }
}
@media (max-width: 860px) {
  :root { --header-h: 74px; }
  .section { padding: 5rem 0; }
  .nav-toggle {
    display: inline-flex; border: 0; background: rgba(255,255,255,.12); color: #fff; width: 44px; height: 44px; align-items: center; justify-content: center; border-radius: 12px;
  }
  .nav-links, .nav-contact { display: none; }
  .nav-cta .btn { display: none; }
  .site-header.is-open .nav-panel {
    opacity: 1; pointer-events: auto; transform: translateY(0);
  }
  .nav-panel {
    position: absolute; left: 1rem; right: 1rem; top: calc(100% + .75rem); opacity: 0; pointer-events: none; transform: translateY(-8px); transition: all .35s ease;
    padding: 1rem; border-radius: 22px; background: rgba(11,15,12,.96); border: 1px solid rgba(255,255,255,.08); box-shadow: 0 25px 70px rgba(0,0,0,.36);
  }
  .nav-panel .nav-links { display: grid; gap: .9rem; }
  .nav-panel .nav-links a { font-size: 1rem; }
  .nav-panel .nav-contact { display: block; margin-top: 1rem; }
  .hero h1 { font-size: clamp(3.4rem, 15vw, 5.4rem); }
  .feature-strip__grid, .grid--3, .grid--4, .quote-strip, .metrics, .form-grid, .tips-grid { grid-template-columns: 1fr; }
  .story-card { grid-template-columns: 1fr; }
  .cta-band__inner, .footer-bottom { flex-direction: column; align-items: start; }
  .mobile-cta { display: block; }
}
@media (max-width: 560px) {
  .hero { padding-bottom: 6.5rem; }
  .hero__scroll { display: none; }
  .page-banner { padding-top: 8rem; }
  .brand__sub { display: none; }
}
'''
write(os.path.join(assets,'css','styles.css'), css)

# ---------- JS ----------
config_js = '''
window.SUNNY_DAY_CONFIG = {
  siteName: 'Sunny Day Orebić',
  phone: '+385 91 730 6770',
  email: 'info@sunnydayorebic.com',
  address: 'Ul. Bana Josipa Jelačića 82, 20250 Orebić, Croatia',
  instagram: '#',
  whatsapp: '385917306770',
  mapQuery: 'Ul. Bana Josipa Jelačića 82, 20250 Orebić, Croatia',
  formEndpoint: 'https://api.web3forms.com/submit',
  web3formsAccessKey: 'YOUR_WEB3FORMS_ACCESS_KEY'
};
'''
write(os.path.join(assets,'js','site-config.js'), config_js)

main_js = r'''
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
'''
write(os.path.join(assets,'js','main.js'), main_js)

forms_js = r'''
(function(){
  const config = window.SUNNY_DAY_CONFIG || {};
  const forms = document.querySelectorAll('.js-inquiry-form');
  if (!forms.length) return;
  const today = new Date().toISOString().split('T')[0];
  forms.forEach(form => {
    const statusEl = form.querySelector('.form-status');
    const arrival = form.querySelector('input[name="arrival"]');
    const departure = form.querySelector('input[name="departure"]');
    if (arrival) arrival.min = today;
    if (departure) departure.min = today;
    if (arrival && departure) {
      arrival.addEventListener('change', () => {
        departure.min = arrival.value || today;
        if (departure.value && departure.value < arrival.value) departure.value = arrival.value;
      });
    }
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const accessInput = form.querySelector('input[name="access_key"]');
      if (accessInput && config.web3formsAccessKey) accessInput.value = config.web3formsAccessKey;
      const formData = new FormData(form);
      const accessKey = formData.get('access_key');
      if (!accessKey || accessKey === 'YOUR_WEB3FORMS_ACCESS_KEY') {
        if (statusEl) statusEl.textContent = 'Replace the Web3Forms access key in assets/js/site-config.js before going live.';
        return;
      }
      if (submitBtn) submitBtn.disabled = true;
      if (statusEl) statusEl.textContent = 'Sending your inquiry...';
      try {
        const response = await fetch(config.formEndpoint || 'https://api.web3forms.com/submit', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        if (data.success) {
          form.reset();
          if (statusEl) statusEl.textContent = 'Thank you — your inquiry has been sent.';
        } else {
          if (statusEl) statusEl.textContent = data.message || 'Something went wrong. Please try again.';
        }
      } catch (err) {
        if (statusEl) statusEl.textContent = 'Unable to send right now. Please try again later.';
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  });
})();
'''
write(os.path.join(assets,'js','forms.js'), forms_js)

sun_mark = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
<circle cx="32" cy="34" r="14" fill="#C4A261"/>
<path d="M12 48C17 43.5 24.3 41 32 41C39.7 41 47 43.5 52 48" stroke="#C4A261" stroke-width="4" stroke-linecap="round"/>
<path d="M32 6V14M18 11L22 17M46 11L42 17M11 25H19M45 25H53" stroke="#C4A261" stroke-width="4" stroke-linecap="round"/>
</svg>'''
write(os.path.join(assets,'images','sun-mark.svg'), sun_mark)
write(os.path.join(assets,'images','favicon.svg'), sun_mark)

# ---------- Page content data ----------
apts = [
    {
        'slug':'apartment-sea-view.html',
        'name':'Deluxe Sea View Apartment',
        'image':'assets/images/living-dining-roundtable.avif',
        'hero':'assets/images/hero-aerial-day.avif',
        'copy':'Bright open-plan interiors, private outdoor space and the kind of sea-facing atmosphere guests remember long after checkout.',
        'meta':'Up to 4 guests • private terrace • open-plan living',
        'gallery':['assets/images/living-dining-roundtable.avif','assets/images/terrace-sofa-view.avif','assets/images/kitchen-dining-openplan.avif','assets/images/bedroom-double.avif','assets/images/bathroom-basin.avif'],
        'amenities':['Sea-view living space','Private outdoor seating','Air conditioning','Fully equipped kitchen','Dining area','Fast Wi-Fi','Private bathroom','Stylish contemporary finish']
    },
    {
        'slug':'apartment-family.html',
        'name':'Family Apartment with Terrace',
        'image':'assets/images/terrace-sofa-day.avif',
        'hero':'assets/images/terrace-sofa-day.avif',
        'copy':'A spacious base for couples or families who want long breakfasts on the terrace, bright interiors and a relaxed rhythm close to the sea.',
        'meta':'Up to 5 guests • terrace lounge • family-friendly layout',
        'gallery':['assets/images/terrace-sofa-day.avif','assets/images/living-dining-sea.avif','assets/images/bedroom-twins.avif','assets/images/bedroom-double-soft.avif','assets/images/bathroom-laundry.avif'],
        'amenities':['Large furnished terrace','Comfortable lounge zone','Sea and neighborhood outlook','Family sleeping setup','Air conditioning','Modern kitchen','Pool access','Parking included']
    },
    {
        'slug':'apartment-pool-view.html',
        'name':'Pool View Apartment',
        'image':'assets/images/pool-wide-day.avif',
        'hero':'assets/images/hero-pool-loungers.avif',
        'copy':'Ideal for guests who love stepping from a calm, modern apartment into sun-drenched poolside moments and slow Mediterranean afternoons.',
        'meta':'Up to 4 guests • pool view • calm boutique atmosphere',
        'gallery':['assets/images/pool-wide-day.avif','assets/images/pool-loungers-day.avif','assets/images/living-room-sofa-sea.avif','assets/images/kitchen-dining-bright.avif','assets/images/bedroom-sea-view.avif'],
        'amenities':['Pool-facing outlook','Sunny outdoor moments','Modern kitchen','Dining and lounge area','Fast Wi‑Fi','Comfortable bedroom','A/C throughout','Private bathroom']
    }
]

experiences = [
    {
        'slug':'korcula.html',
        'name':'Korčula Old Town',
        'image':'assets/images/orebic-harbor-day.avif',
        'lead':'From Orebić, Korčula feels like a natural extension of your stay — a short crossing away, filled with stone lanes, waterfront cafés and old-town atmosphere.',
        'intro':'A day in Korčula is perfect when you want a mix of culture, easy walking, scenic seaside moments and dinner with a view before returning to Orebić.',
        'bullets':['Short boat connection from Orebić','Historic old town and waterfront strolls','Great for an afternoon or evening trip','Ideal for couples, families and relaxed explorers'],
        'tips':['Go later in the afternoon for a softer, more romantic atmosphere.','Plan enough time for the old town, small shops and a slow meal by the sea.','It pairs beautifully with a lazy beach morning back in Orebić.']
    },
    {
        'slug':'mljet.html',
        'name':'Mljet & the Salt Lakes',
        'image':'assets/images/view-aerial-sea.avif',
        'lead':'Mljet is one of the most peaceful island escapes in the southern Adriatic, known for its national park atmosphere, forested landscapes and famous salt lakes.',
        'intro':'For guests who want a nature-focused day trip, Mljet delivers a calm rhythm, scenic boat moments and an experience that feels different from the bustle of classic coastal towns.',
        'bullets':['Best for nature lovers and slow explorers','Salt lakes and island scenery create a unique day trip','Excellent choice for a full-day outing','Beautiful mix of swimming, walking and boat time'],
        'tips':['Choose this trip on a stable, sunny day to enjoy the full outdoor experience.','Bring water, swimwear and comfortable shoes.','Mljet works best as a full-day excursion rather than a rushed stop.']
    },
    {
        'slug':'ston.html',
        'name':'Ston Walls & Salt Pans',
        'image':'assets/images/exterior-front-flowers.avif',
        'lead':'Ston combines history, stone architecture and one of the most memorable heritage stops in the region — ideal for guests who like culture with a culinary edge.',
        'intro':'It is an easy Pelješac-area excursion that blends old fortifications, a distinctive atmosphere and the simple pleasure of exploring somewhere with a strong sense of place.',
        'bullets':['Great half-day or full-day excursion','Historic walls and a characterful old-town setting','Easy to combine with lunch or winery visits','A strong option beyond classic beach days'],
        'tips':['Wear comfortable footwear if you plan to walk the walls.','Combine Ston with nearby wineries for a fuller Pelješac day.','Start earlier in summer to avoid the strongest midday sun.']
    },
    {
        'slug':'viganj.html',
        'name':'Viganj, Beaches & Sea Sports',
        'image':'assets/images/terrace-lounger-sea.avif',
        'lead':'Viganj is one of the most appealing nearby spots for beach time, open views and a more active sea-day energy.',
        'intro':'Even if you are not into water sports, the setting itself is worth the short trip — bright sea, breezy waterfront atmosphere and one of the peninsula’s most relaxed coastal moods.',
        'bullets':['Excellent for beach-hopping and sea views','Popular with active travelers and watersport fans','Easy trip from Orebić','Good mix of energy and laid-back charm'],
        'tips':['Go when you want a more active seaside day.','Ideal for a late afternoon drink after the beach.','Keep it simple: swim, walk, linger and enjoy the wind and light.']
    },
    {
        'slug':'bacina-lakes.html',
        'name':'Baćina Lakes',
        'image':'assets/images/view-aerial-coast.avif',
        'lead':'Baćina Lakes offer a freshwater contrast to the coast — peaceful, scenic and especially attractive for guests looking for something different from a standard beach day.',
        'intro':'It is the kind of excursion that works beautifully when you want a quieter, softer landscape and a slower visual rhythm during your stay on Pelješac.',
        'bullets':['Freshwater setting near the coast','Great scenery and calm atmosphere','Works well as a scenic drive destination','A refreshing alternative to sea-focused outings'],
        'tips':['A very good option for a slower-paced day.','Bring your camera — the setting is especially photogenic.','Combine it with other stops if you want a more complete road trip.']
    },
    {
        'slug':'kravica-waterfalls.html',
        'name':'Kravica Waterfalls',
        'image':'assets/images/orebic-harbor-twilight.avif',
        'lead':'For guests who want a bigger adventure, Kravica Waterfalls bring a dramatic natural scene and a change of pace from the coastline.',
        'intro':'This trip is better suited to visitors who enjoy longer excursions and want to add a memorable natural highlight to their Adriatic holiday.',
        'bullets':['Most suitable as a dedicated day trip','Impressive waterfall scenery','Best for guests who enjoy wider regional exploring','Adds variety to a sea-and-sun holiday'],
        'tips':['Treat it as an all-day excursion.','Check border and travel conditions if combining multiple stops.','Best enjoyed without rushing so the experience feels worthwhile.']
    }
]

# ---------- Index page ----------
index_body = f'''
<main>
  <section class="hero">
    <div class="hero__slides">
      <div class="hero__slide" style="background-image:url('assets/images/hero-aerial-day.avif');"></div>
      <div class="hero__slide" style="background-image:url('assets/images/hero-pool-loungers.avif');"></div>
      <div class="hero__slide" style="background-image:url('assets/images/hero-exterior-night.avif');"></div>
    </div>
    <div class="hero__overlay"></div>
    <div class="hero__gradient"></div>
    <div class="container hero__content reveal">
      <span class="hero__kicker">Sea-view apartments • Orebić • Pelješac</span>
      <h1>Stay where every scroll feels like a longer exhale.</h1>
      <p>Sunny Day Orebić becomes a premium, modern hospitality website built to hold attention: strong photography, cinematic transitions, elegant typography and clear paths toward direct inquiries instead of online booking.</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="contact.html">Check availability</a>
        <a class="btn btn--ghost" href="apartments.html">Explore apartments</a>
      </div>
      <div class="hero__meta">
        <div class="hero__meta-card"><strong>Direct inquiry</strong>Personal contact, date check and fast reply.</div>
        <div class="hero__meta-card"><strong>Best of Orebić</strong>Pool, sea views and the Pelješac lifestyle.</div>
        <div class="hero__meta-card"><strong>Scroll-led story</strong>Designed to keep guests curious and moving.</div>
      </div>
    </div>
    <div class="hero__scroll"><span>Scroll</span><span class="hero__scroll-line"></span><span>Discover</span></div>
  </section>

  <section class="feature-strip">
    <div class="container feature-strip__grid">
      <div class="feature-card reveal"><span>🌊</span><strong>Sea views</strong><small>Bright Adriatic outlooks</small></div>
      <div class="feature-card reveal"><span>☀️</span><strong>Outdoor living</strong><small>Terraces made for slow mornings</small></div>
      <div class="feature-card reveal"><span>🏊</span><strong>Swimming pool</strong><small>Sun-filled shared pool area</small></div>
      <div class="feature-card reveal"><span>❄️</span><strong>Modern comfort</strong><small>A/C and contemporary interiors</small></div>
      <div class="feature-card reveal"><span>🚗</span><strong>Parking</strong><small>Easy arrival and convenience</small></div>
      <div class="feature-card reveal"><span>📍</span><strong>Orebić base</strong><small>Great for Pelješac day trips</small></div>
    </div>
  </section>

  {page_intro}

  <section class="section">
    <div class="container story-grid">
      <article class="story-panel reveal">
        <div class="story-panel__media"><img src="assets/images/terrace-loungers-view.avif" alt="Terrace with loungers and sea view"></div>
        <div class="story-panel__overlay"></div>
        <div class="story-panel__content">
          <p class="eyebrow">A better first impression</p>
          <h3>From generic listing feel to boutique-style arrival.</h3>
          <p>The homepage opens with atmosphere, not clutter: fewer blocks, stronger imagery, more confidence and a cleaner narrative that encourages the next scroll.</p>
        </div>
      </article>
      <div class="story-stack">
        <article class="story-card reveal">
          <img src="assets/images/living-dining-roundtable.avif" alt="Elegant apartment interior">
          <div class="story-card__copy">
            <p class="eyebrow">Beautiful interiors</p>
            <h3>Clean, calm and premium.</h3>
            <p>Every section gives the photos room to breathe, so the property feels more valuable and more memorable.</p>
          </div>
        </article>
        <article class="story-card reveal">
          <img src="assets/images/pool-wide-day.avif" alt="Sunny pool area">
          <div class="story-card__copy">
            <p class="eyebrow">Visual momentum</p>
            <h3>Animation that feels elegant, not gimmicky.</h3>
            <p>Subtle reveal motion, cinematic hero transitions and layered scrolling keep the experience premium while still fast and readable.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container apartment-showcase">
      <div class="apartment-showcase__intro reveal">
        <p class="eyebrow">Apartments</p>
        <h2>Present the stay like a high-end hospitality brand.</h2>
        <p class="lead">Instead of pushing visitors into dense text or template-style layouts, each apartment is given a clear identity, a calm visual story and an obvious next step toward inquiry.</p>
        <div class="badge-row">
          <span class="badge">Sea-view positioning</span>
          <span class="badge">Modern styling</span>
          <span class="badge">Direct booking flow</span>
        </div>
        <div class="metrics">
          <div class="metric"><strong>3</strong><span>featured apartment types</span></div>
          <div class="metric"><strong>1</strong><span>clear inquiry system</span></div>
          <div class="metric"><strong>6</strong><span>regional experience pages</span></div>
        </div>
      </div>
      <div class="grid grid--3">
        {''.join([f'''<article class="card reveal"><div class="card__image"><img src="{a['image']}" alt="{a['name']}"></div><div class="card__body"><h3 class="card__title">{a['name']}</h3><div class="card__meta"><span>{a['meta']}</span></div><p>{a['copy']}</p><a class="link-arrow" href="{a['slug']}">View apartment <span>→</span></a></div></article>''' for a in apts])}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container reveal intro intro--narrow">
      <p class="eyebrow">Explore Orebić & beyond</p>
      <h2>A website that sells the destination as well as the stay.</h2>
      <p>To attract more direct guests, Sunny Day should not only show apartments — it should present Orebić and Pelješac as a reason to stay longer, travel better and inquire directly.</p>
    </div>
    <div class="container grid grid--3 experience-cards" style="margin-top:2rem;">
      {''.join([f'''<article class="card reveal"><div class="card__image"><img src="{e['image']}" alt="{e['name']}"></div><div class="card__body"><h3 class="card__title">{e['name']}</h3><p>{e['lead']}</p><a class="link-arrow" href="{e['slug']}">Discover more <span>→</span></a></div></article>''' for e in experiences[:6]])}
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="reveal intro intro--narrow">
        <p class="eyebrow">Guest confidence</p>
        <h2>Real reassurance, not just pretty visuals.</h2>
      </div>
      <div class="quote-strip" style="margin-top:2rem;">
        <article class="quote reveal">★★★★★<p>“Fantastic views, spotless interiors and a pool area that instantly makes you settle into holiday mode.”</p><strong>Guest review style block</strong></article>
        <article class="quote reveal">★★★★★<p>“The site now highlights exactly what guests care about: the atmosphere, the terraces and how easy it is to reach out directly.”</p><strong>Hospitality-focused messaging</strong></article>
        <article class="quote reveal">★★★★★<p>“Strong typography and elegant spacing help the property feel more premium and trustworthy.”</p><strong>Premium conversion design</strong></article>
        <article class="quote reveal">★★★★★<p>“The experience pages give people a reason to stay longer and send an inquiry instead of continuing to browse elsewhere.”</p><strong>Direct inquiry strategy</strong></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container inquiry-wrap">
      <div>
        <div class="reveal" style="margin-bottom:1.2rem;">
          <p class="eyebrow">Check availability</p>
          <h2>Simple, direct and personal.</h2>
          <p class="lead">No booking engine needed. The form gathers dates, number of guests, phone number and email — exactly what is needed to turn interest into real conversations.</p>
        </div>
        {inquiry_form}
      </div>
      <aside class="contact-card reveal">
        <h3>Why this flow works better</h3>
        <div class="contact-points">
          <div class="contact-point"><strong>1. It feels personal.</strong><br>Guests ask for the dates they want and receive a direct reply instead of leaving the website to compare listings elsewhere.</div>
          <div class="contact-point"><strong>2. It reduces friction.</strong><br>No cluttered booking widgets, no confusing steps — just the essentials that matter.</div>
          <div class="contact-point"><strong>3. It supports higher-value stays.</strong><br>Better design and stronger destination storytelling help position the property as more than “just another apartment”.</div>
        </div>
        <img src="assets/images/terrace-sofa-glass.avif" alt="Terrace and sea view" style="margin-top:1.25rem;border-radius:22px;">
      </aside>
    </div>
  </section>

  {quick_cta}
</main>
'''
write(os.path.join(project,'index.html'), layout('Sunny Day Orebić | Premium Apartments Website', site['tagline'], index_body, 'home'))

# ---------- Apartments overview ----------
apt_cards = ''.join([f'''
<article class="card reveal">
  <div class="card__image"><img src="{a['image']}" alt="{a['name']}"></div>
  <div class="card__body">
    <h2 class="card__title">{a['name']}</h2>
    <div class="card__meta"><span>{a['meta']}</span></div>
    <p>{a['copy']}</p>
    <a class="btn btn--secondary" href="{a['slug']}">View apartment</a>
  </div>
</article>
''' for a in apts])

a_apts_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/hero-aerial-day.avif" alt="Sunny Day Orebić aerial view"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Apartments</span></div>
      <h1>Apartments presented with clarity, calm and appeal.</h1>
      <p>Each apartment page is designed to feel more like a boutique accommodation showcase and less like a standard listing template.</p>
    </div>
  </section>
  <section class="section">
    <div class="container intro intro--narrow reveal">
      <p class="eyebrow">Choose your stay</p>
      <h2>Three featured apartment experiences.</h2>
      <p>These pages are structured to keep information clear: a strong visual introduction, concise amenities, refined galleries and a direct path to inquiry.</p>
    </div>
    <div class="container grid grid--3" style="margin-top:2rem;">{apt_cards}</div>
  </section>
  <section class="section section--soft">
    <div class="container split">
      <div class="split-media reveal"><img src="assets/images/terrace-lounger-sea.avif" alt="Sea-view terrace"></div>
      <div class="info-box reveal">
        <p class="eyebrow">What is intentionally improved</p>
        <h2>Better pages lead to better inquiries.</h2>
        <ul class="check-list">
          <li><span>✓</span><span>Information is grouped in a cleaner, more premium way.</span></li>
          <li><span>✓</span><span>The strongest photographs lead the page instead of being buried.</span></li>
          <li><span>✓</span><span>Every apartment page ends with a direct, visible inquiry option.</span></li>
          <li><span>✓</span><span>The language focuses on comfort, atmosphere and reasons to stay.</span></li>
        </ul>
      </div>
    </div>
  </section>
  {quick_cta}
</main>
'''
write(os.path.join(project,'apartments.html'), layout('Apartments | Sunny Day Orebić', 'Explore the apartment pages for Sunny Day Orebić.', a_apts_body))

# ---------- Apartment detail pages ----------
for a in apts:
    gallery_items = ''.join([f'<div class="gallery-item reveal"><img src="{img}" alt="{a["name"]} photo"><div class="gallery-caption">{a["name"]}</div></div>' for img in a['gallery']])
    amenity_html = ''.join([f'<li><span>✓</span><span>{item}</span></li>' for item in a['amenities']])
    body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="{a['hero']}" alt="{a['name']}"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <a href="apartments.html">Apartments</a> <span>•</span> <span>{a['name']}</span></div>
      <h1>{a['name']}</h1>
      <p>{a['copy']}</p>
      <div class="hero__actions"><a class="btn btn--primary" href="contact.html">Check availability</a><a class="btn btn--ghost" href="#gallery">View gallery</a></div>
    </div>
  </section>
  <section class="section">
    <div class="container split">
      <div class="info-box reveal">
        <p class="eyebrow">Apartment details</p>
        <h2>Everything guests need, presented without noise.</h2>
        <p>{a['meta']}</p>
        <ul class="amenity-grid">{amenity_html}</ul>
      </div>
      <div class="split-media reveal"><img src="{a['image']}" alt="{a['name']} main image"></div>
    </div>
  </section>
  <section class="section section--soft" id="gallery">
    <div class="container intro intro--narrow reveal">
      <p class="eyebrow">Gallery</p>
      <h2>A compact visual story of the apartment.</h2>
    </div>
    <div class="container gallery-grid" style="margin-top:2rem;">{gallery_items}</div>
  </section>
  <section class="section">
    <div class="container inquiry-wrap">
      <div>
        <div class="reveal" style="margin-bottom:1rem;">
          <p class="eyebrow">Availability request</p>
          <h2>Interested in this apartment?</h2>
          <p class="lead">Send the dates that interest you and get a direct response.</p>
        </div>
        {inquiry_form}
      </div>
      <aside class="contact-card reveal">
        <h3>What this page is designed to do</h3>
        <div class="contact-points">
          <div class="contact-point"><strong>Quick orientation.</strong><br>Visitors understand the apartment in a few seconds.</div>
          <div class="contact-point"><strong>Visual confidence.</strong><br>The gallery reinforces quality without overwhelming the page.</div>
          <div class="contact-point"><strong>Immediate action.</strong><br>The inquiry form appears right when interest is highest.</div>
        </div>
      </aside>
    </div>
  </section>
  {quick_cta}
</main>
'''
    write(os.path.join(project,a['slug']), layout(f"{a['name']} | Sunny Day Orebić", a['copy'], body))

# ---------- Experience overview ----------
exp_cards = ''.join([f'''
<article class="card reveal">
  <div class="card__image"><img src="{e['image']}" alt="{e['name']}"></div>
  <div class="card__body">
    <h2 class="card__title">{e['name']}</h2>
    <p>{e['lead']}</p>
    <a class="btn btn--secondary" href="{e['slug']}">Explore page</a>
  </div>
</article>
''' for e in experiences])

exp_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/view-aerial-sea.avif" alt="Pelješac and the sea"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Experience</span></div>
      <h1>Turn the website into a travel reason, not just a property brochure.</h1>
      <p>These regional pages strengthen SEO, create a better browsing journey and help guests imagine longer, more interesting stays in Orebić.</p>
    </div>
  </section>
  <section class="section">
    <div class="container intro intro--narrow reveal">
      <p class="eyebrow">Experience pages</p>
      <h2>More content, more value, more reasons to inquire.</h2>
      <p>For this redesign, the destination content is built as individual subpages instead of being buried in one generic section. That keeps the experience premium and opens strong opportunities for search visibility.</p>
    </div>
    <div class="container grid grid--3 experience-cards" style="margin-top:2rem;">{exp_cards}</div>
  </section>
  <section class="section section--soft">
    <div class="container stat-row">
      <div class="stat-card reveal"><strong>6</strong><span>experience subpages ready</span></div>
      <div class="stat-card reveal"><strong>1</strong><span>main experience hub page</span></div>
      <div class="stat-card reveal"><strong>∞</strong><span>room for future blog-style additions</span></div>
      <div class="stat-card reveal"><strong>SEO</strong><span>stronger depth than a simple brochure site</span></div>
    </div>
  </section>
  {quick_cta}
</main>
'''
write(os.path.join(project,'experience.html'), layout('Experience Pelješac | Sunny Day Orebić', 'Explore destinations and day trips from Sunny Day Orebić.', exp_body))

# ---------- Experience detail pages ----------
for e in experiences:
    bullet_html = ''.join([f'<li><span>•</span><span>{b}</span></li>' for b in e['bullets']])
    tips_html = ''.join([f'<article class="tip reveal"><h3 style="font-family:Cormorant Garamond,serif;font-size:1.7rem;margin:0 0 .6rem;">Tip</h3><p>{t}</p></article>' for t in e['tips']])
    body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="{e['image']}" alt="{e['name']}"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <a href="experience.html">Experience</a> <span>•</span> <span>{e['name']}</span></div>
      <h1>{e['name']}</h1>
      <p>{e['lead']}</p>
    </div>
  </section>
  <section class="section">
    <div class="container split">
      <div class="split-media reveal"><img src="{e['image']}" alt="{e['name']}"></div>
      <div class="info-box reveal rich-text">
        <p class="eyebrow">Why include this page</p>
        <h2>{e['name']} gives guests another reason to choose Orebić.</h2>
        <p>{e['intro']}</p>
        <ul class="check-list">{bullet_html}</ul>
      </div>
    </div>
  </section>
  <section class="section section--soft">
    <div class="container">
      <div class="intro intro--narrow reveal">
        <p class="eyebrow">Practical notes</p>
        <h2>Helpful guidance for guests planning a day out.</h2>
      </div>
      <div class="tips-grid" style="margin-top:2rem;">{tips_html}</div>
    </div>
  </section>
  <section class="section">
    <div class="container split">
      <div class="info-box reveal">
        <p class="eyebrow">How it supports the site</p>
        <h2>These pages add depth, trust and search potential.</h2>
        <ul class="check-list">
          <li><span>✓</span><span>Guests spend more time on the website and see more value in the destination.</span></li>
          <li><span>✓</span><span>The property becomes associated with a fuller travel experience, not just a bed.</span></li>
          <li><span>✓</span><span>It opens space for future content expansion and location-based SEO.</span></li>
        </ul>
      </div>
      <div class="split-media reveal"><img src="assets/images/terrace-sofa-neighborhood.avif" alt="Sunny Day terrace"></div>
    </div>
  </section>
  {quick_cta}
</main>
'''
    write(os.path.join(project,e['slug']), layout(f"{e['name']} | Sunny Day Orebić", e['lead'], body))

# ---------- Gallery page ----------
gallery_images = [
    ('assets/images/hero-aerial-day.avif','Aerial overview of the property and coastal setting'),
    ('assets/images/exterior-front-flowers.avif','Front exterior with Mediterranean landscaping'),
    ('assets/images/pool-loungers-day.avif','Pool area with loungers'),
    ('assets/images/terrace-sofa-view.avif','Covered terrace lounge'),
    ('assets/images/living-dining-roundtable.avif','Bright open-plan interior'),
    ('assets/images/bedroom-double.avif','Double bedroom'),
    ('assets/images/terrace-lounger-sea.avif','Relaxed sea-view terrace detail'),
    ('assets/images/hero-pool-loungers.avif','Pool and façade at golden hour'),
    ('assets/images/kitchen-dining-openplan.avif','Kitchen and dining zone'),
    ('assets/images/living-room-sofa-sea.avif','Living room with sea outlook'),
    ('assets/images/bedroom-sea-view.avif','Bedroom with natural light'),
    ('assets/images/bathroom-basin.avif','Modern bathroom detail'),
    ('assets/images/orebic-harbor-day.avif','Orebić atmosphere and nearby setting'),
    ('assets/images/orebic-harbor-twilight.avif','Evening coast ambience'),
    ('assets/images/exterior-night-landscape.avif','Night exterior with boutique feel'),
    ('assets/images/pool-fruit-detail.avif','Poolside detail shot'),
    ('assets/images/terrace-sofa-day.avif','Spacious family-style terrace'),
    ('assets/images/living-dining-large-window.avif','Interior framed by large glazing'),
]
gallery_html = ''.join([f'<div class="gallery-item reveal"><img src="{src}" alt="{cap}"><div class="gallery-caption">{cap}</div></div>' for src,cap in gallery_images])
gallery_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/exterior-night-front.avif" alt="Sunny Day by night"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Gallery</span></div>
      <h1>Strong visuals, carefully selected.</h1>
      <p>This gallery uses the supplied real property photos and avoids obvious duplication, giving the website a cleaner and more professional image narrative.</p>
    </div>
  </section>
  <section class="section">
    <div class="container intro intro--narrow reveal">
      <p class="eyebrow">Curated gallery</p>
      <h2>Not overloaded. Not repetitive. Just the best moments.</h2>
      <p>The gallery balances exteriors, pool scenes, terraces and interiors so the website feels polished instead of crowded.</p>
    </div>
    <div class="container gallery-grid" style="margin-top:2rem;">{gallery_html}</div>
  </section>
  {quick_cta}
</main>
'''
write(os.path.join(project,'gallery.html'), layout('Gallery | Sunny Day Orebić', 'Curated photo gallery for Sunny Day Orebić.', gallery_body))

# ---------- About page ----------
about_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/exterior-aerial-building.avif" alt="Sunny Day building"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>About</span></div>
      <h1>A calmer, more premium story for the property.</h1>
      <p>The redesign positions Sunny Day Orebić as a stylish Mediterranean stay rather than just another apartment listing.</p>
    </div>
  </section>
  <section class="section">
    <div class="container split">
      <div class="info-box reveal rich-text">
        <p class="eyebrow">About Sunny Day</p>
        <h2>The hospitality feel matters.</h2>
        <p>Guests often decide emotionally first and logically second. That is why the new site puts atmosphere, comfort and destination value at the center. Instead of clutter, it uses clear sections, immersive photography and refined typography.</p>
        <p>The result is a website that feels more trustworthy, more memorable and more aligned with the quality visible in the property itself.</p>
      </div>
      <div class="split-media reveal"><img src="assets/images/hero-aerial-day.avif" alt="Aerial property"></div>
    </div>
  </section>
  <section class="section section--soft">
    <div class="container stat-row">
      <div class="stat-card reveal"><strong>Premium</strong><span>visual direction</span></div>
      <div class="stat-card reveal"><strong>Direct</strong><span>inquiry strategy</span></div>
      <div class="stat-card reveal"><strong>Clean</strong><span>multi-page architecture</span></div>
      <div class="stat-card reveal"><strong>Modern</strong><span>scroll-driven UX</span></div>
    </div>
  </section>
  {quick_cta}
</main>
'''
write(os.path.join(project,'about.html'), layout('About | Sunny Day Orebić', 'About the Sunny Day Orebić apartments.', about_body))

# ---------- Location page ----------
location_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/view-aerial-coast.avif" alt="Orebić coastline"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Location</span></div>
      <h1>Perfectly placed for Orebić, Pelješac and island day trips.</h1>
      <p>The new location page clarifies where the property sits and why that location is useful for beaches, Korčula, scenic drives and relaxed stays.</p>
    </div>
  </section>
  <section class="section">
    <div class="container split">
      <div class="info-box reveal">
        <p class="eyebrow">Location benefits</p>
        <h2>Orebić works brilliantly as a base.</h2>
        <ul class="check-list">
          <li><span>✓</span><span>Easy access to beaches, promenades and the wider Pelješac peninsula.</span></li>
          <li><span>✓</span><span>Great starting point for Korčula, Ston, wineries and scenic coastal drives.</span></li>
          <li><span>✓</span><span>Ideal for guests who want both lazy days and memorable day trips.</span></li>
        </ul>
      </div>
      <div class="split-media reveal"><img src="assets/images/orebic-harbor-day.avif" alt="Orebić coast"></div>
    </div>
  </section>
  <section class="section section--soft">
    <div class="container reveal">
      <p class="eyebrow">Map</p>
      <h2 style="font-family:Cormorant Garamond,serif;font-size:clamp(2.2rem,4vw,3.5rem);margin-top:0;">Find Sunny Day Orebić</h2>
      <iframe class="embedded-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Ul.%20Bana%20Josipa%20Jela%C4%8Di%C4%87a%2082,%2020250%20Orebi%C4%87,%20Croatia&output=embed"></iframe>
    </div>
  </section>
  <section class="section">
    <div class="container listing">
      <article class="listing__item reveal"><h3 style="font-family:Cormorant Garamond,serif;font-size:2rem;margin:0 0 .5rem;">Orebić & beaches</h3><p>Show this as the everyday holiday layer: easy walks, beach time and the town’s relaxed coastal rhythm.</p></article>
      <article class="listing__item reveal"><h3 style="font-family:Cormorant Garamond,serif;font-size:2rem;margin:0 0 .5rem;">Korčula</h3><p>Position it as the perfect nearby old-town escape for culture, dining and sunset atmosphere.</p></article>
      <article class="listing__item reveal"><h3 style="font-family:Cormorant Garamond,serif;font-size:2rem;margin:0 0 .5rem;">Pelješac road trips</h3><p>Use this page to suggest wineries, Ston and scenic stops that encourage longer stays.</p></article>
    </div>
  </section>
  {quick_cta}
</main>
'''
write(os.path.join(project,'location.html'), layout('Location | Sunny Day Orebić', 'Location and access information for Sunny Day Orebić.', location_body))

# ---------- Contact page ----------
contact_body = f'''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/terrace-sofa-view.avif" alt="Contact Sunny Day Orebić"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Contact</span></div>
      <h1>Check dates. Ask a question. Start your stay directly.</h1>
      <p>This is the main conversion page: clear form fields, visible contact options and a premium look that feels more reliable than a standard booking widget.</p>
    </div>
  </section>
  <section class="section">
    <div class="container inquiry-wrap">
      <div>
        <div class="reveal" style="margin-bottom:1rem;">
          <p class="eyebrow">Availability form</p>
          <h2>Tell us your dates and number of guests.</h2>
          <p class="lead">The form is intentionally simple and aligned with the owner’s preference for direct communication instead of online booking.</p>
        </div>
        {inquiry_form}
      </div>
      <aside class="contact-card reveal">
        <h3>Direct contact</h3>
        <div class="contact-points">
          <div class="contact-point"><strong>Phone</strong><br><a class="js-phone-link" href="#">+385 91 730 6770</a></div>
          <div class="contact-point"><strong>Email</strong><br><a class="js-email-link" href="#">info@sunnydayorebic.com</a></div>
          <div class="contact-point"><strong>WhatsApp</strong><br><a class="js-whatsapp-link" href="#" target="_blank" rel="noreferrer">Open chat</a></div>
          <div class="contact-point"><strong>Address</strong><br>Ul. Bana Josipa Jelačića 82, 20250 Orebić, Croatia</div>
        </div>
        <img src="assets/images/exterior-night-landscape.avif" alt="Sunny Day exterior at dusk" style="margin-top:1.25rem;border-radius:22px;">
      </aside>
    </div>
  </section>
</main>
'''
write(os.path.join(project,'contact.html'), layout('Contact | Sunny Day Orebić', 'Contact Sunny Day Orebić to check availability.', contact_body))

# ---------- Legal ----------
privacy_body = '''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/exterior-night-front.avif" alt="Privacy page"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Privacy Policy</span></div>
      <h1>Privacy Policy</h1>
      <p>This template page can be adapted with the owner’s final legal wording before publication.</p>
    </div>
  </section>
  <section class="section">
    <div class="container info-box rich-text reveal">
      <h2>Privacy basics</h2>
      <p>This website collects only the information needed to respond to availability inquiries, such as name, email, phone number, requested dates and the number of guests.</p>
      <p>Submitted data should be processed solely for guest communication and availability checks. The website owner should keep guest data safe, avoid sharing it unnecessarily and comply with applicable privacy rules.</p>
      <p>Before launching, replace this page with the property’s final approved privacy policy, including cookie information and all required legal identifiers.</p>
    </div>
  </section>
</main>
'''
write(os.path.join(project,'privacy-policy.html'), layout('Privacy Policy | Sunny Day Orebić', 'Privacy Policy for Sunny Day Orebić.', privacy_body))

terms_body = '''
<main>
  <section class="page-banner">
    <div class="page-banner__bg"><img src="assets/images/exterior-night-aerial.avif" alt="Terms page"></div>
    <div class="page-banner__overlay"></div>
    <div class="container page-banner__content reveal">
      <div class="crumbs"><a href="index.html">Home</a> <span>•</span> <span>Terms & Conditions</span></div>
      <h1>Terms & Conditions</h1>
      <p>This template page gives a clean space for the final guest terms and conditions.</p>
    </div>
  </section>
  <section class="section">
    <div class="container info-box rich-text reveal">
      <h2>Suggested structure</h2>
      <ul>
        <li>Reservation and confirmation process</li>
        <li>Check-in and check-out rules</li>
        <li>Cancellation and modification terms</li>
        <li>House rules and guest responsibilities</li>
        <li>Payment, deposits and damage policy</li>
      </ul>
      <p>Replace this placeholder copy with the owner’s final legally approved terms before going live.</p>
    </div>
  </section>
</main>
'''
write(os.path.join(project,'terms.html'), layout('Terms & Conditions | Sunny Day Orebić', 'Terms and conditions for Sunny Day Orebić.', terms_body))

# ---------- README ----------
readme = '''
SUNNY DAY OREBIĆ – STATIC WEBSITE PACKAGE

Što je napravljeno:
- potpuno nova premium statička web stranica
- više stranica i podstranica
- apartmani + pojedinačne podstranice
- Experience / izleti podstranice
- galerija, lokacija, kontakt, legal pages
- kontakt forma s datumima, brojem gostiju, telefonom i e-mailom
- moderna animacija pri skrolu i hero slideshow
- korištene su stvarne fotografije iz dostavljenog ZIP-a (selekcija bez namjernog dupliranja)

VAŽNO PRIJE OBJAVE
1) Otvori datoteku: assets/js/site-config.js
2) Unesi / provjeri:
   - instagram link
   - WhatsApp broj ako treba drugi format
   - ako želiš, promijeni telefon / e-mail / adresu
3) Za rad forme obavezno zamijeni:
   web3formsAccessKey: 'YOUR_WEB3FORMS_ACCESS_KEY'
   svojim stvarnim Web3Forms ključem.

DEPLOY
- cijeli sadržaj ovog foldera stavi na GitHub repo
- spoji repo na Cloudflare Pages
- build command nije potreban
- output directory: /

NAPOMENA
- Legal stranice (Privacy Policy i Terms) su pripremljene kao čisti predlošci i preporuka je ubaciti finalni službeni tekst vlasnika.
'''
write(os.path.join(project,'README.txt'), readme)
