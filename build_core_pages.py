"""
Core Pages Generator for BPO Company Website
Generates:
about.html, services.html, industries.html, process.html, technology.html,
quality-assurance.html, data-security.html, infrastructure.html, leadership.html,
team.html, case-studies.html, case-study-details.html, insights.html,
article-details.html, faq.html, contact.html
"""

import os
from builder import render_page, render_placeholder, render_breadcrumb, LOGO_SVG
from generate_pages import render_cta_banner, render_dashboard_mockup

def build_about():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("About Us", None)])}
    
    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">About Our Organization</span>
        <h1>Operational Excellence in Business Process Outsourcing</h1>
        <p class="page-hero-desc">
          We operate structured business process outsourcing and customer experience solutions designed to help organizations streamline routine processes, scale support capacity, and elevate service delivery.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag">Service Philosophy</span>
            <h2>What Business Process Outsourcing Means to Us</h2>
            <p>
              Business Process Outsourcing (BPO) is more than simply transferring repetitive tasks; it is about establishing structured, governed, and accountable workflows that empower organizations to concentrate internal bandwidth on strategic product differentiation.
            </p>
            <p>
              Our operating philosophy centers around transparent communication, standardized documentation (SOPs), rigorous frontline training, and measurable quality assurance. By aligning operational cadences directly with our clients' business goals, we create reliable day-to-day operational support.
            </p>
            
            <div class="demo-callout">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              <div class="demo-callout-text">
                <h4>Demonstration Reference Architecture</h4>
                <p>This website serves as an illustrative demonstration of international BPO organizational models. It does not reflect a specific historical corporate entity or verified client base.</p>
              </div>
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-about-philosophy.jpg", "Service Philosophy & Culture", "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>
      </div>
    </section>

    <section class="section section-light">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Operating Foundations</span>
          <h2 class="section-title">Our Operational Approach</h2>
          <p class="section-desc">How structured governance, frontline empowerment, and process engineering converge to drive consistent operational delivery.</p>
        </div>

        <div class="grid-3">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
            <h3 class="card-title">Customer Experience Focus</h3>
            <p class="card-desc">Every customer interaction is handled with empathy, clear articulation, and rapid issue resolution aligned with brand voice guidelines.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
            <h3 class="card-title">Continuous Process Improvement</h3>
            <p class="card-desc">Iterative error-analysis cycles, weekly QA calibrations, and agent coaching sessions that eliminate workflow bottlenecks over time.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3 class="card-title">Technology-Enabled Operations</h3>
            <p class="card-desc">Modern omnichannel consoles, knowledge base integrations, and automated ticketing triage designed to maintain agent efficiency.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Values Section -->
    <section class="section section-white">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag tag-teal">Guiding Principles</span>
          <h2 class="section-title">Our Core Values</h2>
          <p class="section-desc">The principles that govern our approach to frontline interactions, client relationships, and continuous service refinement.</p>
        </div>

        <div class="grid-3">
          <div class="card reveal">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Accountability</h3>
            <p class="card-desc">Taking clear ownership of process outcomes, transparent reporting of SLA metrics, and proactive identification of operational challenges.</p>
          </div>
          <div class="card reveal reveal-delay-1">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Quality</h3>
            <p class="card-desc">Uncompromising dedication to procedural accuracy, consistent tone of voice, and thorough documentation on every interaction.</p>
          </div>
          <div class="card reveal reveal-delay-2">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Transparency</h3>
            <p class="card-desc">Open operational communication, real-time reporting visibility, and straightforward governance without concealed roadblocks.</p>
          </div>
          <div class="card reveal">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Continuous Improvement</h3>
            <p class="card-desc">Systematic root-cause analysis, regular workflow updates, and ongoing training that steadily elevates baseline performance.</p>
          </div>
          <div class="card reveal reveal-delay-1">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Customer Focus</h3>
            <p class="card-desc">Centering end-user needs in every decision, ensuring customer issues are resolved with care, clarity, and professionalism.</p>
          </div>
          <div class="card reveal reveal-delay-2">
            <h3 class="card-title" style="color: var(--color-corporate-blue);">Collaboration</h3>
            <p class="card-desc">Functioning as an integrated extension of client teams rather than a distant external vendor, cultivating long-term trust.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Operations Center Visual -->
    <section class="section section-light">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            {render_placeholder("bpo-operations-center.jpg", "Operations Center Floor", "ratio-4-3", "1200 &times; 900")}
          </div>
          <div class="reveal reveal-delay-1">
            <span class="section-tag">Modern Environment</span>
            <h2>Engineered for Operational Reliability</h2>
            <p>
              Effective business process execution requires disciplined operational spaces, ergonomic workstations, and high-availability communication infrastructure.
            </p>
            <p>
              Our operational blueprint integrates dedicated team bays, dual-monitor workstations, isolated training rooms, and supervisor monitoring desks to facilitate real-time guidance and swift escalation management.
            </p>
            <div style="margin-top: 1.5rem;">
              <a href="infrastructure.html" class="btn btn-secondary">Explore Infrastructure Details &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "About Us — Corporate BPO Philosophy & Operational Approach",
        "Learn about our operational framework, customer experience philosophy, process governance standards, and core values in business process outsourcing.",
        "about",
        body,
        "about.html"
    )

def build_services():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Services", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Service Catalog</span>
        <h1>Comprehensive BPO &amp; Process Management Solutions</h1>
        <p class="page-hero-desc">
          Structured outsourcing capabilities spanning multichannel customer support, high-volume back office operations, financial data administration, and specialized knowledge workflows.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-services-overview.jpg", "BPO Services Ecosystem", "ratio-21-9", "1920 &times; 820")}
        </div>

        <!-- Regulatory Disclaimer -->
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Operational Scope &amp; Compliance Notice</h4>
            <p>Regulated financial, healthcare, or legal workflows can only be performed within clearly designated, client-authorized operational scopes adhering strictly to verified jurisdictional requirements, controls, and client oversight.</p>
          </div>
        </div>

        <!-- Category A: Customer Experience Services -->
        <div style="margin-bottom: 4rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 1rem; margin-bottom: 2rem;">
            <span class="section-tag">Category A</span>
            <h2>Customer Experience &amp; Contact Center Services</h2>
            <p style="color: var(--color-muted-text); margin: 0;">Frontline voice and non-voice communication solutions supporting end-to-end customer lifecycles.</p>
          </div>

          <div class="grid-3">
            <div class="card reveal">
              <h3 class="card-title">Inbound Call Center</h3>
              <p class="card-desc">Professional telephone support for general inquiries, order status verification, and escalation routing.</p>
              <a href="inbound-call-center.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-1">
              <h3 class="card-title">Outbound Call Center</h3>
              <p class="card-desc">Consent-verified follow-ups, appointment coordination, satisfaction surveys, and client outreach.</p>
              <a href="outbound-call-center.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-2">
              <h3 class="card-title">Customer Support</h3>
              <p class="card-desc">Integrated multichannel care across voice, email, and live messaging with standardized SLA response times.</p>
              <a href="customer-support.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal">
              <h3 class="card-title">Technical Support</h3>
              <p class="card-desc">Tier 1 &amp; Tier 2 troubleshooting, incident diagnosis, step-by-step resolution, and ticket logging.</p>
              <a href="technical-support.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-1">
              <h3 class="card-title">Email Support</h3>
              <p class="card-desc">Structured queue triage, detailed written responses, template-guided resolution, and follow-ups.</p>
              <a href="email-support.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-2">
              <h3 class="card-title">Live Chat Support</h3>
              <p class="card-desc">Real-time web chat assistance, multi-concurrency engagement, and rapid customer issue resolution.</p>
              <a href="chat-support.html" class="card-link">View Service Details &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Category B: Back Office Services -->
        <div style="margin-bottom: 4rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 1rem; margin-bottom: 2rem;">
            <span class="section-tag">Category B</span>
            <h2>Back Office Operations &amp; Data Management</h2>
            <p style="color: var(--color-muted-text); margin: 0;">Precision-driven administrative and transactional processing services.</p>
          </div>

          <div class="grid-3">
            <div class="card reveal">
              <h3 class="card-title">Data Entry &amp; Processing</h3>
              <p class="card-desc">High-speed keying, multi-level validation, spreadsheet cleansing, and core database population.</p>
              <a href="data-entry.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-1">
              <h3 class="card-title">Back Office Operations</h3>
              <p class="card-desc">Comprehensive administrative support, document categorization, and record archival management.</p>
              <a href="back-office.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-2">
              <h3 class="card-title">Document Management</h3>
              <p class="card-desc">Document indexing, OCR verification, digitization workflows, and structured digital filing.</p>
              <a href="document-management.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal">
              <h3 class="card-title">Order Processing</h3>
              <p class="card-desc">Fulfillment status updates, merchant catalog maintenance, return authorizations, and inventory sync.</p>
              <a href="order-processing.html" class="card-link">View Service Details &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Category C: Finance & Business Operations -->
        <div style="margin-bottom: 4rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 1rem; margin-bottom: 2rem;">
            <span class="section-tag">Category C</span>
            <h2>Finance &amp; Business Operations Support</h2>
            <p style="color: var(--color-muted-text); margin: 0;">Supportive accounting workflows executed under strict client-managed authorization boundaries.</p>
          </div>

          <div class="grid-3">
            <div class="card reveal">
              <h3 class="card-title">Finance &amp; Accounting Support</h3>
              <p class="card-desc">Accounts payable coordination, accounts receivable ledger matching, and invoice auditing support.</p>
              <a href="finance-accounting.html" class="card-link">View Service Details &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Category D: Digital & Specialized Services -->
        <div style="margin-bottom: 4rem;">
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 1rem; margin-bottom: 2rem;">
            <span class="section-tag">Category D</span>
            <h2>Digital &amp; Specialized Services</h2>
            <p style="color: var(--color-muted-text); margin: 0;">Niche digital operations covering safety, outbound sales support, and administrative assistance.</p>
          </div>

          <div class="grid-3">
            <div class="card reveal">
              <h3 class="card-title">Content Moderation</h3>
              <p class="card-desc">Policy-guided inspection of user comments, community media, and profiles with moderator wellness safeguards.</p>
              <a href="content-moderation.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-1">
              <h3 class="card-title">Lead Generation Support</h3>
              <p class="card-desc">Contact enrichment, business directory research, prospect verification, and calendar booking assistance.</p>
              <a href="lead-generation.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-2">
              <h3 class="card-title">Virtual Assistance</h3>
              <p class="card-desc">Executive scheduling, email organization, travel logistics research, and digital clerical support.</p>
              <a href="virtual-assistance.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal">
              <h3 class="card-title">Knowledge Process Outsourcing</h3>
              <p class="card-desc">Secondary market research, business intelligence data collection, reporting, and knowledge synthesis.</p>
              <a href="knowledge-process-outsourcing.html" class="card-link">View Service Details &rarr;</a>
            </div>
            <div class="card reveal reveal-delay-1">
              <h3 class="card-title">Healthcare Process Support</h3>
              <p class="card-desc">Non-clinical administrative scheduling, intake document handling, and patient service inquiries.</p>
              <a href="healthcare-process-outsourcing.html" class="card-link">View Service Details &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Category E: Human Resources Services -->
        <div>
          <div style="border-bottom: 2px solid var(--color-border); padding-bottom: 1rem; margin-bottom: 2rem;">
            <span class="section-tag">Category E</span>
            <h2>Human Resources Outsourcing Support</h2>
            <p style="color: var(--color-muted-text); margin: 0;">Administrative support for internal talent lifecycle coordination.</p>
          </div>

          <div class="grid-3">
            <div class="card reveal">
              <h3 class="card-title">HR Outsourcing</h3>
              <p class="card-desc">Candidate screening scheduling, onboarding documentation verification, personnel file updates, and HR queries.</p>
              <a href="human-resources-outsourcing.html" class="card-link">View Service Details &rarr;</a>
            </div>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner("Require a Tailored Outsourcing Solution?",
                       "Schedule a requirements discovery discussion with our operations architects to review your volume, toolsets, and SLAs.",
                       "Request a Consultation", "contact.html",
                       "Discuss Requirements", "contact.html")}
    """
    return render_page(
        "Services Overview — BPO & Multichannel Operations Catalog",
        "Explore our complete spectrum of BPO services: customer support, technical assistance, call center operations, back-office processing, finance administration, and digital moderation.",
        "services",
        body,
        "services.html"
    )

def build_industries():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Industries", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Industry Alignment</span>
        <h1>Specialized Operational Solutions Across Key Industries</h1>
        <p class="page-hero-desc">
          Tailored business process and contact center workflows calibrated to the unique customer journeys, volume dynamics, and operational guidelines of leading vertical markets.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-industries-banner.jpg", "Enterprise Vertical Operations", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Industry Compliance Disclaimer</h4>
            <p>Our solutions are designed around generic operational best practices. We do not claim official regulatory approvals, audits, or industry-specific certifications unless verified through documented client contractual agreements.</p>
          </div>
        </div>

        <div class="grid-2" style="gap: 2.5rem;">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
            <h3 class="card-title">Healthcare &amp; Life Sciences</h3>
            <p class="card-desc">Non-clinical administrative support including patient appointment scheduling, general facility inquiries, registration documentation handling, and records organization.</p>
            <a href="healthcare-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Healthcare &rarr;</a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
            <h3 class="card-title">Banking &amp; Financial Services</h3>
            <p class="card-desc">Back-office document indexing, invoice reconciliation support, account balance query triage, and customer notification assistance under role-based access controls.</p>
            <a href="banking-finance.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Banking &amp; Finance &rarr;</a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg></div>
            <h3 class="card-title">E-Commerce &amp; Retail</h3>
            <p class="card-desc">Managing seasonal volume spikes, order tracking questions, return authorizations, inventory catalog updates, and live chat shopping assistance.</p>
            <a href="ecommerce-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore E-Commerce &rarr;</a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>
            <h3 class="card-title">Technology &amp; Software (SaaS)</h3>
            <p class="card-desc">Tier 1 and Tier 2 technical helpdesk, customer onboarding walkthroughs, product issue categorization, bug verification reporting, and knowledge base curation.</p>
            <a href="technology-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Technology &rarr;</a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg></div>
            <h3 class="card-title">Telecommunications</h3>
            <p class="card-desc">Broadband and wireless service inquiries, billing explanations, plan change coordination, and field technician dispatch logging.</p>
            <a href="telecommunications-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Telecommunications &rarr;</a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg></div>
            <h3 class="card-title">Travel &amp; Hospitality</h3>
            <p class="card-desc">Reservation modifications, booking re-confirmations, loyalty program balance inquiries, and guest feedback response collection.</p>
            <a href="travel-hospitality.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Travel &amp; Hospitality &rarr;</a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h3 class="card-title">Insurance</h3>
            <p class="card-desc">First notice of loss (FNOL) documentation, policy verification, premium payment confirmation, and claims document indexing.</p>
            <a href="insurance-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Insurance &rarr;</a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg></div>
            <h3 class="card-title">Logistics &amp; Transportation</h3>
            <p class="card-desc">Freight tracking inquiries, delivery exception logging, driver check-in communications, and bill of lading data verification.</p>
            <a href="logistics-industry.html" class="btn btn-secondary btn-sm" style="align-self: flex-start;">Explore Logistics &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Industries We Serve — Vertical BPO Operational Support",
        "Explore how our business process outsourcing models support Healthcare, Banking & Finance, E-commerce, Technology, Telecom, Travel, Insurance, and Logistics.",
        "industries",
        body,
        "industries.html"
    )

def build_process():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Our Process", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Methodology</span>
        <h1>A Disciplined 5-Stage Operating Framework</h1>
        <p class="page-hero-desc">
          Structured process discovery, scope standardization, phased resource transition, and rigorous calibration designed to eliminate operational surprises.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-process-lifecycle.jpg", "Operating Process Lifecycle Model", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Governance Blueprint</h4>
            <p>This operating lifecycle illustrates standard enterprise transition methodologies. It represents a structured model rather than an active running client deployment.</p>
          </div>
        </div>

        <!-- Stage 1 -->
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Stage 01</span>
            <h2>Discovery &amp; Requirements Alignment</h2>
            <p>
              In the discovery phase, our solutions architects engage with operational stakeholders to map current volumes, historical seasonality, core contact drivers, and primary pain points.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Historical volume analysis and staffing ratios</li>
              <li>Technology stack and helpdesk platform mapping</li>
              <li>Identification of initial SLA metrics and target CSAT levels</li>
              <li>Baseline quality guidelines and escalation points</li>
            </ul>
          </div>
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg);">
            <h4>Discovery Deliverables</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted-text);">Key documentation generated during Stage 1:</p>
            <ul style="font-size: 0.9rem; margin-bottom: 0;">
              <li>Operational Assessment Report</li>
              <li>Preliminary Staffing Model</li>
              <li>Risk &amp; Dependency Matrix</li>
              <li>Target Timeline &amp; Milestones</li>
            </ul>
          </div>
        </div>

        <!-- Stage 2 -->
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg); order: 2;">
            <h4>Scope Documentation</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted-text);">Agreed boundary assets for Stage 2:</p>
            <ul style="font-size: 0.9rem; margin-bottom: 0;">
              <li>Standard Operating Procedure (SOP) Library</li>
              <li>Escalation Routing Workflows</li>
              <li>Quality Audit Rubrics &amp; Thresholds</li>
              <li>RACI Responsibility Grid</li>
            </ul>
          </div>
          <div class="reveal" style="order: 1;">
            <span class="section-tag">Stage 02</span>
            <h2>Scope Definition &amp; Process Mapping</h2>
            <p>
              Every procedural step must be documented clearly before training begins. We convert tribal knowledge into structured SOP manuals with visual decision trees.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Granular step-by-step workflow documentation</li>
              <li>Clear demarcation of agent authorization boundaries</li>
              <li>Tiered escalation routing protocols</li>
              <li>Knowledge base article development and review</li>
            </ul>
          </div>
        </div>

        <!-- Stage 3 -->
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Stage 03</span>
            <h2>Resource Planning &amp; Training</h2>
            <p>
              Frontline talent is selected based on communication competencies and analytical aptitude. Teams undergo structured curriculum training, role-play scenarios, and mock system practice.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Customized classroom training modules</li>
              <li>System access provisioning and credential management</li>
              <li>Simulated handling of complex edge-case inquiries</li>
              <li>Pre-go-live knowledge assessment and certification</li>
            </ul>
          </div>
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg);">
            <h4>Readiness Verification</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted-text);">Criteria for completing Stage 3:</p>
            <ul style="font-size: 0.9rem; margin-bottom: 0;">
              <li>100% Agent Curriculum Completion</li>
              <li>Tool Connectivity &amp; Access Sign-Off</li>
              <li>Mock Handling Certification Passed</li>
              <li>Supervisory Oversight Assigned</li>
            </ul>
          </div>
        </div>

        <!-- Stage 4 -->
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg); order: 2;">
            <h4>Transition Checkpoints</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted-text);">Key gates during live cutover:</p>
            <ul style="font-size: 0.9rem; margin-bottom: 0;">
              <li>Partial Volume Pilot (20% &ndash; 30%)</li>
              <li>Daily Calibration Audits with Client Team</li>
              <li>Real-time Escalation Support</li>
              <li>Gradual Volume Ramp to 100% Target</li>
            </ul>
          </div>
          <div class="reveal" style="order: 1;">
            <span class="section-tag">Stage 04</span>
            <h2>Transition &amp; Phased Go-Live</h2>
            <p>
              Operations launch through a controlled nesting and pilot phase rather than an abrupt handoff. Supervisors provide hands-on assistance during real-time interactions.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Controlled volume cutover with active hypercare</li>
              <li>Side-by-side coaching and real-time intervention</li>
              <li>Daily operational debriefs to tune procedures</li>
              <li>Progressive ramp-up to full contractual volume</li>
            </ul>
          </div>
        </div>

        <!-- Stage 5 -->
        <div class="grid-2" style="align-items: center;">
          <div class="reveal">
            <span class="section-tag">Stage 05</span>
            <h2>Continuous Improvement &amp; QA Governance</h2>
            <p>
              Once steady-state volume is achieved, our quality assurance and leadership teams focus on continual micro-improvements, root-cause defect elimination, and reporting cadence.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Weekly QA audits and random sample evaluations</li>
              <li>Monthly SLA performance review dashboards</li>
              <li>Quarterly process optimization recommendations</li>
              <li>Ongoing refresher training and knowledge base updates</li>
            </ul>
          </div>
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg);">
            <h4>Ongoing Governance Cadence</h4>
            <p style="font-size: 0.9rem; color: var(--color-muted-text);">Standard cadence for Stage 5:</p>
            <ul style="font-size: 0.9rem; margin-bottom: 0;">
              <li>Daily Team Standups &amp; Queue Reviews</li>
              <li>Weekly QA Calibration Sessions</li>
              <li>Monthly Executive Operations Reviews</li>
              <li>Quarterly Business Review (QBR) Roadmaps</li>
            </ul>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner("Ready to Review Your Process Requirements?",
                       "Schedule an introductory workshop to walk through your operational workflow and receive a structured scope model.",
                       "Request a Consultation", "contact.html",
                       "Explore Our Services", "services.html")}
    """
    return render_page(
        "Our Operating Process — 5-Stage BPO Transition Framework",
        "Explore our structured 5-stage BPO methodology: Discovery, Scope Definition, Resource Planning, Transition, and Continuous Improvement.",
        "process",
        body,
        "process.html"
    )

def build_technology():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Technology", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Digital Enablement</span>
        <h1>Technology &amp; Digital Operations Capabilities</h1>
        <p class="page-hero-desc">
          Enabling responsive omnichannel engagement, automated ticket distribution, secure role-based portals, and actionable operational analytics.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-technology-dashboard.jpg", "Enterprise Operations Technology Architecture", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Architectural Visualizations</h4>
            <p>The system mockups and workflow architectures shown on this page represent conceptual technology paradigms. They do not claim active integrations with specific proprietary software products or third-party vendor platforms.</p>
          </div>
        </div>

        <div class="section-header reveal">
          <span class="section-tag">System Architecture</span>
          <h2 class="section-title">Core Technology Capabilities</h2>
          <p class="section-desc">We operate within enterprise-grade software environments configured to match client security and workflow specifications.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 4rem;">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
            <h3 class="card-title">CRM System Navigation</h3>
            <p class="card-desc">Customer record management, contact history tracking, interaction note logging, and custom field validation.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></div>
            <h3 class="card-title">Contact Center Telephony</h3>
            <p class="card-desc">Automated Call Distribution (ACD), interactive voice response (IVR) mapping, skill-based routing, and call recording archiving.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="9"></line><line x1="9" y1="13" x2="15" y2="13"></line><line x1="9" y1="17" x2="11" y2="17"></line></svg></div>
            <h3 class="card-title">Ticketing &amp; Helpdesk Queues</h3>
            <p class="card-desc">Multi-tier ticket triage, SLA countdown timers, priority sorting, internal escalation notes, and resolution tagging.</p>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></div>
            <h3 class="card-title">Knowledge Management</h3>
            <p class="card-desc">Centralized repository for verified macros, policy updates, troubleshooting decision trees, and agent guidance.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3 class="card-title">Reporting &amp; Analytics</h3>
            <p class="card-desc">Operational dashboards tracking average speed of answer (ASA), first-contact resolution (FCR), and adherence.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg></div>
            <h3 class="card-title">Workflow Automation Support</h3>
            <p class="card-desc">Automated auto-responders, routine data validation scripts, and structured template auto-population.</p>
          </div>
        </div>

        <!-- Illustrative Mockup Section -->
        <div class="reveal" style="margin-bottom: 3.5rem;">
          <h3 style="margin-bottom: 1.5rem; text-align: center;">Illustrative Queue &amp; Analytics Interface</h3>
          {render_dashboard_mockup(
            "Omnichannel Operations Command Center &mdash; Illustrative Overview",
            "ILLUSTRATIVE DEMO DATA &mdash; NOT CONNECTED TO A LIVE SYSTEM",
            [
              ("Active Agents (Demo)", "48"),
              ("Queued Conversations (Demo)", "7"),
              ("First Contact Resolution (Demo)", "91.8%"),
              ("Customer Satisfaction (Demo)", "4.8 / 5.0")
            ],
            ["Channel", "Total Today", "Handled", "Avg Duration", "Current SLA", "Agent Utilization"],
            [
              ["Inbound Voice", "412 calls", "401 calls", "3m 45s", "98.2%", "86%"],
              ["Live Web Chat", "834 chats", "829 chats", "6m 12s", "99.1%", "91%"],
              ["Support Email", "512 tickets", "495 tickets", "14m 20s", "97.5%", "79%"],
              ["Back Office Batches", "128 batches", "126 batches", "22m 10s", "99.4%", "88%"]
            ]
          )}
        </div>
      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Technology & Digital Capabilities — Modern BPO Infrastructure",
        "Explore our technological foundations: CRM integrations, telephony platforms, ticketing distribution systems, knowledge management, and analytics dashboards.",
        "technology",
        body,
        "technology.html"
    )

def build_quality_assurance():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Quality Assurance", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Quality Framework</span>
        <h1>Comprehensive Quality Assurance &amp; Governance</h1>
        <p class="page-hero-desc">
          Structured evaluation rubrics, continuous calibration audits, error taxonomy tracking, and targeted coaching to ensure service consistency.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Quality Analytics Notice</h4>
            <p>The evaluation parameters, sample scorecards, and performance metrics displayed below represent educational models and demo data. They do not constitute actual historical performance records of an operating organization.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Evaluation Dimensions</span>
            <h2>How Quality Is Evaluated Across Operations</h2>
            <p>
              Our quality assurance framework assesses frontline interactions across four primary dimensions, ensuring balanced evaluation between procedural compliance and customer satisfaction.
            </p>
            <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1.5rem;">
              <div style="padding: 1rem; border-left: 3px solid var(--color-corporate-blue); background: var(--color-light-bg); border-radius: var(--radius-sm);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">1. Communication &amp; Empathy</h4>
                <p style="font-size: 0.85rem; color: var(--color-body-text); margin: 0;">Greeting tone, active listening, respectful phrasing, clarity of explanation, and professional closing etiquette.</p>
              </div>
              <div style="padding: 1rem; border-left: 3px solid var(--color-teal-accent); background: var(--color-light-bg); border-radius: var(--radius-sm);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">2. Procedural &amp; SOP Adherence</h4>
                <p style="font-size: 0.85rem; color: var(--color-body-text); margin: 0;">Correct authentication of client identity, following approved troubleshooting workflows, and avoiding unauthorized promises.</p>
              </div>
              <div style="padding: 1rem; border-left: 3px solid var(--color-corporate-blue); background: var(--color-light-bg); border-radius: var(--radius-sm);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">3. Data Accuracy &amp; Note Logging</h4>
                <p style="font-size: 0.85rem; color: var(--color-body-text); margin: 0;">Thorough CRM disposition tagging, accurate summaries of customer issues, and timely ticket closure.</p>
              </div>
              <div style="padding: 1rem; border-left: 3px solid var(--color-teal-accent); background: var(--color-light-bg); border-radius: var(--radius-sm);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">4. Resolution Effectiveness</h4>
                <p style="font-size: 0.85rem; color: var(--color-body-text); margin: 0;">Ensuring the root inquiry was addressed on the first attempt without unnecessary repeat transfers.</p>
              </div>
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-quality-assurance.jpg", "Quality Assurance Review Desk", "ratio-4-3", "1200 &times; 900")}
          </div>
        </div>

        <!-- QA Dashboard Mockup -->
        <div class="reveal" style="margin-bottom: 4rem;">
          <h3 style="margin-bottom: 1.5rem; text-align: center;">Illustrative Quality Review Dashboard</h3>
          {render_dashboard_mockup(
            "Quality Assurance Calibration Console &mdash; Illustrative Overview",
            "DEMO DATA &mdash; NOT ACTUAL COMPANY PERFORMANCE",
            [
              ("Audited Sample (Demo)", "240 tickets"),
              ("Quality Index (Demo)", "96.4%"),
              ("Fatal Error Rate (Demo)", "0.2%"),
              ("Coaching Sessions (Demo)", "32 completed")
            ],
            ["Audit ID", "Agent Code", "Channel", "Evaluation Category", "Score", "Feedback Status"],
            [
              ["#QA-410", "AGT-104", "Voice Inbound", "Tone & Empathy", "98%", "Completed"],
              ["#QA-411", "AGT-219", "Chat Support", "SOP Navigation", "95%", "Reviewed with TL"],
              ["#QA-412", "AGT-087", "Email Queue", "Resolution Accuracy", "100%", "Exemplary"],
              ["#QA-413", "AGT-334", "Technical Desk", "Troubleshooting Tree", "92%", "Coaching Scheduled"],
              ["#QA-414", "AGT-198", "Back Office", "Data Verification", "99%", "Completed"]
            ]
          )}
        </div>

        <!-- QA Lifecycle Steps -->
        <div class="section-header reveal">
          <span class="section-tag">Governance Loop</span>
          <h2 class="section-title">The Quality Improvement Lifecycle</h2>
          <p class="section-desc">How insights collected from routine evaluations translate directly into agent development and process refinement.</p>
        </div>

        <div class="grid-4">
          <div class="card reveal">
            <h4 style="margin-bottom: 0.5rem; color: var(--color-corporate-blue);">1. Sample Auditing</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Independent QA analysts randomly select voice calls and written tickets for rubric scoring.</p>
          </div>
          <div class="card reveal reveal-delay-1">
            <h4 style="margin-bottom: 0.5rem; color: var(--color-corporate-blue);">2. Calibration Sessions</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Bi-weekly reviews between QA team and client leaders to align interpretation of scoring criteria.</p>
          </div>
          <div class="card reveal reveal-delay-2">
            <h4 style="margin-bottom: 0.5rem; color: var(--color-corporate-blue);">3. 1-on-1 Coaching</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Team leaders review recorded sessions with agents to discuss specific procedural opportunities.</p>
          </div>
          <div class="card reveal reveal-delay-3">
            <h4 style="margin-bottom: 0.5rem; color: var(--color-corporate-blue);">4. Knowledge Refinement</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Common customer confusions trigger documentation enhancements in the internal knowledge base.</p>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Quality Assurance — BPO Quality Standards & Governance",
        "Learn about our comprehensive quality assurance framework: interaction scoring rubrics, calibration sessions, root-cause defect taxonomy, and agent coaching.",
        "quality-assurance",
        body,
        "quality-assurance.html"
    )

def build_data_security():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Data Security", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Operational Trust</span>
        <h1>Data Security &amp; Privacy Approach</h1>
        <p class="page-hero-desc">
          Core architectural principles, role-based access governance, data minimization strategies, and confidentiality safeguards for business operations.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <!-- Mandatory Compliance Warning -->
        <div class="demo-callout" style="background: #FEF2F2; border-color: #EF4444; margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4 style="color: #991B1B;">Mandatory Compliance &amp; Certification Notice</h4>
            <p style="color: #B91C1C;">
              This website is a demonstration reference architecture. We do NOT claim ISO 27001, SOC 2, GDPR, HIPAA, or PCI DSS certification. Actual technical security controls, physical security safeguards, and regulatory compliance agreements must be independently established, verified, and contractually executed prior to handling client or personal data.
            </p>
          </div>
        </div>

        <div class="section-header reveal">
          <span class="section-tag">Security Architecture</span>
          <h2 class="section-title">Core Principles of Data Protection</h2>
          <p class="section-desc">Recommended procedural standards that govern how client information should be handled across outsourcing engagements.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 4rem;">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></div>
            <h3 class="card-title">Principle of Least Privilege</h3>
            <p class="card-desc">Frontline associates receive access only to the explicit application screens and records necessary to execute their assigned role.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
            <h3 class="card-title">Data Minimization</h3>
            <p class="card-desc">Workflows should be architected so that customer personal data is masked or tokenized whenever deep details are not strictly required.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h3 class="card-title">Role-Based Access Control (RBAC)</h3>
            <p class="card-desc">System permissions are tied directly to operational tiers (Agent, Lead, QA, Manager) with automated deprovisioning upon role transition.</p>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
            <h3 class="card-title">Confidentiality Agreements</h3>
            <p class="card-desc">Every employee undergoes background screening protocols and signs non-disclosure agreements prior to onboarding.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg></div>
            <h3 class="card-title">Incident Escalation Protocols</h3>
            <p class="card-desc">Documented procedures for rapid reporting of unauthorized access attempts, system anomalies, or accidental disclosures.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18"></path><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></div>
            <h3 class="card-title">Retention &amp; Deletion Governance</h3>
            <p class="card-desc">Establishing defined lifecycle limits ensuring customer interactions and records are not retained longer than contractual terms permit.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            {render_placeholder("bpo-data-security-governance.jpg", "Data Governance & Access Control", "ratio-4-3", "1200 &times; 900")}
          </div>
          <div class="reveal reveal-delay-1">
            <span class="section-tag">Client Collaboration</span>
            <h2>Client-Defined Security Requirements</h2>
            <p>
              Because every enterprise client operates under unique jurisdictional and sector-specific privacy expectations, our security architecture adapts directly to client infrastructure requirements:
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Operation entirely within client-provided Virtual Desktop Infrastructure (VDI)</li>
              <li>Enforcement of clean-desk policies on operational floors</li>
              <li>Restricted USB port access and blocked removable storage devices</li>
              <li>Network segmentation between distinct client accounts</li>
            </ul>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Data Security & Privacy Approach — BPO Governance",
        "Review our principles of data protection, role-based access control, data minimization, and incident escalation protocols for business operations.",
        "data-security",
        body,
        "data-security.html"
    )

def build_infrastructure():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Infrastructure", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Operational Facilities</span>
        <h1>Infrastructure &amp; Operations Environment</h1>
        <p class="page-hero-desc">
          Professional workspace layouts, ergonomic workstations, secure network infrastructure, and collaborative training environments.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Facilities Overview</h4>
            <p>The workspace descriptions and environmental photographs on this page represent conceptual illustrations of BPO delivery centers. We do not claim a specific count of physical facilities, total seats, or verified real estate holdings.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Workplace Engineering</span>
            <h2>Operations Floor &amp; Workstation Layout</h2>
            <p>
              Frontline productivity depends directly on physical ergonomics and acoustic management. Operations floors are structured into modular team bays that minimize ambient noise while enabling supervisors to observe agent performance.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>High-durability commercial workstations with acoustic divider baffles</li>
              <li>Dual-display setups for efficient multi-application navigation</li>
              <li>Commercial enterprise headsets with active noise suppression</li>
              <li>Raised access flooring for structured, secure cabling</li>
            </ul>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-contact-center-floor.jpg", "Operations Floor Layout", "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal" style="order: 2;">
            <span class="section-tag">Talent Development</span>
            <h2>Dedicated Training &amp; Meeting Spaces</h2>
            <p>
              Onboarding and ongoing coaching require dedicated environments isolated from the live floor. Our facility blueprint includes multimedia training rooms and small breakout coaching rooms.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Interactive presentation technology and simulated training pods</li>
              <li>Acoustically treated 1-on-1 coaching spaces for QA debriefs</li>
              <li>Conference spaces for weekly client governance calibrations</li>
            </ul>
          </div>
          <div class="reveal reveal-delay-1" style="order: 1;">
            {render_placeholder("bpo-training-session.jpg", "Training Pods & Coaching Rooms", "ratio-4-3", "1200 &times; 900")}
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag">Team Well-being</span>
            <h2>Collaboration &amp; Rest Facilities</h2>
            <p>
              High-touch customer support requires active cognitive endurance. We incorporate dedicated wellness break areas, cafeteria spaces, and quiet zones that support agent well-being and operational retention.
            </p>
            <ul style="color: var(--color-body-text);">
              <li>Quiet break areas separated from telephony operations</li>
              <li>Locker facilities ensuring adherence to clean-desk protocols</li>
              <li>24/7 security reception and access-controlled entry badges</li>
            </ul>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-modern-workspace.jpg", "Collaborative Workspaces", "ratio-4-3", "1200 &times; 900")}
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Infrastructure & Operations — BPO Workspace Architecture",
        "Explore our facilities model: ergonomic operations floors, dual-monitor workstations, dedicated training pods, and secure collaboration spaces.",
        "infrastructure",
        body,
        "infrastructure.html"
    )

def build_leadership():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Leadership", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Operational Governance</span>
        <h1>Leadership &amp; Management Overview</h1>
        <p class="page-hero-desc">
          Structured operational oversight guiding customer experience strategy, quality calibration, and reliable service execution.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Management Profiles</h4>
            <p>The leadership structure and profiles presented below represent standard executive roles in international BPO operations for demonstration purposes. They do not depict specific real individuals.</p>
          </div>
        </div>

        <div class="grid-3" style="margin-bottom: 4rem;">
          <div class="team-card reveal">
            <div class="team-avatar-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <h3 class="team-name">Vice President of Operations</h3>
            <div class="team-role">Operational Strategy &amp; Delivery</div>
            <p class="team-bio">Responsible for overall service line performance, cross-functional SLA adherence, capacity planning, and strategic client governance cadences.</p>
          </div>

          <div class="team-card reveal reveal-delay-1">
            <div class="team-avatar-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <h3 class="team-name">Head of Quality &amp; Compliance</h3>
            <div class="team-role">QA Governance &amp; Standards</div>
            <p class="team-bio">Oversees interaction evaluation frameworks, agent coaching programs, root-cause defect taxonomy, and client calibration audits.</p>
          </div>

          <div class="team-card reveal reveal-delay-2">
            <div class="team-avatar-placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <h3 class="team-name">Client Solutions Architect</h3>
            <div class="team-role">Transition &amp; Workflow Design</div>
            <p class="team-bio">Directs discovery workshops, standard operating procedure (SOP) documentation, tooling mapping, and phased transition execution.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag">Governance Model</span>
            <h2>Our Operational Governance Cadence</h2>
            <p>
              Reliable delivery requires regular executive touchpoints between our leadership and client operational directors:
            </p>
            <ul style="color: var(--color-body-text);">
              <li><strong>Daily Operations Review:</strong> Queue balance, staffing volume, and immediate escalation debriefs.</li>
              <li><strong>Weekly Calibration Audit:</strong> Reviewing QA score distributions and edge-case exceptions.</li>
              <li><strong>Monthly Service Review:</strong> SLA trend analysis, CSAT scoring, and workforce forecasting.</li>
              <li><strong>Quarterly Business Review (QBR):</strong> Long-term process improvement roadmaps and scope scaling.</li>
            </ul>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-leadership-meeting.jpg", "Executive Governance Session", "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Leadership Overview — BPO Management & Governance",
        "Overview of our operational leadership model: Operations Direction, Quality & Compliance Governance, and Solutions Architecture.",
        "leadership",
        body,
        "leadership.html"
    )

def build_team():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Our Team", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Operational Roster</span>
        <h1>Our Operational Team Structure</h1>
        <p class="page-hero-desc">
          Frontline specialists, experienced team leaders, certified quality analysts, and dedicated trainers working together to deliver consistent excellence.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Illustrative Team Hierarchy</h4>
            <p>This team breakdown presents the standard organizational hierarchy utilized in modern contact center and back-office delivery programs.</p>
          </div>
        </div>

        <div class="grid-4" style="margin-bottom: 4rem;">
          <div class="card reveal">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Frontline Associates</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">Voice, Chat &amp; Email Specialists</p>
            <p style="font-size: 0.9rem; margin: 0;">Directly engage with customers, handle troubleshooting workflows, log detailed CRM dispositions, and execute daily processing.</p>
          </div>

          <div class="card reveal reveal-delay-1">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Operational Team Leaders</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">Floor Supervisors &amp; Coaches</p>
            <p style="font-size: 0.9rem; margin: 0;">Monitor live queues, conduct real-time floor support, assist with customer escalations, and lead 1-on-1 coaching sessions.</p>
          </div>

          <div class="card reveal reveal-delay-2">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Quality Analysts</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">Audit &amp; Calibration Evaluators</p>
            <p style="font-size: 0.9rem; margin: 0;">Perform independent rubric scoring on interactions, identify procedural gaps, and coordinate calibration with client stakeholders.</p>
          </div>

          <div class="card reveal reveal-delay-3">
            <h4 style="color: var(--color-corporate-blue); margin-bottom: 0.5rem;">Training Specialists</h4>
            <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">Curriculum &amp; Knowledge Leads</p>
            <p style="font-size: 0.9rem; margin: 0;">Facilitate new hire classroom modules, maintain SOP documentation, and deliver specialized refresher courses.</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            {render_placeholder("bpo-team-collaboration.jpg", "Team Floor Collaboration", "ratio-16-9", "1200 &times; 675")}
          </div>
          <div class="reveal reveal-delay-1">
            <span class="section-tag">Culture of Accountability</span>
            <h2>Collaborative Operational Delivery</h2>
            <p>
              High performance in customer experience operations is not accidental. It requires a supportive floor culture where frontline agents have direct access to supervisory assistance and structured career trajectories.
            </p>
            <div style="margin-top: 1.5rem;">
              <a href="employee-development.html" class="btn btn-secondary">Explore Training &amp; Development Pathways &rarr;</a>
            </div>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Our Team — BPO Operational Hierarchy & Culture",
        "Explore our team model: Frontline Specialists, Team Leaders, Quality Analysts, and Training Leads working cohesively in business process management.",
        "team",
        body,
        "team.html"
    )

def build_case_studies():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Case Studies", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Operational Models</span>
        <h1>Illustrative Case Scenarios</h1>
        <p class="page-hero-desc">
          Examining typical operational hurdles in customer support, order fulfillment, and back-office processing, and how structured outsourcing workflows provide resolution.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-case-studies-banner.jpg", "Case Studies & Problem Resolution Overview", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>ILLUSTRATIVE DEMO SCENARIO &mdash; NOT A REAL CLIENT CASE STUDY</h4>
            <p>The operational scenarios, challenges, and proposed workflow enhancements described below are fictional models developed to illustrate problem-solving approaches. No actual client project or verified commercial outcome is represented.</p>
          </div>
        </div>

        <div class="grid-3">
          <!-- Case 1 -->
          <div class="article-card reveal">
            <div style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO SCENARIO &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>Customer Experience</span> &bull; <span>SaaS Software</span>
              </div>
              <h3 class="article-title"><a href="case-study-details.html">Customer Support Workflow Improvement</a></h3>
              <p class="article-excerpt">
                <strong>Context:</strong> A growing software platform experienced rising ticket backlog and inconsistent first-contact resolution during product updates.
              </p>
              <p class="article-excerpt">
                <strong>Remediation:</strong> Designed a two-tier queue segregation model, refreshed the internal troubleshooting decision tree, and implemented weekly calibration sessions.
              </p>
              <a href="case-study-details.html" class="btn btn-secondary btn-sm" style="margin-top: auto;">Read Full Scenario &rarr;</a>
            </div>
          </div>

          <!-- Case 2 -->
          <div class="article-card reveal reveal-delay-1">
            <div style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO SCENARIO &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>E-Commerce</span> &bull; <span>Peak Season Surge</span>
              </div>
              <h3 class="article-title"><a href="case-study-details.html">E-Commerce Order Enquiry Management</a></h3>
              <p class="article-excerpt">
                <strong>Context:</strong> Online retailer facing a 4x seasonal surge in "Where Is My Order" (WISMO) requests overwhelming internal staff.
              </p>
              <p class="article-excerpt">
                <strong>Remediation:</strong> Deployed a flexible blended voice/chat support team equipped with direct carrier tracking APIs and macro response templates.
              </p>
              <a href="case-study-details.html" class="btn btn-secondary btn-sm" style="margin-top: auto;">Read Full Scenario &rarr;</a>
            </div>
          </div>

          <!-- Case 3 -->
          <div class="article-card reveal reveal-delay-2">
            <div style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO SCENARIO &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>Back Office Operations</span> &bull; <span>Data Verification</span>
              </div>
              <h3 class="article-title"><a href="case-study-details.html">Back Office Data Processing Workflow</a></h3>
              <p class="article-excerpt">
                <strong>Context:</strong> High error rates and slow processing times in commercial document indexing and invoice ledger matching.
              </p>
              <p class="article-excerpt">
                <strong>Remediation:</strong> Established a dual-analyst verification checkpoint and automated format sanitization rules prior to database entry.
              </p>
              <a href="case-study-details.html" class="btn btn-secondary btn-sm" style="margin-top: auto;">Read Full Scenario &rarr;</a>
            </div>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Case Studies — Illustrative BPO Operational Scenarios",
        "Explore illustrative case study scenarios: Customer support queue optimization, seasonal e-commerce order management, and back-office data processing workflows.",
        "case-studies",
        body,
        "case-studies.html"
    )

def build_case_study_details():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Case Studies", "case-studies.html"), ("Customer Support Optimization", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Illustrative Demo Scenario</span>
        <h1>Customer Support Workflow Improvement</h1>
        <p class="page-hero-desc">
          An in-depth examination of operational triage redesign, tiered escalation workflows, and knowledge base calibration in a high-volume software customer support environment.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-case-study-support.jpg", "Customer Support Workflow Optimization", "ratio-21-9", "1920 &times; 820")}
        </div>

        <!-- Prominent Mandatory Disclaimer -->
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>ILLUSTRATIVE DEMO SCENARIO &mdash; NOT A REAL CLIENT CASE STUDY</h4>
            <p>This document is an educational case model illustrating process redesign methodologies. All operational metrics, business names, challenges, and proposed workflows are fictional.</p>
          </div>
        </div>

        <div class="grid-2-1">
          <div class="prose-content">
            <h2>Business Context &amp; Challenge</h2>
            <p>
              In this illustrative scenario, a growing software enterprise experienced rapid user growth following a product rollout. Internal customer support teams were overwhelmed with inbound inquiries, resulting in ticket queues exceeding 48 hours and high internal staff fatigue.
            </p>
            <p>
              Core challenges identified during preliminary process mapping included:
            </p>
            <ul>
              <li><strong>Unfiltered Inbound Routing:</strong> Complex technical bugs and simple password resets arrived in the same unsegregated inbox queue.</li>
              <li><strong>Fragmented Knowledge Assets:</strong> Support associates relied on unverified internal chat notes rather than indexed, authorized SOP documents.</li>
              <li><strong>Inconsistent First-Contact Resolution:</strong> Customers frequently required 3 or more touchpoints to resolve straightforward account configuration questions.</li>
            </ul>

            <h2>Proposed Operational Workflow</h2>
            <p>
              To remediate these challenges, an outsourcing operational architecture was proposed based on strict ticket categorization and tiered response teams:
            </p>

            <div style="background: var(--color-light-bg); border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem; margin: 2rem 0;">
              <h4 style="margin-bottom: 0.75rem;">Illustrative Process Architecture Diagram</h4>
              <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">End-to-End Inquiry Triage Model:</p>
              <div style="font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.8; color: var(--color-primary-navy);">
                [Customer Inquiry] &rarr; [Automated Keyword Triage &amp; Tagging]<br>
                &nbsp;&nbsp;&boxur;&rarr; [Tier 1 Queue: Account, Billing &amp; Basic Navigation] &rarr; (Immediate Resolution)<br>
                &nbsp;&nbsp;&boxur;&rarr; [Tier 2 Queue: Technical Diagnostics &amp; Bug Verification] &rarr; (Specialist Resolution)<br>
                &nbsp;&nbsp;&boxur;&rarr; [Escalation: Engineering Issue with Structured Logs] &rarr; (Core Product Team)
              </div>
            </div>

            <h2>Operational Execution &amp; Approach</h2>
            <p>
              The transition was structured into three operational phases:
            </p>
            <ol>
              <li><strong>Curated Knowledge Base Creation:</strong> Transforming disparate troubleshooting steps into 45 standardized macro articles with step-by-step screenshots.</li>
              <li><strong>Tier 1 Team Training:</strong> Equipping dedicated frontline associates with scenario-based role-play certifications before handling live queues.</li>
              <li><strong>Daily Calibration Audits:</strong> Team leaders and client product managers held 15-minute daily syncs to review edge cases and refine tagging rules.</li>
            </ol>

            <h2>Key Lessons Learned</h2>
            <p>
              This operational model highlighted several key principles applicable across business process outsourcing implementations:
            </p>
            <ul>
              <li>Segregating transactional inquiries from deep technical problems preserves specialist engineering time.</li>
              <li>Centralized and maintained SOP documentation significantly accelerates frontline onboarding speed.</li>
              <li>Transparent daily operational debriefs eliminate misunderstandings between client leadership and the extended support team.</li>
            </ul>
          </div>

          <aside>
            <div class="sidebar-box">
              <h3 class="sidebar-title">Scenario Summary</h3>
              <div style="font-size: 0.9rem; display: flex; flex-direction: column; gap: 0.75rem;">
                <div><strong>Industry:</strong> Technology / SaaS</div>
                <div><strong>Channels:</strong> Email &amp; Web Chat</div>
                <div><strong>Workflow:</strong> Tiered Support Triage</div>
                <div><strong>Status:</strong> Illustrative Demo Scenario</div>
              </div>
            </div>

            <div class="sidebar-box">
              <h3 class="sidebar-title">Related Scenarios</h3>
              <ul class="sidebar-links">
                <li><a href="case-studies.html">E-Commerce Order Management</a></li>
                <li><a href="case-studies.html">Back Office Data Processing</a></li>
                <li><a href="case-studies.html">View All Scenarios &rarr;</a></li>
              </ul>
            </div>

            <div class="sidebar-box" style="background: var(--color-light-bg);">
              <h3 class="sidebar-title">Discuss Your Workflow</h3>
              <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">
                Connect with our solutions architects to design an operational workflow tailored to your volume.
              </p>
              <a href="contact.html" class="btn btn-primary btn-sm" style="width: 100%;">Request a Consultation</a>
            </div>
          </aside>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Case Study Details — Customer Support Workflow Improvement",
        "Detailed illustrative scenario examining queue segregation, knowledge base calibration, and tiered support operations.",
        "case-studies",
        body,
        "case-study-details.html"
    )

def build_insights():
    articles = [
        ("Understanding Business Process Outsourcing: Modern Operational Strategies", "article-details.html", "Core BPO", "A comprehensive guide to how modern organizations leverage BPO for efficiency, agility, and frontline service excellence."),
        ("Voice vs Non-Voice BPO: Aligning Channels With Customer Expectations", "article-details.html", "Channel Strategy", "Comparing telephony and written support paradigms, agent skillset requirements, and customer satisfaction factors."),
        ("How Customer Support Operations Work: Behind the Scenes", "article-details.html", "Operations", "An inside look at workforce scheduling, real-time queue management, and quality audit workflows in contact centers."),
        ("Back Office Outsourcing Explained: Data, Invoicing, and Archiving", "article-details.html", "Back Office", "Examining how high-volume administrative tasks can be standardized, verified, and delivered with precision."),
        ("Benefits and Strategic Considerations in Business Outsourcing", "article-details.html", "Strategy", "A balanced overview of operational scalability, cost predictability, and organizational readiness considerations."),
        ("Introduction to Modern Contact Center Platforms & Telephony", "article-details.html", "Technology", "Understanding Automatic Call Distribution (ACD), Interactive Voice Response (IVR), and omnichannel ticketing architectures."),
        ("BPO Career Opportunities: Growth Pathways and Skill Building", "article-details.html", "Careers", "How entry-level customer support roles evolve into team leadership, quality analysis, and workforce management."),
        ("Quality Assurance in Customer Support: Beyond Checklist Scoring", "article-details.html", "Quality & QA", "Implementing meaningful feedback loops, empathy evaluations, and root-cause calibration sessions.")
    ]

    cards_html = ""
    for title, url, tag, excerpt in articles:
        cards_html += f"""<div class="article-card reveal">
  <div style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 700; color: #64748B; text-align: center;">
    DEMO EDITORIAL CONTENT
  </div>
  <div class="article-body">
    <div class="article-meta">
      <span class="badge badge-blue">{tag}</span> &bull; <span>5 Min Read</span>
    </div>
    <h3 class="article-title"><a href="{url}">{title}</a></h3>
    <p class="article-excerpt">{excerpt}</p>
    <a href="{url}" class="card-link">Read Full Article &rarr;</a>
  </div>
</div>"""

    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Insights", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Resources &amp; Articles</span>
        <h1>Insights &amp; Operational Perspectives</h1>
        <p class="page-hero-desc">
          Educational articles, industry overviews, and procedural perspectives on business process outsourcing, customer experience, and operational design.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-insights-banner.jpg", "Knowledge & Editorial Resources", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Demo Editorial Content Notice</h4>
            <p>The articles listed on this page represent sample educational content crafted to illustrate website publishing capabilities. They do not claim verified publication dates, academic research, or fabricated external citations.</p>
          </div>
        </div>

        <div class="grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Insights & Resources — BPO Industry Articles & Guides",
        "Browse our educational articles on BPO operations, voice vs non-voice channels, contact center technology, quality assurance, and careers.",
        "insights",
        body,
        "insights.html"
    )

def build_article_details():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Insights", "insights.html"), ("Understanding BPO", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Demo Editorial Article</span>
        <h1>Understanding Business Process Outsourcing: Modern Operational Strategies</h1>
        <p class="page-hero-desc">
          How organizations leverage structured business process partnerships to achieve operational flexibility, service consistency, and customer experience excellence.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div style="margin-bottom: 3rem;">
          {render_placeholder("bpo-article-future-outsourcing.jpg", "Understanding Modern BPO Article", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>DEMO EDITORIAL CONTENT &mdash; EDUCATIONAL OVERVIEW</h4>
            <p>This article represents general informational content on BPO business models. It does not fabricate industry statistics or claim academic research citations.</p>
          </div>
        </div>

        <div class="grid-2-1">
          <article class="prose-content">
            <h2>The Evolution of Business Process Outsourcing</h2>
            <p>
              Business Process Outsourcing (BPO) has transformed from a purely cost-arbitrage model focused on repetitive data processing into a strategic operational partnership centered on customer experience, specialized capabilities, and rapid scalability.
            </p>
            <p>
              Historically, companies outsourced non-core back-office functions primarily to reduce overhead costs. Today, leading enterprises view BPO as an avenue to access trained talent pools, modern contact center technologies, and rigorous quality frameworks that would require substantial capital investment to establish internally.
            </p>

            <h2>Core Categories of Modern BPO</h2>
            <p>
              Modern outsourcing arrangements generally fall into two broad functional categories:
            </p>
            <h3>1. Front-Office Services (Customer Experience)</h3>
            <p>
              Front-office operations encompass customer-facing touchpoints where brand voice, responsiveness, and empathy are paramount. These include:
            </p>
            <ul>
              <li><strong>Inbound Customer Care:</strong> Handling account queries, billing support, and troubleshooting over phone and messaging.</li>
              <li><strong>Technical Helpdesk:</strong> Multi-tiered incident diagnosis for software, hardware, and connected consumer products.</li>
              <li><strong>Multichannel Digital Engagement:</strong> Real-time live web chat, social customer support, and email ticket resolution.</li>
            </ul>

            <h3>2. Back-Office Services (Internal Operations)</h3>
            <p>
              Back-office operations involve non-customer-facing administrative tasks that require accuracy, standardization, and adherence to business rules:
            </p>
            <ul>
              <li><strong>Data Entry &amp; Classification:</strong> Extracting, validating, and updating complex records into enterprise databases.</li>
              <li><strong>Finance &amp; Accounting Support:</strong> Invoice matching, accounts payable documentation, and ledger reconciliation within client-defined access scopes.</li>
              <li><strong>Document Archival &amp; Management:</strong> Scanning, indexing, and digital filing of contractual and transactional records.</li>
            </ul>

            <h2>Key Strategic Considerations Before Outsourcing</h2>
            <p>
              While outsourcing offers notable benefits, successful execution depends heavily on thorough preparation:
            </p>
            <ul>
              <li><strong>Process Documentation:</strong> Clearly defining Standard Operating Procedures (SOPs) before onboarding an external team.</li>
              <li><strong>Technology &amp; Security Alignment:</strong> Establishing role-based access controls and determining whether operations occur on client VDI or managed systems.</li>
              <li><strong>Balanced Metric Architecture:</strong> Evaluating success through a balance of speed (Handle Time, ASA) and quality (First-Contact Resolution, CSAT).</li>
            </ul>

            <h2>Summary</h2>
            <p>
              When designed with clear communication channels, rigorous training, and collaborative quality calibrations, business process outsourcing serves as a reliable operational engine that supports sustained organizational growth.
            </p>
          </article>

          <aside>
            <div class="sidebar-box">
              <h3 class="sidebar-title">Article Information</h3>
              <div style="font-size: 0.9rem; display: flex; flex-direction: column; gap: 0.75rem;">
                <div><strong>Category:</strong> BPO Strategy</div>
                <div><strong>Read Time:</strong> ~5 Minutes</div>
                <div><strong>Type:</strong> Educational Demo Guide</div>
              </div>
            </div>

            <div class="sidebar-box">
              <h3 class="sidebar-title">More Articles</h3>
              <ul class="sidebar-links">
                <li><a href="insights.html">Voice vs Non-Voice BPO</a></li>
                <li><a href="insights.html">How Support Operations Work</a></li>
                <li><a href="insights.html">Quality Assurance in BPO</a></li>
                <li><a href="insights.html">Back Office Explained</a></li>
              </ul>
            </div>

            <div class="sidebar-box" style="background: var(--color-light-bg);">
              <h3 class="sidebar-title">Ready to Discuss Your Operations?</h3>
              <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">
                Schedule a discovery consultation with our business process architects.
              </p>
              <a href="contact.html" class="btn btn-primary btn-sm" style="width: 100%;">Request a Consultation</a>
            </div>
          </aside>
        </div>

      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "Understanding BPO — Insights & Operational Perspectives",
        "An educational guide to modern business process outsourcing strategies, front-office vs back-office models, and operational considerations.",
        "insights",
        body,
        "article-details.html"
    )

def build_faq():
    faqs = [
        ("What is Business Process Outsourcing (BPO)?",
         "Business Process Outsourcing involves contracting non-core operational responsibilities—such as customer contact handling, technical troubleshooting, data entry, order fulfillment, or financial administration—to specialized service teams who execute these workflows according to defined Service Level Agreements (SLAs)."),
        ("What services can be outsourced?",
         "Services commonly outsourced include customer care, inbound and outbound telephone support, email and live chat handling, Tier 1 and Tier 2 technical helpdesk, data entry and sanitization, invoice processing support, content moderation, virtual assistance, and HR administrative coordination."),
        ("What is the difference between voice and non-voice BPO?",
         "Voice BPO refers to real-time spoken telephone conversations (inbound inquiries, support helplines, follow-up calls). Non-voice BPO involves written and digital interaction channels, including email support, live chat queues, social media moderation, and administrative back-office data processing."),
        ("What is inbound customer support?",
         "Inbound customer support entails receiving incoming customer contacts—such as phone calls, chat messages, or tickets—where the customer initiates contact to ask product questions, report an issue, request billing clarification, or seek technical assistance."),
        ("What is outbound customer support?",
         "Outbound customer support involves authorized, outbound contacts initiated to follow up on unresolved customer tickets, confirm appointments, conduct post-service satisfaction surveys, or verify account details. Outbound activities must adhere strictly to applicable telemarketing and consent laws."),
        ("What is back-office outsourcing?",
         "Back-office outsourcing covers transactional administrative tasks that do not involve direct customer contact. Examples include data indexing, digital document organization, invoice validation, merchant catalog updates, and order fulfillment status logging."),
        ("What is Knowledge Process Outsourcing (KPO)?",
         "Knowledge Process Outsourcing involves specialized, information-intensive tasks requiring analytical thinking and subject-matter judgment. This includes market intelligence research, data synthesis, competitive landscape reviews, and business reporting assistance."),
        ("How does the outsourcing transition process work?",
         "The transition typically follows a five-stage lifecycle: Discovery (understanding requirements), Scope Definition (mapping SOPs and metrics), Planning (staffing and training), Transition (phased pilot and cutover), and Continuous Improvement (quality monitoring and calibration)."),
        ("Can businesses outsource specific workflows rather than entire departments?",
         "Yes. Many organizations adopt modular or hybrid outsourcing models, delegating specific sub-processes—such as after-hours weekend coverage, peak-season chat triage, or back-office invoice indexing—while retaining core strategic operations in-house."),
        ("How is quality monitored and evaluated?",
         "Quality is monitored through standardized evaluation rubrics, random sample ticket and call audits, first-contact resolution tracking, customer satisfaction surveys, and regular calibration meetings between client stakeholders and QA leadership."),
        ("How are client data security requirements handled?",
         "Data security is handled through role-based access permissions, least-privilege principles, clean-desk policies, network segmentation, and non-disclosure agreements. Operational controls are customized to align with client-specified technical boundaries and infrastructure."),
        ("How can a business request an operational proposal?",
         "Organizations can submit a preliminary consultation request via our Contact page, detailing expected contact volumes, channel requirements, and timeline expectations. Our solutions team then coordinates an introductory discovery workshop."),
        ("Are there career opportunities in BPO?",
         "Yes. Business process outsourcing offers varied career opportunities spanning frontline customer experience roles, technical support, back-office analytics, team leadership, training, and operational quality management."),
        ("How can candidates apply for job vacancies?",
         "Candidates can explore sample career categories on our Careers page, browse demo openings on the Job Openings page, and submit a demo application through our frontend-only application form.")
    ]

    faq_items_html = ""
    for q, a in faqs:
        faq_items_html += f"""<div class="accordion-item">
  <button class="accordion-btn" aria-expanded="false">
    <span>{q}</span>
    <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
  </button>
  <div class="accordion-content">
    <p>{a}</p>
  </div>
</div>"""

    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("FAQ", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Knowledge Base</span>
        <h1>Frequently Asked Questions</h1>
        <p class="page-hero-desc">
          Key questions regarding business process outsourcing workflows, channel models, quality governance, data handling, and career opportunities.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <div style="margin-bottom: 2.5rem;">
          {render_placeholder("bpo-faq-support.jpg", "Customer Knowledge Base & Help Hub", "ratio-21-9", "1920 &times; 820")}
        </div>

        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>General Informational Reference</h4>
            <p>The answers provided below reflect standard practices within international BPO and business process management industries for demonstrative reference.</p>
          </div>
        </div>

        <div class="accordion reveal">
          {faq_items_html}
        </div>

        <div style="background: var(--color-light-bg); border-radius: var(--radius-lg); padding: 2.5rem; text-align: center; margin-top: 4rem;">
          <h3>Have Additional Questions About Our Services?</h3>
          <p style="color: var(--color-muted-text); margin-bottom: 1.5rem;">Our solutions advisory team is available to discuss specific operational workflows and custom requirements.</p>
          <a href="contact.html" class="btn btn-primary">Contact Our Solutions Team</a>
        </div>
      </div>
    </section>

    {render_cta_banner()}
    """
    return render_page(
        "FAQ — Frequently Asked Questions on BPO Operations",
        "Find answers to common questions about business process outsourcing: voice vs non-voice BPO, quality monitoring, transition lifecycles, and career opportunities.",
        "faq",
        body,
        "faq.html"
    )

def build_contact():
    body = f"""
    {render_breadcrumb([("Home", "index.html"), ("Contact Us", None)])}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">Get in Touch</span>
        <h1>Let's Discuss Your Business Process Requirements</h1>
        <p class="page-hero-desc">
          Connect with our operations architects to review your volume projections, service channels, and quality SLA expectations.
        </p>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <!-- Mandatory Form Disclaimer -->
        <div class="demo-callout" style="margin-bottom: 3.5rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Demonstration Enquiry Form Notice</h4>
            <p>This is a frontend demonstration website. Submitting this form validates input fields entirely in your browser. No personal or business data is transmitted to an external server, database, or email inbox.</p>
          </div>
        </div>

        <div class="grid-2" style="gap: 4rem; align-items: start;">
          <!-- Form Column -->
          <div class="form-card reveal">
            <h3 style="margin-bottom: 0.5rem;">Request an Operational Consultation</h3>
            <p style="font-size: 0.9rem; color: var(--color-muted-text); margin-bottom: 2rem;">Please fill in the details below to receive an illustrative service proposal outline.</p>

            <div id="contact-form-alert" class="alert" style="display: none;"></div>

            <form id="bpo-contact-form" novalidate>
              <div class="form-group">
                <label class="form-label" for="full_name">Full Name <span class="req">*</span></label>
                <input type="text" id="full_name" name="full_name" class="form-control" placeholder="Jane Doe" required>
                <div class="form-error">Please enter your full name (minimum 2 characters).</div>
              </div>

              <div class="grid-2" style="gap: 1rem;">
                <div class="form-group">
                  <label class="form-label" for="email">Business Email <span class="req">*</span></label>
                  <input type="email" id="email" name="email" class="form-control" placeholder="jane@company.com" required>
                  <div class="form-error">Please enter a valid business email address.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="phone">Phone Number <span class="req">*</span></label>
                  <input type="tel" id="phone" name="phone" class="form-control" placeholder="0000000000" required>
                  <div class="form-error">Please enter a valid phone number.</div>
                </div>
              </div>

              <div class="grid-2" style="gap: 1rem;">
                <div class="form-group">
                  <label class="form-label" for="company">Company Name <span class="req">*</span></label>
                  <input type="text" id="company" name="company" class="form-control" placeholder="Enterprise Corp" required>
                  <div class="form-error">Please enter your company name.</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="industry">Industry Sector</label>
                  <select id="industry" name="industry" class="form-control">
                    <option value="">Select Industry</option>
                    <option value="Healthcare">Healthcare &amp; Life Sciences</option>
                    <option value="Banking">Banking &amp; Financial Services</option>
                    <option value="E-Commerce">E-Commerce &amp; Retail</option>
                    <option value="Technology">Technology &amp; SaaS</option>
                    <option value="Telecommunications">Telecommunications</option>
                    <option value="Travel">Travel &amp; Hospitality</option>
                    <option value="Insurance">Insurance</option>
                    <option value="Logistics">Logistics &amp; Transport</option>
                    <option value="Other">Other Industry</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="service">Primary Service Required <span class="req">*</span></label>
                <select id="service" name="service" class="form-control" required>
                  <option value="">Select Primary Service</option>
                  <option value="Customer Support">Customer Support (Multichannel)</option>
                  <option value="Inbound Call Center">Inbound Call Center</option>
                  <option value="Outbound Call Center">Outbound Call Center (Consented)</option>
                  <option value="Technical Support">Technical Support (Tier 1 &amp; Tier 2)</option>
                  <option value="Email Support">Email Ticket Support</option>
                  <option value="Chat Support">Live Chat Support</option>
                  <option value="Back Office">Back Office Processing</option>
                  <option value="Data Entry">Data Entry &amp; Classification</option>
                  <option value="Finance Accounting">Finance &amp; Accounting Support</option>
                  <option value="Content Moderation">Content Moderation</option>
                  <option value="Lead Generation">Lead Generation Support</option>
                  <option value="HR Outsourcing">HR Outsourcing</option>
                  <option value="Knowledge Process">Knowledge Process Outsourcing (KPO)</option>
                </select>
                <div class="form-error">Please select a primary service.</div>
              </div>

              <div class="form-group">
                <label class="form-label" for="expected_volume">Expected Support Volume / Requirements</label>
                <input type="text" id="expected_volume" name="expected_volume" class="form-control" placeholder="e.g. 5,000 inquiries/month, 24/7 coverage, or 10 agents">
              </div>

              <div class="form-group">
                <label class="form-label" for="message">Project Description / Requirements <span class="req">*</span></label>
                <textarea id="message" name="message" class="form-control" placeholder="Describe your current operational process, target timeline, and specific goals..." required></textarea>
                <div class="form-error">Please provide a brief message (minimum 10 characters).</div>
              </div>

              <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Submit Demo Consultation Request</button>
            </form>
          </div>

          <!-- Contact Details Column -->
          <div class="reveal reveal-delay-1">
            <div style="margin-bottom: 2rem;">
              {render_placeholder("bpo-business-consultation.jpg", "Operational Discovery Consultation", "ratio-4-3", "1200 &times; 900")}
            </div>

            <div style="background: var(--color-light-bg); border-radius: var(--radius-xl); padding: 2.5rem; border: 1px solid var(--color-border); margin-bottom: 2rem;">
              <h3 style="margin-bottom: 1.5rem;">Corporate Information</h3>

              <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                  <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  </div>
                  <div>
                    <h4 style="font-size: 0.95rem; margin-bottom: 0.2rem;">Telephone Enquiries</h4>
                    <p style="font-size: 0.9rem; color: var(--color-muted-text); margin: 0;">0000000000</p>
                    <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">Alternative: 0000000000</p>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                  <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                  </div>
                  <div>
                    <h4 style="font-size: 0.95rem; margin-bottom: 0.2rem;">Corporate Email</h4>
                    <p style="font-size: 0.9rem; color: var(--color-muted-text); margin: 0;">demo@example.com</p>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                  <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  </div>
                  <div>
                    <h4 style="font-size: 0.95rem; margin-bottom: 0.2rem;">Demo Office Address</h4>
                    <p style="font-size: 0.9rem; color: var(--color-muted-text); margin: 0;">
                      Plot No. 000, Demo Road, Sample Area,<br>Hyderabad, Telangana &ndash; 000000.
                    </p>
                  </div>
                </div>

                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                  <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  </div>
                  <div>
                    <h4 style="font-size: 0.95rem; margin-bottom: 0.2rem;">Business Hours</h4>
                    <p style="font-size: 0.9rem; color: var(--color-muted-text); margin: 0;">Monday &ndash; Saturday, 9:00 AM &ndash; 6:00 PM</p>
                    <p style="font-size: 0.85rem; color: #94A3B8; margin: 0;">(Illustrative demo hours)</p>
                  </div>
                </div>
              </div>
            </div>

            <div style="background: var(--color-white); border-radius: var(--radius-xl); padding: 2rem; border: 1px solid var(--color-border);">
              <h4>Other Inquiries</h4>
              <p style="font-size: 0.9rem; color: var(--color-muted-text); margin-bottom: 1rem;">
                Looking for career opportunities or common operational answers?
              </p>
              <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                <a href="careers.html" class="btn btn-secondary btn-sm">Explore Careers &rarr;</a>
                <a href="faq.html" class="btn btn-secondary btn-sm">View FAQs &rarr;</a>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner("Looking for Recruitment &amp; Career Inquiries?",
                       "Visit our dedicated careers section to review demo vacancies, training programs, and talent pathways.",
                       "View Job Openings", "job-openings.html",
                       "Careers Overview", "careers.html")}
    """
    return render_page(
        "Contact Us — Business Consultation & Enquiry",
        "Request an operational consultation for BPO and customer experience services. Fictional demo contact details and interactive form validation.",
        "contact",
        body,
        "contact.html"
    )

print("Core pages generator ready.")
