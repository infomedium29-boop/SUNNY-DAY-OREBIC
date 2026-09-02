
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
