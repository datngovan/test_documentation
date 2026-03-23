import json, os

BASE = r"C:\Users\Admin\desktop\github-page\docs"
OUT  = r"C:\Users\Admin\desktop\github-page\search-index.json"

# (id, title, section, sectionLabel, sectionColor, rel_path, restricted, tags, breadcrumb, lang)
DOCS = [
    # ── ENGLISH ────────────────────────────────────────────────────────────────
    ("align-overview",        "Align Overview",              "align","Align","#F2C75C", r"align\overview",        False, ["align","vision","mission"],                   [], "en"),
    ("align-stakeholders",    "Stakeholder Management",      "align","Align","#F2C75C", r"align\stakeholders",    False, ["stakeholder","RACI","communication"],          ["Stakeholders"], "en"),
    ("align-goals",           "Goals and Objectives",        "align","Align","#F2C75C", r"align\goals",           False, ["goals","OKR","SMART","objectives"],            ["Strategy"], "en"),
    ("align-market-analysis", "Market & Competitive Analysis","align","Align","#F2C75C",r"align\market-analysis", False, ["market","competitive","SWOT","TAM"],           ["Strategy","Competitive Positioning"], "en"),
    ("align-market-entry",    "Market Entry Strategy",       "align","Align","#F2C75C", r"align\strategy\competitive-positioning\market-entry", False, ["GTM","ICP","market entry"], ["Strategy","Competitive Positioning"], "en"),
    ("align-executive-strategy","Executive Strategy (Confidential)","align","Align","#F2C75C",r"align\executive-strategy",True,["strategy","confidential","board"], ["Strategy","Confidential"], "en"),
    ("align-vision-mission",  "Mission Statement",           "align","Align","#F2C75C", r"align\vision\mission-statement",   False, ["mission","vision","purpose"],       ["Vision"], "en"),
    ("align-vision-core-values","Core Values",               "align","Align","#F2C75C", r"align\vision\values\core-values",        False, ["values","culture","integrity"],["Vision","Values"], "en"),
    ("align-vision-guiding-principles","Guiding Principles", "align","Align","#F2C75C", r"align\vision\values\guiding-principles",  False, ["principles","engineering"],   ["Vision","Values"], "en"),
    ("plan-overview",         "Plan Overview",               "plan","Plan","#1B6B3A",   r"plan\overview",         False, ["plan","planning","methodology"],               [], "en"),
    ("plan-technical-architecture","Technical Architecture", "plan","Plan","#1B6B3A",   r"plan\technical-architecture", False, ["architecture","system","microservices"],  ["Architecture"], "en"),
    ("plan-solution-arch-deep","Solution Architecture Deep Dive","plan","Plan","#1B6B3A",r"plan\solution-architecture-deep",False,["deep dive","component","DAG","Rust"],  ["Architecture","Services"], "en"),
    ("plan-auth-service",     "Auth Service Design",         "plan","Plan","#1B6B3A",   r"plan\architecture\services\auth-service", False, ["auth","JWT","SSO","SAML"],    ["Architecture","Services"], "en"),
    ("plan-schema-design",    "Database Schema Design",      "plan","Plan","#1B6B3A",   r"plan\architecture\data\schema-design",    False, ["schema","PostgreSQL","migration"],["Architecture","Data"], "en"),
    ("plan-resources",        "Resources and Capacity",      "plan","Plan","#1B6B3A",   r"plan\resources",        False, ["resources","capacity","team","tools"],          ["Resources"], "en"),
    ("plan-budget-confidential","Budget Details (Confidential)","plan","Plan","#1B6B3A",r"plan\budget-confidential",True,["budget","salary","confidential"],              ["Resources","Confidential"], "en"),
    ("plan-roadmap",          "Roadmap Overview",            "plan","Plan","#1B6B3A",   r"plan\roadmap",          False, ["roadmap","milestones","quarterly"],             ["Roadmap"], "en"),
    ("plan-q2-2026",          "Q2 2026 Roadmap",             "plan","Plan","#1B6B3A",   r"plan\roadmap\q2-2026",  False, ["Q2","2026","roadmap","GA","ISO"],               ["Roadmap"], "en"),
    ("plan-h1-milestones",    "H1 2026 Milestones",          "plan","Plan","#1B6B3A",   r"plan\roadmap\milestones\h1-milestones", False, ["milestones","H1","tracker"],    ["Roadmap","Milestones"], "en"),
    ("execute-overview",      "Execute Overview",            "execute","Execute","#9B2335",r"execute\overview",   False, ["execute","execution","sprint"],                 [], "en"),
    ("execute-operations-handbook","Operations Handbook",    "execute","Execute","#9B2335",r"execute\operations-handbook",False,["operations","on-call","SRE","incident"], ["Operations"], "en"),
    ("execute-deployment-runbook","Deployment Runbook",      "execute","Execute","#9B2335",r"execute\deployment-runbook",False,["deployment","CI/CD","kubernetes","bash"],  ["Operations","Runbooks"], "en"),
    ("execute-security-credentials","Security Credentials",  "execute","Execute","#9B2335",r"execute\security-credentials",True,["security","credentials","vault"],        ["Operations","Security"], "en"),
    ("execute-unit-test-guide","Unit Testing Guide",         "execute","Execute","#9B2335",r"execute\quality\testing\unit-test-guide",False,["testing","unit test","AAA","Go"],["Quality","Testing"], "en"),
    ("execute-integration-test-guide","Integration Testing Guide","execute","Execute","#9B2335",r"execute\quality\testing\integration-test-guide",False,["integration","testcontainers"],["Quality","Testing"], "en"),
    ("execute-progress",      "Progress Tracking",           "execute","Execute","#9B2335",r"execute\progress",   False, ["progress","sprint","velocity","KPI"],           ["Sprints"], "en"),
    ("execute-blockers",      "Blockers and Escalation",     "execute","Execute","#9B2335",r"execute\blockers",   False, ["blockers","escalation","mitigation"],           ["Sprints"], "en"),
    ("execute-sprint-26-06",  "Sprint 26-06",                "execute","Execute","#9B2335",r"execute\sprints\sprint-26-06",False,["sprint","planning","stories","standup"], ["Sprints"], "en"),
    ("execute-sprint-26-01",  "Sprint 26-01 Archive",        "execute","Execute","#9B2335",r"execute\sprints\archive\sprint-26-01",False,["sprint","archive","retrospective"],["Sprints","Archive"], "en"),
    ("improve-overview",      "Improve Overview",            "improve","Improve","#4A1942",r"improve\overview",   False, ["improve","continuous improvement","feedback"],   [], "en"),
    ("improve-maturity-model","APEI Capability Maturity Model","improve","Improve","#4A1942",r"improve\maturity-model",False,["maturity","CMM","DORA","capability"],       ["Frameworks"], "en"),
    ("improve-personnel-reviews","Personnel Performance Reviews","improve","Improve","#4A1942",r"improve\personnel-reviews",True,["personnel","performance","confidential"],["HR"], "en"),
    ("improve-recommended-books","Recommended Reading List",  "improve","Improve","#4A1942",r"improve\learning\recommended-books",False,["books","reading","learning"],     ["Learning"], "en"),
    ("improve-engineering-track","Engineering Learning Track","improve","Improve","#4A1942",r"improve\learning\courses\engineering-track",False,["courses","certifications","AWS"],["Learning","Courses"], "en"),
    ("improve-metrics",       "Metrics and Measurement",     "improve","Improve","#4A1942",r"improve\metrics",    False, ["metrics","KPI","measurement","dashboard"],       ["Metrics"], "en"),
    ("improve-quarterly-review","Q1 2026 Quarterly Review",  "improve","Improve","#4A1942",r"improve\quarterly-review",False,["quarterly","OKR","KPI","Q1"],               ["Metrics"], "en"),
    ("improve-retrospective", "Retrospective Guide",         "improve","Improve","#4A1942",r"improve\retrospective",False,["retrospective","lessons","action items"],       ["Retrospectives"], "en"),
    ("improve-q1-2026-retro", "Q1 2026 Retrospective",       "improve","Improve","#4A1942",r"improve\retrospectives\q1-2026-retro",False,["retrospective","start stop continue"],["Retrospectives"], "en"),
    ("improve-q4-2025-retro", "Q4 2025 Retrospective",       "improve","Improve","#4A1942",r"improve\retrospectives\archive\q4-2025-retro",False,["retrospective","Q4","2025","archive"],["Retrospectives","Archive"], "en"),

    # ── VIETNAMESE ─────────────────────────────────────────────────────────────
    ("align-overview-vi",          "Tổng Quan — Liên Kết",            "align","Align","#F2C75C", r"vi\align\overview",        False, ["liên kết","tổng quan","sứ mệnh","tầm nhìn"],    [], "vi"),
    ("align-stakeholders-vi",      "Quản Lý Các Bên Liên Quan",       "align","Align","#F2C75C", r"vi\align\stakeholders",    False, ["bên liên quan","RACI","giao tiếp"],             ["Stakeholders"], "vi"),
    ("align-goals-vi",             "Mục Tiêu và Kết Quả",             "align","Align","#F2C75C", r"vi\align\goals",           False, ["mục tiêu","OKR","SMART"],                       ["Strategy"], "vi"),
    ("align-market-entry-vi",      "Chiến Lược Thâm Nhập Thị Trường", "align","Align","#F2C75C", r"vi\align\strategy\competitive-positioning\market-entry", False, ["GTM","ICP","thâm nhập"], ["Strategy","Competitive Positioning"], "vi"),
    ("align-vision-mission-vi",    "Tuyên Bố Sứ Mệnh",                "align","Align","#F2C75C", r"vi\align\vision\mission-statement", False, ["sứ mệnh","tầm nhìn","mục đích"],       ["Vision"], "vi"),
    ("align-vision-core-values-vi","Giá Trị Cốt Lõi",                 "align","Align","#F2C75C", r"vi\align\vision\values\core-values", False, ["giá trị","văn hóa","chính trực"],      ["Vision","Values"], "vi"),
    ("align-vision-guiding-principles-vi","Nguyên Tắc Định Hướng",    "align","Align","#F2C75C", r"vi\align\vision\values\guiding-principles", False, ["nguyên tắc","kỹ thuật"],        ["Vision","Values"], "vi"),
    ("plan-overview-vi",           "Tổng Quan — Lập Kế Hoạch",        "plan","Plan","#1B6B3A",   r"vi\plan\overview",         False, ["kế hoạch","lập kế hoạch","phương pháp"],        [], "vi"),
    ("plan-resources-vi",          "Nguồn Lực và Năng Lực",           "plan","Plan","#1B6B3A",   r"vi\plan\resources",        False, ["nguồn lực","năng lực","nhóm","công cụ"],        ["Resources"], "vi"),
    ("plan-q2-2026-vi",            "Lộ Trình Q2 2026",                 "plan","Plan","#1B6B3A",   r"vi\plan\roadmap\q2-2026",  False, ["lộ trình","Q2","2026","GA","ISO"],               ["Roadmap"], "vi"),
    ("plan-h1-milestones-vi",      "Cột Mốc H1 2026",                  "plan","Plan","#1B6B3A",   r"vi\plan\roadmap\milestones\h1-milestones", False, ["cột mốc","H1","theo dõi"],      ["Roadmap","Milestones"], "vi"),
    ("execute-overview-vi",        "Tổng Quan — Thực Thi",             "execute","Execute","#9B2335",r"vi\execute\overview",  False, ["thực thi","sprint","thực hiện"],                [], "vi"),
    ("execute-sprint-26-06-vi",    "Sprint 26-06",                      "execute","Execute","#9B2335",r"vi\execute\sprints\sprint-26-06", False, ["sprint","lập kế hoạch","nhiệm vụ"],  ["Sprints"], "vi"),
    ("execute-unit-test-guide-vi", "Hướng Dẫn Unit Test",              "execute","Execute","#9B2335",r"vi\execute\quality\testing\unit-test-guide", False, ["kiểm thử","unit test","Go"],["Quality","Testing"], "vi"),
    ("improve-overview-vi",        "Tổng Quan — Cải Tiến",             "improve","Improve","#4A1942",r"vi\improve\overview",  False, ["cải tiến","liên tục","phản hồi"],               [], "vi"),
    ("improve-q1-2026-retro-vi",   "Hồi Cố Q1 2026",                   "improve","Improve","#4A1942",r"vi\improve\retrospectives\q1-2026-retro", False, ["hồi cố","Q1","bắt đầu dừng tiếp tục"],["Retrospectives"], "vi"),
    ("improve-recommended-books-vi","Danh Sách Sách Đề Xuất",          "improve","Improve","#4A1942",r"vi\improve\learning\recommended-books", False, ["sách","đọc sách","học hỏi"],    ["Learning"], "vi"),
]

documents = []
for row in DOCS:
    doc_id, title, section, sectionLabel, sectionColor, rel_path, restricted, tags, breadcrumb, lang = row
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
        "content": content, "tags": tags, "lang": lang
    })

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"documents": documents}, f, ensure_ascii=False, separators=(',',':'))

print("Written " + str(len(documents)) + " documents")
for d in documents:
    r = " [RESTRICTED]" if d["restricted"] else ""
    crumb = " > ".join(d["breadcrumb"]) if d["breadcrumb"] else "(root)"
    print("  [" + d["lang"].upper() + "/" + d["section"].upper() + "] " + crumb + " > " + d["title"] + r)
