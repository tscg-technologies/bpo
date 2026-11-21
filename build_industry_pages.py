"""
Industry Pages Generator (8 Vertical Industry Pages)
"""

import os
from builder import render_page, render_placeholder, render_breadcrumb, LOGO_SVG
from generate_pages import render_cta_banner

INDUSTRIES_DATA = [
    # 1. Healthcare
    {
        "slug": "healthcare-industry",
        "title": "Healthcare & Life Sciences Outsourcing",
        "meta_desc": "Non-clinical administrative support, patient appointment scheduling, and registration document handling for healthcare providers.",
        "hero_tag": "Healthcare Operations",
        "hero_h1": "Healthcare &amp; Life Sciences Administrative Outsourcing",
        "hero_desc": "Providing non-clinical administrative support to help medical facilities, health clinics, and life science organizations streamline patient scheduling and intake operations.",
        "placeholder_filename": "bpo-industry-healthcare.jpg",
        "placeholder_label": "Healthcare Operational Environment",
        "overview": "<p>Modern healthcare providers face intense operational burdens: coordinating thousands of patient appointments, verifying registration documents, and managing high telephone inquiry volumes. These clerical distractions can overwhelm front-desk staff and pull clinical personnel away from direct patient care.</p><p>We provide structured, non-clinical administrative workflows that handle routine patient inquiries, appointment confirmations, and medical record indexing with empathy and confidentiality.</p>",
        "disclaimer": "MANDATORY HEALTHCARE DISCLAIMER: All services described on this page are strictly non-clinical administrative workflows. We do not provide medical diagnosis, clinical triage, or patient treatment advice. Furthermore, we do not claim unverified HIPAA certification or access to protected health information (PHI) without verified, client-established technical safeguards and executed Business Associate Agreements (BAAs).",
        "challenges": [
            ("Clinic Front Desk Overload", "Front desk receptionists interrupted constantly by ringing telephones while patients wait in line."),
            ("High Patient No-Show Rates", "Unfilled clinical slots resulting from lack of timely appointment reminder calls."),
            ("Incomplete Registration Records", "Missing insurance scans, illegible handwriting, and incomplete intake questionnaires."),
            ("Patient Frustration on Hold", "Long hold times for basic inquiries regarding clinic hours, directions, and doctor availability.")
        ],
        "workflow_example": ("Patient Scheduling & Intake Workflow", [
            ("Patient Call Ingestion", "Patient calls clinic number; call answered with professional, empathetic etiquette."),
            ("Identity & Insurance Check", "Verifying patient registration details and collecting intake insurance information."),
            ("Provider Slot Matching", "Scheduling appointment into clinic EHR system following provider duration rules."),
            ("Automated Reminder", "Scheduling SMS or voice reminder call 48 hours prior to appointment time."),
            ("Clinic Record Update", "Logging patient appointment status in clinic management software.")
        ]),
        "benefits": [
            ("Enhanced Front-Desk Focus", "Allows on-site staff to provide personal, unhurried attention to arriving patients."),
            ("Reduced Appointment Vacancies", "Proactive reminder workflows maximize clinical provider utilization rates."),
            ("Improved Patient Satisfaction", "Prompt telephone answers reduce hold times and improve overall patient trust.")
        ],
        "data_considerations": "Healthcare administration requires role-based access controls, minimal necessary data exposure, session timeouts, clean-desk operations, and execution exclusively inside client-managed portals.",
        "relevant_services": [
            ("Healthcare Process Support", "healthcare-process-outsourcing.html", "Dedicated non-clinical appointment and intake workflows."),
            ("Inbound Call Center", "inbound-call-center.html", "Telephone customer care operations."),
            ("Document Management", "document-management.html", "Digitization and record filing.")
        ]
    },

    # 2. Banking & Financial Services
    {
        "slug": "banking-finance",
        "title": "Banking & Financial Services Outsourcing",
        "meta_desc": "Back-office document indexing, invoice reconciliation, and customer query routing for financial institutions under strict access controls.",
        "hero_tag": "Financial Operations",
        "hero_h1": "Banking &amp; Financial Services BPO Support",
        "hero_desc": "Supporting financial institutions, fintech platforms, and credit providers with back-office transactional processing, document indexing, and non-advisory customer care.",
        "placeholder_filename": "bpo-industry-banking-finance.jpg",
        "placeholder_label": "Banking & Financial Services Operations",
        "overview": "<p>Financial services institutions operate under intense scrutiny, requiring meticulous documentation trails, strict access controls, and absolute accuracy in daily transactional processing.</p><p>Our financial services operational support model provides disciplined document verification, invoice matching, account balance query triage, and non-advisory customer assistance within client-defined access boundaries.</p>",
        "disclaimer": "FINANCIAL REGULATORY DISCLAIMER: We provide non-advisory operational and back-office support only. We do not provide banking, securities brokerage, statutory auditing, or investment advisory services. Actual technical security controls and regulatory compliance agreements must be independently established per client contract.",
        "challenges": [
            ("Manual Document Verification Spikes", "High volumes of loan paperwork, account applications, and tax proofs requiring verification."),
            ("Routine Account Balance Inquiries", "High call queues for routine transaction lookups distracting relationship managers."),
            ("Delayed Reconciliation Cycles", "Manual reconciliation of payment gateway settlements creating month-end bottlenecks."),
            ("Strict Audit Compliance", "Risk of human error during routine data transcription into core banking systems.")
        ],
        "workflow_example": ("Account Application Document Triage", [
            ("Application Receipt", "Application bundle uploaded to secure banking document portal."),
            ("Field Completeness Audit", "Reviewing that all mandatory identity proofs and proof-of-income files are present."),
            ("Data Keying & Indexing", "Entering validated application fields into core banking CRM under role-based logins."),
            ("Discrepancy Escalation", "Flagging incomplete or unreadable documents and requesting applicant follow-up."),
            ("Underwriter Queue Handover", "Passing clean, fully indexed dossier to client internal underwriting officers.")
        ]),
        "benefits": [
            ("Accelerated Application Cycles", "Pre-verified dossiers speed up loan and account approval timelines."),
            ("Lower Cost per Transaction", "Standardized back-office processing significantly reduces operational overhead."),
            ("Audit-Ready Trails", "Timestamped indexing ensures full traceability for internal and external auditors.")
        ],
        "data_considerations": "Requires strict segregation of client networks, masked PII display, multi-factor authentication, clean-desk policies, and execution on client-controlled VDI.",
        "relevant_services": [
            ("Finance & Accounting", "finance-accounting.html", "AP/AR and reconciliation support."),
            ("Data Entry & Processing", "data-entry.html", "High-accuracy financial data keying."),
            ("Customer Support", "customer-support.html", "Multichannel customer service.")
        ]
    },

    # 3. E-commerce & Retail
    {
        "slug": "ecommerce-industry",
        "title": "E-Commerce & Retail Outsourcing",
        "meta_desc": "Scalable customer care, order tracking, return processing, and catalog management for high-growth e-commerce brands.",
        "hero_tag": "Retail & Digital Commerce",
        "hero_h1": "E-Commerce &amp; Retail Operational Outsourcing",
        "hero_desc": "Empowering digital retail brands to deliver rapid live chat support, order status tracking, returns management, and catalog maintenance across peak seasonal surges.",
        "placeholder_filename": "bpo-industry-ecommerce-retail.jpg",
        "placeholder_label": "E-Commerce Logistics & Support Hub",
        "overview": "<p>E-commerce success hinges on frictionless customer experiences: fast shipping answers, immediate live chat on product pages, and hassle-free returns. During holiday surges, customer contact volume can quadruple overnight.</p><p>Our retail outsourcing solutions provide flexible, multi-skilled teams trained in modern e-commerce platforms, order tracking consoles, and shopping assistance chat.</p>",
        "disclaimer": "RETAIL COMPLIANCE NOTICE: Customer interactions and payment handling must occur through client-authorized PCI-compliant gateways. Our demonstration workflows do not collect or store raw payment card data.",
        "challenges": [
            ("Holiday Volume Volatility", "Handling 3x to 5x inquiry surges during Black Friday, Cyber Monday, and peak promotions."),
            ("Where Is My Order (WISMO) Dominance", "Up to 50% of incoming contacts asking for carrier tracking updates."),
            ("Cart Abandonment", "Shoppers leaving items in cart due to unanswered questions on sizing, materials, or delivery dates."),
            ("Time-Consuming Catalog Updates", "Uploading hundreds of new product SKUs, tags, and images across merchant channels.")
        ],
        "workflow_example": ("Order Inquiry & Returns Lifecycle", [
            ("Customer Contact", "Customer opens live chat asking about delayed package delivery."),
            ("Carrier Integration Check", "Agent queries integrated shipping API to check real-time package location."),
            ("Delivery Clarification", "Agent explains estimated delivery arrival or carrier weather delay."),
            ("Return Authorization (RMA)", "If return is requested, agent checks eligibility and generates return label."),
            ("Order Sync", "Updating order record in Shopify or ERP and dispatching confirmation email.")
        ]),
        "benefits": [
            ("Elastic Seasonal Scalability", "Quickly ramp agent counts before peak shopping seasons without long-term overhead."),
            ("Protected Merchant Ratings", "Rapid response times safeguard seller ratings on Amazon, Shopify, and Google."),
            ("Reduced Cart Drop-Offs", "Proactive live chat assistance resolves pre-purchase hesitation at checkout.")
        ],
        "data_considerations": "Customer personal address records and transaction histories must be accessed only via authorized e-commerce admin permissions with strict session auditing.",
        "relevant_services": [
            ("Order Processing", "order-processing.html", "Fulfillment updates and RMA handling."),
            ("Live Chat Support", "chat-support.html", "Real-time shopper assistance."),
            ("Customer Support", "customer-support.html", "Multichannel retail customer care.")
        ]
    },

    # 4. Technology & Software (SaaS)
    {
        "slug": "technology-industry",
        "title": "Technology & Software (SaaS) Outsourcing",
        "meta_desc": "Tier 1 and Tier 2 technical helpdesk, customer onboarding, bug verification, and knowledge base management for software companies.",
        "hero_tag": "SaaS & Tech Support",
        "hero_h1": "Technology &amp; Software BPO Solutions",
        "hero_desc": "Providing technical tier 1 &amp; 2 helpdesk support, user onboarding walkthroughs, bug reproduction, and documentation curation for software and SaaS enterprises.",
        "placeholder_filename": "bpo-industry-tech-software.jpg",
        "placeholder_label": "Technology Helpdesk & Support Station",
        "overview": "<p>Software users expect knowledgeable, rapid technical assistance when configuring workflows, encountering bugs, or navigating new features. When routine support tickets flood engineering backlogs, core product development slows.</p><p>We provide technically adept support teams that diagnose user inquiries, reproduce software issues, create comprehensive bug tickets, and guide users through onboarding decision trees.</p>",
        "disclaimer": "SOFTWARE COMPLIANCE NOTICE: Technical support workflows operate within client sandbox environments and approved access credentials. We do not claim access to production source code or proprietary IP without verified security arrangements.",
        "challenges": [
            ("Developer Distraction", "Senior engineers spending valuable sprint time answering basic user configuration queries."),
            ("Incomplete Bug Reports", "Support tickets filed without browser specifications, error console logs, or reproduction steps."),
            ("High Customer Churn During Onboarding", "New trial users dropping off due to lack of immediate technical guidance."),
            ("Outdated Help Documentation", "Knowledge base articles falling out of date after rapid software releases.")
        ],
        "workflow_example": ("Technical Issue Triage & Bug Escalation", [
            ("Ticket Ingestion", "User submits support ticket with error screenshot via helpdesk portal."),
            ("Diagnostic Reproduction", "Support associate recreates user steps in test sandbox to verify defect."),
            ("Tier 1 Resolution", "If issue is configuration-related, associate provides guided walkthrough to fix."),
            ("Bug Ticket Formulation", "If defect is confirmed, associate compiles structured ticket with logs and steps."),
            ("Engineering Backlog Handoff", "Ticket formatted into client Jira backlog and user kept updated.")
        ]),
        "benefits": [
            ("Preserved Engineering Bandwidth", "Protects developers from routine questions, keeping sprint velocities high."),
            ("High First-Contact Resolution", "Structured troubleshooting trees resolve user setup hurdles immediately."),
            ("Polished Bug Documentation", "Developers receive actionable, reproducible tickets with zero ambiguity.")
        ],
        "data_considerations": "Associates operate strictly within staging or permission-restricted user accounts, ensuring customer tenant data remains completely confidential.",
        "relevant_services": [
            ("Technical Support", "technical-support.html", "Tier 1 and Tier 2 technical helpdesk."),
            ("Email Support", "email-support.html", "Structured ticket queue resolution."),
            ("Live Chat Support", "chat-support.html", "Real-time in-app user assistance.")
        ]
    },

    # 5. Telecommunications
    {
        "slug": "telecommunications-industry",
        "title": "Telecommunications BPO Services",
        "meta_desc": "High-volume customer support, billing inquiries, service activation coordination, and network status communications for telecom providers.",
        "hero_tag": "Telecom Customer Care",
        "hero_h1": "Telecommunications Operational Outsourcing",
        "hero_desc": "Supporting wireless, broadband, and telecom providers with high-volume customer care, plan change requests, billing clarification, and field dispatch logging.",
        "placeholder_filename": "bpo-industry-telecom.jpg",
        "placeholder_label": "Telecom Operations & Contact Floor",
        "overview": "<p>Telecommunications operators manage massive subscriber bases demanding continuous connectivity. Service disruptions, billing complexity, and device upgrades generate enormous contact volumes that require disciplined routing.</p><p>Our telecom BPO teams deliver high-volume voice and digital customer care, guiding subscribers through account changes, explaining billing line items, and coordinating technician dispatch appointments.</p>",
        "disclaimer": "TELECOM REGULATORY NOTICE: Subscriber account updates and line changes must follow client authentication protocols and applicable telecommunications privacy standards. We operate strictly as an administrative support partner.",
        "challenges": [
            ("Network Outage Contact Spikes", "Severe volume surges during weather disruptions or maintenance windows."),
            ("Billing Explanations", "Subscribers confused by promotional expirations, roaming charges, or device installments."),
            ("Service Provisioning Delays", "Subscribers waiting for broadband modem activations or SIM card transfers."),
            ("Field Technician Coordination", "Missed home installation appointments causing high customer dissatisfaction.")
        ],
        "workflow_example": ("Broadband Billing & Service Triage", [
            ("Subscriber Call Receipt", "Subscriber calls helpline with invoice inquiry; IVR routes based on phone number."),
            ("Security Verification", "Caller confirms account pin and registered billing address."),
            ("Bill Breakdown Explanation", "Associate inspects CRM billing ledger and explains promotional discount expiration."),
            ("Plan Optimization", "Associate offers approved alternative plan package to maintain subscriber retention."),
            ("Confirmation SMS Dispatch", "Sending confirmation message and updating subscriber account record.")
        ]),
        "benefits": [
            ("Lower Average Wait Times", "High-capacity telephony teams absorb peak morning and evening call spikes."),
            ("Enhanced Subscriber Retention", "Professional, empathetic billing explanations reduce churn requests."),
            ("Accurate Field Scheduling", "Rigorous address and contact verification eliminates missed technician visits.")
        ],
        "data_considerations": "Requires strict verification of subscriber PINs, masked credit card details, and compliance with telecommunications confidentiality guidelines.",
        "relevant_services": [
            ("Inbound Call Center", "inbound-call-center.html", "Voice telephony operations."),
            ("Customer Support", "customer-support.html", "Multichannel subscriber support."),
            ("Technical Support", "technical-support.html", "Modem and connectivity troubleshooting.")
        ]
    },

    # 6. Travel & Hospitality
    {
        "slug": "travel-hospitality",
        "title": "Travel & Hospitality BPO Services",
        "meta_desc": "24/7 guest assistance, reservation modifications, booking confirmation, and customer feedback handling for travel operators.",
        "hero_tag": "Hospitality & Guest Care",
        "hero_h1": "Travel &amp; Hospitality Customer Operations",
        "hero_desc": "Delivering 24/7 reservation assistance, booking modifications, flight and hotel cancellation handling, and guest loyalty program support.",
        "placeholder_filename": "bpo-industry-travel-hospitality.jpg",
        "placeholder_label": "Travel Operations & Guest Concierge Desk",
        "overview": "<p>Travel plans are unpredictable: flight cancellations, weather delays, and last-minute hotel changes generate urgent, high-stress customer inquiries that require immediate resolution.</p><p>Our travel and hospitality BPO teams provide 24/7, round-the-clock customer assistance, managing booking adjustments, confirming reservations, and resolving guest concerns with empathy and professionalism.</p>",
        "disclaimer": "TRAVEL COMPLIANCE NOTICE: Reservation modifications and refund disbursements must be processed strictly within airline, hotel, and merchant partner contractual policy rules and authorized client systems.",
        "challenges": [
            ("Weather & Cancellation Crises", "Mass cancellations creating massive, immediate call queues requiring rapid rebooking."),
            ("24/7 Global Time Zone Coverage", "Guests traveling across international time zones needing assistance at all hours."),
            ("Complex Itinerary Modifications", "Multi-leg travel changes involving disparate airlines, hotels, and car rental rules."),
            ("Loyalty Program Management", "Guests requesting point balance redemptions and tier qualification adjustments.")
        ],
        "workflow_example": ("Urgent Itinerary Rebooking Workflow", [
            ("Emergency Guest Contact", "Traveler contacts 24/7 chat desk following airline flight cancellation."),
            ("Itinerary Lookup", "Associate retrieves booking confirmation across Global Distribution System (GDS)."),
            ("Alternative Option Mapping", "Locating next available flights adhering to passenger schedule constraints."),
            ("Rebooking Confirmation", "Executing flight exchange according to airline disruption waivers."),
            ("Itinerary Dispatch", "Transmitting updated e-tickets and hotel arrival notices to traveler phone and email.")
        ]),
        "benefits": [
            ("True 24/7 Global Reliability", "Travelers always reach a live, helpful representative regardless of time zone."),
            ("Crisis Surge Management", "Flexible cross-trained teams absorb weather cancellation volume surges smoothly."),
            ("Elevated Brand Loyalty", "Calm, capable assistance during travel stress turns anxious travelers into lifelong advocates.")
        ],
        "data_considerations": "Passport numbers, birth dates, and payment tokens must be handled through encrypted, secure booking interfaces without local data persistence.",
        "relevant_services": [
            ("Customer Support", "customer-support.html", "24/7 multichannel support operations."),
            ("Inbound Call Center", "inbound-call-center.html", "Urgent voice rebooking assistance."),
            ("Live Chat Support", "chat-support.html", "Real-time in-transit mobile messaging.")
        ]
    },

    # 7. Insurance
    {
        "slug": "insurance-industry",
        "title": "Insurance Process Outsourcing",
        "meta_desc": "First Notice of Loss (FNOL) documentation, policy verification, premium inquiries, and claims administrative support.",
        "hero_tag": "Insurance Operations",
        "hero_h1": "Insurance Process Outsourcing &amp; Claims Support",
        "hero_desc": "Supporting property, auto, and life insurers with First Notice of Loss (FNOL) intake, policy documentation verification, and claims administrative handling.",
        "placeholder_filename": "bpo-industry-insurance.jpg",
        "placeholder_label": "Insurance Claims Administrative Hub",
        "overview": "<p>When policyholders experience property damage, accidents, or illness, their first contact with an insurance company sets the tone for their entire claims experience.</p><p>We provide compassionate, structured First Notice of Loss (FNOL) intake, capturing precise incident facts, indexing supporting police reports and photos, and routing files to designated adjusters.</p>",
        "disclaimer": "INSURANCE REGULATORY DISCLAIMER: We provide non-licensed administrative and intake support only. We do not adjudicate claims, determine liability, make coverage settlement decisions, or provide insurance brokerage advice.",
        "challenges": [
            ("Catastrophic Storm Surges", "Natural weather events generating sudden 10x surges in property damage claims."),
            ("Emotional Policyholder Distress", "Claimants in distress requiring highly empathetic, calm, and patient intake listening."),
            ("Incomplete FNOL Documentation", "Missing accident details or claimant photos causing delays in adjuster assignment."),
            ("High Policy Status Inquiries", "Policyholders repeatedly calling for basic updates on claim payment timing.")
        ],
        "workflow_example": ("First Notice of Loss (FNOL) Intake", [
            ("Claimant Contact", "Policyholder calls reporting automotive collision or property damage."),
            ("Policy Verification", "Associate verifies active policy number, effective dates, and deductible limits."),
            ("Incident Documentation", "Collecting location, time, parties involved, description, and safety status."),
            ("Photo & Document Upload", "Instructing claimant on secure upload of repair estimates and police reports."),
            ("Adjuster Assignment", "Creating clean claim file in claims software and routing to field adjuster.")
        ]),
        "benefits": [
            ("Rapid FNOL Processing", "Immediate, structured intake accelerates the claims adjudication lifecycle."),
            ("Catastrophe Surge Resilience", "Elastic operational staffing absorbs storm claim spikes without crashing systems."),
            ("Empathetic Policyholder Care", "Trained intake specialists provide reassurance and clear next steps to distressed callers.")
        ],
        "data_considerations": "Requires strict data privacy governance, encrypted document archives, role-based access to claim files, and clean-desk operational protocols.",
        "relevant_services": [
            ("Inbound Call Center", "inbound-call-center.html", "Empathetic voice claim intake."),
            ("Document Management", "document-management.html", "Claim photo and document indexing."),
            ("Back Office Operations", "back-office.html", "Administrative claims processing.")
        ]
    },

    # 8. Logistics & Transportation
    {
        "slug": "logistics-industry",
        "title": "Logistics & Transportation Outsourcing",
        "meta_desc": "Shipment tracking, delivery exception logging, driver coordination, and bill of lading document verification for freight carriers.",
        "hero_tag": "Freight & Supply Chain",
        "hero_h1": "Logistics &amp; Transportation Operational Support",
        "hero_desc": "Streamlining supply chain operations through real-time freight tracking inquiries, delivery exception management, driver check-in coordination, and bill of lading indexing.",
        "placeholder_filename": "bpo-industry-logistics-transport.jpg",
        "placeholder_label": "Freight Logistics & Dispatch Command",
        "overview": "<p>In global transportation and freight forwarding, timing is everything. Supply chain managers and shippers demand real-time visibility into cargo movements, customs delays, and delivery milestones.</p><p>Our logistics BPO teams monitor transportation management systems (TMS), answer shipper tracking questions, log carrier exceptions, and index bills of lading (BOL).</p>",
        "disclaimer": "LOGISTICS REGULATORY NOTICE: Transportation workflows are administrative coordination and data entry support only. We do not provide licensed customs brokerage, commercial freight dispatch, or freight forwarding warranties.",
        "challenges": [
            ("Constant 'Where Is My Freight' Calls", "Shippers flooding phone lines for updates on container and truckload status."),
            ("Delivery Exceptions & Holds", "Weather closures, mechanical breakdowns, or customs holds requiring immediate communication."),
            ("Paperwork Indexing Delays", "Delayed billing cycles caused by late processing of proof-of-delivery (POD) documents."),
            ("Driver Check-In Friction", "Overworked dispatchers struggling to handle driver arrival calls and dock appointment slots.")
        ],
        "workflow_example": ("Shipment Exception & Tracking Management", [
            ("Carrier Alert Receipt", "TMS flags delivery exception alert (e.g. carrier delay at intermodal terminal)."),
            ("Status Verification", "Associate calls carrier terminal or queries GPS tracking feed to confirm status."),
            ("Shipper Notification", "Proactively alerting shipper with revised delivery window and cause of delay."),
            ("POD Verification", "Upon delivery, reviewing scanned Proof of Delivery (POD) for signature clarity."),
            ("Invoice Release", "Clearing shipment record in TMS so accounting can issue final freight invoice.")
        ]),
        "benefits": [
            ("Proactive Exception Handling", "Notifying shippers of delays before they have to call minimizes customer frustration."),
            ("Accelerated Freight Billing", "Prompt verification of POD documents shortens days sales outstanding (DSO)."),
            ("Relieved Dispatch Teams", "Removes routine check-in calls from dispatchers so they can optimize routes.")
        ],
        "data_considerations": "Commercial shipping documents and manifests must be accessed strictly through authenticated logistics management consoles with audit logs.",
        "relevant_services": [
            ("Back Office Operations", "back-office.html", "Document indexing and POD processing."),
            ("Data Entry & Processing", "data-entry.html", "Bill of lading transcription and entry."),
            ("Customer Support", "customer-support.html", "Shipper inquiry and tracking support.")
        ]
    }
]

def render_industry_page(ind):
    crumbs = [("Home", "index.html"), ("Industries", "industries.html"), (ind["title"].split(" Outsourcing")[0].split(" BPO")[0], None)]
    breadcrumb_html = render_breadcrumb(crumbs)

    challenges_html = "".join([f"""<div style="padding: 1.25rem; background: var(--color-light-bg); border-radius: var(--radius-md); border-left: 3px solid var(--color-corporate-blue);">
  <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">{c[0]}</h4>
  <p style="font-size: 0.875rem; color: var(--color-body-text); margin: 0;">{c[1]}</p>
</div>""" for c in ind["challenges"]])

    wf_steps_html = "".join([f"""<div class="process-step reveal">
  <div class="process-num">{i+1}</div>
  <h4 class="process-title" style="font-size: 1rem;">{step[0]}</h4>
  <p class="process-desc">{step[1]}</p>
</div>""" for i, step in enumerate(ind["workflow_example"][1])])

    benefits_html = "".join([f"""<li style="margin-bottom: 0.75rem;"><strong>{b[0]}:</strong> {b[1]}</li>""" for b in ind["benefits"]])

    services_html = "".join([f"""<div class="card reveal">
  <h4 style="margin-bottom: 0.5rem;"><a href="{r[1]}">{r[0]}</a></h4>
  <p style="font-size: 0.85rem; color: var(--color-muted-text); margin-bottom: 1rem;">{r[2]}</p>
  <a href="{r[1]}" class="card-link">View Service &rarr;</a>
</div>""" for r in ind["relevant_services"]])

    body = f"""
    {breadcrumb_html}

    <section class="page-hero">
      <div class="container">
        <span class="section-tag tag-teal">{ind["hero_tag"]}</span>
        <h1>{ind["hero_h1"]}</h1>
        <p class="page-hero-desc">{ind["hero_desc"]}</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary btn-lg">Request a Consultation</a>
          <a href="industries.html" class="btn btn-outline-white btn-lg">All Industries</a>
        </div>
      </div>
    </section>

    <section class="section section-white">
      <div class="container">
        <div class="demo-callout" style="margin-bottom: 3rem;">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <div class="demo-callout-text">
            <h4>Regulatory &amp; Compliance Notice</h4>
            <p>{ind["disclaimer"]}</p>
          </div>
        </div>

        <div class="grid-2" style="align-items: center; gap: 4rem; margin-bottom: 4rem;">
          <div class="reveal">
            <span class="section-tag">Sector Context</span>
            <h2>Industry Operational Overview</h2>
            <div class="prose-content">
              {ind["overview"]}
            </div>
          </div>
          <div class="reveal reveal-delay-1">
            {render_placeholder(ind["placeholder_filename"], ind["placeholder_label"], "ratio-16-9", "1200 &times; 675")}
          </div>
        </div>

        <!-- Challenges -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">Sector Friction</span>
            <h2 class="section-title">Common Operational Challenges</h2>
            <p class="section-desc">Key operational vulnerabilities organizations in this vertical encounter as volumes scale.</p>
          </div>
          <div class="grid-2" style="gap: 1.5rem;">
            {challenges_html}
          </div>
        </div>

        <!-- Workflow Example -->
        <div style="margin-bottom: 4rem;">
          <div class="section-header reveal">
            <span class="section-tag">Workflow Blueprint</span>
            <h2 class="section-title">{ind["workflow_example"][0]}</h2>
            <p class="section-desc">An illustrative operational procedure demonstrating standard intake, processing, and resolution steps.</p>
          </div>
          <div class="process-grid" style="grid-template-columns: repeat({len(ind["workflow_example"][1])}, 1fr);">
            {wf_steps_html}
          </div>
        </div>

        <!-- Benefits & Data Security -->
        <div class="grid-2" style="gap: 3rem; margin-bottom: 4rem;">
          <div class="card reveal" style="padding: 2rem;">
            <h3 style="margin-bottom: 1rem;">Potential Business Benefits</h3>
            <ul style="color: var(--color-body-text); padding-left: 1.25rem; margin: 0;">
              {benefits_html}
            </ul>
          </div>
          <div class="card reveal reveal-delay-1" style="padding: 2rem; background: var(--color-light-bg);">
            <h3 style="margin-bottom: 1rem;">Data Handling &amp; Privacy Considerations</h3>
            <p style="font-size: 0.9rem; color: var(--color-body-text); margin-bottom: 1rem;">
              {ind["data_considerations"]}
            </p>
            <div style="font-size: 0.85rem; color: #64748B; border-top: 1px solid var(--color-border); padding-top: 0.75rem;">
              All operations strictly observe client-specified access authorizations and regulatory restrictions.
            </div>
          </div>
        </div>

        <!-- Relevant Services -->
        <div>
          <div class="section-header reveal">
            <span class="section-tag">Recommended Services</span>
            <h2 class="section-title">Relevant BPO Capabilities for this Sector</h2>
          </div>
          <div class="grid-3">
            {services_html}
          </div>
        </div>

      </div>
    </section>

    {render_cta_banner(f"Discuss Your {ind['hero_tag']} Requirements",
                       "Connect with our vertical solutions team to design an operational workflow calibrated to your industry.",
                       "Request a Consultation", "contact.html",
                       "Contact Us", "contact.html")}
    """

    return render_page(
        f"{ind['title']} — BPO Vertical Solutions",
        ind["meta_desc"],
        "industries",
        body,
        f"{ind['slug']}.html"
    )

def generate_all_industries():
    for ind in INDUSTRIES_DATA:
        html = render_industry_page(ind)
        filepath = f"{ind['slug']}.html"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated industry page: {filepath}")

if __name__ == "__main__":
    generate_all_industries()
