"""
Complete 50-Page Generator for BPO Company Website
"""

import os
from builder import render_page, render_placeholder, render_breadcrumb, LOGO_SVG

# Helper for standard CTA section
def render_cta_banner(title="Let's Discuss Your Business Process Requirements",
                      subtitle="Connect with our solutions team to explore how structured outsourcing workflows can support your operational goals.",
                      primary_text="Request a Consultation", primary_url="contact.html",
                      secondary_text="Explore Our Services", secondary_url="services.html"):
    return f"""<section class="section section-dark" style="background: linear-gradient(135deg, #0B1426 0%, #172B49 100%);">
  <div class="container text-center">
    <div class="section-header" style="margin-bottom: 2rem;">
      <span class="section-tag tag-teal">Operational Collaboration</span>
      <h2 style="color: #fff;">{title}</h2>
      <p style="color: #94A3B8;">{subtitle}</p>
    </div>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="{primary_url}" class="btn btn-primary btn-lg">{primary_text}</a>
      <a href="{secondary_url}" class="btn btn-outline-white btn-lg">{secondary_text}</a>
    </div>
  </div>
</section>"""

# Helper for UI Dashboard Mockup
def render_dashboard_mockup(title, badge_text, stats, table_headers, table_rows):
    stats_html = "".join([f"""<div class="stat-card">
  <div class="stat-label">{s[0]}</div>
  <div class="stat-value">{s[1]}</div>
</div>""" for s in stats])

    headers_html = "".join([f"<th>{h}</th>" for h in table_headers])
    rows_html = "".join([
        "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
        for row in table_rows
    ])

    return f"""<div class="mockup-window">
  <div class="mockup-header">
    <div class="mockup-dots">
      <span class="dot-red"></span>
      <span class="dot-yellow"></span>
      <span class="dot-green"></span>
    </div>
    <div class="mockup-title">{title}</div>
    <span class="mockup-badge">{badge_text}</span>
  </div>
  <div class="mockup-body">
    <div class="stat-grid">
      {stats_html}
    </div>
    <div style="overflow-x: auto;">
      <table class="mockup-table">
        <thead>
          <tr>{headers_html}</tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>
  </div>
</div>"""

def build_index():
    body = f"""
    <!-- Hero Section -->
    <section class="page-hero" style="padding: 6rem 0 6.5rem 0;">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 3.5rem;">
          <div class="reveal">
            <span class="section-tag tag-teal"><span class="pulse-indicator"></span> Enterprise Operations &bull; Multichannel CX</span>
            <h1 style="margin-top: 0.75rem;">Streamline Your Business Operations With Smarter Outsourcing</h1>
            <p class="page-hero-desc">
              Focus on growing your business while dedicated business process outsourcing solutions support your customer interactions, back-office operations, and day-to-day processes.
            </p>
            <div class="hero-actions">
              <a href="contact.html" class="btn btn-primary btn-lg">Request a Consultation</a>
              <a href="services.html" class="btn btn-outline-white btn-lg">Explore Our Services</a>
            </div>
            <div style="margin-top: 2rem; display: flex; gap: 2rem; align-items: center; font-size: 0.85rem; color: #94A3B8;">
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#21B6A8" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Voice &amp; Non-Voice</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#21B6A8" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Standardized Workflows</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#21B6A8" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Process Governance</span>
              </div>
            </div>
          </div>
          <div class="reveal reveal-delay-2">
            {render_placeholder("bpo-hero-operations.jpg", "Hero Operations Environment", "ratio-16-9", "1920 &times; 1080")}
          </div>
        </div>
      </div>
    </section>

    <!-- Services Overview Section -->
    <section class="section section-white">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Core BPO Offerings</span>
          <h2 class="section-title">Comprehensive Business Process Solutions</h2>
          <p class="section-desc">From front-line customer engagement to intensive back-office record processing, our structured service capabilities integrate seamlessly with enterprise operational roadmaps.</p>
        </div>

        <div class="grid-3">
          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
            <h3 class="card-title">Customer Experience Management</h3>
            <p class="card-desc">End-to-end support across voice, email, chat, and social channels designed to maintain brand loyalty and response consistency.</p>
            <a href="customer-support.html" class="card-link">Explore Customer Support <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></div>
            <h3 class="card-title">Inbound &amp; Outbound Call Center</h3>
            <p class="card-desc">Professional voice telephony operations covering customer inquiries, verification calls, account updates, and consented outreach.</p>
            <a href="inbound-call-center.html" class="card-link">Explore Call Center <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
            <h3 class="card-title">Technical Support</h3>
            <p class="card-desc">Tier 1 and Tier 2 technical assistance, hardware/software troubleshooting, and structured incident escalation workflows.</p>
            <a href="technical-support.html" class="card-link">Explore Tech Support <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></div>
            <h3 class="card-title">Email &amp; Chat Support</h3>
            <p class="card-desc">Rapid-response written ticket resolution and conversational live chat workflows integrated with modern helpdesk platforms.</p>
            <a href="email-support.html" class="card-link">Explore Digital Support <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg></div>
            <h3 class="card-title">Back Office Operations</h3>
            <p class="card-desc">High-volume transactional workflows, record organization, administrative coordination, and systematic archiving.</p>
            <a href="back-office.html" class="card-link">Explore Back Office <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div>
            <h3 class="card-title">Data Entry &amp; Processing</h3>
            <p class="card-desc">Precision capture, multi-stage validation, data sanitization, spreadsheet consolidation, and database population.</p>
            <a href="data-entry.html" class="card-link">Explore Data Entry <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
            <h3 class="card-title">Finance &amp; Accounting Support</h3>
            <p class="card-desc">Accounts payable, accounts receivable, invoice matching, and ledger reconciliation within client-defined access controls.</p>
            <a href="finance-accounting.html" class="card-link">Explore Finance Operations <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h3 class="card-title">Content Moderation</h3>
            <p class="card-desc">Policy-guided review of user-generated text, profiles, comments, and media with well-being safety protocols for moderators.</p>
            <a href="content-moderation.html" class="card-link">Explore Moderation <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg></div>
            <h3 class="card-title">Lead Generation</h3>
            <p class="card-desc">Systematic contact enrichment, prospecting research, CRM validation, and appointment scheduling assistance.</p>
            <a href="lead-generation.html" class="card-link">Explore Lead Support <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div>
            <h3 class="card-title">Virtual Assistance</h3>
            <p class="card-desc">Executive calendar management, routine inbox triage, meeting scheduling, and digital administrative assistance.</p>
            <a href="virtual-assistance.html" class="card-link">Explore Virtual Assistance <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-1">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
            <h3 class="card-title">HR Outsourcing</h3>
            <p class="card-desc">Candidate screening logistics, onboarding paperwork verification, personnel records maintenance, and HR administrative coordination.</p>
            <a href="human-resources-outsourcing.html" class="card-link">Explore HR Outsourcing <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>

          <div class="card reveal reveal-delay-2">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></div>
            <h3 class="card-title">Knowledge Process (KPO)</h3>
            <p class="card-desc">Secondary business research, data consolidation, market information synthesis, and structured reporting delivery.</p>
            <a href="knowledge-process-outsourcing.html" class="card-link">Explore KPO Services <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Consider Outsourcing -->
    <section class="section section-light">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag">Strategic Value</span>
            <h2>Why Organizations Consider Strategic Outsourcing</h2>
            <p class="section-desc" style="font-size: 1rem; margin-bottom: 1.5rem;">
              Outsourcing non-core business activities allows enterprise leadership to focus internal capital and talent on strategic innovation, product engineering, and core market growth.
            </p>

            <div class="demo-callout" style="margin-bottom: 2rem;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              <div class="demo-callout-text">
                <h4>Illustrative Business Benefits</h4>
                <p>The operational advantages outlined below represent standard industry benchmarks observed in modern business process management, not guaranteed results of this demonstration website.</p>
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-weight: bold;">1</div>
                <div>
                  <h4 style="font-size: 1.05rem; margin-bottom: 0.25rem;">Operational Flexibility &amp; Scalability</h4>
                  <p style="font-size: 0.9rem; color: var(--color-body-text); margin: 0;">Rapidly expand or streamline frontline capacity in response to seasonal volume fluctuations and marketing campaigns.</p>
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-weight: bold;">2</div>
                <div>
                  <h4 style="font-size: 1.05rem; margin-bottom: 0.25rem;">Process Standardization &amp; Governance</h4>
                  <p style="font-size: 0.9rem; color: var(--color-body-text); margin: 0;">Institutionalize standard operating procedures (SOPs) with transparent metrics, QA audits, and structured workflows.</p>
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-weight: bold;">3</div>
                <div>
                  <h4 style="font-size: 1.05rem; margin-bottom: 0.25rem;">Specialized Operational Capabilities</h4>
                  <p style="font-size: 0.9rem; color: var(--color-body-text); margin: 0;">Leverage trained talent pools versed in modern contact center ticketing tools, CRM environments, and data workflows.</p>
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-weight: bold;">4</div>
                <div>
                  <h4 style="font-size: 1.05rem; margin-bottom: 0.25rem;">Enhanced Customer Experience Focus</h4>
                  <p style="font-size: 0.9rem; color: var(--color-body-text); margin: 0;">Maintain responsive response times and high resolution rates across diverse customer touchpoints without overtaxing core staff.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-business-flexibility.jpg", "Strategic Operational Value", "ratio-4-3", "1200 &times; 900")}
          </div>
        </div>
      </div>
    </section>

    <!-- Industries Section -->
    <section class="section section-white">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Sector Expertise</span>
          <h2 class="section-title">Industries We Support</h2>
          <p class="section-desc">Tailoring business process and contact center workflows to the operational realities and compliance requirements of diverse enterprise sectors.</p>
        </div>

        <div class="grid-4">
          <a href="healthcare-industry.html" class="card reveal" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Healthcare</h3>
            <p class="card-desc">Non-clinical administrative support, appointment scheduling, and patient record filing workflows.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="banking-finance.html" class="card reveal reveal-delay-1" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Banking &amp; Finance</h3>
            <p class="card-desc">Back-office document indexing, transaction matching support, and customer query routing.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="ecommerce-industry.html" class="card reveal reveal-delay-2" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">E-Commerce &amp; Retail</h3>
            <p class="card-desc">Order tracking, return authorizations, catalog updates, and peak-season chat triage.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="technology-industry.html" class="card reveal reveal-delay-3" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Technology &amp; SaaS</h3>
            <p class="card-desc">Tier 1 technical support, user onboarding guidance, ticket triage, and knowledge documentation.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="telecommunications-industry.html" class="card reveal" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Telecommunications</h3>
            <p class="card-desc">Service activation inquiries, billing clarification assistance, and account verification handling.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="travel-hospitality.html" class="card reveal reveal-delay-1" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Travel &amp; Hospitality</h3>
            <p class="card-desc">Booking modifications, reservation support, itinerary inquiries, and customer feedback surveys.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="insurance-industry.html" class="card reveal reveal-delay-2" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Insurance</h3>
            <p class="card-desc">First notice of loss (FNOL) documentation, policy status queries, and claims administrative support.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>

          <a href="logistics-industry.html" class="card reveal reveal-delay-3" style="text-decoration: none; color: inherit;">
            <div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg></div>
            <h3 class="card-title" style="font-size: 1.15rem;">Logistics &amp; Transport</h3>
            <p class="card-desc">Shipment tracking, delivery exception logging, driver coordination assistance, and dispatch dispatching support.</p>
            <span class="card-link">View Industry Details &rarr;</span>
          </a>
        </div>
      </div>
    </section>

    <!-- How The Process Works -->
    <section class="section section-light">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Structured Methodology</span>
          <h2 class="section-title">How Our Operational Process Works</h2>
          <p class="section-desc">A five-stage governance model designed to de-risk transitions, clarify SLA metrics, and maintain continuous service quality.</p>
        </div>

        <div class="process-grid">
          <div class="process-step reveal">
            <div class="process-num">01</div>
            <h3 class="process-title">Discovery</h3>
            <p class="process-desc">Understand business objectives, current operating volume, technology landscape, and KPIs.</p>
          </div>

          <div class="process-step reveal reveal-delay-1">
            <div class="process-num">02</div>
            <h3 class="process-title">Scope Definition</h3>
            <p class="process-desc">Map explicit workflows, boundary limits, RACI matrices, and standard operating procedures (SOPs).</p>
          </div>

          <div class="process-step reveal reveal-delay-2">
            <div class="process-num">03</div>
            <h3 class="process-title">Resource Planning</h3>
            <p class="process-desc">Staff allocation, training material development, tooling configurations, and access controls setup.</p>
          </div>

          <div class="process-step reveal reveal-delay-3">
            <div class="process-num">04</div>
            <h3 class="process-title">Transition</h3>
            <p class="process-desc">Pilot execution, shadow testing, SLA baseline validation, and full operational launch.</p>
          </div>

          <div class="process-step reveal reveal-delay-4">
            <div class="process-num">05</div>
            <h3 class="process-title">Continuous Improvement</h3>
            <p class="process-desc">Weekly calibration audits, QA scorecards, root cause analysis, and ongoing process optimization.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="process.html" class="btn btn-secondary">Learn More About Our 5-Stage Process &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Operational Capabilities -->
    <section class="section section-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            {render_placeholder("bpo-multichannel-support.jpg", "Multichannel Support Operations", "ratio-16-9", "1200 &times; 675")}
          </div>
          <div class="reveal reveal-delay-1">
            <span class="section-tag tag-teal">Operational Breadth</span>
            <h2>Multichannel Capabilities Across Enterprise Operations</h2>
            <p class="section-desc" style="font-size: 1rem; margin-bottom: 1.5rem;">
              We deploy modular teams configured to execute diverse operational formats with consistent adherence to client quality guidelines.
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem;">
              <div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-corporate-blue);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Voice Support</h4>
                <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Inbound call resolution and telephone assistance.</p>
              </div>
              <div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-teal-accent);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Non-Voice Support</h4>
                <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Email ticketing, chat queues, and portal messages.</p>
              </div>
              <div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-corporate-blue);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Back Office Processing</h4>
                <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">Document indexing, data sanitization, and reconciliations.</p>
              </div>
              <div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-teal-accent);">
                <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">CX Management</h4>
                <p style="font-size: 0.85rem; color: var(--color-muted-text); margin: 0;">CSAT scoring, sentiment logging, and feedback loops.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Technology & Illustrative Mockup Section -->
    <section class="section section-dark">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag tag-teal">Technology Capabilities</span>
          <h2 style="color: #fff;">Modern Tooling &amp; Illustrative Workflows</h2>
          <p style="color: #94A3B8;">Illustrative overview of contact center management consoles, ticketing triage, and operational reporting dashboards.</p>
        </div>

        <div class="reveal">
          {render_dashboard_mockup(
            "Contact Center & Ticket Management Console &mdash; Illustrative Overview",
            "ILLUSTRATIVE DEMO DATA &mdash; NOT CONNECTED TO A LIVE SYSTEM",
            [
              ("Active Queue (Demo)", "14"),
              ("Avg Handle Time (Demo)", "4m 12s"),
              ("QA Pass Rate (Demo)", "97.4%"),
              ("SLA Adherence (Demo)", "98.8%")
            ],
            ["Ticket ID", "Channel", "Category", "Priority", "Status", "Wait Time"],
            [
              ["#TK-9021", "Live Chat", "Billing Inquiry", "Normal", "In Progress", "0m 42s"],
              ["#TK-9022", "Inbound Call", "Technical Escalation", "High", "Assigned", "1m 15s"],
              ["#TK-9023", "Email Ticket", "Account Verification", "Normal", "Under Review", "5m 20s"],
              ["#TK-9024", "Web Form", "Order Tracking", "Low", "Resolved", "12m 04s"],
              ["#TK-9025", "Live Chat", "Product Setup", "Normal", "Active", "0m 18s"]
            ]
          )}
        </div>

        <div style="margin-top: 2.5rem; text-align: center;">
          <a href="technology.html" class="btn btn-outline-white">Explore Technology &amp; Capabilities &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Case Studies Preview -->
    <section class="section section-white">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Operational Scenarios</span>
          <h2 class="section-title">Illustrative Case Scenarios</h2>
          <p class="section-desc">Sample operational challenges and standard BPO workflow remediation models.</p>
        </div>

        <div class="grid-3">
          <div class="article-card reveal">
            <div style="background: #F1F5F9; padding: 0.75rem 1rem; border-bottom: 1px solid #E2E8F0; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO CASE STUDY &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>Customer Experience</span> &bull; <span>Process Redesign</span>
              </div>
              <h3 class="article-title"><a href="case-study-details.html">Customer Support Workflow Improvement</a></h3>
              <p class="article-excerpt">How a tiered routing model and updated knowledge base architecture reduced ticket backlogs in a simulated software environment.</p>
              <a href="case-study-details.html" class="card-link">Read Scenario Details &rarr;</a>
            </div>
          </div>

          <div class="article-card reveal reveal-delay-1">
            <div style="background: #F1F5F9; padding: 0.75rem 1rem; border-bottom: 1px solid #E2E8F0; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO CASE STUDY &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>E-Commerce Operations</span> &bull; <span>Peak Season Surge</span>
              </div>
              <h3 class="article-title"><a href="case-studies.html">E-Commerce Order Enquiry Management</a></h3>
              <p class="article-excerpt">Structuring flexible staffing schedules and automated template triage to absorb a holiday order volume spike.</p>
              <a href="case-studies.html" class="card-link">Read Scenario Details &rarr;</a>
            </div>
          </div>

          <div class="article-card reveal reveal-delay-2">
            <div style="background: #F1F5F9; padding: 0.75rem 1rem; border-bottom: 1px solid #E2E8F0; font-size: 0.75rem; font-weight: 700; color: #B45309; text-align: center;">
              ILLUSTRATIVE DEMO CASE STUDY &mdash; NOT A REAL CLIENT PROJECT
            </div>
            <div class="article-body">
              <div class="article-meta">
                <span>Back Office BPO</span> &bull; <span>Data Verification</span>
              </div>
              <h3 class="article-title"><a href="case-studies.html">Back Office Data Processing Workflow</a></h3>
              <p class="article-excerpt">Implementing double-blind verification and dual-analyst checks to increase accuracy across complex invoice validation.</p>
              <a href="case-studies.html" class="card-link">Read Scenario Details &rarr;</a>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="case-studies.html" class="btn btn-secondary">View All Case Study Scenarios &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Careers Preview -->
    <section class="section section-light">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 4rem;">
          <div class="reveal">
            <span class="section-tag tag-teal">Join Our Operations Talent</span>
            <h2>Build Your Career in Business Process Outsourcing</h2>
            <p class="section-desc" style="font-size: 1rem; margin-bottom: 1.5rem;">
              We provide structured training pathways, clear operational leadership trajectories, and professional development programs in customer experience and business operations.
            </p>

            <div class="demo-callout" style="margin-bottom: 1.5rem;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              <div class="demo-callout-text">
                <h4>DEMO JOB LISTING &mdash; NOT A VERIFIED LIVE VACANCY</h4>
                <p>All roles displayed on this website represent sample positions for demonstration purposes only.</p>
              </div>
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 2rem;">
              <span class="badge badge-blue">Customer Support Executive</span>
              <span class="badge badge-blue">Technical Support Associate</span>
              <span class="badge badge-blue">Back Office Executive</span>
              <span class="badge badge-blue">Data Processing Associate</span>
              <span class="badge badge-blue">Quality Analyst</span>
              <span class="badge badge-blue">Team Leader</span>
            </div>

            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="job-openings.html" class="btn btn-primary">Browse Sample Job Openings</a>
              <a href="careers.html" class="btn btn-secondary">Careers Overview</a>
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder("bpo-career-opportunities.jpg", "Career Growth & Development", "ratio-4-3", "1200 &times; 900")}
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Preview -->
    <section class="section section-white">
      <div class="container" style="max-width: 860px;">
        <div class="section-header reveal">
          <span class="section-tag">Frequently Asked Questions</span>
          <h2 class="section-title">Common Questions About Outsourcing</h2>
          <p class="section-desc">Key considerations for organizations exploring business process outsourcing partnerships.</p>
        </div>

        <div class="accordion reveal">
          <div class="accordion-item">
            <button class="accordion-btn" aria-expanded="false">
              <span>What is Business Process Outsourcing (BPO)?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-content">
              <p>Business Process Outsourcing involves delegating specific non-core operational functions—such as customer contact handling, technical troubleshooting, data entry, or invoice processing—to specialized service teams who execute the workflows according to agreed service standards.</p>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-btn" aria-expanded="false">
              <span>What is the difference between voice and non-voice BPO?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-content">
              <p>Voice BPO encompasses spoken telephone communication, such as inbound customer support, technical assistance helplines, and verified follow-up calls. Non-voice BPO encompasses written and back-office channels, including email support, live web chat, data processing, catalog moderation, and transaction filing.</p>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-btn" aria-expanded="false">
              <span>How is service quality monitored and evaluated?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-content">
              <p>Quality management typically includes standardized call scoring rubrics, ticket QA checks, sample validation audits, SLA compliance monitoring, and periodic calibration sessions with client stakeholders to maintain consistent accuracy.</p>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2rem;">
          <a href="faq.html" class="card-link" style="font-size: 1rem;">View All Frequently Asked Questions &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Final CTA -->
    {render_cta_banner("Let's Discuss Your Business Process Requirements",
                       "Connect with our solutions team to explore how structured outsourcing workflows can support your operational goals.",
                       "Request a Consultation", "contact.html",
                       "Contact Us", "contact.html")}
    """

    return render_page(
        "Modern Business Process Outsourcing & Multichannel CX",
        "Streamline business operations with professional customer experience management, inbound and outbound call center services, technical support, and back-office outsourcing.",
        "home",
        body,
        "index.html"
    )

print("Index builder ready.")
