/**
 * BPO COMPANY — Navigation Module
 * Header stickiness, responsive drawer, dropdowns, keyboard accessibility
 */

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mainNav = document.querySelector('.main-nav');
  const navDropdowns = document.querySelectorAll('.nav-item.has-dropdown');

  // Sticky Header on Scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // Mobile Menu Toggle
  if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isActive = mainNav.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', String(isActive));
      document.body.style.overflow = isActive ? 'hidden' : '';
    });
  }

  // Mobile Dropdown toggles
  navDropdowns.forEach(dropdown => {
    const link = dropdown.querySelector('.nav-link');
    if (link) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 992) {
          e.preventDefault();
          dropdown.classList.toggle('open');
          const isExpanded = dropdown.classList.contains('open');
          link.setAttribute('aria-expanded', String(isExpanded));
        }
      });
    }
  });

  // Close nav on click outside
  document.addEventListener('click', (e) => {
    if (mainNav && mainNav.classList.contains('active') && !mainNav.contains(e.target) && !mobileToggle.contains(e.target)) {
      mainNav.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });

  // Escape key to close mobile nav
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (mainNav && mainNav.classList.contains('active')) {
        mainNav.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
      navDropdowns.forEach(d => d.classList.remove('open'));
    }
  });

  // Active link detection
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-item');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
      const parentDropdown = link.closest('.nav-item.has-dropdown');
      if (parentDropdown) {
        parentDropdown.querySelector('.nav-link')?.classList.add('active');
      }
    }
  });
});
