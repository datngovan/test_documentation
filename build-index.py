import json, os

BASE = r"C:\Users\Admin\desktop\github-page\docs"
OUT  = r"C:\Users\Admin\desktop\github-page\search-index.json"

DOCS = [
    ("align-overview",        "Align Overview",              "align","Align","#10b981", r"align\overview",        False, ["align","vision","mission"],                   []),
    ("align-stakeholders",    "Stakeholder Management",      "align","Align","#10b981", r"align\stakeholders",    False, ["stakeholder","RACI","communication"],          ["Stakeholders"]),
    ("align-goals",           "Goals and Objectives",        "align","Align","#10b981", r"align\goals",           False, ["goals","OKR","SMART","objectives"],            ["Strategy"]),
    ("align-market-analysis", "Market & Competitive Analysis","align","Align","#10b981",r"align\market-analysis", False, ["market","competitive","SWOT","TAM"],           ["Strategy","Competitive Positioning"]),
    ("align-market-entry",    "Market Entry Strategy",       "align","Align","#10b981", r"align\strategy\competitive-positioning\market-entry", False, ["GTM","ICP","market entry"], ["Strategy","Competitive Positioning"]),
    ("align-executive-strategy","Executive Strategy (Confidential)","align","Align","#10b981",r"align\executive-strategy",True,["strategy","confidential","board"], ["Strategy","Confidential"]),
    ("align-vision-mission",  "Mission Statement",           "align","Align","#10b981", r"align\vision\mission-statement",   False, ["mission","vision","purpose"],       ["Vision"]),
    ("align-vision-core-values","Core Values",               "align","Align","#10b981", r"align\vision\values\core-values",        False, ["values","culture","integrity"],["Vision","Values"]),
    ("align-vision-guiding-principles","Guiding Principles", "align","Align","#10b981", r"align\vision\values\guiding-principles",  False, ["principles","engineering"],   ["Vision","Values"]),
    ("plan-overview",         "Plan Overview",               "plan","Plan","#3b82f6",   r"plan\overview",         False, ["plan","planning","methodology"],               []),
    ("plan-technical-architecture","Technical Architecture", "plan","Plan","#3b82f6",   r"plan\technical-architecture", False, ["architecture","system","microservices"],  ["Architecture"]),
    ("plan-solution-arch-deep","Solution Architecture Deep Dive","plan","Plan","#3b82f6",r"plan\solution-architecture-deep",False,["deep dive","component","DAG","Rust"],  ["Architecture","Services"]),
    ("plan-auth-service",     "Auth Service Design",         "plan","Plan","#3b82f6",   r"plan\architecture\services\auth-service", False, ["auth","JWT","SSO","SAML"],    ["Architecture","Services"]),
    ("plan-schema-design",    "Database Schema Design",      "plan","Plan","#3b82f6",   r"plan\architecture\data\schema-design",    False, ["schema","PostgreSQL","migration"],["Architecture","Data"]),
    ("plan-resources",        "Resources and Capacity",      "plan","Plan","#3b82f6",   r"plan\resources",        False, ["resources","capacity","team","tools"],          ["Resources"]),
    ("plan-budget-confidential","Budget Details (Confidential)","plan","Plan","#3b82f6",r"plan\budget-confidential",True,["budget","salary","confidential"],              ["Resources","Confidential"]),
    ("plan-roadmap",          "Roadmap Overview",            "plan","Plan","#3b82f6",   r"plan\roadmap",          False, ["roadmap","milestones","quarterly"],             ["Roadmap"]),
    ("plan-q2-2026",          "Q2 2026 Roadmap",             "plan","Plan","#3b82f6",   r"plan\roadmap\q2-2026",  False, ["Q2","2026","roadmap","GA","ISO"],               ["Roadmap"]),
    ("plan-h1-milestones",    "H1 2026 Milestones",          "plan","Plan","#3b82f6",   r"plan\roadmap\milestones\h1-milestones", False, ["milestones","H1","tracker"],    ["Roadmap","Milestones"]),
    ("execute-overview",      "Execute Overview",            "execute","Execute","#f59e0b",r"execute\overview",   False, ["execute","execution","sprint"],                 []),
    ("execute-operations-handbook","Operations Handbook",    "execute","Execute","#f59e0b",r"execute\operations-handbook",False,["operations","on-call","SRE","incident"], ["Operations"]),
    ("execute-deployment-runbook","Deployment Runbook",      "execute","Execute","#f59e0b",r"execute\deployment-runbook",False,["deployment","CI/CD","kubernetes","bash"],  ["Operations","Runbooks"]),
    ("execute-security-credentials","Security Credentials",  "execute","Execute","#f59e0b",r"execute\security-credentials",True,["security","credentials","vault"],        ["Operations","Security"]),
    ("execute-unit-test-guide","Unit Testing Guide",         "execute","Execute","#f59e0b",r"execute\quality\testing\unit-test-guide",False,["testing","unit test","AAA","Go"],["Quality","Testing"]),
    ("execute-integration-test-guide","Integration Testing Guide","execute","Execute","#f59e0b",r"execute\quality\testing\integration-test-guide",False,["integration","testcontainers"],["Quality","Testing"]),
    ("execute-progress",      "Progress Tracking",           "execute","Execute","#f59e0b",r"execute\progress",   False, ["progress","sprint","velocity","KPI"],           ["Sprints"]),
    ("execute-blockers",      "Blockers and Escalation",     "execute","Execute","#f59e0b",r"execute\blockers",   False, ["blockers","escalation","mitigation"],           ["Sprints"]),
    ("execute-sprint-26-06",  "Sprint 26-06",                "execute","Execute","#f59e0b",r"execute\sprints\sprint-26-06",False,["sprint","planning","stories","standup"], ["Sprints"]),
    ("execute-sprint-26-01",  "Sprint 26-01 Archive",        "execute","Execute","#f59e0b",r"execute\sprints\archive\sprint-26-01",False,["sprint","archive","retrospective"],["Sprints","Archive"]),
    ("improve-overview",      "Improve Overview",            "improve","Improve","#8b5cf6",r"improve\overview",   False, ["improve","continuous improvement","feedback"],   []),
    ("improve-maturity-model","APEI Capability Maturity Model","improve","Improve","#8b5cf6",r"improve\maturity-model",False,["maturity","CMM","DORA","capability"],       ["Frameworks"]),
    ("improve-personnel-reviews","Personnel Performance Reviews","improve","Improve","#8b5cf6",r"improve\personnel-reviews",True,["personnel","performance","confidential"],["HR"]),
    ("improve-recommended-books","Recommended Reading List",  "improve","Improve","#8b5cf6",r"improve\learning\recommended-books",False,["books","reading","learning"],     ["Learning"]),
    ("improve-engineering-track","Engineering Learning Track","improve","Improve","#8b5cf6",r"improve\learning\courses\engineering-track",False,["courses","certifications","AWS"],["Learning","Courses"]),
    ("improve-metrics",       "Metrics and Measurement",     "improve","Improve","#8b5cf6",r"improve\metrics",    False, ["metrics","KPI","measurement","dashboard"],       ["Metrics"]),
    ("improve-quarterly-review","Q1 2026 Quarterly Review",  "improve","Improve","#8b5cf6",r"improve\quarterly-review",False,["quarterly","OKR","KPI","Q1"],               ["Metrics"]),
    ("improve-retrospective", "Retrospective Guide",         "improve","Improve","#8b5cf6",r"improve\retrospective",False,["retrospective","lessons","action items"],       ["Retrospectives"]),
    ("improve-q1-2026-retro", "Q1 2026 Retrospective",       "improve","Improve","#8b5cf6",r"improve\retrospectives\q1-2026-retro",False,["retrospective","start stop continue"],["Retrospectives"]),
    ("improve-q4-2025-retro", "Q4 2025 Retrospective",       "improve","Improve","#8b5cf6",r"improve\retrospectives\archive\q4-2025-retro",False,["retrospective","Q4","2025","archive"],["Retrospectives","Archive"]),
]

documents = []
for row in DOCS:
    doc_id, title, section, sectionLabel, sectionColor, rel_path, restricted, tags, breadcrumb = row
    if restricted:
        content = "[RESTRICTED] This document contains classified information and cannot be displayed."
    else:
        md_path = os.path.join(BASE, rel_path + ".md")
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            content = "# " + title + "\n\nContent not found."
            print("WARNING: " + md_path + " not found")

    documents.append({
        "id": doc_id, "title": title, "section": section,
        "sectionLabel": sectionLabel, "sectionColor": sectionColor,
        "filename": rel_path.split("\\")[-1],
        "restricted": restricted, "breadcrumb": breadcrumb,
        "content": content, "tags": tags
    })

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"documents": documents}, f, ensure_ascii=False, separators=(',',':'))

print("Written " + str(len(documents)) + " documents")
for d in documents:
    r = " [RESTRICTED]" if d["restricted"] else ""
    crumb = " > ".join(d["breadcrumb"]) if d["breadcrumb"] else "(root)"
    print("  [" + d["section"].upper() + "] " + crumb + " > " + d["title"] + r)
