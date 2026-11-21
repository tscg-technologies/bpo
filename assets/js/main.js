/**
 * BPO COMPANY — Main Entry Script
 * Scroll reveals, back-to-top button, interactive helpers
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Footer Year
  const yearEls = document.querySelectorAll('.current-year');
  const currentYear = new Date().getFullYear();
  yearEls.forEach(el => el.textContent = currentYear);

  // 2. Back to Top Button
  const backToTopBtn = document.querySelector('.back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 3. Scroll Reveal via Intersection Observer
  if ('IntersectionObserver' in window) {
    const revealElements = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          obs.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.1
    });

    revealElements.forEach(el => observer.observe(el));
  } else {
    // Fallback for older browsers
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-revealed'));
  }

  // 4. Smooth Anchor Link Scrolling
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});
