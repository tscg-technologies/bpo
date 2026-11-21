/**
 * BPO COMPANY — FAQ Accordion Module
 * Accessible keyboard navigation and animated collapsible panels
 */

document.addEventListener('DOMContentLoaded', () => {
  const accordionItems = document.querySelectorAll('.accordion-item');

  accordionItems.forEach(item => {
    const btn = item.querySelector('.accordion-btn');
    const content = item.querySelector('.accordion-content');

    if (!btn || !content) return;

    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      // Close other open accordions in the same group (optional cleaner UX)
      const parentGroup = item.closest('.accordion');
      if (parentGroup) {
        parentGroup.querySelectorAll('.accordion-item.active').forEach(activeItem => {
          if (activeItem !== item) {
            activeItem.classList.remove('active');
            activeItem.querySelector('.accordion-btn')?.setAttribute('aria-expanded', 'false');
            const activeContent = activeItem.querySelector('.accordion-content');
            if (activeContent) activeContent.style.maxHeight = '0px';
          }
        });
      }

      if (isOpen) {
        item.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
        content.style.maxHeight = '0px';
      } else {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
        content.style.maxHeight = content.scrollHeight + 30 + 'px';
      }
    });

    // Keyboard support for space/enter
    btn.addEventListener('keydown', (e) => {
      if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        btn.click();
      }
    });
  });
});
