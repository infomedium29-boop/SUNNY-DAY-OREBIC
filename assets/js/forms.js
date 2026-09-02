
(function(){
  const config = window.SUNNY_DAY_CONFIG || {};
  const isHR = location.pathname.includes('/hr/');
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
        if (statusEl) statusEl.textContent = (isHR ? 'Prije objave unesite Web3Forms access key u assets/js/site-config.js.' : 'Replace the Web3Forms access key in assets/js/site-config.js before going live.');
        return;
      }
      if (submitBtn) submitBtn.disabled = true;
      if (statusEl) statusEl.textContent = (isHR ? 'Šaljem upit...' : 'Sending your inquiry...');
      try {
        const response = await fetch(config.formEndpoint || 'https://api.web3forms.com/submit', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        if (data.success) {
          form.reset();
          if (statusEl) statusEl.textContent = (isHR ? 'Hvala — vaš upit je poslan.' : 'Thank you — your inquiry has been sent.');
        } else {
          if (statusEl) statusEl.textContent = data.message || (isHR ? 'Došlo je do pogreške. Pokušajte ponovno.' : 'Something went wrong. Please try again.');
        }
      } catch (err) {
        if (statusEl) statusEl.textContent = (isHR ? 'Upit trenutačno nije moguće poslati. Pokušajte ponovno kasnije.' : 'Unable to send right now. Please try again later.');
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  });
})();
