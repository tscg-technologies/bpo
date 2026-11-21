"""
BPO Service Pages Generator (17 Individual Service Pages)
"""

import os
from builder import render_page, render_placeholder, render_breadcrumb, LOGO_SVG
from generate_pages import render_cta_banner

def render_service_template(
    slug, title, meta_desc, hero_tag, hero_h1, hero_desc,
    placeholder_filename, placeholder_label,
    overview_text, problems_addressed, scope_items,
    workflow_steps, tools_channels, quality_considerations,
    benefits_list, faqs, related_services, extra_disclaimer=None
):
    crumbs = [("Home", "index.html"), ("Services", "services.html"), (title, None)]
    breadcrumb_html = render_breadcrumb(crumbs)

    disclaimer_html = ""
    if extra_disclaimer:
        disclaimer_html = f"""<div class="demo-callout" style="margin-bottom: 2.5rem;">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
  <div class="demo-callout-text">
    <h4>Operational Scope &amp; Compliance Protocol</h4>
    <p>{extra_disclaimer}</p>
  </div>
</div>"""

    # Problems list
    problems_html = "".join([f"""<div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-corporate-blue);">
  <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">{p[0]}</h4>
  <p style="font-size: 0.875rem; color: var(--color-body-text); margin: 0;">{p[1]}</p>
</div>""" for p in problems_addressed])

    # Scope items
    scope_html = "".join([f"""<div class="card reveal" style="padding: 1.5rem;">
  <div style="width: 36px; height: 36px; border-radius: var(--radius-sm); background: rgba(40,100,216,0.1); color: var(--color-corporate-blue); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
  </div>
  <h4 style="margin-bottom: 0.5rem; font-size: 1.1rem;">{s[0]}</h4>
  <p style="font-size: 0.875rem; color: var(--color-muted-text); margin: 0;">{s[1]}</p>
</div>""" for s in scope_items])

    # Workflow steps
    wf_html = "".join([f"""<div class="process-step reveal">
  <div class="process-num">{i+1}</div>
  <h4 class="process-title" style="font-size: 1rem;">{step[0]}</h4>
  <p class="process-desc">{step[1]}</p>
</div>""" for i, step in enumerate(workflow_steps)])

    # FAQs
    faq_html = "".join([f"""<div class="accordion-item">
  <button class="accordion-btn" aria-expanded="false">
    <span>{q}</span>
    <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
  </button>
  <div class="accordion-content">
    <p>{a}</p>
  </div>
</div>""" for q, a in faqs])

    # Related services
    related_html = "".join([f"""<div class="card reveal">
  <h4 style="margin-bottom: 0.5rem;"><a href="{r[1]}">{r[0]}</a></h4>
  <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">{r[2]}</p>
  <a href="{r[1]}" class="card-link">View Service &rarr;</a>
</div>""" for r in related_services])

    # Benefits
    benefits_html = "".join([f"""<li style="margin-bottom: 0.75rem;"><strong>{b[0]}:</strong> {b[1]}</li>""" for b in benefits_list])

    body = f"""
    {breadcrumb_html}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">{hero_tag}</span>
        <h1>{hero_h1}</h1>
        <p class="page-hero-desc">{hero_desc}</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary btn-lg">Request a Consultation</a>
          <a href="services.html" class="btn btn-outline-white btn-lg">All BPO Services</a>
        </div>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        {disclaimer_html}

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Service Overview</span>
            <h2>Operational Context &amp; Purpose</h2>
            <div class="prose-content">
              {overview_text}
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder(placeholder_filename, placeholder_label, "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

        <!-- Problems Addressed -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">Operational Challenges</span>
            <h2 class="section-title">Business Problems Addressed</h2>
            <p class="section-desc">Key operational bottlenecks and delivery risks mitigated through this service workflow.</p>
          </div>
          <div class="grid-2" style="gap: 1.5rem;">
            {problems_html}
          </div>
        </div>

        <!-- Scope Grid -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">Service Scope</span>
            <h2 class="section-title">Detailed Operational Scope</h2>
            <p class="section-desc">Specific tasks, procedural duties, and administrative checkpoints included within this delivery model.</p>
          </div>
          <div class="grid-3">
            {scope_html}
          </div>
        </div>

        <!-- Typical Workflow -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">Execution Lifecycle</span>
            <h2 class="section-title">Typical Operating Workflow</h2>
            <p class="section-desc">Step-by-step procedure governing how incoming tasks are received, verified, executed, and archived.</p>
          </div>
          <div class="process-grid" style="grid-template-columns: repeat({len(workflow_steps)}, 1fr);">
            {wf_html}
          </div>
        </div>

        <!-- Quality & Tools -->
        <div class="grid-2" style="gap: 3rem; margin-bottom: 4rem;">
          <div class="card reveal" style="background: var(--color-light-bg);">
            <h3 style="margin-bottom: 1rem; color: var(--color-primary-navy);">Communication &amp; Tooling</h3>
            <p style="font-size: 0.9rem; color: var(--color-body-text); margin-bottom: 1rem;">{tools_channels}</p>
          </div>
          <div class="card reveal reveal-delay-1" style="background: var(--color-light-bg);">
            <h3 style="margin-bottom: 1rem; color: var(--color-primary-navy);">Quality Considerations</h3>
            <p style="font-size: 0.9rem; color: var(--color-body-text); margin-bottom: 1rem;">{quality_considerations}</p>
          </div>
        </div>

        <!-- Potential Benefits -->
        <div style="margin-bottom: 4rem;">
          <div class="card reveal" style="padding: 2.5rem; border-left: 4px solid var(--color-corporate-blue);">
            <h3 style="margin-bottom: 1rem;">Potential Business Benefits</h3>
            <ul style="color: var(--color-body-text); padding-left: 1.25rem; margin: 0;">
              {benefits_html}
            </ul>
          </div>
        </div>

        <!-- Service-Specific FAQs -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">FAQs</span>
            <h2 class="section-title">Questions About {title}</h2>
          </div>
          <div class="accordion reveal" style="max-width: 860px; margin: 0 auto;">
            {faq_html}
          </div>
        </div>

        <!-- Related Services -->
        <div>
          <div class="section-header reveal">
            <span class="section-tag">Explore More</span>
            <h2 class="section-title">Related Operational Services</h2>
          </div>
          <div class="grid-3">
            {related_html}
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner(f"Discuss Your {title} Requirements",
                       "Connect with our solutions team to evaluate your volume, team sizing, and quality SLA expectations.",
                       "Request a Consultation", "contact.html",
                       "Contact Us", "contact.html")}
    """

    return render_page(
        f"{title} — BPO Service Capabilities",
        meta_desc,
        "services",
        body,
        f"{slug}.html"
    )

print("Service template engine ready.")
