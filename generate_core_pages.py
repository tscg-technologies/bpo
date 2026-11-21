"""
Runner to generate all 17 Core HTML Pages
"""

from generate_pages import build_index
from build_core_pages import (
    build_about, build_services, build_industries, build_process,
    build_technology, build_quality_assurance, build_data_security,
    build_infrastructure, build_leadership, build_team,
    build_case_studies, build_case_study_details, build_insights,
    build_article_details, build_faq, build_contact
)

CORE_PAGES = [
    ("index.html", build_index()),
    ("about.html", build_about()),
    ("services.html", build_services()),
    ("industries.html", build_industries()),
    ("process.html", build_process()),
    ("technology.html", build_technology()),
    ("quality-assurance.html", build_quality_assurance()),
    ("data-security.html", build_data_security()),
    ("infrastructure.html", build_infrastructure()),
    ("leadership.html", build_leadership()),
    ("team.html", build_team()),
    ("case-studies.html", build_case_studies()),
    ("case-study-details.html", build_case_study_details()),
    ("insights.html", build_insights()),
    ("article-details.html", build_article_details()),
    ("faq.html", build_faq()),
    ("contact.html", build_contact())
]

def generate_core():
    for filename, content in CORE_PAGES:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated core page: {filename}")

if __name__ == "__main__":
    generate_core()
