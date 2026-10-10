"""
Build a fully self-contained static HTML portfolio site from portfolio_content.py.
Output goes to  static-site/index.html  (all CSS/JS inlined, one file).
Run:  python build_static.py
"""

from __future__ import annotations
from data import portfolio_content as C
import base64, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ── helpers ────────────────────────────────────────────────────────────────
def esc(s: str) -> str:
    return (str(s)
        .replace("&", "&amp;").replace("<", "&lt;")
        .replace(">", "&gt;").replace('"', "&quot;"))

def img_b64(rel: str, fallback_icon: str = "🖼️") -> str:
    """Return an <img> tag with base64 data-URI, or a placeholder div."""
    p = ROOT / rel
    if rel and p.is_file():
        ext = p.suffix.lstrip(".").lower()
        mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png",
                "gif": "gif", "webp": "webp"}.get(ext, "png")
        data = base64.b64encode(p.read_bytes()).decode()
        return f'<img src="data:image/{mime};base64,{data}" alt="image" loading="lazy">'
    return f'<div class="img-ph">{fallback_icon}<span>Image to be added</span></div>'

def profile_img() -> str:
    p = ROOT / C.STUDENT.get("profile_image", "")
    if p.is_file():
        data = base64.b64encode(p.read_bytes()).decode()
        return f'<img src="data:image/jpeg;base64,{data}" alt="{esc(C.STUDENT["name"])}" class="profile-img">'
    initials = "".join(w[0] for w in C.STUDENT["name"].split()[:2]).upper()
    return f'<div class="profile-avatar">{esc(initials)}<span class="pa-hint">Replace with your photo</span></div>'

def bullet(items) -> str:
    lis = "".join(f"<li>{esc(str(i))}</li>" for i in items)
    return f"<ul class='bullet-list'>{lis}</ul>"

def chip(items) -> str:
    spans = "".join(f"<span class='chip'>{esc(str(i))}</span>" for i in items)
    return f"<div class='chip-wrap'>{spans}</div>"

def tech_tags(items) -> str:
    spans = "".join(f"<span class='tech'>{esc(str(i))}</span>" for i in items)
    return f"<div class='tech-tags'>{spans}</div>"

def status_pill(label: str, kind: str = "amber") -> str:
    return f"<span class='status-pill {esc(kind)}'>{esc(label)}</span>"

def reflection_box(title: str, text: str) -> str:
    return (f"<div class='reflection'>"
            f"<div class='reflection-title'>{esc(title)}</div>"
            f"<p>{esc(text)}</p></div>")

def placeholder_note(text: str) -> str:
    return f"<div class='placeholder-note'>✎ {esc(text)}</div>"

def link_btn(label: str, url: str) -> str:
    if url:
        return f"<a href='{esc(url)}' target='_blank' class='btn btn-primary'>{esc(label)}</a>"
    return (f"<button class='btn btn-disabled' disabled>{esc(label)}</button>"
            f"<span class='btn-note'>Link to be added</span>")

def fact_list(items) -> str:
    rows = "".join(
        f"<div class='fact'><span class='k'>{esc(k)}</span><span class='v'>{esc(v)}</span></div>"
        for k, v in items)
    return f"<div class='fact-list'>{rows}</div>"

def timeline_html(items) -> str:
    rows = "".join(
        f"<div class='tl-item'><div class='tl-card'><h4>{esc(t)}</h4><p>{esc(b)}</p></div></div>"
        for t, b in items)
    return f"<div class='timeline'>{rows}</div>"

def card3(icon: str, title: str, body: str, accent: str = "") -> str:
    return (f"<div class='card {esc(accent)}'>"
            f"<div class='card-icon'>{icon}</div>"
            f"<h3 class='card-title'>{esc(title)}</h3>"
            f"<p class='card-body'>{esc(body)}</p></div>")

def plain_card(title: str, body: str, accent: str = "") -> str:
    return (f"<div class='card {esc(accent)}'>"
            f"<h3 class='card-title'>{esc(title)}</h3>"
            f"<p class='card-body'>{esc(body)}</p></div>")

def card_grid(items, cols: int = 3, accents=None, plain: bool = False) -> str:
    acc_list = accents or []
    cards = ""
    for idx, item in enumerate(items):
        acc = acc_list[idx % len(acc_list)] if acc_list else ""
        if plain:
            cards += plain_card(item[0], item[1], acc)
        else:
            cards += card3(item[0], item[1], item[2], acc)
    return f"<div class='grid grid-{cols}'>{cards}</div>"

def evidence_card(item: dict, i: int) -> str:
    thumb = img_b64(item.get("image", "")) if item.get("image") else ""
    title = f"<h4 class='card-title'>{esc(item.get('title',''))}</h4>" if item.get("title") else placeholder_note("Title to be added")
    desc  = f"<p class='card-body'>{esc(item.get('description',''))}</p>" if item.get("description") else placeholder_note("Description to be added")
    btn   = link_btn("Open evidence", item.get("url",""))
    return (f"<div class='evidence-card'>{thumb}{title}{desc}"
            f"<div class='btn-row'>{btn}</div></div>")

def evidence_area(items, empty_msg: str) -> str:
    if not items:
        return placeholder_note(empty_msg)
    return "".join(evidence_card(it, i) for i, it in enumerate(items))

def field(label: str, value: str) -> str:
    if value:
        return f"<p class='card-body'><b>{esc(label)}.</b> {esc(value)}</p>"
    return f"<p class='card-body'><b>{esc(label)}</b></p>" + placeholder_note("To be added")

# ── section builders ────────────────────────────────────────────────────────

def page_about() -> str:
    a = C.ABOUT
    accents = ["accent-blue","accent-purple","accent-lav"]
    accents2 = ["accent-purple","accent-blue","accent-pink"]
    return f"""
<div class="hero">
  <span class="hero-shape s1"></span><span class="hero-shape s2"></span><span class="hero-shape s3"></span>
  <div class="hero-sub">{esc(a["subtitle"])}</div>
  <div class="hero-title">{esc(a["hero_title"])}</div>
  <p class="hero-text">{esc(a["intro"])}</p>
</div>

<h3 class="section-title">Who I Am</h3>
<div class="two-col">
  <div>{profile_img()}</div>
  <div><p class="card-body" style="font-size:.97rem">{esc(a["who_i_am"])}</p></div>
</div>
<div class="divider"></div>

<h3 class="section-title">Why I Chose the IBCP</h3>
<div class="card accent-blue"><p class="card-body">{esc(a["why_ibcp"])}</p></div>

<h3 class="section-title">Why Artificial Intelligence?</h3>
<div class="card accent-purple"><p class="card-body">{esc(a["why_ai"])}</p></div>
<div class="divider"></div>

<h3 class="section-title">My Academic Journey</h3>
{fact_list(a["journey_facts"])}
{timeline_html(a["journey_timeline"])}
<div class="divider"></div>

<h3 class="section-title">My Interests</h3>
{card_grid(a["interests"], 3, accents)}
<h3 class="section-title">My Strengths</h3>
{card_grid(a["strengths"], 3, accents2)}
<div class="divider"></div>

<h3 class="section-title">My Approach to Learning</h3>
{reflection_box("How I learn", a["approach"])}

<div class="quote-card"><p class="quote">"{esc(a["quote"])}"</p></div>
<div class="divider"></div>
<div class="glass"><p class="card-body" style="margin:0">
Thank you for visiting. Use the navigation above to explore my DP subjects,
core components, AI projects, activities, achievements and contact details.
</p></div>
"""

def dp_physics() -> str:
    d = C.DP["Physics HL"]
    csp = d["csp"]
    ia  = d["ia"]
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body">{esc(d["learning_experience"])}</p>
<div class="divider"></div>
<h3 class="section-title">Coursework — Collaborative Science Project (CSP)</h3>
<div class="card accent-blue">
  <h3 class="card-title">{esc(csp["title"])}</h3>
  <p class="card-body"><b>Overview.</b> {esc(csp["overview"])}</p>
  <p class="card-body"><b>Aim.</b> {esc(csp["aim"])}</p>
</div>
<p class="card-body"><b>Scientific principles</b></p>{bullet(csp["principles"])}
<p class="card-body"><b>Teamwork.</b> {esc(csp["teamwork"])}</p>
<p class="card-body"><b>What I learned.</b> {esc(csp["learned"])}</p>
{reflection_box("Reflection", csp["reflection"])}
<div class="btn-row">{link_btn("View My CSP Presentation", csp.get("presentation_url",""))}</div>
<div class="divider"></div>
<h3 class="section-title">Internal Assessment (IA)</h3>
{status_pill(ia["status"])}
<p class="card-body" style="margin-top:.7rem"><b>Topic.</b> {esc(ia["topic"])}</p>
<p class="card-body"><b>Research question.</b> {esc(ia["research_question"])}</p>
<p class="card-body"><b>Overview.</b> {esc(ia["overview"])}</p>
<p class="card-body"><b>Variables</b></p>{bullet(ia["variables"])}
<p class="card-body"><b>Approach.</b> {esc(ia["approach"])}</p>
<p class="card-body"><b>Data collection.</b> {esc(ia["data_collection"])}</p>
<p class="card-body"><b>Analysis.</b> {esc(ia["analysis"])}</p>
{placeholder_note(ia["notice"])}
<h4 class="mini-head">Evidence</h4>
{evidence_area(ia.get("evidence",[]), "IA evidence will be added when ready.")}
<div class="divider"></div>
{reflection_box("Reflection on Physics", d["reflection"])}
"""

def dp_chemistry() -> str:
    d = C.DP["Chemistry SL"]
    csp = d["csp"]
    ia  = d["ia"]
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body">{esc(d["learning_experience"])}</p>
<div class="divider"></div>
<h3 class="section-title">Coursework — Collaborative Science Project (CSP)</h3>
<div class="card">
  <h3 class="card-title">Chemistry CSP</h3>
  {field("Project title", csp.get("title",""))}
  {field("Overview", csp.get("overview",""))}
  {field("Aim", csp.get("aim",""))}
  {field("Scientific concepts", csp.get("concepts",""))}
  {field("My contribution", csp.get("contribution",""))}
  {field("Skills developed", csp.get("skills",""))}
  {field("Reflection", csp.get("reflection",""))}
  <div class="btn-row">{link_btn("Watch My CSP Project Video", csp.get("video_url",""))}</div>
</div>
<div class="divider"></div>
<h3 class="section-title">Internal Assessment (IA)</h3>
{status_pill(ia["status"])}
<p class="card-body" style="margin-top:.7rem"><b>Topic.</b> {esc(ia["topic"])}</p>
<p class="card-body"><b>Research question.</b> {esc(ia["research_question"])}</p>
<p class="card-body"><b>Background.</b> {esc(ia["background"])}</p>
<p class="card-body"><b>Variables</b></p>{bullet(ia["variables"])}
<p class="card-body"><b>Method.</b> {esc(ia["method"])}</p>
<p class="card-body"><b>Data collection.</b> {esc(ia["data_collection"])}</p>
<p class="card-body"><b>Analysis.</b> {esc(ia["analysis"])}</p>
<p class="card-body"><b>Evaluation.</b> {esc(ia["evaluation"])}</p>
{placeholder_note(ia["notice"])}
<h4 class="mini-head">Evidence</h4>
{evidence_area(ia.get("evidence",[]), "IA evidence will be added when ready.")}
<div class="divider"></div>
{reflection_box("Reflection on Chemistry", d["reflection"])}
"""

def dp_math() -> str:
    d = C.DP["Mathematics AA HL"]
    ia  = d["ia"]
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body">{esc(d["learning_experience"])}</p>
<div class="divider"></div>
<h3 class="section-title">Concepts Covered</h3>
{card_grid(d["concepts"], 3, ["accent-blue","accent-purple","accent-lav"], plain=True)}
<div class="divider"></div>
<h3 class="section-title">Classwork and Evidence</h3>
<p class="card-body">{esc(d["classwork_intro"])}</p>
{evidence_area(d.get("classwork_evidence",[]), "Classwork evidence will be added as the course continues.")}
<div class="divider"></div>
<h3 class="section-title">My Mathematics IA</h3>
{status_pill(ia["status"])}
<br><br>
{field("IA title", ia.get("title",""))}
{field("Research question", ia.get("research_question",""))}
{placeholder_note(ia["notice"])}
<div class="btn-row">{link_btn("View My Mathematics IA", ia.get("document_url",""))}</div>
{evidence_area(ia.get("evidence",[]), "IA evidence will be added when ready.")}
<div class="divider"></div>
{reflection_box("Reflection on Mathematics", d["reflection"])}
"""

def dp_english() -> str:
    d = C.DP["English B SL"]
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
{reflection_box("Where I am starting from", d["learning_experience"])}
<div class="divider"></div>
<h3 class="section-title">Themes</h3>
{card_grid(d["themes"], 2, ["accent-blue","accent-purple","accent-lav","accent-pink"], plain=True)}
<div class="divider"></div>
<h3 class="section-title">Learning Experiences</h3>
{bullet(d["learning_experiences"])}
<div class="divider"></div>
<h3 class="section-title">Future Evidence</h3>
<p class="card-body">{esc(d["future_evidence_intro"])}</p>
{evidence_area(d.get("future_evidence",[]), "Presentations, written work and oral tasks will be added here.")}
<div class="divider"></div>
{reflection_box("Reflection on English B", d["reflection"])}
"""

def core_pps() -> str:
    d = C.CORE["Personal and Professional Skills"]
    outcomes_html = ""
    for o in d["outcomes"]:
        code = o["code"]
        heading = f'{code} — {o["outcome"]}' if o.get("outcome") else code
        outcomes_html += f"""
<details class="expander">
  <summary>{esc(heading)}</summary>
  <div class="expander-body">
    {field("Outcome", o.get("outcome",""))}
    {field("What I did", o.get("what_i_did",""))}
    {field("Skills developed", o.get("skills",""))}
    {field("Evidence", o.get("evidence",""))}
    {field("Reflection", o.get("reflection",""))}
  </div>
</details>"""
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body"><b>What it is.</b> {esc(d["what_is"])}</p>
<p class="card-body"><b>My journey.</b> {esc(d["journey"])}</p>
<div class="divider"></div>
<h3 class="section-title">Skills I Am Developing</h3>
{card_grid(d["skills"], 3, ["accent-blue","accent-purple","accent-lav"])}
<div class="divider"></div>
<h3 class="section-title">Learning Outcomes</h3>
{outcomes_html}
<div class="divider"></div>
<h3 class="section-title">My PPS Work</h3>
{evidence_area(d.get("evidence_links",[]), "PPS evidence will be linked here when ready.")}
<div class="divider"></div>
{reflection_box("Reflection on PPS", d["reflection"])}
"""

def core_lcs() -> str:
    d = C.CORE["Language and Cultural Studies"]
    eng_html = ""
    for idx, eng in enumerate(d.get("engagements",[])):
        thumb = img_b64(eng.get("image","")) if eng.get("image") else ""
        eng_html += f"""<div class="card">{thumb}
{field("Engagement title", eng.get("title",""))}
{field("Description", eng.get("description",""))}
{field("Topic / issue explored", eng.get("topic",""))}
{field("What I learned", eng.get("learned",""))}
{field("Perspective considered", eng.get("perspective",""))}
<div class="btn-row">{link_btn("Open engagement", eng.get("url",""))}</div>
</div>"""
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body"><b>What it is.</b> {esc(d["what_is"])}</p>
<p class="card-body"><b>Learning engagements.</b> {esc(d["engagements_intro"])}</p>
<div class="divider"></div>
<h3 class="section-title">Learning Engagements</h3>
{eng_html or placeholder_note("Learning engagements will be added here.")}
<div class="divider"></div>
{reflection_box("Reflection", d["reflection"])}
<div class="divider"></div>
<h3 class="section-title">Skills Developed</h3>
{chip(d["skills"])}
<div class="divider"></div>
<h3 class="section-title">Canva / Evidence Links</h3>
{evidence_area(d.get("evidence_links",[]), "Canva links and other evidence will be added here.")}
"""

def core_reflective() -> str:
    d = C.CORE["Reflective Project"]
    sections_html = "".join(field(t, c) for t, c in d["sections"])
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body"><b>My research question.</b> {esc(d["research_question"])}</p>
<p class="card-body"><b>What it is.</b> {esc(d["what_is"])}</p>
<p class="card-body"><b>The ethical dilemma.</b> {esc(d["dilemma"])}</p>
<div class="divider"></div>
<h3 class="section-title">Stakeholders</h3>
{card_grid(d["stakeholders"], 3, ["accent-blue","accent-purple","accent-lav"])}
<div class="divider"></div>
<h3 class="section-title">Research and Analysis</h3>
{sections_html}
<div class="divider"></div>
{status_pill(d["status"])}
<br><br>
{placeholder_note(d["notice"])}
<div class="btn-row">{link_btn("View My Reflective Project", d.get("document_url",""))}</div>
"""

def core_community() -> str:
    d = C.CORE["Community Engagement"]
    proj = d["project"]
    return f"""
<h3 class="section-title">{esc(d["title"])}</h3>
<p class="card-body"><b>What it is.</b> {esc(d["what_is"])}</p>
<div class="divider"></div>
<div class="card accent-purple">
  <h3 class="card-title">{esc(proj["name"])}</h3>
  <p class="card-body"><b>Location.</b> {esc(proj["location"])}</p>
  <p class="card-body">{esc(proj["overview"])}</p>
</div>
<p class="card-body"><b>Why embroidery?</b> {esc(proj["why_embroidery"])}</p>
<h3 class="section-title">What We Did</h3>
{card_grid(proj["activities"], 3, ["accent-blue","accent-purple","accent-lav"])}
<h3 class="section-title">What I Developed</h3>
{bullet(proj["developed"])}
<div class="divider"></div>
<h3 class="section-title">Evidence</h3>
<h4 class="mini-head">Project Proposal</h4>
{evidence_card(proj["proposal"], 0)}
<h4 class="mini-head">Community Engagement Learning Journal</h4>
{evidence_card(proj["journal"], 1)}
"""

def page_crs() -> str:
    d = C.CRS
    projects_html = ""
    for proj in d["projects"]:
        feats = bullet(proj.get("features",[]))
        techs = tech_tags(proj.get("technologies",[]))
        thumb = img_b64(proj.get("image",""), "🖥️")
        projects_html += f"""
<div class="project-card">
  <div class="project-media">{thumb}</div>
  <div class="project-body">
    <div class="project-title">{proj.get("icon","")} {esc(proj.get("name",""))}</div>
    <p class="card-body">{esc(proj.get("intro",""))}</p>
    <p class="card-body"><b>Problem.</b> {esc(proj.get("problem",""))}</p>
    <p class="card-body"><b>Purpose.</b> {esc(proj.get("purpose",""))}</p>
    <p class="card-body"><b>Key features</b></p>{feats}
    {techs}
    <p class="card-body"><b>What I learned.</b> {esc(proj.get("learning",""))}</p>
    <div class="btn-row">
      {link_btn("GitHub", proj.get("github",""))}
      {link_btn("Live App", proj.get("streamlit",""))}
      {link_btn("Presentation", proj.get("presentation",""))}
    </div>
  </div>
</div>"""
    return f"""
<p class="card-body"><b>What it is.</b> {esc(d["what_is"])}</p>
{reflection_box("Why Artificial Intelligence?", d["why_ai"])}
<div class="divider"></div>
<h3 class="section-title">Areas of Learning</h3>
<p class="card-body">These are the areas I am exploring through my CRS. They describe areas of learning rather than verified proficiency levels.</p>
{card_grid(d["skills"], 4, ["accent-blue","accent-purple","accent-lav","accent-pink"])}
<div class="divider"></div>
<h3 class="section-title">Project Showcase</h3>
{projects_html}
<div class="divider"></div>
{reflection_box("Reflection on my CRS", d["reflection"])}
"""

def page_activities() -> str:
    d = C.ACTIVITIES
    return f"""
<p class="card-body">{esc(d["intro"])}</p>
{card_grid(d["cards"], 3, ["accent-blue","accent-purple","accent-lav","accent-pink"])}
<div class="divider"></div>
<h3 class="section-title">Photos</h3>
{placeholder_note("Photos will be added here when they are ready.") if not d.get("photos") else ""}
"""

def page_certificates() -> str:
    d = C.CERTIFICATES
    items = d.get("items",[])
    confirmed_html = fact_list(d["confirmed"])
    cats_html = chip(d["sections"])
    if items:
        cols = ""
        for i, it in enumerate(items):
            thumb = img_b64(it.get("image",""))
            btn   = link_btn("View certificate", it.get("url",""))
            cols += f"""<div class='cert-card'>{thumb}
<h4 class='card-title'>{esc(it.get("title","Certificate"))}</h4>
<p class='cert-org'>{esc(it.get("organisation",""))}</p>
<p class='cert-date'>{esc(it.get("date",""))}</p>
<p class='card-body'>{esc(it.get("description",""))}</p>
<div class='btn-row'>{btn}</div></div>"""
        gallery = f"<div class='grid grid-3'>{cols}</div>"
    else:
        gallery = placeholder_note(
            "No certificates have been added yet. Add real certificates in "
            "data/portfolio_content.py and they will appear here automatically.")
    return f"""
<h3 class="section-title">Confirmed Academic Details</h3>
{confirmed_html}
<div class="divider"></div>
<h3 class="section-title">Categories</h3>
{cats_html}
<div class="divider"></div>
<h3 class="section-title">Certificates and Achievements</h3>
{gallery}
"""

def page_contact() -> str:
    contact = C.CONTACT
    student = C.STUDENT
    email_btn   = link_btn("Open Email",    "mailto:"+contact["email"] if contact.get("email") else "")
    github_btn  = link_btn("Open GitHub",   contact.get("github",""))
    li_btn      = link_btn("Open LinkedIn", contact.get("linkedin",""))
    return f"""
<div class="card">
  <h3 class="card-title">{esc(student["name"])}</h3>
  {fact_list([
      ("Grade / Programme", f'{student["grade"]} · {student["programme"]}'),
      ("School", student["school"]),
      ("Career-related Study", student["crs"]),
  ])}
</div>
<div class="grid grid-3" style="margin-top:1rem">
  <div class="contact-card"><h4>Email</h4><div class="btn-row">{email_btn}</div></div>
  <div class="contact-card"><h4>GitHub</h4><div class="btn-row">{github_btn}</div></div>
  <div class="contact-card"><h4>LinkedIn</h4><div class="btn-row">{li_btn}</div></div>
</div>
<div class="divider"></div>
{reflection_box("Thank you", contact["thank_you"])}
"""

# ── CSS ─────────────────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap');
:root {
  --bg:#F5F7FA; --card:#FFFFFF; --primary:#2F80ED; --lavender:#B9A7FF;
  --purple:#8B5CF6; --blush:#FFD6E7; --text:#1F2937; --secondary:#667085;
  --border:#E5E7EB;
  --grad:linear-gradient(120deg,#2F80ED 0%,#8B5CF6 55%,#EC4899 100%);
  --grad-soft:linear-gradient(120deg,rgba(47,128,237,.10),rgba(139,92,246,.10),rgba(255,214,231,.35));
  --shadow-sm:0 2px 8px rgba(31,41,55,.05);
  --shadow-md:0 10px 28px rgba(31,41,55,.08);
  --shadow-lg:0 20px 48px rgba(31,41,55,.10);
  --r:18px; --r-sm:12px; --r-lg:24px;
  --font-body:'Inter',system-ui,sans-serif;
  --font-head:'Poppins','Inter',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{font-family:var(--font-body);color:var(--text);background:
  radial-gradient(38rem 38rem at 8% 0%,rgba(47,128,237,.07),transparent 60%),
  radial-gradient(34rem 34rem at 96% 4%,rgba(139,92,246,.07),transparent 60%),
  radial-gradient(34rem 34rem at 80% 100%,rgba(255,214,231,.35),transparent 60%),
  var(--bg); min-height:100vh;}
h1,h2,h3,h4,h5{font-family:var(--font-head);color:var(--text);font-weight:700}
p,li{color:var(--text)}
a{color:var(--primary)}

/* ── Layout ── */
.site-wrap{max-width:1120px;margin:0 auto;padding:0 1.2rem 3rem}

/* ── Topbar ── */
.topbar{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;
  gap:.5rem;padding:1rem 1.2rem .5rem;max-width:1120px;margin:0 auto}
.tb-brand{font-family:var(--font-head);font-weight:700;font-size:1.05rem}
.tb-tag{font-size:.8rem;color:var(--secondary)}

/* ── Main nav ── */
.main-nav{display:flex;flex-wrap:wrap;gap:.4rem;padding:.5rem 1.2rem .8rem;
  max-width:1120px;margin:0 auto}
.main-nav button{background:var(--card);border:1px solid var(--border);
  border-radius:999px;padding:.42rem .95rem;font-size:.87rem;font-weight:600;
  color:var(--secondary);cursor:pointer;transition:.18s}
.main-nav button:hover{border-color:var(--primary);color:var(--primary)}
.main-nav button.active{background:var(--primary);color:#fff;border-color:var(--primary)}

/* ── Sub nav ── */
.sub-nav{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.2rem}
.sub-nav button{background:var(--card);border:1px solid var(--border);
  border-radius:var(--r-sm);padding:.38rem .85rem;font-size:.84rem;font-weight:600;
  color:var(--secondary);cursor:pointer;transition:.18s}
.sub-nav button:hover{border-color:var(--purple);color:var(--purple)}
.sub-nav button.active{background:var(--purple);color:#fff;border-color:var(--purple)}

/* ── Page header ── */
.page-head{margin:.2rem 0 1.2rem}
.eyebrow{display:inline-block;font-size:.73rem;font-weight:700;letter-spacing:.14em;
  text-transform:uppercase;color:var(--primary);margin-bottom:.3rem}
.page-title{font-size:1.9rem;line-height:1.2;margin:.1rem 0 .35rem}
.page-sub{color:var(--secondary);font-size:1rem;max-width:760px}
.nav-underline{height:3px;border-radius:999px;margin:.2rem 0 1.4rem;
  background:var(--grad);opacity:.85}
.section-title{font-size:1.28rem;margin:1.4rem 0 .6rem}
.divider{height:1px;margin:1.6rem 0;background:linear-gradient(90deg,transparent,var(--border),transparent)}
.mini-head{font-family:var(--font-head);font-weight:700;font-size:1rem;
  color:var(--text);margin:.9rem 0 .5rem}

/* ── Hero ── */
.hero{position:relative;overflow:hidden;border-radius:var(--r-lg);
  padding:2.4rem 2rem;color:#fff;box-shadow:var(--shadow-lg);background:var(--grad)}
.hero-title{color:#fff;font-size:2.1rem;margin:.2rem 0 .4rem}
.hero-sub{color:rgba(255,255,255,.95);font-weight:600;letter-spacing:.02em;margin-bottom:.2rem}
.hero-text{color:rgba(255,255,255,.95);max-width:780px;margin-top:.7rem}
.hero-shape{position:absolute;border-radius:50%;background:rgba(255,255,255,.12)}
.hero-shape.s1{width:200px;height:200px;top:-70px;left:-40px}
.hero-shape.s2{width:120px;height:120px;bottom:-40px;right:8%}
.hero-shape.s3{width:70px;height:70px;top:22%;right:16%}

/* ── Cards ── */
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);
  padding:1.2rem 1.3rem;margin-bottom:1rem;box-shadow:var(--shadow-sm);
  transition:transform .22s,box-shadow .22s}
.card:hover{transform:translateY(-3px);box-shadow:var(--shadow-md)}
.card-icon{font-size:1.5rem;line-height:1;margin-bottom:.5rem}
.card-title{font-size:1rem;margin:0 0 .35rem}
.card-body{color:var(--secondary);font-size:.93rem;margin-bottom:.45rem;line-height:1.6}
.card-body b{color:var(--text)}
.accent-blue{border-left:4px solid var(--primary)}
.accent-purple{border-left:4px solid var(--purple)}
.accent-lav{border-left:4px solid var(--lavender)}
.accent-pink{border-left:4px solid #EC4899}

.glass{background:rgba(255,255,255,.72);border:1px solid rgba(255,255,255,.9);
  border-radius:var(--r);padding:1.3rem;margin-bottom:1rem;
  box-shadow:var(--shadow-md);backdrop-filter:blur(12px)}

/* ── Grids ── */
.grid{display:grid;gap:1rem}
.grid-2{grid-template-columns:repeat(2,minmax(0,1fr))}
.grid-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.grid-4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media(max-width:1000px){.grid-4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:900px){.grid-3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){.grid-2,.grid-3,.grid-4{grid-template-columns:1fr}}

/* ── Two-col for who-i-am ── */
.two-col{display:grid;grid-template-columns:220px 1fr;gap:1.8rem;align-items:start;margin-bottom:1.2rem}
@media(max-width:700px){.two-col{grid-template-columns:1fr}}

/* ── Status pill ── */
.status-pill{display:inline-flex;align-items:center;gap:.4rem;font-size:.78rem;
  font-weight:700;padding:.3rem .75rem;border-radius:999px;
  background:rgba(245,158,11,.12);color:#B45309;border:1px solid rgba(245,158,11,.3)}
.status-pill::before{content:"";width:7px;height:7px;border-radius:50%;background:#F59E0B}

/* ── Placeholders ── */
.placeholder-note{display:flex;align-items:center;gap:.5rem;font-size:.88rem;
  color:var(--secondary);background:rgba(185,167,255,.14);
  border:1px solid rgba(185,167,255,.4);border-radius:var(--r-sm);
  padding:.6rem .85rem;margin:.4rem 0}
.img-ph{display:grid;place-items:center;gap:.3rem;text-align:center;
  border-radius:var(--r-sm);border:2px dashed #D7DCE5;
  background:rgba(102,112,133,.05);color:var(--secondary);
  font-size:.86rem;padding:2rem 1rem;min-height:120px}
.img-ph span{font-size:.8rem}

/* ── Reflection ── */
.reflection{background:var(--grad-soft);border:1px solid var(--border);
  border-radius:var(--r);padding:1.1rem 1.3rem;margin:1rem 0}
.reflection-title{font-family:var(--font-head);font-weight:700;font-size:.95rem;
  margin:0 0 .3rem;color:var(--purple)}
.reflection p{margin:0;color:var(--text);font-size:.94rem}

/* ── Quote ── */
.quote-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);
  padding:1.2rem 1.4rem;box-shadow:var(--shadow-sm);text-align:center;margin:1rem 0}
.quote{font-family:var(--font-head);font-style:italic;font-size:1.05rem;color:var(--primary)}

/* ── Fact list ── */
.fact-list{display:grid;gap:.5rem;margin:.5rem 0 1rem}
.fact{display:flex;justify-content:space-between;gap:1rem;padding:.55rem .8rem;
  border-radius:var(--r-sm);background:rgba(47,128,237,.05);border:1px solid var(--border)}
.fact .k{color:var(--secondary);font-size:.85rem;font-weight:600}
.fact .v{color:var(--text);font-size:.88rem;font-weight:600;text-align:right}

/* ── Timeline ── */
.timeline{position:relative;margin:.6rem 0 1rem;padding-left:1.5rem;
  border-left:2px solid var(--border)}
.tl-item{position:relative;margin-bottom:1rem}
.tl-item::before{content:"";position:absolute;left:-1.95rem;top:.35rem;
  width:12px;height:12px;border-radius:50%;background:var(--grad);
  box-shadow:0 0 0 3px rgba(139,92,246,.15)}
.tl-card{background:var(--card);border:1px solid var(--border);
  border-radius:var(--r-sm);padding:.9rem 1.1rem;box-shadow:var(--shadow-sm)}
.tl-card h4{margin:0 0 .25rem;font-size:.98rem}
.tl-card p{color:var(--secondary);font-size:.88rem;margin:0}

/* ── Bullet list ── */
.bullet-list{margin:.3rem 0 .6rem;padding-left:1.1rem;color:var(--secondary);font-size:.87rem}
.bullet-list li{margin-bottom:.25rem}

/* ── Chip ── */
.chip-wrap{display:flex;flex-wrap:wrap;gap:.5rem;margin:.5rem 0 1rem}
.chip{display:inline-block;padding:.38rem .8rem;border-radius:999px;font-size:.82rem;
  font-weight:600;color:var(--purple);background:rgba(185,167,255,.18);
  border:1px solid rgba(185,167,255,.45)}

/* ── Tech tags ── */
.tech-tags{display:flex;flex-wrap:wrap;gap:.4rem;margin:.5rem 0 .7rem}
.tech{font-size:.74rem;font-weight:600;padding:.25rem .6rem;border-radius:8px;
  background:rgba(139,92,246,.12);color:var(--purple)}

/* ── Buttons ── */
.btn-row{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:.8rem;align-items:center}
.btn{display:inline-flex;align-items:center;padding:.45rem 1rem;border-radius:12px;
  font-size:.88rem;font-weight:600;text-decoration:none;cursor:pointer;
  border:none;transition:.18s}
.btn-primary{background:var(--grad);color:#fff}
.btn-primary:hover{opacity:.88;color:#fff}
.btn-disabled{background:var(--border);color:var(--secondary);cursor:not-allowed}
.btn-note{font-size:.78rem;color:var(--secondary)}

/* ── Profile ── */
.profile-img{width:100%;border-radius:var(--r);object-fit:cover;display:block}
.profile-avatar{display:grid;place-items:center;min-height:180px;
  border-radius:var(--r);background:var(--grad);color:#fff;font-family:var(--font-head);
  font-size:3rem;font-weight:700;position:relative;padding-bottom:2rem}
.pa-hint{position:absolute;bottom:.7rem;font-size:.78rem;font-weight:400;
  letter-spacing:.02em;opacity:.85}

/* ── Evidence card ── */
.evidence-card{background:var(--card);border:1px solid var(--border);
  border-radius:var(--r);padding:1rem 1.1rem;box-shadow:var(--shadow-sm);margin-bottom:1rem}
.evidence-card h4{margin:0 0 .3rem;font-size:1rem}
.evidence-card img{width:100%;border-radius:var(--r-sm);margin-bottom:.7rem}

/* ── Project card ── */
.project-card{background:var(--card);border:1px solid var(--border);
  border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-md);margin-bottom:1.2rem;
  transition:transform .22s,box-shadow .22s}
.project-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg)}
.project-media{height:168px;background:var(--grad);display:grid;place-items:center;overflow:hidden}
.project-media img{width:100%;height:100%;object-fit:cover}
.project-body{padding:1.1rem 1.3rem 1.3rem}
.project-title{font-family:var(--font-head);font-size:1.12rem;font-weight:700;margin:0 0 .4rem}

/* ── Certificate card ── */
.cert-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);
  padding:1rem 1.1rem;box-shadow:var(--shadow-sm);margin-bottom:1rem}
.cert-org{color:var(--primary);font-size:.82rem;font-weight:600;margin:.1rem 0}
.cert-date{color:var(--secondary);font-size:.78rem;margin:.1rem 0 .4rem}

/* ── Contact card ── */
.contact-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);
  padding:1.1rem 1.2rem;box-shadow:var(--shadow-sm)}
.contact-card h4{margin:0 0 .7rem;font-size:1rem}

/* ── Expander ── */
.expander{border:1px solid var(--border);border-radius:var(--r-sm);margin-bottom:.6rem;
  background:var(--card);overflow:hidden}
.expander summary{padding:.8rem 1rem;font-weight:600;font-size:.93rem;cursor:pointer;
  list-style:none;display:flex;justify-content:space-between;align-items:center}
.expander summary::after{content:"▸";font-size:.8rem;color:var(--secondary)}
.expander[open] summary::after{content:"▾"}
.expander-body{padding:.8rem 1rem 1rem;border-top:1px solid var(--border)}

/* ── Footer ── */
.footer{margin-top:2.6rem;padding:1.8rem 1rem;text-align:center;
  border-top:1px solid var(--border);color:var(--secondary)}
.footer .brand{font-family:var(--font-head);font-weight:700;font-size:1.1rem;color:var(--text)}
.footer .line{font-size:.84rem;margin-top:.3rem}

/* ── Section wrapper (hidden / visible) ── */
.section-content{display:none}
.section-content.active{display:block}
.subsection{display:none}
.subsection.active{display:block}
"""

# ── JavaScript ───────────────────────────────────────────────────────────────
JS = r"""
function showSection(id) {
  document.querySelectorAll('.section-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.main-nav button').forEach(b => b.classList.remove('active'));
  const sec = document.getElementById('sec-' + id);
  if (sec) sec.classList.add('active');
  const btn = document.getElementById('navbtn-' + id);
  if (btn) btn.classList.add('active');
  // default sub
  const firstSub = sec && sec.querySelector('.sub-nav button');
  if (firstSub && !sec.querySelector('.sub-nav button.active')) firstSub.click();
  window.scrollTo(0,0);
}
function showSub(sectionId, subId) {
  const sec = document.getElementById('sec-' + sectionId);
  if (!sec) return;
  sec.querySelectorAll('.subsection').forEach(el => el.classList.remove('active'));
  sec.querySelectorAll('.sub-nav button').forEach(b => b.classList.remove('active'));
  const sub = document.getElementById(subId);
  if (sub) sub.classList.add('active');
  const btn = document.getElementById('subbtn-' + subId);
  if (btn) btn.classList.add('active');
}
window.addEventListener('DOMContentLoaded', () => {
  showSection('about');
});
"""

# ── Main builder ─────────────────────────────────────────────────────────────
def nav_id(label: str) -> str:
    return label.lower().replace(" ","_").replace("&","and").replace(".","").replace("/","_").replace("-","_")

MAIN_SECTIONS = [
    ("about",        "About Me",                    page_about()),
    ("dp",           "DP Subjects",                 None),
    ("core",         "Core Components",             None),
    ("crs",          "AI Career-related Studies",   page_crs()),
    ("activities",   "Activities &amp; Interests",  page_activities()),
    ("certs",        "Certificates &amp; Achievements", page_certificates()),
    ("contact",      "Contact",                     page_contact()),
]

DP_SUBS = [
    ("dp_physics",  "Physics HL",         dp_physics()),
    ("dp_chem",     "Chemistry SL",       dp_chemistry()),
    ("dp_math",     "Mathematics AA HL",  dp_math()),
    ("dp_english",  "English B SL",       dp_english()),
]

CORE_SUBS = [
    ("core_pps",  "Personal and Professional Skills", core_pps()),
    ("core_lcs",  "Language and Cultural Studies",    core_lcs()),
    ("core_rp",   "Reflective Project",               core_reflective()),
    ("core_ce",   "Community Engagement",             core_community()),
]

PAGE_HEADERS = {
    "about":      ("IBCP Student Portfolio", "About Me", ""),
    "dp":         ("Diploma Programme", "DP Subjects",
                   "My four Diploma Programme subjects and the learning, coursework and assessments within each."),
    "core":       ("IBCP Core", "Core Components",
                   "The four core elements of the IBCP: Personal and Professional Skills, Language and "
                   "Cultural Studies, the Reflective Project and Community Engagement."),
    "crs":        ("Career-related Study", "AI Career-related Studies",
                   "My career-related study is Artificial Intelligence — a practical, project-based area of learning."),
    "activities": ("Activities &amp; Interests", "Beyond Academics",
                   "Alongside my studies, I have interests and experiences that shape who I am and how I learn."),
    "certs":      ("Recognition", "Certificates &amp; Achievements",
                   "Confirmed academic results and, as they become available, certificates, workshops and competitions."),
    "contact":    ("Get in touch", "Let's Connect",
                   "Thank you for visiting my portfolio. You can reach me through the details below."),
}

def build_section(sid, label, content) -> str:
    ey, ti, sub = PAGE_HEADERS[sid]
    sub_html = f'<p class="page-sub">{sub}</p>' if sub else ""
    if content is None:
        return ""   # handled separately for dp/core
    return f"""
<div id="sec-{sid}" class="section-content">
  <div class="page-head">
    <span class="eyebrow">{ey}</span>
    <div class="page-title">{ti}</div>
    {sub_html}
  </div>
  <div class="nav-underline"></div>
  {content}
</div>"""

def build_dp_section() -> str:
    ey, ti, sub = PAGE_HEADERS["dp"]
    sub_btns = "".join(
        f'<button id="subbtn-{sid}" onclick="showSub(\'dp\',\'{sid}\')">{lbl}</button>'
        for sid, lbl, _ in DP_SUBS)
    subs = "".join(
        f'<div id="{sid}" class="subsection">{content}</div>'
        for sid, _, content in DP_SUBS)
    return f"""
<div id="sec-dp" class="section-content">
  <div class="page-head">
    <span class="eyebrow">{ey}</span>
    <div class="page-title">{ti}</div>
    <p class="page-sub">{sub}</p>
  </div>
  <div class="nav-underline"></div>
  <div class="sub-nav">{sub_btns}</div>
  {subs}
</div>"""

def build_core_section() -> str:
    ey, ti, sub = PAGE_HEADERS["core"]
    sub_btns = "".join(
        f'<button id="subbtn-{sid}" onclick="showSub(\'core\',\'{sid}\')">{lbl}</button>'
        for sid, lbl, _ in CORE_SUBS)
    subs = "".join(
        f'<div id="{sid}" class="subsection">{content}</div>'
        for sid, _, content in CORE_SUBS)
    return f"""
<div id="sec-core" class="section-content">
  <div class="page-head">
    <span class="eyebrow">{ey}</span>
    <div class="page-title">{ti}</div>
    <p class="page-sub">{sub}</p>
  </div>
  <div class="nav-underline"></div>
  <div class="sub-nav">{sub_btns}</div>
  {subs}
</div>"""

def build_html() -> str:
    nav_btns = "".join(
        f'<button id="navbtn-{sid}" onclick="showSection(\'{sid}\')">{lbl}</button>'
        for sid, lbl, _ in MAIN_SECTIONS)

    sections_html = ""
    for sid, lbl, content in MAIN_SECTIONS:
        if sid == "dp":
            sections_html += build_dp_section()
        elif sid == "core":
            sections_html += build_core_section()
        else:
            sections_html += build_section(sid, lbl, content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Harini Priya Karthikeyan · IBCP Portfolio</title>
<style>{CSS}</style>
</head>
<body>
<div class="topbar">
  <span class="tb-brand">Harini Priya K.</span>
  <span class="tb-tag">IBCP Portfolio · Artificial Intelligence</span>
</div>
<nav class="main-nav">{nav_btns}</nav>
<div class="site-wrap">
  {sections_html}
</div>
<footer class="footer">
  <div class="brand">Harini Priya K.</div>
  <div class="line">IBCP Portfolio · Artificial Intelligence</div>
  <div class="line">Grade 12 · Jain Vidyalaya IB World School</div>
</footer>
<script>{JS}</script>
</body>
</html>"""


if __name__ == "__main__":
    out_dir = Path("static-site")
    out_dir.mkdir(exist_ok=True)
    html = build_html()
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    size_kb = (out_dir / "index.html").stat().st_size // 1024
    print(f"Built static-site/index.html  ({size_kb} KB)")
