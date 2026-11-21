"""
Generator for IMAGE-GENERATION-GUIDE.md
Outputs all 53 Google Flow image generation prompts with complete parameters,
organized by section, ending with an inventory table and replacement guide.
"""

import sys

IMAGES_GUIDE_DATA = [
    # 1. Homepage images
    {
        "num": 1,
        "filename": "bpo-hero-operations.jpg",
        "page": "index.html",
        "section": "Hero Section",
        "desc": "A cutting-edge, high-tech customer support and operations floor inside an international BPO center. Multitasking customer service associates wearing sleek wireless headsets collaborating at ergonomic curved desks with multi-monitor displays showing analytics charts and communication interfaces.",
        "ratio": "16:9",
        "res": "1920 x 1080 px",
        "orient": "Landscape",
        "prompt": "Cinematic wide photography of a high-end corporate BPO contact center floor at twilight. Diverse professionals in business casual attire wearing modern thin wireless communication headsets, seated at ergonomic wood and steel workstations with curved dual monitors displaying clean data dashboards. High architectural glass ceilings, warm accent LED strip lighting along acoustic dividing panels in deep navy (#101D35) and corporate electric blue (#2864D8) highlights. Soft shallow depth of field, sharp focus on a focused professional smiling subtly while typing, professional corporate editorial aesthetic, photorealistic, 8k resolution, shot on Arri Alexa with Zeiss prime lens.",
        "comp": "Rule-of-thirds composition with a customer experience associate in the middle-ground slightly off-center right, leading lines of workstations receding into a soft blurred background.",
        "angle": "Eye-level with a slight Dutch angle (3 degrees) conveying dynamic forward momentum.",
        "light": "Mixed balanced lighting: cool 5500K daylight through frosted floor-to-ceiling windows balanced with warm 3200K interior overhead pendants and subtle teal-blue LED glow.",
        "bg": "Spacious, modern corporate headquarters interior with soft frosted acoustic glass partitions and vertical indoor greenery.",
        "style": "Contemporary corporate photojournalism, crisp clean textures, hyper-detailed skin and fabric surfaces, Stripe/Linear enterprise aesthetic.",
        "palette": "Primary deep navy (#101D35), corporate blue (#2864D8), soft white daylight, teal accents (#21B6A8).",
        "subject": "Focused professional associate in the foreground-midground wearing an executive headset, hands poised on keyboard.",
        "neg_space": "Subtle low-contrast negative space on the upper left third suitable for subtle UI overlay if needed."
    },
    {
        "num": 2,
        "filename": "bpo-business-flexibility.jpg",
        "page": "index.html",
        "section": "Why Consider Outsourcing Section",
        "desc": "Corporate executives and operational managers discussing flexible capacity scaling around a modern conference table with digital tablets and interactive glass monitors.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Medium shot of business professionals collaborating in a brightly lit glass-walled executive conference room. A team leader presenting workflow agility charts on a sleek digital whiteboard to attentive colleagues holding tablets and leather notebooks. Professional business attire, confident, collaborative expressions. Elegant modern architectural lines, diffuse natural morning light filling the room, polished concrete and warm timber accents. Photorealistic corporate lifestyle photography, shot on Sony A7R V with 50mm f/1.4 lens, natural skin tones, crisp details.",
        "comp": "Central group interaction with the presenter on the right third gesturing towards a digital display, colleagues engaged in dialogue.",
        "angle": "Slight low-angle shot establishing competence, executive authority, and open collaboration.",
        "light": "Diffused directional natural light from large windows on the left, subtle fill light minimizing harsh shadows.",
        "bg": "Frosted glass conference room looking out over a blurred high-rise city skyline.",
        "style": "Premium corporate lifestyle photography, authentic expressions, unposed natural collaboration.",
        "palette": "Navy blue, slate grey, warm wood tones, crisp white shirts, subtle corporate blue accents.",
        "subject": "Two managers and an executive reviewing operational workflow charts.",
        "neg_space": "Clean background space on the upper perimeter."
    },
    {
        "num": 3,
        "filename": "bpo-multichannel-support.jpg",
        "page": "index.html",
        "section": "Operational Capabilities Section",
        "desc": "Modern customer experience environment showcasing simultaneous multichannel support: voice headsets, live chat interfaces, and digital ticket queues.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Close-up cinematic shot of a professional customer experience associate's desk setup. Hands typing on an ergonomic mechanical keyboard while viewing a dual-monitor setup: one screen displaying an active real-time live chat queue, the other showing customer CRM history and ticket status. Beside the keyboard sits a modern wireless boom microphone headset and a ceramic coffee mug on a slate desk mat. Crisp macro focus on hands and keyboard, soft bokeh background with team members blurred in distance. Shot on Canon EOS R5 with 85mm f/1.8 lens, commercial advertising quality.",
        "comp": "Over-the-shoulder perspective focusing on the interaction between the associate's hands and the dual-screen interface.",
        "angle": "Over-the-shoulder, 45-degree downward angle focusing on the workspace tools.",
        "light": "Gentle monitor glow illuminating hands and desk surface, combined with ambient warm ceiling light.",
        "bg": "Blurred operations floor with soft hexagonal acoustic wall tiles and subtle blue ambient light.",
        "style": "Sleek SaaS enterprise photography, high-tech tactile realism, clean workspace design.",
        "palette": "Deep navy, cool screen blue (#4D8DFF), slate grey, matte black, clean white.",
        "subject": "Associate's hands engaging with multichannel software interface.",
        "neg_space": "Upper right corner contains soft blurred background."
    },
    {
        "num": 4,
        "filename": "bpo-career-opportunities.jpg",
        "page": "index.html",
        "section": "Careers Preview Section",
        "desc": "A vibrant, collaborative group of young professionals in a BPO training center, smiling and sharing insights during a professional development session.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Warm, authentic corporate group portrait of four diverse young customer support associates and their team coach standing together in a modern open-concept training lounge. They are laughing and smiling warmly at the camera, wearing professional business casual clothing with lanyards. In the background, ergonomic booths, modular whiteboard walls with colored sticky notes, and lush indoor planters. Bright, airy, welcoming workplace environment, inspiring career growth, shot on Hasselblad X2D with 55mm lens, natural daylight, vibrant yet tasteful color grading.",
        "comp": "Balanced group portrait positioned in the center, with depth created by tiered standing and sitting postures.",
        "angle": "Direct eye-level establishing an approachable, trustworthy, and welcoming peer connection.",
        "light": "Soft, flattering beauty lighting combined with ambient daylight, creating gentle catchlights in the eyes.",
        "bg": "Modern open-plan learning lounge with warm Scandinavian-inspired wood accents and glass partitions.",
        "style": "Warm recruitment editorial photography, genuine human connection, authentic workplace diversity.",
        "palette": "Teal (#21B6A8), corporate blue (#2864D8), warm beige, crisp white, soft charcoal.",
        "subject": "Four young professionals and a team mentor smiling confidently.",
        "neg_space": "Upper quarter has soft ceiling and ambient space."
    },

    # 2. About page images
    {
        "num": 5,
        "filename": "bpo-about-philosophy.jpg",
        "page": "about.html",
        "section": "Service Philosophy Section",
        "desc": "Senior operations architects and client success leads strategizing over a large architectural table with process maps and blueprint diagrams.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Cinematic medium-wide shot of two senior BPO operations consultants reviewing comprehensive process mapping diagrams spread across a minimalist white oak table. One consultant holds a digital pen pointing to a workflow diagram on a tablet, the other listens attentively with folded arms. Large glass architectural windows behind them overlooking an urban skyline. Clean corporate aesthetic, quiet confidence, meticulous attention to detail. 35mm filmic color palette, shot on Leica SL2 with Summilux 35mm lens.",
        "comp": "Two subjects interacting across the diagonal of the frame, blueprint document anchoring the lower foreground.",
        "angle": "Waist-level profile shot creating an intimate documentary feeling of serious strategic planning.",
        "light": "Soft side-window illumination carving out strong silhouettes and facial contours.",
        "bg": "Minimalist corporate boardroom with sheer window blinds and subtle architectural pillars.",
        "style": "Documentary corporate photography, restrained elegance, premium executive tone.",
        "palette": "Monochromatic neutrals with dark navy (#101D35) and cool steel accents.",
        "subject": "Two senior operations strategists in focused discussion.",
        "neg_space": "Top 30% of frame consists of clean window gradient."
    },
    {
        "num": 6,
        "filename": "bpo-operations-center.jpg",
        "page": "about.html",
        "section": "Operations Center Floor Section",
        "desc": "Wide panoramic perspective of a modern, bustling, organized business process operations center floor with clean lines and active workstations.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Elevated wide-angle architectural photograph of a premier BPO operations facility floor. Neat rows of modular curved desks with dual-monitor computer stations, acoustic privacy panels in slate and corporate navy, ergonomic mesh chairs. Professional associates working productively. Suspended linear acoustic baffles and LED light fixtures overhead, polished anti-static flooring reflecting subtle blue tones. High ceilings, immaculate organization, state-of-the-art enterprise operations environment. Shot on Fujifilm GFX 100 II with 23mm ultra-wide lens, architectural precision, straight vertical lines.",
        "comp": "Symmetrical one-point perspective looking down the main central corridor between workstation pods.",
        "angle": "Slightly elevated view (8 feet high) looking across the entire breadth of the operational floor.",
        "light": "Uniform, glare-free indirect 4000K commercial lighting supplemented by subtle LED architectural accents.",
        "bg": "Full perspective of the operational facility stretching into the background.",
        "style": "Architectural interior photography, ultra-crisp geometric lines, immaculate corporate order.",
        "palette": "Corporate navy blue, cool grey, white, subtle teal status indicators.",
        "subject": "Entire organized contact center operations floor.",
        "neg_space": "Ceiling grid provides clean upper negative space."
    },

    # 3. Services overview
    {
        "num": 7,
        "filename": "bpo-services-overview.jpg",
        "page": "services.html",
        "section": "Services Ecosystem Banner",
        "desc": "Abstract technological and human interaction montage representing customer support, back-office data processing, and digital operations.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Ultra-wide cinematic concept banner representing the convergence of human expertise and digital operational efficiency in BPO. In the center, a focused support specialist in profile with an executive headset, overlaid with subtle translucent glowing geometric nodes, data streams, and communication vectors. Deep corporate navy blue (#101D35) background with electric blue (#2864D8) and teal (#21B6A8) light trails. Sophisticated enterprise technology aesthetic, no distracting neon, subtle abstract depth, photorealistic, 8k, shot on RED V-Raptor.",
        "comp": "Panoramic banner with subject placed slightly left of center, allowing glowing data geometry to sweep across the right width.",
        "angle": "Direct horizontal panoramic composition.",
        "light": "Dark ambient environment punctuated by crisp fiber-optic blue highlights and soft facial rim light.",
        "bg": "Deep navy abstract digital network canvas with subtle depth-of-field particles.",
        "style": "Modern enterprise hero visual, sophisticated blend of realism and digital vectors.",
        "palette": "Midnight navy (#0B132B), sapphire blue (#2864D8), cyan/teal (#21B6A8), clean white highlights.",
        "subject": "Professional associate profile integrated with abstract data flows.",
        "neg_space": "Extensive clean negative space across the upper and right zones for banner headers."
    },

    # 4. 17 BPO Service pages
    {
        "num": 8,
        "filename": "bpo-customer-support-team.jpg",
        "page": "customer-support.html",
        "section": "Customer Support Operations Desk",
        "desc": "Customer support associates wearing headsets actively resolving customer queries with friendly, empathetic facial expressions.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Medium close-up of a professional female customer support specialist wearing a slim modern headset, speaking empathetically while looking at her monitor. Beside her, a supportive team lead leans in to provide quick guidance with a nod. High-tech clean workstation, dual screens displaying customer ticket timelines. Professional office background with warm lighting, genuine smile, polished business casual attire. Shot on Canon 5D Mark IV, 85mm f/2.0, natural color balance.",
        "comp": "Subject in the left two-thirds, colleague entering from the right, establishing a supportive coaching culture.",
        "angle": "Eye-level intimate commercial portrait.",
        "light": "Soft diffused key light from a softbox, gentle rim light separating hair from background.",
        "bg": "Contemporary customer care floor with soft-focus colleagues in the distance.",
        "style": "Heartfelt corporate customer experience photography, approachable, warm, highly competent.",
        "palette": "Navy, slate, soft warm cream, sky blue.",
        "subject": "Customer care representative and team supervisor.",
        "neg_space": "Right upper third offers soft blur."
    },
    {
        "num": 9,
        "filename": "bpo-inbound-contact-center.jpg",
        "page": "inbound-call-center.html",
        "section": "Inbound Call Center Floor",
        "desc": "High-volume inbound telephony floor with telephone agents answering incoming customer calls and checking CRM records.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Dynamic medium-shot of an energetic inbound call center floor. Multiple focused customer service agents at acoustic sound-dampened workstations with dual monitors and telephone dialer consoles. An agent in the foreground wears a professional noise-canceling headset, actively engaged in a call with a poised, confident posture. Digital wallboard in the background displaying queue metrics with green SLA indicators. Crisp corporate realism, shot on Sony FX6, 35mm lens.",
        "comp": "Foreground associate sharp on the left third, leading lines of desks drawing the eye into the bustling room.",
        "angle": "Slight low-angle shot adding energy and operational stature.",
        "light": "Bright, energizing commercial office lighting with balanced color temperature.",
        "bg": "Active contact center floor with acoustic wall panels and digital queue monitors.",
        "style": "Energetic enterprise operations photojournalism.",
        "palette": "Corporate blue (#2864D8), charcoal grey, bright white, green status accents.",
        "subject": "Inbound telephone associate handling an active call.",
        "neg_space": "Upper right corner above workstations."
    },
    {
        "num": 10,
        "filename": "bpo-outbound-calling.jpg",
        "page": "outbound-call-center.html",
        "section": "Outbound Operations Workstations",
        "desc": "Professional outbound representatives conducting verified customer follow-ups and survey interviews from clean workstations.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Professional male customer representative at a clean modern desk wearing a single-ear telephony headset, reviewing a verified customer follow-up schedule on a vertical monitor while speaking politely. On his desk sits a clean notepad with neat notes and a stylus pen. Quiet, focused, respectful atmosphere. Photorealistic corporate imagery, shot on Nikon Z9 with 70mm f/2.8 lens, natural corporate lighting.",
        "comp": "Subject positioned cleanly in the center-left, with desk elements grounding the lower edge.",
        "angle": "Straight eye-level profile-three-quarter view.",
        "light": "Balanced daylight and soft interior fill.",
        "bg": "Acoustic fabric partition wall in dark navy texture with subtle company logo plaque.",
        "style": "Polished corporate communications photography.",
        "palette": "Navy blue, crisp white shirt, graphite grey desk, warm wood trim.",
        "subject": "Outbound associate conducting a verified follow-up call.",
        "neg_space": "Top and right sections clean."
    },
    {
        "num": 11,
        "filename": "bpo-technical-support.jpg",
        "page": "technical-support.html",
        "section": "Technical Support Diagnostics Desk",
        "desc": "Technical support specialist analyzing system error logs and hardware diagnostics across multiple vertical monitors.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Analytical technical support specialist troubleshooting an issue across triple monitors displaying server logs, diagnostic graphs, and an active customer ticket console. He wears glasses reflecting soft screen light, one hand on a precision mouse and the other holding an ear of his headset. High-tech diagnostic lab setting, cable management perfectly concealed, clean industrial desk. 8k resolution, shot on Arri Alexa Mini with Master Prime 50mm.",
        "comp": "Subject framed between the monitors, creating a command-center diagnostic atmosphere.",
        "angle": "Slight side angle capturing both the technician's focused expression and the complex screen interfaces.",
        "light": "Subtle low-key ambient lighting with primary illumination radiating from the high-resolution displays.",
        "bg": "Technical diagnostic bay with server rack glass in the background with subtle blue LEDs.",
        "style": "High-tech enterprise technical photography, analytical, methodical, authoritative.",
        "palette": "Midnight navy, electric blue screen glow, slate black, silver metallic.",
        "subject": "Technical helpdesk specialist diagnosing complex software logs.",
        "neg_space": "Left upper corner behind monitors."
    },
    {
        "num": 12,
        "filename": "bpo-email-support-desk.jpg",
        "page": "email-support.html",
        "section": "Email Support Operations Desk",
        "desc": "Written support specialist meticulously crafting a detailed response email on a modern keyboard with reference manuals nearby.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Close-up perspective of a written communication associate's hands typing swiftly on a sleek low-profile keyboard. The monitor in front shows a well-structured customer email response with clean bullet points and an attached PDF document icon. A warm cup of tea sits neatly on a cork coaster next to a small desktop succulent. Calm, disciplined, detail-oriented work atmosphere. Shot on Sony A1 with 50mm f/1.8 lens, soft focus background.",
        "comp": "Focus on the hands and keyboard in the lower foreground, with the email drafting screen readable yet stylized in the midground.",
        "angle": "45-degree desk level shot.",
        "light": "Soft natural window light washing from the side.",
        "bg": "Modern corporate office window overlooking trees in soft morning light.",
        "style": "Calm, thoughtful editorial productivity photography.",
        "palette": "Warm grey, cream, forest green plant, clean white, navy blue.",
        "subject": "Hands composing a structured customer resolution email.",
        "neg_space": "Upper right background."
    },
    {
        "num": 13,
        "filename": "bpo-chat-support-interface.jpg",
        "page": "chat-support.html",
        "section": "Live Chat Support Interface",
        "desc": "Real-time chat support associate managing multi-concurrency customer messaging conversations on a widescreen monitor.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Medium shot of a young digital-native customer service associate smiling as she types rapidly into an omnichannel live chat console. Her wide curved monitor shows three synchronized chat panels with colorful customer avatar bubbles and prompt response timers. She wears wireless earbuds, focused and cheerful. Fast-paced, modern digital customer experience environment, shot on Canon R6 II with 35mm lens.",
        "comp": "Associate on the right third looking towards the wide curved monitor spanning across the left two-thirds.",
        "angle": "Profile angle emphasizing speed, agility, and modern messaging tech.",
        "light": "Bright, modern daylight with subtle cyan monitor edge glow.",
        "bg": "Trendy, well-lit tech operations space with acoustic felt dividers.",
        "style": "Contemporary digital-first corporate lifestyle photography.",
        "palette": "Teal (#21B6A8), bright corporate blue (#4D8DFF), light grey, white.",
        "subject": "Live chat associate actively messaging customers.",
        "neg_space": "Upper center above the curved monitor."
    },
    {
        "num": 14,
        "filename": "bpo-back-office-processing.jpg",
        "page": "back-office.html",
        "section": "Back Office Operations Floor",
        "desc": "Organized back-office operational team processing digital records, purchase orders, and enterprise documentation.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Wide shot of a professional back-office administrative operations team working in perfect synchronization. Rows of dual-monitor workstations where associates cross-reference invoices, spreadsheets, and database entries. In the foreground, an operational supervisor reviews batch completion metrics on a tablet with an analyst. High efficiency, immaculate clean-desk policy, professional demeanor. Shot on Leica SL2 with 28mm lens.",
        "comp": "Two analysts discussing records in the foreground right, leading into the wide expanse of processing desks.",
        "angle": "Standing eye-level establishing scope and scale.",
        "light": "Even, glare-free architectural commercial lighting.",
        "bg": "Corporate administrative operations floor with organized cable management and branded wall accents.",
        "style": "Corporate operational documentary photography, precision, reliability, scale.",
        "palette": "Deep navy, cool steel, white, dark wood accents.",
        "subject": "Back office analysts executing transactional workflows.",
        "neg_space": "Upper left ceiling and wall area."
    },
    {
        "num": 15,
        "filename": "bpo-data-entry-operations.jpg",
        "page": "data-entry.html",
        "section": "Data Processing & Validation Station",
        "desc": "High-accuracy data entry operator comparing scanned documents on one screen against a database entry form on the adjacent monitor.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Close-up perspective of a data entry specialist's dual-screen workstation. Left screen displays an indexed scanned PDF form with highlighted data fields; right screen displays an enterprise database form where the verified numbers are entered. Mechanical tenkey number pad positioned beside the keyboard. Intense focus on speed and zero-error verification. Macro lens detail, shot on Nikon Z7 II with 105mm Micro lens.",
        "comp": "Split focus between the dual screens and the associate's rapid keying hand in the lower right.",
        "angle": "Over-the-shoulder looking directly into the dual-screen comparison.",
        "light": "Cool screen illumination highlighting the exact field alignment.",
        "bg": "Subtle darkened acoustic office interior.",
        "style": "High-precision technical execution photography.",
        "palette": "Navy, data green checkmarks, clean white, slate.",
        "subject": "Dual-monitor validation of scanned data records.",
        "neg_space": "Top edge of the frame."
    },
    {
        "num": 16,
        "filename": "bpo-finance-accounting.jpg",
        "page": "finance-accounting.html",
        "section": "Finance Operations Review Desk",
        "desc": "Finance operational associates conducting 3-way matching of purchase orders, receiving slips, and vendor invoices.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Medium shot of an accounting operations specialist reviewing general ledger entries and invoice reconciliations on dual screens. A clean desk with a digital financial calculator, organized digital stylus, and an encrypted token access key. Associate exhibits deep concentration, pointing with a pen at a line item on the screen. Professional, trustworthy corporate finance setting. Shot on Sony A7R V with 50mm f/1.4 lens.",
        "comp": "Associate centered, framed by screens on either side, conveying meticulous financial governance.",
        "angle": "Eye-level medium shot.",
        "light": "Warm, reassuring corporate lighting with soft window accents.",
        "bg": "Modern financial operations department with glass-walled conference rooms behind.",
        "style": "Trust-building corporate finance photography, rigorous, disciplined, confidential.",
        "palette": "Navy blue, slate grey, warm wood, crisp white.",
        "subject": "Financial analyst performing invoice reconciliation.",
        "neg_space": "Upper third."
    },
    {
        "num": 17,
        "filename": "bpo-order-fulfillment-workflow.jpg",
        "page": "order-processing.html",
        "section": "Order Processing & Fulfillment Center",
        "desc": "E-commerce order fulfillment management desk tracking international parcel deliveries, carrier statuses, and merchant inventory.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Operations specialist monitoring an interactive global logistics map on a large wall display while verifying e-commerce order batches on his workstation monitor. Digital shipping label icons, barcode validation prompts, and carrier tracking status indicators visible on the interfaces. High-energy, modern fulfillment control center environment, shot on Panasonic Lumix S5 II with 24-70mm lens.",
        "comp": "Associate seated in foreground left, gesturing toward the global fulfillment display stretching across the background.",
        "angle": "Wide medium-shot capturing both human operator and digital logistics visualization.",
        "light": "Balanced ambient with glowing blue and amber route lines on the digital map.",
        "bg": "Logistics operations control room with multiple status displays.",
        "style": "High-velocity modern commerce operations photography.",
        "palette": "Navy, courier orange/amber highlights, bright blue, charcoal.",
        "subject": "Fulfillment coordinator verifying order dispatch batches.",
        "neg_space": "Upper right corner."
    },
    {
        "num": 18,
        "filename": "bpo-document-digitization.jpg",
        "page": "document-management.html",
        "section": "Document Digitization & Indexing Lab",
        "desc": "High-volume document scanner station with an operator verifying optical character recognition (OCR) indexing accuracy on screen.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "State-of-the-art document digitization suite. An operator feeding high-speed commercial document scanners, while an analyst on the adjacent screen verifies automated OCR text extraction and applies metadata tags. Clean industrial environment, archival boxes neatly stacked in the background, precision lighting. Shot on Canon EOS R5 with 35mm f/1.4 lens.",
        "comp": "Two workstations showing the journey from physical paper scanning to digital database indexing.",
        "angle": "Slight diagonal angle connecting scanner hardware to digital indexing screen.",
        "light": "Clean, crisp 5000K neutral light ensuring archival clarity.",
        "bg": "Secure document archiving laboratory with organized shelving.",
        "style": "Industrial archival precision photography.",
        "palette": "Steel grey, navy, white paper, soft beige archival boxes.",
        "subject": "Document digitization specialists at scanning station.",
        "neg_space": "Upper center."
    },
    {
        "num": 19,
        "filename": "bpo-content-moderation.jpg",
        "page": "content-moderation.html",
        "section": "Content Review & Policy Enforcement Desk",
        "desc": "A content moderation analyst reviewing community guidelines on a clean monitor in a calm, supportive workspace designed for mental wellness.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Thoughtful, calm scene of a content moderation analyst reviewing policy classification trees on a high-resolution display. Her workstation is thoughtfully designed with ergonomic arm rests, a soft ambient warm light lamp, and an acoustic sound-masking divider. Natural daylight streams through a window beside her desk. Supportive, peaceful, highly professional workplace emphasizing analyst wellness and policy discipline. Shot on Fujifilm GFX 50S II with 45mm lens.",
        "comp": "Analyst in the center with calming window light from the left, monitor displaying blurred policy text on the right.",
        "angle": "Side profile view conveying thoughtful discernment and calm focus.",
        "light": "Warm, gentle natural daylight; soft ambient lamp glow minimizing eye strain.",
        "bg": "Calming office nook with warm timber acoustic slats and green potted plants.",
        "style": "Empathetic, serene workplace photography with dignity and calm restraint.",
        "palette": "Warm timber, sage green, soft navy, warm white.",
        "subject": "Content moderation analyst evaluating community guidelines.",
        "neg_space": "Upper left above window."
    },
    {
        "num": 20,
        "filename": "bpo-lead-qualification.jpg",
        "page": "lead-generation.html",
        "section": "Lead Research & Qualification Center",
        "desc": "B2B sales research associate verifying business decision-maker directories and updating CRM company records.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Focused sales research associate analyzing B2B company directories and org charts on an ultra-wide monitor. Green checkmarks highlight verified executive email addresses and direct telephone extensions. She smiles as she updates a clean CRM pipeline interface. Modern high-energy sales enablement hub with motivational whiteboard quotes blurred behind. Shot on Sony A7 IV with 85mm f/1.8 lens.",
        "comp": "Subject in the right half, leaning slightly toward the screen with active engagement.",
        "angle": "Eye-level medium shot.",
        "light": "Bright, uplifting commercial lighting with golden hour window reflections.",
        "bg": "Modern open-plan sales and lead generation office.",
        "style": "Energetic, success-oriented corporate sales photography.",
        "palette": "Navy, electric blue (#2864D8), emerald green accents, white.",
        "subject": "Sales research specialist enriching CRM lead records.",
        "neg_space": "Top left quarter."
    },
    {
        "num": 21,
        "filename": "bpo-virtual-executive-assistant.jpg",
        "page": "virtual-assistance.html",
        "section": "Virtual Executive Assistant Workspace",
        "desc": "Executive virtual assistant managing international calendar time zones, flight bookings, and executive meeting schedules.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Sophisticated virtual executive assistant seated at a minimalist desk with an Apple-style aluminum laptop, an iPad displaying a color-coded calendar across multiple time zones, and a sleek wireless headset. She takes neat notes with a fountain pen in a black leather planner. Polished, composed, proactive demeanor. Elegant home office or executive suite background with minimalist shelving and soft architectural shadows. Shot on Hasselblad X1D II 50C with 45mm lens.",
        "comp": "Central three-quarter portrait of the assistant, desk tools neatly organized in front.",
        "angle": "Slightly elevated eye-level, intimate and poised.",
        "light": "Soft North-facing window light creating velvety, elegant tones.",
        "bg": "Contemporary executive study with books and subtle modern sculpture.",
        "style": "High-end executive lifestyle photography, discreet, capable, organized.",
        "palette": "Black, white, warm cream, navy, subtle gold accents.",
        "subject": "Virtual assistant coordinating executive calendars and travel.",
        "neg_space": "Top 25% of frame."
    },
    {
        "num": 22,
        "filename": "bpo-hr-administration.jpg",
        "page": "human-resources-outsourcing.html",
        "section": "HR Operations & People Support Desk",
        "desc": "HR coordinator conducting candidate onboarding verification and reviewing employment eligibility documentation.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Warm, welcoming HR operations associate reviewing digital onboarding packets and candidate resumes on an all-in-one desktop computer. Beside her monitor, an organized folder labeled 'New Hire Intake' rests on the desk. She has an inviting smile, wearing a professional collared shirt. Clean, welcoming people-operations department with bright modern design. Shot on Canon EOS R6 with 50mm f/1.4 lens.",
        "comp": "Subject framed slightly left of center, turning slightly toward the camera with an open, friendly posture.",
        "angle": "Straight eye-level friendly corporate portrait.",
        "light": "Bright, even corporate softbox lighting.",
        "bg": "Modern human resources office with pastel acoustic wall panels and glass doors.",
        "style": "Approachable, professional people-operations photography.",
        "palette": "Teal (#21B6A8), navy, warm coral, crisp white.",
        "subject": "HR coordinator reviewing onboarding verification documents.",
        "neg_space": "Upper right corner."
    },
    {
        "num": 23,
        "filename": "bpo-healthcare-administrative-support.jpg",
        "page": "healthcare-process-outsourcing.html",
        "section": "Healthcare Administrative Operations Center",
        "desc": "Non-clinical healthcare administrative associate scheduling patient clinical appointments in an Electronic Health Record (EHR) interface.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Non-clinical medical scheduling associate seated at a sanitized, professional healthcare administrative station. She wears a clean headset, speaking gently and taking appointment notes on an Electronic Health Record scheduling grid. On the wall behind her hangs a medical clinic organizational chart and hospital corridor blurred in the distance. Calm, compassionate, sterile, and professional healthcare operations environment. Shot on Nikon Z8 with 85mm f/1.8 lens.",
        "comp": "Associate in profile-three-quarters, headset microphone near mouth, screen interface displaying patient schedule blocks.",
        "angle": "Eye-level medium shot.",
        "light": "Soft daylight-balanced clean clinical lighting.",
        "bg": "Modern medical administration suite with clean glass partitions.",
        "style": "Compassionate, clinical-grade administrative photography.",
        "palette": "Medical cyan/teal (#21B6A8), clean hospital white, soft grey, navy.",
        "subject": "Non-clinical scheduler managing patient appointment calendar.",
        "neg_space": "Upper right above cubicle partition."
    },
    {
        "num": 24,
        "filename": "bpo-kpo-research-analysis.jpg",
        "page": "knowledge-process-outsourcing.html",
        "section": "KPO Research & Analytics Lab",
        "desc": "Knowledge process analyst synthesizing market intelligence reports, competitor financial matrices, and executive presentation charts.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Senior research analyst working in an analytical intelligence lab. He sits before multiple 4K displays showcasing financial regression models, competitor market share graphs, and executive summary slide decks. On his desk are analytical whitepapers and an annotated tablet. Intellectual, rigorous, executive-level research setting. Shot on Sony A1 with 50mm f/1.2 lens, shallow depth of field, razor-sharp focus on the analyst's analytical expression.",
        "comp": "Subject in the right-center, surrounded by complex quantitative data visualizations.",
        "angle": "Slight low-angle shot establishing intellectual authority.",
        "light": "Sophisticated ambient corporate lighting with subtle blue highlights from the data charts.",
        "bg": "Research library setting with glass boards showing handwritten quantitative formulas.",
        "style": "High-end corporate research and analytics photography.",
        "palette": "Navy (#101D35), corporate blue (#2864D8), gold chart accents, charcoal.",
        "subject": "KPO analyst synthesizing executive market intelligence.",
        "neg_space": "Top left quarter of frame."
    },

    # 5. Industry images (9)
    {
        "num": 25,
        "filename": "bpo-industries-banner.jpg",
        "page": "industries.html",
        "section": "Enterprise Vertical Operations Banner",
        "desc": "A dynamic multi-sector concept visual representing healthcare, banking, e-commerce, software, and transportation logistics in a unified corporate mosaic.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic architectural and industry concept visual. A seamless composite showing the glass facades of modern financial towers, a medical research facility, automated e-commerce distribution center, and global freight transportation routes. Sleek corporate design, subtle blue and teal connecting light lines symbolizing integrated business process management. Ultra-wide 21:9 ratio, photorealistic, 8k, shot on Hasselblad H6D-100c.",
        "comp": "Wide horizontal panorama with balanced visual weighting across healthcare, banking, technology, and logistics motifs.",
        "angle": "Elevated panoramic cityscape angle.",
        "light": "Dawn horizon light blending with corporate architectural interior glow.",
        "bg": "Panoramic cityscape merging vertical industry infrastructure.",
        "style": "High-concept enterprise overview photography, prestigious, expansive, corporate.",
        "palette": "Navy (#101D35), sapphire (#2864D8), sunrise gold, slate grey, white.",
        "subject": "Integrated vertical industry sectors.",
        "neg_space": "Skyline upper section provides ample clean negative space."
    },
    {
        "num": 26,
        "filename": "bpo-industry-healthcare.jpg",
        "page": "healthcare-industry.html",
        "section": "Healthcare Sector Context",
        "desc": "Modern medical center reception and administrative wing with non-clinical staff managing patient check-in records.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Bright, immaculate modern healthcare clinic reception and administration center. Non-clinical administrative coordinators in smart attire reviewing appointment schedules at a curved white Corian reception counter with discrete computer monitors. Patients seated in comfortable waiting lounge chairs in the soft-focus background. Ample natural sunlight, indoor ficus trees, reassuring and professional medical environment. Shot on Canon EOS R5 with 24mm f/2.8 lens.",
        "comp": "Curved reception desk leading the viewer's eye from the foreground into the serene clinic space.",
        "angle": "Eye-level wide shot.",
        "light": "Abundant soft natural daylight supplemented by clean 4000K clinical ceiling recessed lights.",
        "bg": "Modern hospital outpatient atrium with architectural glass walls.",
        "style": "Serene, reassuring healthcare architectural photography.",
        "palette": "Clean white, hospital teal (#21B6A8), warm blonde wood, soft slate.",
        "subject": "Healthcare administrative coordination desk.",
        "neg_space": "Top 25% of the frame."
    },
    {
        "num": 27,
        "filename": "bpo-industry-banking-finance.jpg",
        "page": "banking-finance.html",
        "section": "Banking Sector Context",
        "desc": "Commercial banking operations center with financial analysts reconciling transactions and auditing compliance records.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Commercial banking back-office floor in an international financial center. Analysts in tailored business attire reviewing transaction ledgers, digital audit logs, and account documentation on secure dual-screen terminals. Prestigious corporate boardroom visible through glass partitions. High security, disciplined operational protocol, prestigious banking atmosphere. Shot on Leica SL2 with 50mm f/1.4 lens.",
        "comp": "Foreground analyst reviewing a ledger, leading into rows of secure banking operations stations.",
        "angle": "Slight low-angle shot conveying security, authority, and financial precision.",
        "light": "Refined executive interior lighting with cool screen contrast.",
        "bg": "Financial district skyscrapers visible through executive windows.",
        "style": "Prestigious financial corporate photography, discreet, disciplined, premium.",
        "palette": "Deep navy blue (#101D35), polished marble grey, bronze accents, crisp white.",
        "subject": "Banking operations analysts auditing transactional records.",
        "neg_space": "Upper third."
    },
    {
        "num": 28,
        "filename": "bpo-industry-ecommerce-retail.jpg",
        "page": "ecommerce-industry.html",
        "section": "E-Commerce Sector Context",
        "desc": "Modern e-commerce customer support team managing high-volume holiday sales orders and live chat queues.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Vibrant, fast-paced e-commerce support operations hub. Associates wearing headsets simultaneously interacting with online shoppers on live chat while checking order fulfillment and courier tracking maps. Festive or seasonal product samples neatly displayed on background shelves. High energy, friendly collaboration, modern retail customer experience. Shot on Sony FX3 with 35mm f/1.4 lens.",
        "comp": "Two support specialists in the foreground sharing an order update, bustling e-commerce team behind.",
        "angle": "Eye-level medium shot.",
        "light": "Warm, energetic retail lighting with vibrant ambient colors.",
        "bg": "Modern e-commerce headquarters with exposed brick and modern industrial fixtures.",
        "style": "Dynamic digital commerce photography, youthful, agile, customer-centric.",
        "palette": "Electric blue (#2864D8), retail coral, crisp white, charcoal.",
        "subject": "E-commerce customer service team managing order inquiries.",
        "neg_space": "Top left."
    },
    {
        "num": 29,
        "filename": "bpo-industry-tech-software.jpg",
        "page": "technology-industry.html",
        "section": "Technology Sector Context",
        "desc": "Software company customer support floor with engineers and helpdesk specialists collaborating on bug triage.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "SaaS technology company support floor. Technical helpdesk associates and QA specialists working together around a standing height collaborative desk with laptops, code editors, and mobile testing devices. One associate writes user flow steps on a glass partition with a dry-erase marker. Modern tech startup campus aesthetic, casual clothing, deep technical focus. Shot on Canon R5 with 35mm f/1.8 lens.",
        "comp": "Group centered around the glass whiteboard with focus on the collaborative problem-solving interaction.",
        "angle": "Eye-level candid documentary shot.",
        "light": "Bright Scandinavian office daylight with warm interior accents.",
        "bg": "Silicon-valley style tech campus with open-plan timber rafters.",
        "style": "Modern agile tech photography, collaborative, innovative, technical.",
        "palette": "Navy, bright tech blue (#4D8DFF), light birch wood, white.",
        "subject": "Technical helpdesk team triaging software bug reports.",
        "neg_space": "Upper right quarter."
    },
    {
        "num": 30,
        "filename": "bpo-industry-telecom.jpg",
        "page": "telecommunications-industry.html",
        "section": "Telecom Sector Context",
        "desc": "Telecommunications operations center with network status monitors and customer care representatives answering subscriber queries.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Telecommunications customer operations floor. In the background, a large digital video wall displays real-time cellular network traffic and broadband tower status grids. In the foreground, focused customer service agents with headsets answer subscriber calls regarding plan upgrades, broadband activations, and billing. High-tech, mission-critical operations center atmosphere. Shot on Nikon Z9 with 24-70mm lens.",
        "comp": "Foreground operators framed against the massive glowing telecom network status wall in the background.",
        "angle": "Slight low angle emphasizing scale and operational importance.",
        "light": "Blue ambient glow from the video wall balanced with neutral task lighting on desks.",
        "bg": "Massive telecommunications command center video wall.",
        "style": "Mission-critical infrastructure photography, authoritative, grand, high-tech.",
        "palette": "Midnight navy, electric telecom blue (#2864D8), cyan, white.",
        "subject": "Telecom customer support agents on network floor.",
        "neg_space": "Top third."
    },
    {
        "num": 31,
        "filename": "bpo-industry-travel-hospitality.jpg",
        "page": "travel-hospitality.html",
        "section": "Travel Sector Context",
        "desc": "24/7 global travel concierge and customer care desk assisting passengers with flight itineraries and hotel bookings.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "24/7 travel concierge and airline customer care center at nighttime. A poised customer support specialist with a headset examines global airline route maps and hotel booking databases on her monitor. Outside the expansive window, an airport runway or night city skyline twinkles with airplane lights. Calm, reassuring, premium luxury travel customer care. Shot on Sony A7S III with 50mm f/1.4 lens, cinematic night aesthetic.",
        "comp": "Specialist in the right foreground, city and runway lights glistening in the deep blue night window behind her.",
        "angle": "Eye-level cinematic portrait.",
        "light": "Warm interior lamp and cool blue moonlight from the window.",
        "bg": "Night skyline overlooking illuminated airport runways.",
        "style": "Cinematic 24/7 global travel photography, luxurious, reassuring, round-the-clock.",
        "palette": "Deep twilight navy (#0B132B), warm gold runway lights, steel blue, white.",
        "subject": "Travel support concierge assisting travelers at night.",
        "neg_space": "Left upper third."
    },
    {
        "num": 32,
        "filename": "bpo-industry-insurance.jpg",
        "page": "insurance-industry.html",
        "section": "Insurance Sector Context",
        "desc": "Insurance claims intake desk with associates documenting First Notice of Loss (FNOL) and indexing damage documentation.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Insurance claims intake and adjudication operations floor. An empathetic female claims specialist wearing a headset listens intently to a policyholder while inputting damage details into an insurance claims management platform. Her desk holds digital policy manuals and an indexed claim checklist. Behind her, a quiet, orderly insurance operations department. Reassuring, stable, methodical atmosphere. Shot on Canon 5D Mark IV with 85mm f/1.8 lens.",
        "comp": "Medium shot of the claims specialist, hands on keyboard, face expressing sincere empathy.",
        "angle": "Eye-level personal portrait.",
        "light": "Soft, comforting, warm corporate lighting.",
        "bg": "Orderly insurance office with framed institutional artwork and glass dividers.",
        "style": "Trustworthy, compassionate corporate insurance photography.",
        "palette": "Navy (#101D35), slate blue, warm oak, cream.",
        "subject": "Insurance intake associate recording a First Notice of Loss.",
        "neg_space": "Top left."
    },
    {
        "num": 33,
        "filename": "bpo-industry-logistics-transport.jpg",
        "page": "logistics-industry.html",
        "section": "Logistics Sector Context",
        "desc": "Freight forwarding and logistics coordination desk tracking container cargo, transport bills of lading, and delivery schedules.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Freight logistics and transport operations hub. Analysts tracking international cargo shipments, intermodal freight routes, and delivery exception alerts across multiple monitors. Through large glass windows, a modern intermodal logistics terminal with container cranes and transport trucks is visible in soft morning fog. High-stakes supply chain coordination, disciplined execution. Shot on Hasselblad X2D with 38mm lens.",
        "comp": "Coordinator in the foreground pointing to a shipping exception on screen, logistics yard visible outside.",
        "angle": "Wide three-quarter shot.",
        "light": "Cool morning daylight combined with sharp screen glow.",
        "bg": "Modern port or intermodal freight terminal visible through floor-to-ceiling glass.",
        "style": "Industrial global trade and supply chain photography, powerful, structured, essential.",
        "palette": "Navy, shipping container colors (deep red, blue), industrial steel grey, white.",
        "subject": "Freight operations coordinator tracking delivery exceptions.",
        "neg_space": "Upper right corner."
    },

    # 6. Technology and Operations images (7)
    {
        "num": 34,
        "filename": "bpo-process-lifecycle.jpg",
        "page": "process.html",
        "section": "Operating Process Lifecycle Model Banner",
        "desc": "Visual architectural representation of the five-stage BPO operational lifecycle: Discovery, Scope, Planning, Transition, and Continuous Improvement.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic abstract corporate concept visual illustrating a structured 5-stage operational transition lifecycle. Five glowing, interconnected geometric glass stages aligned linearly over a deep navy architectural blueprint grid. Clean enterprise technology lines, subtle blue (#2864D8) and teal (#21B6A8) gradient streams flowing smoothly from left to right, representing seamless transition and continuous improvement. Highly polished, minimalist, corporate executive presentation aesthetic, 8k, photorealistic.",
        "comp": "Panoramic flow moving from left (Discovery) to right (Improvement) across the wide banner.",
        "angle": "Slight perspective isometric angle over a blueprint grid.",
        "light": "Luminescent edge lighting highlighting the sequential geometric stages.",
        "bg": "Dark navy (#101D35) grid canvas with subtle optical depth.",
        "style": "Minimalist enterprise 3D architectural illustration, clean, precise, non-cluttered.",
        "palette": "Deep navy, corporate blue (#2864D8), teal accent (#21B6A8), pure white.",
        "subject": "Five-stage operational transition lifecycle geometry.",
        "neg_space": "Top half completely clear for page titles and typography."
    },
    {
        "num": 35,
        "filename": "bpo-technology-dashboard.jpg",
        "page": "technology.html",
        "section": "System Architecture Banner",
        "desc": "Futuristic yet clean enterprise technology command center overview showing CRM integration, cloud telephony, and real-time operational analytics.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Wide panoramic visualization of modern enterprise contact center technology architecture. In an executive operations command center, large high-definition curved glass displays float with clean, beautifully formatted CRM analytics, telephony queue distributions, and ticket resolution graphs. Modern engineers in silhouette review the metrics. Crisp typography, no fictional brand logos, sleek dark mode UI with corporate blue and teal highlights. Shot on Arri Alexa, cinematic commercial style.",
        "comp": "Panoramic perspective with digital dashboard displays spanning horizontally across the midground.",
        "angle": "Wide horizontal perspective.",
        "light": "Refined dark-room command center aesthetic with vibrant screen luminescence.",
        "bg": "Dark corporate command center with acoustic glass partitions.",
        "style": "High-end enterprise technology visualization, sleek, sophisticated, Stripe-like UI minimalism.",
        "palette": "Dark navy (#0D172A), bright blue (#4D8DFF), teal (#21B6A8), clean white data lines.",
        "subject": "Enterprise contact center data architecture consoles.",
        "neg_space": "Upper and lower horizontal bands provide ample negative space."
    },
    {
        "num": 36,
        "filename": "bpo-contact-center-floor.jpg",
        "page": "infrastructure.html",
        "section": "Operations Floor Layout",
        "desc": "Spacious, ergonomic contact center operations floor showing modular workstations, acoustic dividers, and supervisor oversight desks.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Architectural wide-angle view of a state-of-the-art contact center floor. Ergonomic height-adjustable desks arranged in modular clusters, separated by fabric acoustic privacy baffles in navy and light grey. Dual monitor mounts with clean concealed cable conduits. In the center, a raised supervisor collaboration island with digital queue dashboards. High-efficiency acoustic ceiling tiles, abundant natural light from large windows. Shot on Sony A7R V with 24mm tilt-shift lens, perfect vertical lines.",
        "comp": "Strong architectural leading lines converging toward the central supervisor island.",
        "angle": "Eye-level architectural shot.",
        "light": "Balanced mix of 4000K indirect LED troffers and natural daylight.",
        "bg": "Modern corporate facility with floor-to-ceiling windows and indoor plants.",
        "style": "Architectural design showcase photography, pristine, spacious, impeccably clean.",
        "palette": "Navy (#101D35), cool grey, white oak, brushed steel.",
        "subject": "Ergonomic operations floor layout.",
        "neg_space": "Ceiling and upper walls."
    },
    {
        "num": 37,
        "filename": "bpo-training-session.jpg",
        "page": "infrastructure.html",
        "section": "Training Pods & Coaching Section",
        "desc": "A dedicated BPO training classroom with a trainer guiding new associates through simulated customer scenarios on interactive monitors.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Medium shot of an interactive corporate training classroom inside a BPO delivery center. A dynamic training specialist stands beside an interactive 75-inch touch display demonstrating a customer troubleshooting workflow to six attentive new associates seated at training pods with dual monitors and headsets. Notebooks, coffee cups, and engaged postures. Bright, inspiring, high-quality learning facility. Shot on Canon R5 with 35mm f/1.8 lens.",
        "comp": "Trainer on the right third engaging with associates seated along the left and center.",
        "angle": "Eye-level medium shot.",
        "light": "Bright, uplifting commercial classroom lighting.",
        "bg": "Modern training room with writeable glass walls and company values posters.",
        "style": "Educational corporate lifestyle photography, inspiring, professional, dynamic.",
        "palette": "Corporate blue, crisp white, warm wood accents, grey.",
        "subject": "Corporate trainer leading an interactive onboarding workshop.",
        "neg_space": "Upper quarter."
    },
    {
        "num": 38,
        "filename": "bpo-modern-workspace.jpg",
        "page": "infrastructure.html",
        "section": "Collaborative Workspaces Section",
        "desc": "Ergonomic breakout lounges, meeting pods, and wellness areas designed for agent rest and team collaboration between operational shifts.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Contemporary workplace breakout and employee wellness lounge. High-end Scandinavian-style acoustic booths, comfortable modular armchairs in slate and navy upholstery, warm timber coffee tables, and a modern espresso bar in the background. Two associates in casual business clothes chatting over coffee, another reading a tablet in a quiet booth. Relaxing, restorative, premium corporate culture environment. Shot on Leica Q3 with 28mm f/1.7 lens.",
        "comp": "Balanced architectural interior with quiet booth on left, open lounge in center, and cafe in background right.",
        "angle": "Eye-level natural perspective.",
        "light": "Warm residential-feel 3000K ambient light, floor lamps, and soft natural daylight.",
        "bg": "Modern corporate lounge with vertical moss wall and wood acoustic paneling.",
        "style": "High-end corporate interior design photography, welcoming, restful, modern.",
        "palette": "Warm oak, navy blue, forest green, warm white, charcoal.",
        "subject": "Restorative employee collaboration and wellness lounge.",
        "neg_space": "Top third."
    },
    {
        "num": 39,
        "filename": "bpo-leadership-meeting.jpg",
        "page": "leadership.html",
        "section": "Governance Cadence Section",
        "desc": "Executive leadership team conducting a quarterly operational governance review in a modern glass boardroom.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Executive operations leadership team seated around a polished marble conference table in a sunlit corner boardroom. A female Vice President of Operations listens thoughtfully as the Solutions Director presents operational capacity charts on a slim wall-mounted OLED screen. Professional business suits, leather portfolios, crystal water glasses. Uncompromising executive gravitas, strategic governance. Shot on Sony A1 with 50mm f/1.2 lens.",
        "comp": "Leadership team arranged along the conference table, executive in foreground slightly blurred, sharp focus on the VP.",
        "angle": "Waist-level medium shot down the length of the executive table.",
        "light": "Soft, natural directional daylight from floor-to-ceiling corner windows.",
        "bg": "High-rise boardroom with sweeping city panoramic views.",
        "style": "Prestigious executive corporate editorial photography, refined, commanding, strategic.",
        "palette": "Deep navy, charcoal, crisp white, marble grey, rich espresso wood.",
        "subject": "Senior BPO leadership conducting an executive governance review.",
        "neg_space": "Upper left."
    },
    {
        "num": 40,
        "filename": "bpo-team-collaboration.jpg",
        "page": "team.html",
        "section": "Floor Collaboration Section",
        "desc": "Cross-functional team leader, quality analyst, and frontline agent collaborating at an open huddle table on an operational floor.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Candid collaboration moment on an operational delivery floor. A team leader, quality analyst, and frontline support associate gathered around a standing huddle table reviewing interaction quality scorecards on a laptop. They are smiling and discussing constructive feedback with genuine camaraderie and professional respect. High-tech floor visible in soft blur behind. Shot on Nikon Z8 with 50mm f/1.8 lens.",
        "comp": "Three colleagues forming a triangular collaborative grouping in the center.",
        "angle": "Eye-level candid perspective.",
        "light": "Even, bright, flattering commercial office light.",
        "bg": "Active operations floor with acoustic baffles and workstations.",
        "style": "Authentic, collaborative workplace photography, encouraging, respectful.",
        "palette": "Corporate blue (#2864D8), teal accents, navy, soft grey.",
        "subject": "Team leader and associates in collaborative coaching dialogue.",
        "neg_space": "Upper quarter."
    },

    # 7. Quality and Security images (2)
    {
        "num": 41,
        "filename": "bpo-quality-assurance.jpg",
        "page": "quality-assurance.html",
        "section": "Evaluation Dimensions Section",
        "desc": "Quality assurance analyst listening to call recordings with professional headphones while scoring interaction rubrics on screen.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Methodical quality assurance auditor seated at a dedicated QA review desk. She wears studio-grade over-ear monitor headphones, listening intently to an audio waveform on her left screen while scoring evaluation criteria on a customized QA rubric interface on her right monitor. A small notebook with neat checklist notes sits beside her keyboard. Serious, objective, focused demeanor. Shot on Fujifilm X-T5 with 56mm f/1.2 lens.",
        "comp": "Side-profile shot capturing the analyst with headphones and the detailed audio waveform and scorecard on the screens.",
        "angle": "Eye-level medium close-up.",
        "light": "Soft directional desk lamp light combined with ambient office daylight.",
        "bg": "Quiet quality assurance review suite separated from the main floor.",
        "style": "Methodical, objective analytical photography, precise, uncompromising standards.",
        "palette": "Navy (#101D35), slate, cool white, amber waveform accents.",
        "subject": "QA analyst evaluating customer interaction recording.",
        "neg_space": "Top and upper right."
    },
    {
        "num": 42,
        "filename": "bpo-data-security-governance.jpg",
        "page": "data-security.html",
        "section": "Client Collaboration Section",
        "desc": "Information security officer reviewing role-based access logs and encryption protocols on a high-security operations terminal.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Cybersecurity and data governance specialist reviewing network access authorization logs on an encrypted terminal. Screen displays stylized network topology nodes, access permission matrices, and token verification statuses. Keycard badge and security token on the desk. Clean-desk policy strictly observed, zero loose paper. Professional, high-security corporate environment. Shot on Canon R5 with 50mm f/1.4 lens.",
        "comp": "Specialist in the center-left, with monitor displaying security topology on the right.",
        "angle": "Eye-level three-quarter view.",
        "light": "Cool-toned, security-oriented lighting with crisp blue accents.",
        "bg": "Secure network operations room with frosted glass walls.",
        "style": "Corporate cybersecurity and data governance photography, vigilant, rigorous, secure.",
        "palette": "Dark navy (#101D35), cyber blue (#4D8DFF), steel grey, white.",
        "subject": "Data security specialist monitoring access governance protocols.",
        "neg_space": "Upper left."
    },

    # 8. Careers images (5)
    {
        "num": 43,
        "filename": "bpo-careers-culture.jpg",
        "page": "careers.html",
        "section": "Working With Us Section",
        "desc": "A vibrant group of international BPO customer care associates enjoying coffee and conversation in an airy corporate cafeteria.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Vibrant, candid corporate lifestyle photograph of four diverse customer experience professionals laughing together over coffee at a sunny cafeteria communal table. Modern architect-designed canteen with hanging pendant lights, wooden dining benches, and floor-to-ceiling glass looking out onto a landscaped garden courtyard. Authentic smiles, relaxed post-shift camaraderie, stylish business casual attire. Shot on Sony A7R V with 35mm f/1.4 lens.",
        "comp": "Four colleagues gathered around a light wood table, natural framing through glass architecture.",
        "angle": "Eye-level candid documentary shot.",
        "light": "Sun-drenched natural morning light filling the cafeteria.",
        "bg": "Contemporary corporate cafeteria with garden terrace.",
        "style": "Warm, inspiring employer branding photography, community, friendship, vitality.",
        "palette": "Warm golden daylight, teal, light oak, fresh green, white.",
        "subject": "Colleagues sharing a genuine moment of laughter and connection.",
        "neg_space": "Upper third."
    },
    {
        "num": 44,
        "filename": "bpo-workplace-diversity.jpg",
        "page": "job-openings.html",
        "section": "Openings Header Banner",
        "desc": "A dynamic wide-angle banner showing diverse customer support specialists, team leaders, and analysts walking together down a modern corporate atrium.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic corporate recruitment banner. A diverse group of young, talented professionals walking confidently forward down a bright architectural glass atrium. They carry laptops, tablets, and lanyards, smiling and chatting energetically. High soaring ceilings, white steel beams, soft sunlight streaming through glass skylights. Empowering, forward-looking, inspiring career journey aesthetic. Ultra-wide 21:9 ratio, shot on Arri Alexa 65.",
        "comp": "Symmetrical architectural atrium with the group walking toward the camera in the central third.",
        "angle": "Low-angle dynamic walking shot.",
        "light": "Luminous, ethereal natural sunlight pouring from the atrium ceiling.",
        "bg": "Modern corporate headquarters glass atrium.",
        "style": "Empowering corporate recruitment photography, aspirational, forward-moving.",
        "palette": "Crisp white, corporate blue (#2864D8), soft grey, warm skin tones.",
        "subject": "Diverse group of BPO professionals walking in modern corporate atrium.",
        "neg_space": "High ceiling area provides abundant space for banner titles."
    },
    {
        "num": 45,
        "filename": "bpo-professional-workspace.jpg",
        "page": "job-details.html",
        "section": "Job Details Hero Banner",
        "desc": "An immaculate, fully equipped customer support workstation featuring dual screens, modern headset, and ergonomic mesh chair.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic architectural shot of an immaculate, welcoming customer service workstation ready for a new associate. Dual curved monitors displaying welcoming onboarding desktop wallpaper, modern wireless headset resting neatly on an aluminum stand, sleek backlit keyboard, ergonomic mesh chair with lumbar support. Polished wood desk with clean cable management, warm morning sunlight across the surface. Shot on Leica SL2 with 24mm lens.",
        "comp": "Central focus on the empty, inviting workstation symbolizing career opportunity and readiness.",
        "angle": "Eye-level medium wide shot.",
        "light": "Gentle morning sunbeams washing across the clean desktop.",
        "bg": "Quiet, orderly contact center floor bathed in soft morning light.",
        "style": "Inviting, pristine corporate workplace photography, welcoming, modern.",
        "palette": "Warm timber, navy blue, clean white, brushed chrome.",
        "subject": "Pristine customer support workstation ready for new hire.",
        "neg_space": "Upper horizontal half."
    },
    {
        "num": 46,
        "filename": "bpo-talent-application.jpg",
        "page": "apply-job.html",
        "section": "Application Intro Banner",
        "desc": "A talent acquisition coordinator reviewing a clean digital candidate profile on a tablet in a welcoming interview lounge.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic lifestyle visual of talent acquisition and recruitment. A smiling HR recruiter seated in a bright corporate interview lounge with a digital tablet displaying candidate application documents. A welcoming candidate chair and a glass coffee table in front of her. Modern art on the wall, comfortable designer armchairs, peaceful natural light. Shot on Canon R5 with 35mm lens.",
        "comp": "Recruiter on the right third looking forward with an encouraging smile, welcoming seating area on the left.",
        "angle": "Eye-level welcoming perspective.",
        "light": "Warm, diffused, welcoming natural light.",
        "bg": "Bright, stylish corporate interview lounge.",
        "style": "Warm, encouraging recruitment photography, approachable, respectful.",
        "palette": "Teal (#21B6A8), warm grey, linen cream, corporate navy.",
        "subject": "Talent acquisition professional welcoming applicants.",
        "neg_space": "Top half."
    },
    {
        "num": 47,
        "filename": "bpo-skills-learning-center.jpg",
        "page": "employee-development.html",
        "section": "Learning Architecture Section",
        "desc": "Associates in a specialized computer simulation lab testing customer service call handling during a nesting training session.",
        "ratio": "16:9",
        "res": "1200 x 675 px",
        "orient": "Landscape",
        "prompt": "Wide shot of a dedicated skills learning and simulation laboratory inside an international BPO academy. Associates seated at simulation carrels with headsets and dual monitors, practicing simulated customer interactions under the watchful eye of roaming mentors. A mentor points gently to a decision tree flowchart on an associate's screen, offering encouraging guidance. Dedicated, structured, high-investment learning environment. Shot on Nikon Z8 with 35mm f/1.8 lens.",
        "comp": "Mentor and associate in focus in the foreground left, other training carrels receding diagonally.",
        "angle": "Eye-level medium-wide shot.",
        "light": "Bright, glare-free indirect commercial lighting.",
        "bg": "Advanced BPO learning academy with digital whiteboard screens.",
        "style": "Educational institutional excellence photography, structured, supportive.",
        "palette": "Corporate navy (#101D35), bright blue, warm blonde wood, white.",
        "subject": "Associates and mentor in customer service simulation lab.",
        "neg_space": "Upper right."
    },

    # 9. Case Study images (2)
    {
        "num": 48,
        "filename": "bpo-case-studies-banner.jpg",
        "page": "case-studies.html",
        "section": "Case Studies Banner",
        "desc": "Abstract business metrics, operational growth curves, and process flowcharts illustrating operational problem solving.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic abstract corporate visualization of operational problem resolution. Translucent 3D layered glass panels floating in deep navy space, displaying upward resolution curves, workflow process diagrams, and queue reduction benchmarks in luminous teal (#21B6A8) and corporate blue (#2864D8). Clean minimalist data aesthetic, high architectural elegance, photorealistic, 8k resolution, shot on RED Monstro 8K.",
        "comp": "Panoramic horizontal flow of glowing analytical glass panels.",
        "angle": "Slight isometric perspective.",
        "light": "Edge luminescence illuminating glass data layers.",
        "bg": "Deep corporate navy (#101D35) canvas with subtle optical depth.",
        "style": "Ultra-modern enterprise data visualization, polished, intellectual, prestigious.",
        "palette": "Midnight navy (#0B132B), electric blue (#2864D8), teal accent (#21B6A8), white.",
        "subject": "Abstract operational problem-solving glass data layers.",
        "neg_space": "Top half completely clear for header typography."
    },
    {
        "num": 49,
        "filename": "bpo-case-study-support.jpg",
        "page": "case-study-details.html",
        "section": "Support Case Study Banner",
        "desc": "A case study header showing a customer support operations team successfully collaborating to reduce ticket queues and optimize workflows.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic corporate case study header image. A cross-functional customer support operations squad gathered around a large interactive dashboard screen celebrating a milestone. The dashboard displays falling ticket backlog graphs and rising customer satisfaction indicators. High-five and collaborative gestures, confident expressions, modern tech office environment. Cinematic 21:9 ratio, shot on Arri Alexa Mini with 35mm lens.",
        "comp": "Team members grouped on the right two-thirds celebrating results, dashboard interface displayed prominently.",
        "angle": "Eye-level wide shot.",
        "light": "Warm, victorious commercial office lighting.",
        "bg": "Modern open-plan customer operations center.",
        "style": "Authentic corporate success and collaboration photography.",
        "palette": "Navy, electric blue, victory green accents, crisp white.",
        "subject": "Customer support team celebrating operational queue turnaround.",
        "neg_space": "Upper left section."
    },

    # 10. Insights & Resources images (2)
    {
        "num": 50,
        "filename": "bpo-insights-banner.jpg",
        "page": "insights.html",
        "section": "Resources Banner",
        "desc": "Executive reading an operational research report on a tablet in an architectural business library.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic corporate editorial visual. An executive seated in a quiet, sunlit corporate library overlooking a city skyline, reading an in-depth operational whitepaper on a tablet. Architectural bookshelves, leather armchairs, and architectural models in the background. Intellectual, authoritative, quiet contemplation. Ultra-wide 21:9 ratio, shot on Leica SL2 with 50mm Summilux.",
        "comp": "Executive on the right third, long perspective of the architectural library stretching across the left.",
        "angle": "Eye-level medium-wide shot.",
        "light": "Soft natural side daylight casting long, gentle shadows.",
        "bg": "Modern corporate knowledge library with floor-to-ceiling glass.",
        "style": "Thought leadership editorial photography, intellectual, sophisticated, calm.",
        "palette": "Warm timber, navy blue, charcoal, natural paper white.",
        "subject": "Executive reviewing business process research.",
        "neg_space": "Upper left."
    },
    {
        "num": 51,
        "filename": "bpo-article-future-outsourcing.jpg",
        "page": "article-details.html",
        "section": "Article Header Banner",
        "desc": "Conceptual panoramic image representing modern business process outsourcing: human intelligence combined with digital workflow automation.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic concept editorial banner representing modern business process management. Two business architects examining a translucent holographic model of global operational workflows floating between them. Clean geometric lines, subtle data streams connecting cities, deep navy and cyan light. Sophisticated, realistic, thought-provoking enterprise photography. Shot on RED V-Raptor, 8k.",
        "comp": "Two architects in profile framing the glowing operational model in the center.",
        "angle": "Eye-level horizontal panorama.",
        "light": "Subtle ambient twilight with glowing cyan and blue interface light.",
        "bg": "Minimalist dark corporate penthouse overlooking evening city lights.",
        "style": "Visionary enterprise thought-leadership photography.",
        "palette": "Midnight navy (#0B132B), cyan (#21B6A8), corporate blue (#2864D8), white.",
        "subject": "Business architects discussing global operational strategies.",
        "neg_space": "Upper third."
    },

    # 11. FAQ & Contact images (2)
    {
        "num": 52,
        "filename": "bpo-faq-support.jpg",
        "page": "faq.html",
        "section": "FAQ Header Banner",
        "desc": "Helpful customer concierge representative standing near an interactive digital knowledge directory kiosk in a corporate lobby.",
        "ratio": "21:9",
        "res": "1920 x 820 px",
        "orient": "Landscape",
        "prompt": "Panoramic corporate knowledge visual. A friendly, professional customer service ambassador standing beside a sleek interactive knowledge directory in a sun-drenched corporate headquarters lobby. She gestures warmly with an open hand, ready to answer questions. High ceilings, polished stone floors, architectural greenery. Reassuring, welcoming, helpful corporate atmosphere. Shot on Canon EOS R5 with 35mm lens.",
        "comp": "Ambassador on the right third, interactive knowledge kiosk and spacious lobby extending across the left.",
        "angle": "Eye-level wide shot.",
        "light": "Luminous natural sunlight pouring through lobby glass.",
        "bg": "Airy, high-end corporate atrium with indoor greenery.",
        "style": "Welcoming, customer-first service photography, helpful, approachable.",
        "palette": "Warm stone, navy blue, soft teal, clean white.",
        "subject": "Customer service ambassador standing beside knowledge directory.",
        "neg_space": "Top half."
    },
    {
        "num": 53,
        "filename": "bpo-business-consultation.jpg",
        "page": "contact.html",
        "section": "Operational Consultation Section",
        "desc": "A senior BPO solutions architect greeting a client executive with a warm professional handshake in a modern consultation lounge.",
        "ratio": "4:3",
        "res": "1200 x 900 px",
        "orient": "Landscape",
        "prompt": "Medium shot of a senior BPO solutions director and an enterprise client executive shaking hands warmly across a modern conference table in an executive consultation suite. Both are dressed in tailored corporate attire, smiling with authentic professional rapport and mutual respect. On the table are sleek laptops, project roadmaps, and coffee cups. Bright, trust-building, professional B2B partnership atmosphere. Shot on Sony A7R V with 50mm f/1.4 lens, natural skin tones.",
        "comp": "Two professionals centered, their handshake forming the focal point of mutual commitment and trust.",
        "angle": "Eye-level medium shot.",
        "light": "Soft, flattering corporate daylight with warm ambient interior fill.",
        "bg": "Floor-to-ceiling glass conference suite overlooking a modern business park.",
        "style": "Trust-building B2B executive photography, authentic, dignified, professional.",
        "palette": "Corporate navy blue (#101D35), slate grey, crisp white, warm wood accents.",
        "subject": "Solutions architect and client executive sealing an operational partnership.",
        "neg_space": "Upper third."
    }
]

def generate_markdown():
    md = []
    md.append("# GOOGLE FLOW IMAGE GENERATION GUIDE")
    md.append("## Complete Image Inventory, Exact Prompts & Asset Replacement Instructions")
    md.append("### Generic International BPO Company Demonstration Website")
    md.append("")
    md.append("> **IMPORTANT NOTICE FOR GOOGLE FLOW USERS:**")
    md.append("> This guide contains individual, custom-crafted Google Flow image generation prompts for every single image placeholder across the complete 50-page website. Every image has been meticulously planned with exact aspect ratios, resolutions, camera angles, composition guidelines, color palettes, and subject positioning. Do NOT write generic prompts; copy each individual prompt below directly into Google Flow.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Table of Contents")
    md.append("1. [Homepage Images (Images 1–4)](#1-homepage-images)")
    md.append("2. [About Us Images (Images 5–6)](#2-about-us-images)")
    md.append("3. [Services Overview Images (Image 7)](#3-services-overview-images)")
    md.append("4. [Individual BPO Service Images (Images 8–24)](#4-individual-bpo-service-images)")
    md.append("5. [Industry Vertical Images (Images 25–33)](#5-industry-vertical-images)")
    md.append("6. [Technology & Operations Images (Images 34–40)](#6-technology--operations-images)")
    md.append("7. [Quality & Data Security Images (Images 41–42)](#7-quality--data-security-images)")
    md.append("8. [Careers & Talent Images (Images 43–47)](#8-careers--talent-images)")
    md.append("9. [Case Study Images (Images 48–49)](#9-case-study-images)")
    md.append("10. [Insights & Editorial Images (Images 50–51)](#10-insights--editorial-images)")
    md.append("11. [FAQ & Contact Images (Images 52–53)](#11-faq--contact-images)")
    md.append("12. [Complete Image Inventory Table](#12-complete-image-inventory-table)")
    md.append("13. [Recommended Generation Order & Replacement Workflow](#13-recommended-generation-order--replacement-workflow)")
    md.append("")
    md.append("---")
    md.append("")

    current_group = ""
    for img in IMAGES_GUIDE_DATA:
        # Group headers
        if img["num"] == 1:
            md.append("## 1. Homepage Images\n")
        elif img["num"] == 5:
            md.append("## 2. About Us Images\n")
        elif img["num"] == 7:
            md.append("## 3. Services Overview Images\n")
        elif img["num"] == 8:
            md.append("## 4. Individual BPO Service Images\n")
        elif img["num"] == 25:
            md.append("## 5. Industry Vertical Images\n")
        elif img["num"] == 34:
            md.append("## 6. Technology & Operations Images\n")
        elif img["num"] == 41:
            md.append("## 7. Quality & Data Security Images\n")
        elif img["num"] == 43:
            md.append("## 8. Careers & Talent Images\n")
        elif img["num"] == 48:
            md.append("## 9. Case Study Images\n")
        elif img["num"] == 50:
            md.append("## 10. Insights & Editorial Images\n")
        elif img["num"] == 52:
            md.append("## 11. FAQ & Contact Images\n")

        md.append(f"### Image {img['num']}: `{img['filename']}`")
        md.append(f"- **HTML Page:** `{img['page']}`")
        md.append(f"- **Section Name:** {img['section']}")
        md.append(f"- **Recommended Aspect Ratio:** {img['ratio']}")
        md.append(f"- **Recommended Resolution:** {img['res']}")
        md.append(f"- **Orientation:** {img['orient']}")
        md.append(f"- **Detailed Visual Description:** {img['desc']}")
        md.append("")
        md.append("#### Complete Individual Google Flow Prompt:")
        md.append("```text")
        md.append(img['prompt'])
        md.append("```")
        md.append("")
        md.append("#### Technical Camera & Composition Specifications:")
        md.append(f"- **Composition Instructions:** {img['comp']}")
        md.append(f"- **Camera Angle:** {img['angle']}")
        md.append(f"- **Lighting Conditions:** {img['light']}")
        md.append(f"- **Background Environment:** {img['bg']}")
        md.append(f"- **Visual Style:** {img['style']}")
        md.append(f"- **Color Palette:** {img['palette']}")
        md.append(f"- **Subject Positioning:** {img['subject']}")
        md.append(f"- **Negative Space Considerations:** {img['neg_space']}")
        md.append("")
        md.append("---")
        md.append("")

    # Section 12: Inventory Table
    md.append("## 12. Complete Image Inventory Table")
    md.append("")
    md.append("| # | Exact Filename | HTML Page | Section Name | Aspect Ratio | Resolution | Orientation |")
    md.append("|---|----------------|-----------|--------------|--------------|------------|-------------|")
    for img in IMAGES_GUIDE_DATA:
        md.append(f"| {img['num']} | `{img['filename']}` | `{img['page']}` | {img['section']} | {img['ratio']} | {img['res']} | {img['orient']} |")
    md.append("")
    md.append("### Summary Statistics")
    md.append(f"- **Total Image Count:** {len(IMAGES_GUIDE_DATA)} unique images")
    md.append(f"- **Landscape Images (16:9 & 21:9):** 44 images")
    md.append(f"- **Landscape Images (4:3):** 9 images")
    md.append(f"- **Portrait Images:** 0 images")
    md.append(f"- **Square Images:** 0 images")
    md.append("")
    md.append("---")
    md.append("")

    # Section 13: Recommended Generation Order & Replacement Workflow
    md.append("## 13. Recommended Generation Order & Replacement Workflow")
    md.append("")
    md.append("### Recommended Generation Priority")
    md.append("To ensure the most impactful visual presentation first, generate images in the following phased batches:")
    md.append("1. **Phase 1 — Core Brand Identity & Homepage (Images 1–7):**")
    md.append("   - `bpo-hero-operations.jpg`, `bpo-business-flexibility.jpg`, `bpo-multichannel-support.jpg`, `bpo-career-opportunities.jpg`, `bpo-about-philosophy.jpg`, `bpo-operations-center.jpg`, `bpo-services-overview.jpg`.")
    md.append("2. **Phase 2 — High-Volume CX Service Pages (Images 8–13):**")
    md.append("   - Customer Support, Inbound/Outbound Call Center, Technical Support, Email Support, Live Chat.")
    md.append("3. **Phase 3 — Operational Infrastructure & Technology (Images 34–40):**")
    md.append("   - Process lifecycle, Technology architecture, Call center floor, Training pods, Modern workspaces, Leadership.")
    md.append("4. **Phase 4 — Vertical Industry Pages (Images 25–33):**")
    md.append("   - Healthcare, Banking, E-Commerce, Tech/SaaS, Telecom, Travel, Insurance, Logistics.")
    md.append("5. **Phase 5 — Back-Office & Specialized Services (Images 14–24):**")
    md.append("   - Back office, Data entry, Finance, Order processing, Digitization, Moderation, Leads, VA, HR, Healthcare, KPO.")
    md.append("6. **Phase 6 — Quality, Careers, Case Studies, Insights, Contact (Images 41–53):**")
    md.append("   - QA review, Data security, Careers culture, Job details, Application, Case studies, Insights, FAQ, Contact.")
    md.append("")
    md.append("### Step-by-Step Asset Replacement Instructions")
    md.append("Once an image has been generated in Google Flow:")
    md.append("1. **Verify File Name & Format:**")
    md.append("   - Save the file as a high-quality JPEG (`.jpg`) using the **exact filename** listed in the table above (e.g. `bpo-hero-operations.jpg`).")
    md.append("2. **Place File into Assets Directory:**")
    md.append("   - Move the saved file into `assets/images/` inside the website directory.")
    md.append("3. **Update HTML Templates:**")
    md.append("   - In the corresponding HTML page, find the placeholder container:")
    md.append("   ```html")
    md.append("   <!-- Before: CSS/SVG Placeholder -->")
    md.append("   <div class=\"image-placeholder ratio-16-9\">")
    md.append("     ...")
    md.append("     <span class=\"image-placeholder-filename\">bpo-hero-operations.jpg</span>")
    md.append("     ...")
    md.append("   </div>")
    md.append("   ```")
    md.append("   - Replace it with a modern, responsive `<img>` element:")
    md.append("   ```html")
    md.append("   <!-- After: Production Image Asset -->")
    md.append("   <img src=\"assets/images/bpo-hero-operations.jpg\" ")
    md.append("        alt=\"Modern BPO contact center and customer operations floor\" ")
    md.append("        class=\"ratio-16-9\" ")
    md.append("        style=\"width: 100%; object-fit: cover; border-radius: var(--radius-lg);\" ")
    md.append("        loading=\"lazy\">")
    md.append("   ```")
    md.append("4. **Zero Layout Shift:**")
    md.append("   - Because the placeholder classes (`ratio-16-9`, `ratio-4-3`, `ratio-21-9`) enforce CSS aspect ratios, replacing the placeholders with images will produce zero layout shift.")
    md.append("")

    return "\n".join(md)

with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
    f.write(generate_markdown())

print("IMAGE-GENERATION-GUIDE.md generated successfully.")
