/**
 * BPO COMPANY — Job Search and Filtering Module
 * Real-time frontend search and multi-criteria facet filtering
 */

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('job-search-input');
  const departmentFilter = document.getElementById('job-dept-filter');
  const experienceFilter = document.getElementById('job-exp-filter');
  const typeFilter = document.getElementById('job-type-filter');
  const resetBtn = document.getElementById('job-reset-filters');
  const jobList = document.getElementById('job-listings-container');
  const jobCount = document.getElementById('job-count-display');
  const emptyState = document.getElementById('job-empty-state');

  if (!jobList) return;

  const jobCards = jobList.querySelectorAll('.job-card');

  const filterJobs = () => {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const dept = departmentFilter ? departmentFilter.value.toLowerCase() : '';
    const exp = experienceFilter ? experienceFilter.value.toLowerCase() : '';
    const type = typeFilter ? typeFilter.value.toLowerCase() : '';

    let visibleCount = 0;

    jobCards.forEach(card => {
      const title = card.getAttribute('data-title')?.toLowerCase() || '';
      const cardDept = card.getAttribute('data-department')?.toLowerCase() || '';
      const cardExp = card.getAttribute('data-experience')?.toLowerCase() || '';
      const cardType = card.getAttribute('data-type')?.toLowerCase() || '';
      const textContent = card.innerText.toLowerCase();

      const matchesQuery = !query || title.includes(query) || textContent.includes(query);
      const matchesDept = !dept || cardDept === dept;
      const matchesExp = !exp || cardExp === exp;
      const matchesType = !type || cardType === type;

      if (matchesQuery && matchesDept && matchesExp && matchesType) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (jobCount) {
      jobCount.textContent = `Showing ${visibleCount} demo open role${visibleCount === 1 ? '' : 's'}`;
    }

    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  };

  // Event listeners
  if (searchInput) searchInput.addEventListener('input', filterJobs);
  if (departmentFilter) departmentFilter.addEventListener('change', filterJobs);
  if (experienceFilter) experienceFilter.addEventListener('change', filterJobs);
  if (typeFilter) typeFilter.addEventListener('change', filterJobs);

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      if (departmentFilter) departmentFilter.value = '';
      if (experienceFilter) experienceFilter.value = '';
      if (typeFilter) typeFilter.value = '';
      filterJobs();
    });
  }

  // Initial trigger
  filterJobs();
});
