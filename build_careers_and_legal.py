"""
Careers and Legal Pages Generator (8 Pages Total)
Generates:
careers.html, job-openings.html, job-details.html, apply-job.html,
employee-development.html, privacy-policy.html, terms-and-conditions.html,
cookie-policy.html
"""

import os
from builder import render_page, render_placeholder, render_breadcrumb, LOGO_SVG
from generate_pages import render_cta_banner

def build_careers():
    crumbs = [("Home", "index.html"), ("Careers", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Talent &amp; Culture</span>
        <h1>Build Your Career in Business Process Outsourcing</h1>
        <p class="page-hero-desc">
          Structured training programs, global service delivery exposure, and defined leadership trajectories across customer experience and operational management.
        </p>
        <div class="hero-actions">
          <a href="job-openings.html" class="btn btn-primary btn-lg">Browse Demo Job Openings</a>
          <a href="employee-development.html" class="btn btn-outline-white btn-lg">Training &amp; Development</a>
        </div>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>DEMO RECRUITMENT NOTICE &mdash; NOT A VERIFIED LIVE VACANCY</h4>
            <p>All job descriptions, career opportunities, and application processes on this website are illustrative demonstrations. We do not represent a live hiring entity or guarantee employment outcomes.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Working With Us</span>
            <h2>A Culture of Continuous Growth &amp; Support</h2>
            <p>
              In business process outsourcing, your talent is the operational backbone. We invest in extensive onboarding, transparent feedback mechanisms, and collaborative team structures where associates can develop lifelong professional communication and technical skills.
            </p>
            <p>
              Whether joining in front-line customer care, analytical back-office data processing, or technical helpdesk triage, every associate has access to continuous coaching and defined leadership pathways.
            </p>
            <div style="margin-top: 1.5rem;">
              <a href="job-openings.html" class="btn btn-secondary">Explore Sample Vacancies &rarr;</a>
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-careers-culture.jpg", "Diverse Workplace Culture", "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

        <div class="section-header reveal">
          <span class="section-tag">Career Paths</span>
          <h2 class="section-title">Operational Career Categories</h2>
          <p class="section-desc">Explore the primary functional tracks available within international business process outsourcing organizations.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 4rem;">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
            <h3 class="card-title">Customer Experience Operations</h3>
            <p class="card-desc">Voice, live chat, and email support roles focusing on brand communication, empathy, and rapid customer inquiry resolution.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3 class="card-title">Technical Support &amp; Helpdesk</h3>
            <p class="card-desc">Tier 1 and Tier 2 technical diagnostics, troubleshooting trees, bug reporting, and software configuration guidance.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg></div>
            <h3 class="card-title">Back Office &amp; Data Operations</h3>
            <p class="card-desc">High-precision data entry, document indexing, transaction verification, and administrative workflow processing.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
            <h3 class="card-title">Quality Assurance &amp; Auditing</h3>
            <p class="card-desc">Independent interaction scoring, SOP compliance auditing, calibration sessions, and coaching feedback loops.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
            <h3 class="card-title">Operational Team Leadership</h3>
            <p class="card-desc">Floor supervision, queue balance management, real-time escalation support, and team performance mentorship.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></div>
            <h3 class="card-title">Training &amp; Curriculum Development</h3>
            <p class="card-desc">Designing onboarding coursework, maintaining SOP knowledge manuals, and leading simulated role-play certifications.</p>
            <span class="badge badge-demo">Illustrative Track</span>
          </div>
        </div>

        <div style="background: var(--color-light-bg); border-radius: var(--radius-xl); padding: 3rem; text-align: center; border: 1px solid var(--color-border);">
          <h2>Ready to Explore Sample Opportunities?</h2>
          <p style="color: var(--color-muted-text); max-width: 600px; margin: 0.75rem auto 1.75rem auto;">
            Review our sample job openings with real-time filtering by department, experience level, and employment type.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="job-openings.html" class="btn btn-primary">Browse Sample Job Openings</a>
            <a href="apply-job.html" class="btn btn-secondary">Demo Application Form</a>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner("Looking for Business Outsourcing Solutions Instead?",
                       "Explore how our enterprise BPO services can support your operational roadmap.",
                       "Explore Services", "services.html",
                       "Contact Sales", "contact.html")}
    """
    return render_page(
        "Careers — Build Your Future in Business Process Outsourcing",
        "Explore career opportunities in BPO: customer experience, technical support, back-office operations, quality assurance, and operational leadership.",
        "careers",
        body,
        "careers.html"
    )

def build_job_openings():
    crumbs = [("Home", "index.html"), ("Careers", "careers.html"), ("Job Openings", None)]

    jobs_data = [
        ("Customer Support Executive (Voice & Non-Voice)", "Customer Experience", "Entry Level (0-2 Yrs)", "Full-Time", "sample-role-1"),
        ("Technical Support Associate (Tier 1 Helpdesk)", "Technical Support", "Mid Level (2-4 Yrs)", "Full-Time", "sample-role-2"),
        ("Back Office Executive (Data Operations)", "Back Office", "Entry Level (0-2 Yrs)", "Full-Time", "sample-role-3"),
        ("Data Entry & Validation Associate", "Back Office", "Entry Level (0-2 Yrs)", "Full-Time", "sample-role-4"),
        ("Quality Analyst (Interaction Auditing)", "Quality Assurance", "Mid Level (2-4 Yrs)", "Full-Time", "sample-role-5"),
        ("Customer Service Team Leader", "Operations Management", "Senior Level (4+ Yrs)", "Full-Time", "sample-role-6"),
        ("E-Commerce Chat Support Specialist", "Customer Experience", "Entry Level (0-2 Yrs)", "Rotational Shift", "sample-role-7"),
        ("HR Recruitment Coordinator Associate", "Human Resources", "Entry Level (0-2 Yrs)", "Full-Time", "sample-role-8")
    ]

    cards_html = ""
    for title, dept, exp, emp_type, _ in jobs_data:
        cards_html += f"""<div class="job-card reveal" data-title="{title}" data-department="{dept}" data-experience="{exp}" data-type="{emp_type}">
  <div class="job-info">
    <div style="margin-bottom: 0.35rem;">
      <span class="badge badge-demo">DEMO JOB LISTING &mdash; NOT A VERIFIED LIVE VACANCY</span>
    </div>
    <h3><a href="job-details.html">{title}</a></h3>
    <div class="job-meta-tags">
      <span class="job-meta-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
        {dept}
      </span>
      <span class="job-meta-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        {exp}
      </span>
      <span class="job-meta-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
        Hyderabad &bull; On-Site
      </span>
      <span class="badge badge-blue">{emp_type}</span>
    </div>
  </div>
  <div style="display: flex; gap: 0.75rem; flex-shrink: 0;">
    <a href="job-details.html" class="btn btn-secondary btn-sm">View Details</a>
    <a href="apply-job.html" class="btn btn-primary btn-sm">Demo Apply</a>
  </div>
</div>"""

    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Demo Opportunities</span>
        <h1>Sample BPO Job Openings</h1>
        <p class="page-hero-desc">
          Browse illustrative vacancies across customer care, technical troubleshooting, data processing, and quality assurance.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>DEMO JOB LISTING &mdash; NOT A VERIFIED LIVE VACANCY</h4>
            <p>The positions below represent sample operational roles for website demonstration purposes. Submitting applications does not connect to an active recruitment team.</p>
          </div>
        </div>

        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-workplace-diversity.jpg", "Workplace Diversity & Operations Culture", "ratio-21-9", "1920 &times; 820")}
        </div>

        <!-- Filter Bar -->
        <div class="filter-bar reveal">
          <div class="filter-grid">
            <div>
              <label class="form-label" for="job-search-input">Search by Job Title</label>
              <input type="text" id="job-search-input" class="form-control" placeholder="Search by role title or keyword...">
            </div>
            <div>
              <label class="form-label" for="job-dept-filter">Department</label>
              <select id="job-dept-filter" class="form-control">
                <option value="">All Departments</option>
                <option value="Customer Experience">Customer Experience</option>
                <option value="Technical Support">Technical Support</option>
                <option value="Back Office">Back Office</option>
                <option value="Quality Assurance">Quality Assurance</option>
                <option value="Operations Management">Operations Management</option>
                <option value="Human Resources">Human Resources</option>
              </select>
            </div>
            <div>
              <label class="form-label" for="job-exp-filter">Experience</label>
              <select id="job-exp-filter" class="form-control">
                <option value="">All Experience</option>
                <option value="Entry Level (0-2 Yrs)">Entry Level (0-2 Yrs)</option>
                <option value="Mid Level (2-4 Yrs)">Mid Level (2-4 Yrs)</option>
                <option value="Senior Level (4+ Yrs)">Senior Level (4+ Yrs)</option>
              </select>
            </div>
            <div>
              <label class="form-label" for="job-type-filter">Type</label>
              <select id="job-type-filter" class="form-control">
                <option value="">All Types</option>
                <option value="Full-Time">Full-Time</option>
                <option value="Rotational Shift">Rotational Shift</option>
              </select>
            </div>
            <div>
              <button id="job-reset-filters" class="btn btn-secondary btn-sm" style="height: 42px;">Reset</button>
            </div>
          </div>
        </div>

        <!-- Counter & Results -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
          <span id="job-count-display" style="font-weight: 600; color: var(--color-primary-navy);">Showing 8 demo open roles</span>
          <span style="font-size: 0.8125rem; color: var(--color-muted-text);">Filter results update instantly</span>
        </div>

        <div id="job-listings-container" class="job-cards-list">
          {cards_html}
        </div>

        <div id="job-empty-state" style="display: none; text-align: center; padding: 4rem 1rem; background: var(--color-light-bg); border-radius: var(--radius-lg); margin-top: 1.5rem;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--color-muted-text)" stroke-width="1.5" style="margin: 0 auto 1rem auto;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <h3>No matching job roles found</h3>
          <p style="color: var(--color-muted-text); margin-bottom: 1rem;">Try clearing your search query or selecting a different department filter.</p>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Job Openings — Search Sample BPO Careers",
        "Browse sample vacancies across customer care, technical troubleshooting, data entry, quality assurance, and operations management. Interactive search and filtering.",
        "careers",
        body,
        "job-openings.html",
        extra_scripts='<script src="assets/js/job-search.js"></script>'
    )

def build_job_details():
    crumbs = [("Home", "index.html"), ("Careers", "careers.html"), ("Job Openings", "job-openings.html"), ("Sample Job Details", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Demo Job Listing</span>
        <h1>Customer Support Executive (Voice &amp; Non-Voice)</h1>
        <p class="page-hero-desc">
          Illustrative job specification detailing typical role responsibilities, required qualifications, and candidate competencies for customer experience operations.
        </p>
        <div class="hero-actions">
          <a href="apply-job.html" class="btn btn-primary btn-lg">Submit Demo Application</a>
          <a href="job-openings.html" class="btn btn-outline-white btn-lg">Back to Job Openings</a>
        </div>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>DEMO JOB LISTING &mdash; NOT A VERIFIED LIVE VACANCY</h4>
            <p>This job description represents an illustrative profile for website demonstration purposes. It does not represent an active commercial recruitment campaign.</p>
          </div>
        </div>

        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-professional-workspace.jpg", "Professional Support Workspace", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="grid-2-1">
          <div class="prose-content">
            <h2>Role Overview</h2>
            <p>
              As a Customer Support Executive, the associate is the primary ambassador for customer care across telephone, email ticket, and live chat channels. The role centers on delivering prompt, empathetic, and accurate assistance in resolving customer inquiries, updating accounts, and documenting dispositions.
            </p>

            <h2>Primary Responsibilities</h2>
            <ul>
              <li>Handle incoming voice telephone inquiries, live web chats, and email tickets in accordance with established Service Level Agreements (SLAs).</li>
              <li>Authenticate customer identities and verify account details adhering strictly to confidentiality and privacy procedures.</li>
              <li>Diagnose customer issues using verified Standard Operating Procedure (SOP) manuals and decision tree documentation.</li>
              <li>Provide step-by-step guidance on account navigation, order status, return authorization, and billing questions.</li>
              <li>Log thorough, accurate disposition tags and interaction notes in the CRM system upon contact completion.</li>
              <li>Escalate complex or ambiguous inquiries to Tier 2 specialists or team leads with full context and customer history.</li>
              <li>Participate actively in weekly quality calibration sessions and individual coaching reviews to continuously elevate performance.</li>
            </ul>

            <h2>Example Eligibility Criteria</h2>
            <ul>
              <li><strong>Education:</strong> Bachelor's degree or equivalent high school diploma with demonstrated English proficiency.</li>
              <li><strong>Experience:</strong> 0 to 2 years of prior experience in customer support, contact centers, retail client service, or hospitality.</li>
              <li><strong>Communication Skills:</strong> Fluent verbal and written English with a polite, empathetic, and professional tone.</li>
              <li><strong>Technical Aptitude:</strong> Comfort navigating dual-monitor computer environments, typing speed of 35+ WPM with 95% accuracy.</li>
              <li><strong>Shift Flexibility:</strong> Ability to work rotational shifts, including weekends and holidays based on operational rosters.</li>
            </ul>

            <h2>Key Skills &amp; Competencies</h2>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0;">
              <span class="badge badge-blue">Active Listening</span>
              <span class="badge badge-blue">Written Empathy</span>
              <span class="badge badge-blue">CRM Navigation</span>
              <span class="badge badge-blue">Typing Accuracy</span>
              <span class="badge badge-blue">De-Escalation Techniques</span>
              <span class="badge badge-blue">SOP Adherence</span>
            </div>

            <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--color-border);">
              <a href="apply-job.html" class="btn btn-primary btn-lg">Submit Demo Application for this Role</a>
            </div>
          </div>

          <aside>
            <div class="sidebar-box">
              <h3 class="sidebar-title">Job Information</h3>
              <div style="font-size: 0.9rem; display: flex; flex-direction: column; gap: 0.75rem;">
                <div><strong>Department:</strong> Customer Experience</div>
                <div><strong>Experience:</strong> Entry Level (0-2 Yrs)</div>
                <div><strong>Type:</strong> Full-Time (Rotational Shifts)</div>
                <div><strong>Location:</strong> Hyderabad (Illustrative Location)</div>
                <div><strong>Listing ID:</strong> DEMO-JOB-101</div>
              </div>
            </div>

            <div class="sidebar-box">
              <h3 class="sidebar-title">Application Notice</h3>
              <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">
                This position is an illustrative demo. Our application form demonstrates frontend validation without delivering resumes to real recruiters.
              </p>
              <a href="apply-job.html" class="btn btn-secondary btn-sm" style="width: 100%;">Open Demo Application Form</a>
            </div>
          </aside>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Job Details — Customer Support Executive (Demo Listing)",
        "Review sample job description, responsibilities, eligibility criteria, and skills for Customer Support Executive role. Frontend demonstration.",
        "careers",
        body,
        "job-details.html"
    )

def build_apply_job():
    crumbs = [("Home", "index.html"), ("Careers", "careers.html"), ("Job Openings", "job-openings.html"), ("Demo Job Application", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Demo Application</span>
        <h1>Submit Demo Job Application</h1>
        <p class="page-hero-desc">
          Frontend-only application demonstration. Interactive file validation, form field checks, and client-side feedback without server persistence.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <!-- Mandatory Notice -->
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>DEMO APPLICATION NOTICE &mdash; FRONTEND ONLY</h4>
            <p>This website is a frontend demonstration. No resume files, personal contact information, or form data will be uploaded, transmitted, or stored on any server or delivered to a recruiter.</p>
          </div>
        </div>

        <div style="margin-bottom: 2.5rem;">
          {render_placeholder("bpo-talent-application.jpg", "Talent Acquisition & Application Desk", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="form-card reveal">
          <h2 style="margin-bottom: 0.5rem;">Job Application Form (Demonstration)</h2>
          <p style="font-size: 0.9rem; color: var(--color-muted-text); margin-bottom: 2rem;">Fields marked with <span class="req">*</span> are required for interactive validation.</p>

          <div id="job-form-alert" class="alert" style="display: none;"></div>

          <form id="demo-job-application-form" novalidate>
            <div class="grid-2" style="gap: 1.5rem;">
              <div class="form-group">
                <label class="form-label" for="applicant_name">Full Name <span class="req">*</span></label>
                <input type="text" id="applicant_name" name="applicant_name" class="form-control" placeholder="Alex Morgan" required>
                <div class="form-error">Please enter your full name (minimum 2 characters).</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="applicant_email">Email Address <span class="req">*</span></label>
                <input type="email" id="applicant_email" name="applicant_email" class="form-control" placeholder="alex@example.com" required>
                <div class="form-error">Please enter a valid email address.</div>
              </div>
            </div>

            <div class="grid-2" style="gap: 1.5rem;">
              <div class="form-group">
                <label class="form-label" for="applicant_phone">Phone Number <span class="req">*</span></label>
                <input type="tel" id="applicant_phone" name="applicant_phone" class="form-control" placeholder="0000000000" required>
                <div class="form-error">Please enter a valid phone number.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="applicant_location">Current Location <span class="req">*</span></label>
                <input type="text" id="applicant_location" name="applicant_location" class="form-control" placeholder="City, State" required>
                <div class="form-error">Please enter your current location.</div>
              </div>
            </div>

            <div class="grid-2" style="gap: 1.5rem;">
              <div class="form-group">
                <label class="form-label" for="job_role">Job Role Applied For <span class="req">*</span></label>
                <select id="job_role" name="job_role" class="form-control" required>
                  <option value="">Select Sample Role</option>
                  <option value="Customer Support Executive">Customer Support Executive (Voice &amp; Non-Voice)</option>
                  <option value="Technical Support Associate">Technical Support Associate (Tier 1 Helpdesk)</option>
                  <option value="Back Office Executive">Back Office Executive (Data Operations)</option>
                  <option value="Data Entry Associate">Data Entry &amp; Validation Associate</option>
                  <option value="Quality Analyst">Quality Analyst (Auditing)</option>
                  <option value="Team Leader">Customer Service Team Leader</option>
                  <option value="Chat Specialist">E-Commerce Chat Support Specialist</option>
                  <option value="HR Coordinator">HR Recruitment Coordinator</option>
                </select>
                <div class="form-error">Please select a job role.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="experience_level">Total Relevant Experience <span class="req">*</span></label>
                <select id="experience_level" name="experience_level" class="form-control" required>
                  <option value="">Select Experience Level</option>
                  <option value="Fresher (0 Years)">Fresher / Recent Graduate (0 Years)</option>
                  <option value="1-2 Years">1 &ndash; 2 Years</option>
                  <option value="3-5 Years">3 &ndash; 5 Years</option>
                  <option value="5+ Years">5+ Years</option>
                </select>
                <div class="form-error">Please select your experience level.</div>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="skills">Key Skills &amp; Proficiencies</label>
              <input type="text" id="skills" name="skills" class="form-control" placeholder="e.g. Customer Care, Zendesk, Live Chat, Typing 45 WPM, Excel">
            </div>

            <!-- Resume Upload Component -->
            <div class="form-group">
              <label class="form-label">Resume / CV Document (Demo Upload Interface)</label>
              <div id="file-drop-zone" class="file-upload-area">
                <input type="file" id="resume-file-input" class="file-upload-input" accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document">
                <svg class="file-upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                  <polyline points="17 8 12 3 7 8"></polyline>
                  <line x1="12" y1="3" x2="12" y2="15"></line>
                </svg>
                <div style="font-weight: 600; color: var(--color-primary-navy); margin-bottom: 0.25rem;">
                  Choose a file or drag and drop here
                </div>
                <div style="font-size: 0.8125rem; color: var(--color-muted-text);">
                  Accepts PDF, DOC, or DOCX formats (Max 5MB). Simulated client-side validation only.
                </div>
              </div>

              <!-- Selected File Preview -->
              <div id="file-preview-card" class="file-preview">
                <div class="file-preview-info">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-corporate-blue)" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                  </svg>
                  <div>
                    <span id="file-name-text" style="font-weight: 600; color: var(--color-primary-navy);">filename.pdf</span>
                    <span id="file-size-text" style="color: var(--color-muted-text); margin-left: 0.5rem; font-size: 0.75rem;">(1.2 MB)</span>
                  </div>
                </div>
                <button type="button" id="clear-file-btn" class="file-preview-clear">Clear File</button>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="short_intro">Short Candidate Introduction</label>
              <textarea id="short_intro" name="short_intro" class="form-control" placeholder="Briefly describe your customer service background, language skills, or relevant goals..."></textarea>
            </div>

            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Submit Demo Application</button>
          </form>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Apply for Job — Demo Application Form",
        "Frontend-only job application form with file validation for PDF, DOC, and DOCX files. Simulated submission with zero data transmission.",
        "careers",
        body,
        "apply-job.html"
    )

def build_employee_development():
    crumbs = [("Home", "index.html"), ("Careers", "careers.html"), ("Training & Development", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Skill Mastery</span>
        <h1>Training &amp; Professional Development</h1>
        <p class="page-hero-desc">
          Structured learning roadmaps, scenario simulations, quality calibration workshops, and progressive leadership tracks.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Curriculum Reference Model</h4>
            <p>The training tracks, modules, and leadership pathways shown below reflect standard instructional frameworks used in modern international BPO organizations for demonstration purposes.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Learning Architecture</span>
            <h2>Empowering Associates Through Structured Training</h2>
            <p>
              Frontline success requires more than a single orientation session; it requires sustained, multi-phase curriculum training that transforms raw communication talent into confident customer experience professionals.
            </p>
            <p>
              Our learning methodology combines foundational classroom theory, interactive system simulations, side-by-side shadowing, and ongoing weekly coaching sessions.
            </p>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-skills-learning-center.jpg", "Employee Training & Simulation Lab", "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

        <div class="section-header reveal">
          <span class="section-tag">Training Phases</span>
          <h2 class="section-title">The Four Pillars of Employee Learning</h2>
          <p class="section-desc">From new hire induction to continuous professional mastery, our curriculum progresses methodically.</p>
        </div>

        <div class="grid-4" style="margin-bottom: 4rem;">
          <div class="card reveal">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Pillar 1: Induction</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 0.75rem;">Company culture &amp; values</p>
            <p style="font-size: 0.9rem; margin: 0;">Code of conduct, workplace policies, information security hygiene, and clean-desk principles.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Pillar 2: Communication</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 0.75rem;">Voice &amp; written etiquette</p>
            <p style="font-size: 0.9rem; margin: 0;">Active listening, de-escalation, empathy, articulation, and professional written email tone.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Pillar 3: Process Mastery</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 0.75rem;">Client SOPs &amp; systems</p>
            <p style="font-size: 0.9rem; margin: 0;">CRM navigation, helpdesk ticketing, diagnostic decision trees, and simulated role-playing.</p>
          </div>

          <div class="card reveal reveal-delay-3">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Pillar 4: Nesting</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 0.75rem;">Supervised live practice</p>
            <p style="font-size: 0.9rem; margin: 0;">Handling real-time inquiries under side-by-side supervisor coaching and daily debriefs.</p>
          </div>
        </div>

        <!-- Leadership Trajectory -->
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag">Career Acceleration</span>
            <h2>Progression to Operations Leadership</h2>
            <p>
              We believe in developing talent from within. High-performing frontline associates are encouraged to enter our Emerging Leadership Program, which prepares them for supervisory, quality analysis, and management roles:
            </p>
            <ul style="color: var(--color-body-text);">
              <li><strong>Frontline Associate:</strong> Mastering communication and procedural execution.</li>
              <li><strong>Subject Matter Expert (SME):</strong> Assisting peers with complex escalations and edge cases.</li>
              <li><strong>Quality Analyst (QA):</strong> Conducting rubric scoring and calibration audits.</li>
              <li><strong>Operational Team Leader:</strong> Managing floor staffing, coaching, and daily queue metrics.</li>
            </ul>
          </div>
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg); padding: 2.5rem;">
            <h3>Explore Careers in BPO</h3>
            <p style="color: var(--color-muted-text); margin-bottom: 1.5rem;">
              Review our demo career opportunities to understand the roles and responsibilities across our operations.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="job-openings.html" class="btn btn-primary">View Demo Vacancies</a>
              <a href="careers.html" class="btn btn-secondary">Careers Overview</a>
            </div>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Training & Development — BPO Employee Skill Building",
        "Explore our training and development frameworks: induction, communication etiquette, process mastery, and leadership acceleration.",
        "careers",
        body,
        "employee-development.html"
    )

def build_privacy_policy():
    crumbs = [("Home", "index.html"), ("Privacy Policy", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Legal Information</span>
        <h1>Privacy Policy</h1>
        <p class="page-hero-desc">
          Transparency regarding information handling, static website technology, and demonstrative data practices.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Demonstration Website Privacy Statement</h4>
            <p>This static website is a demonstration reference architecture for a generic BPO Company. It does not collect, sell, or transmit personal consumer data to commercial third parties.</p>
          </div>
        </div>

        <div class="prose-content">
          <h2>1. Overview</h2>
          <p>
            This Privacy Policy explains how "BPO COMPANY" ("we", "us", or "our") treats information when visitors browse this static demonstration website. This website is hosted as a static frontend project and does not operate backend database services for persistent tracking.
          </p>

          <h2>2. Information Handled on this Website</h2>
          <p>
            Because this is a static demonstration website, all interactive forms (such as the business enquiry form and the job application form) execute purely within your local browser runtime using Vanilla JavaScript:
          </p>
          <ul>
            <li><strong>No Data Transmission:</strong> Information entered into form fields is validated on the client side and is not transmitted to external servers, recruiters, or marketing databases.</li>
            <li><strong>No File Storage:</strong> Files selected through the demo resume upload interface are read locally by your web browser solely to calculate and display file size and format validation. No files are stored or uploaded.</li>
          </ul>

          <h2>3. Cookies &amp; Local Storage</h2>
          <p>
            This website does not use tracking cookies, analytics pixels, or advertising tracking beacons. Temporary session data or preferences may be stored purely in your browser's local memory to support basic interface interactions.
          </p>

          <h2>4. Third-Party Links &amp; Services</h2>
          <p>
            This website does not include active third-party tracking scripts, external font APIs, external CDNs, or real commercial tracking tools. All CSS, JavaScript, and SVG icons are hosted natively within this static project.
          </p>

          <h2>5. Contacting Us Regarding This Demo</h2>
          <p>
            If you have questions regarding this demonstration frontend website, you may reference our illustrative contact details:
          </p>
          <p>
            <strong>Email:</strong> demo@example.com<br>
            <strong>Address:</strong> Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana &ndash; 000000.
          </p>
        </div>
      </div>
    </section>
    """
    return render_page(
        "Privacy Policy — BPO Company Demonstration Website",
        "Privacy policy for BPO Company static website demonstration. Information handling, local validation, and static hosting transparency.",
        "privacy",
        body,
        "privacy-policy.html"
    )

def build_terms_and_conditions():
    crumbs = [("Home", "index.html"), ("Terms & Conditions", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Legal Information</span>
        <h1>Terms &amp; Conditions</h1>
        <p class="page-hero-desc">
          Conditions of use, intellectual property notes, and demonstrative disclaimer of warranties.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Demonstration Website Terms</h4>
            <p>This website is presented solely as a frontend portfolio demonstration of corporate BPO website architecture. It does not constitute a legally binding commercial service contract.</p>
          </div>
        </div>

        <div class="prose-content">
          <h2>1. Acceptance of Terms</h2>
          <p>
            By accessing and browsing this demonstration website, you acknowledge that you have read, understood, and agreed to be bound by these Terms and Conditions. If you do not agree, you should discontinue viewing the site.
          </p>

          <h2>2. Demonstration Nature of Content</h2>
          <p>
            All content on this website—including service descriptions, operational workflows, case studies, job vacancies, and performance metrics—is published exclusively for illustrative demonstration purposes:
          </p>
          <ul>
            <li>No actual corporate legal entity named "BPO COMPANY" is incorporated through this website.</li>
            <li>Case study scenarios represent fictional operational models, not verified client results.</li>
            <li>Job vacancies represent sample listings, not active commercial job offers.</li>
          </ul>

          <h2>3. Intellectual Property</h2>
          <p>
            The layout, HTML5 markup, CSS3 stylesheets, Vanilla JavaScript code, and abstract geometric SVG branding elements created for this project are intellectual property developed for demonstration purposes.
          </p>

          <h2>4. Disclaimer of Warranties</h2>
          <p>
            This website is provided on an "as is" and "as available" basis without warranties of any kind, whether express or implied. We do not warrant that the website will be uninterrupted, error-free, or free of technical anomalies.
          </p>

          <h2>5. Governing Law</h2>
          <p>
            These terms shall be interpreted in accordance with standard international web publication guidelines and applicable local laws.
          </p>
        </div>
      </div>
    </section>
    """
    return render_page(
        "Terms & Conditions — BPO Company Demonstration Website",
        "Terms and conditions governing the use of the BPO Company demonstration static website. Educational and portfolio usage disclaimers.",
        "terms",
        body,
        "terms-and-conditions.html"
    )

def build_cookie_policy():
    crumbs = [("Home", "index.html"), ("Cookie Policy", None)]
    body = f"""
    {render_breadcrumb(crumbs)}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Legal Information</span>
        <h1>Cookie Policy</h1>
        <p class="page-hero-desc">
          How static cookies and local storage are utilized on this demonstration website.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Static Website Cookie Notice</h4>
            <p>This static website does not deploy persistent third-party advertising cookies or cross-site tracking mechanisms.</p>
          </div>
        </div>

        <div class="prose-content">
          <h2>1. What Are Cookies?</h2>
          <p>
            Cookies are small text files that websites store on your computer or mobile device when you visit a webpage. They are widely used to make websites work efficiently and provide basic navigation memory.
          </p>

          <h2>2. How We Use Cookies</h2>
          <p>
            This static website operates without third-party tracking cookies or advertising networks. Basic functional browser storage may be utilized solely for:
          </p>
          <ul>
            <li><strong>Session Memory:</strong> Retaining navigation drawer states or form reset confirmations during your single browsing session.</li>
            <li><strong>Accessibility Preferences:</strong> Remembering high-contrast or reduced-motion display preferences if selected in your browser.</li>
          </ul>

          <h2>3. Third-Party Tracking</h2>
          <p>
            We do not embed third-party analytics trackers, social media retargeting pixels, or commercial advertising beacons on this static site.
          </p>

          <h2>4. Managing Browser Cookies</h2>
          <p>
            You can modify your browser settings to accept, reject, or delete cookies at any time. Refer to your browser's official help documentation (Chrome, Firefox, Safari, or Edge) to learn how to manage cookie preferences.
          </p>
        </div>
      </div>
    </section>
    """
    return render_page(
        "Cookie Policy — BPO Company Demonstration Website",
        "Cookie policy for BPO Company static website. Explanation of session storage, lack of third-party tracking, and browser controls.",
        "cookie",
        body,
        "cookie-policy.html"
    )

def generate_careers_and_legal():
    pages = [
        ("careers.html", build_careers()),
        ("job-openings.html", build_job_openings()),
        ("job-details.html", build_job_details()),
        ("apply-job.html", build_apply_job()),
        ("employee-development.html", build_employee_development()),
        ("privacy-policy.html", build_privacy_policy()),
        ("terms-and-conditions.html", build_terms_and_conditions()),
        ("cookie-policy.html", build_cookie_policy())
    ]
    for filename, content in pages:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_careers_and_legal()
