
(() => {
  const journey = document.querySelector('[data-cinematic-journey]');
  if (!journey) return;

  const frames = Array.from(journey.querySelectorAll('.cinematic-frame'));
  const chapters = Array.from(journey.querySelectorAll('.journey-chapter'));
  const dots = Array.from(journey.querySelectorAll('.journey-dot'));
  const fill = journey.querySelector('.cinematic-journey__progress-fill');
  const count = journey.querySelector('[data-journey-count]');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  frames.forEach((img, index) => {
    if (index > 0) {
      const preload = new Image();
      preload.src = img.currentSrc || img.src;
    }
  });

  if (reduceMotion) return;

  let ticking = false;
  let lastProgress = -1;

  const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
  const smoothstep = (a, b, x) => {
    const t = clamp((x - a) / (b - a), 0, 1);
    return t * t * (3 - 2 * t);
  };

  function render() {
    ticking = false;
    const rect = journey.getBoundingClientRect();
    const scrollable = Math.max(1, journey.offsetHeight - window.innerHeight);
    const progress = clamp((-rect.top) / scrollable, 0, 1);
    if (Math.abs(progress - lastProgress) < 0.00025) return;
    lastProgress = progress;

    const rawFrame = progress * (frames.length - 1);
    const baseIndex = Math.floor(rawFrame);
    const blend = rawFrame - baseIndex;

    frames.forEach((frame, index) => {
      let opacity = 0;
      if (index === baseIndex) opacity = 1 - blend;
      if (index === baseIndex + 1) opacity = blend;
      if (progress === 1 && index === frames.length - 1) opacity = 1;

      const distance = rawFrame - index;
      const activeDistance = clamp(distance, -1, 1);
      const zoom = 1.06 + (activeDistance * 0.065);
      const driftX = (index % 2 === 0 ? 1 : -1) * activeDistance * 1.15;
      const driftY = activeDistance * -0.8;
      const blur = Math.abs(activeDistance) > .82 ? 2.2 : 0;

      frame.style.opacity = opacity.toFixed(4);
      frame.style.transform = `scale(${zoom.toFixed(4)}) translate3d(${driftX.toFixed(3)}%, ${driftY.toFixed(3)}%, 0)`;
      frame.style.filter = `saturate(.98) contrast(1.035) brightness(${(0.91 + opacity * 0.09).toFixed(3)}) blur(${blur.toFixed(2)}px)`;
      frame.style.zIndex = opacity > 0 ? '1' : '0';
    });

    chapters.forEach((chapter, index) => {
      const start = Number(chapter.dataset.start || 0);
      const end = Number(chapter.dataset.end || 1);
      const fadeInEnd = start + Math.min(.055, (end - start) * .32);
      const fadeOutStart = end - Math.min(.055, (end - start) * .32);
      let opacity = 0;
      if (progress >= start && progress <= end) {
        const inOpacity = smoothstep(start, fadeInEnd, progress);
        const outOpacity = 1 - smoothstep(fadeOutStart, end, progress);
        opacity = Math.min(inOpacity, outOpacity);
      }
      if (index === 0 && progress < start + .01) opacity = 1;
      if (index === chapters.length - 1 && progress > end - .01) opacity = 1;
      chapter.style.opacity = opacity.toFixed(4);
      chapter.style.transform = `translate3d(0, ${(1 - opacity) * 24}px, 0)`;
      chapter.classList.toggle('is-active', opacity > .5);
    });

    const activeChapter = chapters.findIndex(ch => {
      const s = Number(ch.dataset.start || 0);
      const e = Number(ch.dataset.end || 1);
      return progress >= s && progress < e;
    });
    dots.forEach((dot, idx) => dot.classList.toggle('is-active', idx === (activeChapter === -1 ? dots.length - 1 : activeChapter)));

    if (fill) fill.style.width = `${(progress * 100).toFixed(2)}%`;
    if (count) count.textContent = `${String(Math.min(frames.length, Math.floor(rawFrame) + 1)).padStart(2,'0')} / ${String(frames.length).padStart(2,'0')}`;
    journey.classList.toggle('is-complete', progress > .965);
  }

  function requestRender() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(render);
    }
  }

  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      const chapter = chapters[index];
      if (!chapter) return;
      const start = Number(chapter.dataset.start || 0);
      const targetY = window.scrollY + journey.getBoundingClientRect().top + start * (journey.offsetHeight - window.innerHeight) + 2;
      window.scrollTo({ top: targetY, behavior: 'smooth' });
    });
  });

  render();
  window.addEventListener('scroll', requestRender, { passive: true });
  window.addEventListener('resize', requestRender, { passive: true });
})();
