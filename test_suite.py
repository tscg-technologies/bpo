import glob
import re
import os

print("--- STARTING COMPREHENSIVE BPO WEBSITE AUDIT ---")

# 1. 50 HTML Pages Check
html_files = sorted(glob.glob("*.html"))
print(f"Total HTML files found: {len(html_files)}")
assert len(html_files) == 50, f"Expected 50 HTML files, found {len(html_files)}"

# 2. Check for empty files
for h in html_files:
    size = os.path.getsize(h)
    assert size > 1000, f"File {h} is too small ({size} bytes)"

# 3. Internal link validation
broken_links = []
external_img_urls = []
all_html_basenames = set([os.path.basename(f) for f in html_files])

link_pattern = re.compile(r'href="([^"#:]+\.html)"')
img_pattern = re.compile(r'<img[^>]+src="([^"]+)"')

for h in html_files:
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()

    # Check links
    links = link_pattern.findall(content)
    for link in links:
        target = link.split("?")[0].split("#")[0]
        if target not in all_html_basenames:
            broken_links.append((h, link))

    # Check images
    imgs = img_pattern.findall(content)
    for img_src in imgs:
        if img_src.startswith("http://") or img_src.startswith("https://"):
            external_img_urls.append((h, img_src))

print(f"Broken internal links: {len(broken_links)}")
if broken_links:
    for b in broken_links:
        print("Broken link:", b)
assert len(broken_links) == 0, "Found broken internal links!"

print(f"External image URLs found: {len(external_img_urls)}")
assert len(external_img_urls) == 0, "Found external image URLs!"

# 4. Verified Image Assets Check
missing_images = []
total_images = 0

for h in html_files:
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()
    imgs = img_pattern.findall(content)
    for img_src in imgs:
        total_images += 1
        normalized_path = img_src.replace("/", os.sep)
        if not os.path.exists(normalized_path):
            missing_images.append((h, img_src))

print(f"Total production image elements across website: {total_images}")
print(f"Missing images on disk: {len(missing_images)}")
if missing_images:
    print("Missing images:", missing_images)
assert len(missing_images) == 0, "Some images are missing on disk!"

# 5. Check disclaimers and forbidden certification claims
forbidden_claims = [
    "we are ISO 27001 certified",
    "certified ISO 27001",
    "we are SOC 2 certified",
    "certified SOC 2",
    "we are HIPAA compliant",
    "HIPAA certified",
    "PCI DSS certified"
]

found_forbidden = []
for h in html_files:
    with open(h, "r", encoding="utf-8") as f:
        content = f.read().lower()
    for claim in forbidden_claims:
        if claim in content:
            found_forbidden.append((h, claim))

print(f"Forbidden certification claims found: {len(found_forbidden)}")
assert len(found_forbidden) == 0, f"Found forbidden claims: {found_forbidden}"

# 6. Check required dummy contact details
with open("contact.html", "r", encoding="utf-8") as f:
    contact_content = f.read()

assert "0000000000" in contact_content, "Missing required dummy phone number!"
assert "demo@example.com" in contact_content, "Missing required dummy email!"
assert "Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000" in contact_content or "Hyderabad, Telangana" in contact_content, "Missing dummy address!"

print("--- AUDIT COMPLETED: 100% PASSING ON ALL CRITERIA! ---")
