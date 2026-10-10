"""
=====================================================================
 app.py  —  IBCP Student Portfolio  (single Streamlit entry point)
 Harini Priya Karthikeyan
 International Baccalaureate Career-related Programme (IBCP)
 Career-related Study: Artificial Intelligence
=====================================================================

HOW TO RUN
----------
    streamlit run app.py

WHERE THINGS LIVE
-----------------
    data/portfolio_content.py  ->  ALL editable content (links, text,
                                   projects, certificates, contact...).
    assets/style.css           ->  the design system (colours, cards...).
    assets/                    ->  images (profile.jpg, projects/, ...).

This file contains only the layout, the navigation/router and the
reusable UI components. You should NOT need to edit it to add a link,
a project or a certificate — edit data/portfolio_content.py instead.
=====================================================================
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import streamlit as st

# Central, editable content — the single source of truth.
from data import portfolio_content as C


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"
CSS_FILE = ASSETS_DIR / "style.css"


# ---------------------------------------------------------------------
# Page configuration (must be the first Streamlit call)
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Harini Priya Karthikeyan · IBCP Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =====================================================================
#  LOW-LEVEL HELPERS
# =====================================================================
def load_css() -> None:
    """Inject the design-system stylesheet (once per rerun)."""
    if CSS_FILE.exists():
        st.markdown(
            f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def html(markup: str) -> None:
    """Render a trusted HTML fragment."""
    st.markdown(markup, unsafe_allow_html=True)


def slug(text: str) -> str:
    """Make a safe, unique-ish widget key fragment."""
    return "".join(ch if ch.isalnum() else "_" for ch in str(text))


def asset_exists(rel_path: str) -> bool:
    """True only when a relative asset path points to a real file."""
    if not rel_path:
        return False
    try:
        return (ROOT / rel_path).resolve().is_file()
    except (OSError, ValueError):
        return False


def show_image(rel_path: str, placeholder: str = "Image to be added") -> None:
    """Show an image if it exists, otherwise a tidy placeholder."""
    if asset_exists(rel_path):
        st.image(str(ROOT / rel_path), width="stretch")
    else:
        placeholder_box(placeholder)


# =====================================================================
#  SMALL PRESENTATION COMPONENTS
# =====================================================================
def placeholder_box(text: str) -> None:
    html(f'<div class="placeholder-box">{text}</div>')


def placeholder_note(text: str) -> None:
    html(f'<div class="placeholder-note"><span class="ic">✎</span><span>{text}</span></div>')


def status_pill(label: str, kind: str = "") -> str:
    """Return the HTML for a status pill. kind: '' | 'amber' | 'done'."""
    cls = "status-pill" + (f" {kind}" if kind else "")
    return f'<span class="{cls}">{label}</span>'


def reflection_box(title: str, text: str) -> None:
    html(f'<div class="reflection"><div class="reflection-title">{title}</div><p>{text}</p></div>')


def quote_card(text: str) -> None:
    html(f'<div class="quote-card"><p class="quote">“{text}”</p></div>')


def chip_list(items) -> None:
    chips = "".join(f'<span class="chip">{item}</span>' for item in items)
    html(f'<div class="chip-wrap">{chips}</div>')


def page_header(eyebrow: str, title: str, subtitle: str = "") -> None:
    sub = f'<p class="page-sub">{subtitle}</p>' if subtitle else ""
    html(
        f'<div class="page-head">'
        f'<span class="eyebrow">{eyebrow}</span>'
        f'<div class="page-title">{title}</div>'
        f"{sub}"
        f"</div>"
        f'<div class="nav-underline"></div>'
    )


def section_title(text: str, sub: str = "") -> None:
    sub_html = f'<p class="section-sub">{sub}</p>' if sub else ""
    html(f'<h3 class="section-title">{text}</h3>{sub_html}')


def mini_head(text: str) -> None:
    html(f'<div class="mini-head">{text}</div>')


def divider() -> None:
    html('<div class="divider"></div>')


def info_card(icon: str, title: str, body: str, accent: str = "") -> str:
    acc = f" {accent}" if accent else ""
    return (
        f'<div class="card{acc}">'
        f'<div class="card-icon">{icon}</div>'
        f'<h3 class="card-title">{title}</h3>'
        f'<p class="card-body">{body}</p>'
        f"</div>"
    )


def card_grid(items, cols: int = 3, accents=None) -> None:
    """items: iterable of (icon, title, body) tuples."""
    cards = ""
    for idx, (icon, title, body) in enumerate(items):
        accent = accents[idx % len(accents)] if accents else ""
        cards += info_card(icon, title, body, accent)
    html(f'<div class="grid grid-{cols}">{cards}</div>')


def plain_card(title: str, body: str, accent: str = "") -> str:
    acc = f" {accent}" if accent else ""
    return f'<div class="card{acc}"><h3 class="card-title">{title}</h3><p class="card-body">{body}</p></div>'


def plain_card_grid(items, cols: int = 3, accents=None) -> None:
    """items: iterable of (title, body) tuples."""
    cards = ""
    for idx, (title, body) in enumerate(items):
        accent = accents[idx % len(accents)] if accents else ""
        cards += plain_card(title, body, accent)
    html(f'<div class="grid grid-{cols}">{cards}</div>')


def fact_list(items) -> None:
    rows = "".join(
        f'<div class="fact"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in items
    )
    html(f'<div class="fact-list">{rows}</div>')


def timeline(items) -> None:
    rows = "".join(
        f'<div class="tl-item"><div class="tl-card"><h4>{title}</h4><p>{body}</p></div></div>'
        for title, body in items
    )
    html(f'<div class="timeline">{rows}</div>')


def bullet_list(items) -> None:
    lis = "".join(f"<li>{item}</li>" for item in items)
    html(f'<ul class="feature-list">{lis}</ul>')


def field(label: str, value: str) -> None:
    """A labelled content field. Shows a placeholder note when empty."""
    if value:
        html(f'<p class="card-body"><b>{label}.</b> {value}</p>')
    else:
        html(f'<p class="card-body" style="margin-bottom:.15rem;"><b>{label}</b></p>')
        placeholder_note("To be added")


def link_row(buttons, key: str, note: str = "Link to be added") -> None:
    """
    Render a row of action buttons.
    buttons: list of (label, url). A missing url -> disabled button + note.
    """
    cols = st.columns(len(buttons))
    for col, (label, url) in zip(cols, buttons):
        with col:
            if url:
                st.link_button(label, url, width="stretch")
            else:
                st.button(
                    label,
                    key=f"missing_{slug(key)}_{slug(label)}",
                    disabled=True,
                    width="stretch",
                )
                st.caption(note)


def evidence_card(item: dict, key: str) -> None:
    """One evidence item: {title, url, description, image}."""
    with st.container(border=True):
        if asset_exists(item.get("image", "")):
            st.image(str(ROOT / item["image"]), width="stretch")
        if item.get("title"):
            html(f'<h4 class="card-title">{item["title"]}</h4>')
        else:
            placeholder_note("Title to be added")
        if item.get("description"):
            html(f'<p class="card-body">{item["description"]}</p>')
        else:
            placeholder_note("Description to be added")
        if item.get("url"):
            st.link_button("Open evidence", item["url"], width="stretch")
        else:
            st.button("Open evidence", key=f"ev_{slug(key)}", disabled=True, width="stretch")
            st.caption("Link to be added")


def evidence_items_area(items, key_prefix: str, empty_message: str) -> None:
    """Render a list of evidence items, or a friendly empty state."""
    if not items:
        placeholder_note(empty_message)
        return
    for idx, item in enumerate(items):
        evidence_card(item, f"{key_prefix}_{idx}")


def project_card(project: dict) -> None:
    """A single project in the CRS showcase."""
    with st.container(border=True):
        left, right = st.columns([1, 1.7], gap="large")
        with left:
            if asset_exists(project.get("image", "")):
                st.image(str(ROOT / project["image"]), width="stretch")
            else:
                placeholder_box("Project screenshot to be added")
        with right:
            html(f'<div class="project-title">{project.get("icon", "")} {project.get("name", "")}</div>')
            if project.get("intro"):
                html(f'<p class="card-body">{project["intro"]}</p>')
            if project.get("problem"):
                html(f'<p class="card-body"><b>Problem.</b> {project["problem"]}</p>')
            if project.get("purpose"):
                html(f'<p class="card-body"><b>Purpose.</b> {project["purpose"]}</p>')
            if project.get("features"):
                html('<p class="card-body" style="margin-bottom:.1rem;"><b>Key features</b></p>')
                bullet_list(project["features"])
            if project.get("technologies"):
                tags = "".join(f'<span class="tech">{t}</span>' for t in project["technologies"])
                html(f'<div class="tech-tags">{tags}</div>')
            if project.get("learning"):
                html(f'<p class="card-body"><b>What I learned.</b> {project["learning"]}</p>')

        link_row(
            [
                ("GitHub", project.get("github", "")),
                ("Live App", project.get("streamlit", "")),
                ("Presentation", project.get("presentation", "")),
            ],
            key=f"proj_{project.get('name', '')}",
        )


def certificate_card(item: dict, key: str) -> None:
    """One certificate: {title, organisation, date, description, category, image, url}."""
    with st.container(border=True):
        if asset_exists(item.get("image", "")):
            st.image(str(ROOT / item["image"]), width="stretch")
        else:
            placeholder_box("Certificate image to be added")
        html(f'<h4 class="card-title">{item.get("title") or "Certificate title"}</h4>')
        if item.get("organisation"):
            html(f'<p class="cert-org">{item["organisation"]}</p>')
        if item.get("date"):
            html(f'<p class="cert-date">{item["date"]}</p>')
        if item.get("description"):
            html(f'<p class="desc">{item["description"]}</p>')
        if item.get("url"):
            st.link_button("View certificate", item["url"], width="stretch")


def gallery(items, cols: int = 3) -> None:
    """items: list of {image, caption}."""
    columns = st.columns(cols)
    for idx, item in enumerate(items):
        with columns[idx % cols]:
            show_image(item.get("image", ""), "Photo to be added")
            if item.get("caption"):
                st.caption(item["caption"])


def certificate_chart(items) -> None:
    """Small chart of certificates by category — only when entries exist."""
    try:
        import plotly.graph_objects as go
    except Exception:
        return
    counts = Counter((item.get("category") or "Other") for item in items)
    if not counts:
        return
    palette = ["#2F80ED", "#8B5CF6", "#B9A7FF", "#EC4899", "#22C55E", "#F59E0B"]
    fig = go.Figure(
        go.Bar(
            x=list(counts.keys()),
            y=list(counts.values()),
            marker_color=palette[: len(counts)],
        )
    )
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title="Certificates by category",
        font=dict(color="#1F2937"),
    )
    st.plotly_chart(fig, width="stretch")


def footer() -> None:
    html(
        '<div class="footer">'
        f'<div class="brand">{C.FOOTER["brand"]}</div>'
        f'<div class="line">{C.FOOTER["tagline"]}</div>'
        '<div class="line">Built with Streamlit · Python</div>'
        "</div>"
    )


# =====================================================================
#  NAVIGATION  (functional, session-state backed)
# =====================================================================
def _nav_control(state_key: str, options, widget_key: str, label: str) -> str:
    """A segmented control that always keeps a valid selection."""
    if state_key not in st.session_state or st.session_state[state_key] not in options:
        st.session_state[state_key] = options[0]

    choice = st.segmented_control(
        label,
        options,
        selection_mode="single",
        default=st.session_state[state_key],
        required=True,
        key=widget_key,
        label_visibility="collapsed",
        width="stretch",
        wrap=True,
    )
    if choice is None:  # safety net (e.g. older Streamlit)
        choice = st.session_state[state_key]
    st.session_state[state_key] = choice
    return choice


def main_nav() -> str:
    return _nav_control("section", C.MAIN_NAV, "nav_main", "Main navigation")


def dp_sub_nav() -> str:
    return _nav_control("dp_sub", C.DP_NAV, "nav_dp", "DP subject")


def core_sub_nav() -> str:
    return _nav_control("core_sub", C.CORE_NAV, "nav_core", "Core component")


# =====================================================================
#  PAGE 1 — ABOUT ME
# =====================================================================
def page_about() -> None:
    a = C.ABOUT

    html(
        '<div class="hero">'
        '<span class="hero-shape s1"></span>'
        '<span class="hero-shape s2"></span>'
        '<span class="hero-shape s3"></span>'
        f'<div class="hero-sub">{a["subtitle"]}</div>'
        f'<div class="hero-title">{a["hero_title"]}</div>'
        f'<p class="hero-text">{a["intro"]}</p>'
        "</div>"
    )
    st.write("")

    # (A) Who I Am — with optional profile image
    section_title("Who I Am")
    left, right = st.columns([1, 2.2], gap="large")
    with left:
        show_image(C.STUDENT.get("profile_image", ""), "Profile photo to be added")
    with right:
        html(f'<p class="card-body" style="font-size:.98rem;">{a["who_i_am"]}</p>')

    divider()

    # (B) Why I Chose IBCP
    section_title("Why I Chose the IBCP")
    html(f'<div class="card accent-blue"><p class="card-body" style="font-size:.96rem;">{a["why_ibcp"]}</p></div>')

    # (C) Why Artificial Intelligence?
    section_title("Why Artificial Intelligence?")
    html(f'<div class="card accent-purple"><p class="card-body" style="font-size:.96rem;">{a["why_ai"]}</p></div>')

    divider()

    # (D) My Academic Journey
    section_title("My Academic Journey")
    fact_list(a["journey_facts"])
    st.write("")
    timeline(a["journey_timeline"])

    divider()

    # (E) My Interests and Strengths
    section_title("My Interests and Strengths", "What I enjoy exploring, and the qualities I bring to my learning.")
    mini_head("Interests")
    card_grid(a["interests"], cols=3, accents=["accent-blue", "accent-purple", "accent-lav"])
    mini_head("Strengths")
    card_grid(a["strengths"], cols=3, accents=["accent-purple", "accent-blue", "accent-pink"])

    divider()

    # (F) My Approach to Learning
    section_title("My Approach to Learning")
    reflection_box("How I learn", a["approach"])

    # (G) Personal Quote
    quote_card(a["quote"])

    divider()
    html(
        '<div class="glass"><p class="card-body" style="margin:0;">'
        "Thank you for visiting. Use the navigation above to explore my DP subjects, "
        "core components, AI projects, activities, achievements and contact details."
        "</p></div>"
    )


# =====================================================================
#  PAGE 2 — DP SUBJECTS
# =====================================================================
def dp_physics() -> None:
    d = C.DP["Physics HL"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;">{d["learning_experience"]}</p>')

    divider()
    section_title("Coursework — Collaborative Science Project (CSP)")
    csp = d["csp"]
    html(
        f'<div class="card accent-blue">'
        f'<h3 class="card-title">{csp["title"]}</h3>'
        f'<p class="card-body"><b>Overview.</b> {csp["overview"]}</p>'
        f'<p class="card-body"><b>Aim.</b> {csp["aim"]}</p>'
        f"</div>"
    )
    html('<p class="card-body" style="margin-bottom:.1rem;"><b>Scientific principles involved</b></p>')
    bullet_list(csp["principles"])
    html(f'<p class="card-body"><b>Teamwork.</b> {csp["teamwork"]}</p>')
    html(f'<p class="card-body"><b>What I learned.</b> {csp["learned"]}</p>')
    reflection_box("Reflection", csp["reflection"])
    link_row([("View My CSP Presentation", csp.get("presentation_url", ""))], key="phys_csp")

    divider()
    section_title("Internal Assessment (IA)")
    ia = d["ia"]
    html(status_pill(ia["status"], "amber"))
    html(f'<p class="card-body" style="margin-top:.7rem;"><b>Topic.</b> {ia["topic"]}</p>')
    html(f'<p class="card-body"><b>Research question.</b> {ia["research_question"]}</p>')
    html(f'<p class="card-body"><b>Overview.</b> {ia["overview"]}</p>')
    html('<p class="card-body" style="margin-bottom:.1rem;"><b>Variables</b></p>')
    bullet_list(ia["variables"])
    html(f'<p class="card-body"><b>Approach.</b> {ia["approach"]}</p>')
    html(f'<p class="card-body"><b>Data collection.</b> {ia["data_collection"]}</p>')
    html(f'<p class="card-body"><b>Analysis.</b> {ia["analysis"]}</p>')
    placeholder_note(ia["notice"])
    mini_head("Evidence")
    evidence_items_area(
        ia.get("evidence", []),
        "phys_ia",
        "IA evidence and documents will be added here when they are ready.",
    )

    divider()
    reflection_box("Reflection on Physics", d["reflection"])


def dp_chemistry() -> None:
    d = C.DP["Chemistry SL"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;">{d["learning_experience"]}</p>')

    divider()
    section_title("Coursework — Collaborative Science Project (CSP)")
    csp = d["csp"]
    with st.container(border=True):
        html('<h3 class="card-title">Chemistry CSP</h3>')
        field("Project title", csp.get("title", ""))
        field("Overview", csp.get("overview", ""))
        field("Aim", csp.get("aim", ""))
        field("Scientific concepts involved", csp.get("concepts", ""))
        field("My contribution to the team", csp.get("contribution", ""))
        field("Skills developed", csp.get("skills", ""))
        field("Reflection", csp.get("reflection", ""))
        link_row([("Watch My CSP Project Video", csp.get("video_url", ""))], key="chem_csp")

    divider()
    section_title("Internal Assessment (IA)")
    ia = d["ia"]
    html(status_pill(ia["status"], "amber"))
    html(f'<p class="card-body" style="margin-top:.7rem;"><b>Topic.</b> {ia["topic"]}</p>')
    html(f'<p class="card-body"><b>Research question.</b> {ia["research_question"]}</p>')
    html(f'<p class="card-body"><b>Background.</b> {ia["background"]}</p>')
    html('<p class="card-body" style="margin-bottom:.1rem;"><b>Variables</b></p>')
    bullet_list(ia["variables"])
    html(f'<p class="card-body"><b>Method.</b> {ia["method"]}</p>')
    html(f'<p class="card-body"><b>Data collection.</b> {ia["data_collection"]}</p>')
    html(f'<p class="card-body"><b>Graphs.</b> {ia["graphs"]}</p>')
    html(f'<p class="card-body"><b>Analysis.</b> {ia["analysis"]}</p>')
    html(f'<p class="card-body"><b>Evaluation.</b> {ia["evaluation"]}</p>')
    placeholder_note(ia["notice"])
    mini_head("Evidence")
    evidence_items_area(
        ia.get("evidence", []),
        "chem_ia",
        "IA evidence and documents will be added here when they are ready.",
    )

    divider()
    reflection_box("Reflection on Chemistry", d["reflection"])


def dp_math() -> None:
    d = C.DP["Mathematics AA HL"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;">{d["learning_experience"]}</p>')

    divider()
    section_title("Concepts Covered", "A selection of the topics I am studying in Mathematics: Analysis and Approaches HL.")
    plain_card_grid(
        d["concepts"],
        cols=3,
        accents=["accent-blue", "accent-purple", "accent-lav"],
    )

    divider()
    section_title("Classwork and Evidence")
    html(f'<p class="card-body">{d["classwork_intro"]}</p>')
    evidence_items_area(
        d.get("classwork_evidence", []),
        "math_cw",
        "Classwork, notes and practice evidence will be added here as the course continues.",
    )

    divider()
    section_title("My Mathematics IA")
    ia = d["ia"]
    html(status_pill(ia["status"], "amber"))
    st.write("")
    field("IA title", ia.get("title", ""))
    field("Research question", ia.get("research_question", ""))
    placeholder_note(ia["notice"])
    link_row([("View My Mathematics IA", ia.get("document_url", ""))], key="math_ia")
    mini_head("Evidence")
    evidence_items_area(
        ia.get("evidence", []),
        "math_ia_ev",
        "IA evidence will be added here when it is ready.",
    )

    divider()
    reflection_box("Reflection on Mathematics", d["reflection"])


def dp_english() -> None:
    d = C.DP["English B SL"]
    section_title(d["title"])
    reflection_box("Where I am starting from", d["learning_experience"])

    divider()
    section_title("Themes", "The English B themes we explore through language and culture.")
    plain_card_grid(
        d["themes"],
        cols=2,
        accents=["accent-blue", "accent-purple", "accent-lav", "accent-pink"],
    )

    divider()
    section_title("Learning Experiences")
    bullet_list(d["learning_experiences"])

    divider()
    section_title("Future Evidence")
    html(f'<p class="card-body">{d["future_evidence_intro"]}</p>')
    evidence_items_area(
        d.get("future_evidence", []),
        "eng_ev",
        "Presentations, written work and oral tasks will be added here as they are completed.",
    )

    divider()
    reflection_box("Reflection on English B", d["reflection"])


def page_dp_subjects() -> None:
    page_header(
        "Diploma Programme",
        "DP Subjects",
        "My four Diploma Programme subjects and the learning, coursework and assessments within each.",
    )
    subject = dp_sub_nav()
    renderers = {
        "Physics HL": dp_physics,
        "Chemistry SL": dp_chemistry,
        "Mathematics AA HL": dp_math,
        "English B SL": dp_english,
    }
    renderers.get(subject, dp_physics)()


# =====================================================================
#  PAGE 3 — CORE COMPONENTS
# =====================================================================
def core_pps() -> None:
    d = C.CORE["Personal and Professional Skills"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;"><b>What it is.</b> {d["what_is"]}</p>')
    html(f'<p class="card-body"><b>My journey.</b> {d["journey"]}</p>')

    divider()
    section_title("Skills I Am Developing")
    card_grid(d["skills"], cols=3, accents=["accent-blue", "accent-purple", "accent-lav"])

    divider()
    section_title(
        "Learning Outcomes",
        "Expand each outcome to see my notes. Content will be added as the programme continues.",
    )
    for outcome in d["outcomes"]:
        code = outcome["code"]
        heading = f'{code} — {outcome["outcome"]}' if outcome.get("outcome") else code
        with st.expander(heading):
            field("Outcome", outcome.get("outcome", ""))
            field("What I did", outcome.get("what_i_did", ""))
            field("Skills developed", outcome.get("skills", ""))
            field("Evidence", outcome.get("evidence", ""))
            field("Reflection", outcome.get("reflection", ""))

    divider()
    section_title("My PPS Work")
    evidence_items_area(
        d.get("evidence_links", []),
        "pps_ev",
        "PPS evidence and documents will be linked here when they are ready.",
    )

    divider()
    reflection_box("Reflection on PPS", d["reflection"])


def core_lcs() -> None:
    d = C.CORE["Language and Cultural Studies"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;"><b>What it is.</b> {d["what_is"]}</p>')
    html(f'<p class="card-body"><b>Learning engagements.</b> {d["engagements_intro"]}</p>')

    divider()
    section_title("Learning Engagements")
    for idx, engagement in enumerate(d.get("engagements", [])):
        with st.container(border=True):
            if asset_exists(engagement.get("image", "")):
                st.image(str(ROOT / engagement["image"]), width="stretch")
            field("Engagement title", engagement.get("title", ""))
            field("Description", engagement.get("description", ""))
            field("Topic / issue explored", engagement.get("topic", ""))
            field("What I learned", engagement.get("learned", ""))
            field("Perspective considered", engagement.get("perspective", ""))
            if engagement.get("url"):
                st.link_button("Open engagement", engagement["url"], width="stretch")
            else:
                st.button("Open engagement", key=f"lcs_eng_{idx}", disabled=True, width="stretch")
                st.caption("Link to be added")

    divider()
    reflection_box("Reflection", d["reflection"])

    divider()
    section_title("Skills Developed")
    chip_list(d["skills"])

    divider()
    section_title("Canva / Evidence Links")
    evidence_items_area(
        d.get("evidence_links", []),
        "lcs_ev",
        "Canva links and other evidence will be added here when they are ready.",
    )


def core_reflective() -> None:
    d = C.CORE["Reflective Project"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;"><b>My research question.</b> {d["research_question"]}</p>')
    html(f'<p class="card-body"><b>What it is.</b> {d["what_is"]}</p>')
    html(f'<p class="card-body"><b>The ethical dilemma.</b> {d["dilemma"]}</p>')

    divider()
    section_title("Stakeholders")
    card_grid(d["stakeholders"], cols=3, accents=["accent-blue", "accent-purple", "accent-lav"])

    divider()
    section_title("Research and Analysis", "These sections will be completed as my project develops.")
    for title, content in d["sections"]:
        field(title, content)

    divider()
    html(status_pill(d["status"], "amber"))
    st.write("")
    placeholder_note(d["notice"])
    link_row([("View My Reflective Project", d.get("document_url", ""))], key="rp_doc")


def core_community() -> None:
    d = C.CORE["Community Engagement"]
    project = d["project"]
    section_title(d["title"])
    html(f'<p class="card-body" style="font-size:.96rem;"><b>What it is.</b> {d["what_is"]}</p>')

    divider()
    html(
        f'<div class="card accent-purple">'
        f'<h3 class="card-title">{project["name"]}</h3>'
        f'<p class="card-body"><b>Location.</b> {project["location"]}</p>'
        f'<p class="card-body">{project["overview"]}</p>'
        f"</div>"
    )
    html(f'<p class="card-body"><b>Why embroidery?</b> {project["why_embroidery"]}</p>')

    section_title("What We Did")
    card_grid(project["activities"], cols=3, accents=["accent-blue", "accent-purple", "accent-lav"])

    section_title("What I Developed")
    bullet_list(project["developed"])

    divider()
    section_title("Evidence", "Two separate evidence areas for this project.")
    mini_head("Project Proposal")
    evidence_card(project["proposal"], "community_proposal")
    mini_head("Community Engagement Learning Journal")
    evidence_card(project["journal"], "community_journal")


def page_core_components() -> None:
    page_header(
        "IBCP Core",
        "Core Components",
        "The four core elements of the IBCP: Personal and Professional Skills, Language and "
        "Cultural Studies, the Reflective Project and Community Engagement.",
    )
    component = core_sub_nav()
    renderers = {
        "Personal and Professional Skills": core_pps,
        "Language and Cultural Studies": core_lcs,
        "Reflective Project": core_reflective,
        "Community Engagement": core_community,
    }
    renderers.get(component, core_pps)()


# =====================================================================
#  PAGE 4 — AI CAREER-RELATED STUDIES
# =====================================================================
def page_crs() -> None:
    d = C.CRS
    page_header(
        "Career-related Study",
        "AI Career-related Studies",
        "My career-related study is Artificial Intelligence — a practical, project-based area of learning.",
    )

    section_title("What Career-related Studies Are")
    html(f'<p class="card-body" style="font-size:.96rem;">{d["what_is"]}</p>')
    reflection_box("Why Artificial Intelligence?", d["why_ai"])

    divider()
    section_title(
        "Areas of Learning",
        "These are the areas I am exploring through my CRS. They describe areas of learning rather "
        "than verified proficiency levels.",
    )
    card_grid(d["skills"], cols=4, accents=["accent-blue", "accent-purple", "accent-lav", "accent-pink"])

    divider()
    section_title(
        "Project Showcase",
        "A selection of the applications I have explored and built while learning Artificial Intelligence.",
    )
    for project in d["projects"]:
        project_card(project)

    divider()
    reflection_box("Reflection on my CRS", d["reflection"])

    with st.expander("How to update these project links"):
        html(
            '<p class="card-body">Open <b>data/portfolio_content.py</b> and edit the '
            "<b>CRS &rarr; projects</b> list. Each project has its own <b>github</b>, "
            "<b>streamlit</b> and <b>presentation</b> fields, plus an <b>image</b> path. "
            'Leave a field as an empty string "" until the link is ready and the app will '
            "show a friendly placeholder instead of a broken button.</p>"
        )


# =====================================================================
#  PAGE 5 — ACTIVITIES AND INTERESTS
# =====================================================================
def page_activities() -> None:
    d = C.ACTIVITIES
    page_header("Activities & Interests", d["title"], d["intro"])
    card_grid(d["cards"], cols=3, accents=["accent-blue", "accent-purple", "accent-lav", "accent-pink"])

    divider()
    section_title("Photos")
    if d.get("photos"):
        gallery(d["photos"])
    else:
        placeholder_note("Photos will be added here when they are ready.")


# =====================================================================
#  PAGE 6 — CERTIFICATES AND ACHIEVEMENTS
# =====================================================================
def page_certificates() -> None:
    d = C.CERTIFICATES
    page_header(
        "Recognition",
        d["title"],
        "Confirmed academic results and, as they become available, certificates, workshops and competitions.",
    )

    section_title("Confirmed Academic Details")
    fact_list(d["confirmed"])

    divider()
    section_title("Categories")
    chip_list(d["sections"])

    divider()
    section_title("Certificates and Achievements")
    items = d.get("items", [])
    if items:
        count = len(items)
        html(f'<p class="card-body">{count} entr{"y" if count == 1 else "ies"} recorded.</p>')
        certificate_chart(items)
        columns = st.columns(3)
        for idx, item in enumerate(items):
            with columns[idx % 3]:
                certificate_card(item, f"cert_{idx}")
    else:
        placeholder_note(
            "No certificates have been added yet. Add real certificates in "
            "data/portfolio_content.py and they will appear here automatically."
        )

    with st.expander("How to add a certificate"):
        html(
            '<p class="card-body">In <b>data/portfolio_content.py</b>, open '
            "<b>CERTIFICATES &rarr; items</b> and add a dictionary for each certificate:</p>"
            '<pre style="white-space:pre-wrap;background:rgba(47,128,237,.06);'
            'padding:.8rem;border-radius:12px;font-size:.82rem;">'
            '{<br>'
            '&nbsp;&nbsp;"title": "Certificate name",<br>'
            '&nbsp;&nbsp;"organisation": "Issuing organisation",<br>'
            '&nbsp;&nbsp;"date": "Month Year",<br>'
            '&nbsp;&nbsp;"description": "Short description",<br>'
            '&nbsp;&nbsp;"category": "Course certificates",<br>'
            '&nbsp;&nbsp;"image": "assets/certificates/my-cert.png",<br>'
            '&nbsp;&nbsp;"url": ""<br>'
            '}</pre>'
        )


# =====================================================================
#  PAGE 7 — CONTACT
# =====================================================================
def contact_method(column, label: str, value: str, prefix: str, empty_note: str) -> None:
    with column:
        with st.container(border=True):
            html(f'<h4 class="card-title">{label}</h4>')
            if value:
                url = value if value.startswith("http") else f"{prefix}{value}"
                st.link_button(f"Open {label}", url, width="stretch")
            else:
                placeholder_note(empty_note)


def page_contact() -> None:
    contact = C.CONTACT
    student = C.STUDENT
    page_header(
        "Get in touch",
        "Let's Connect",
        "Thank you for visiting my portfolio. You can reach me through the details below.",
    )

    with st.container(border=True):
        html(f'<h3 class="card-title">{student["name"]}</h3>')
        fact_list(
            [
                ("Grade / Programme", f'{student["grade"]} · {student["programme"]}'),
                ("School", student["school"]),
                ("Career-related Study", student["crs"]),
            ]
        )

    st.write("")
    columns = st.columns(3)
    contact_method(columns[0], "Email", contact.get("email", ""), "mailto:", "Email to be added")
    contact_method(columns[1], "GitHub", contact.get("github", ""), "", "GitHub link to be added")
    contact_method(columns[2], "LinkedIn", contact.get("linkedin", ""), "", "LinkedIn link to be added")

    divider()
    reflection_box("Thank you", contact["thank_you"])


# =====================================================================
#  ROUTER
# =====================================================================
def render_app() -> None:
    load_css()

    html(
        '<div class="topbar">'
        f'<span class="tb-brand">{C.STUDENT["short_name"]}</span>'
        f'<span class="tb-tag">{C.FOOTER["tagline"]}</span>'
        "</div>"
    )

    section = main_nav()

    pages = {
        "About Me": page_about,
        "DP Subjects": page_dp_subjects,
        "Core Components": page_core_components,
        "AI Career-related Studies": page_crs,
        "Activities & Interests": page_activities,
        "Certificates & Achievements": page_certificates,
        "Contact": page_contact,
    }
    pages.get(section, page_about)()

    footer()


# Run the app (Streamlit executes this script top-to-bottom).
render_app()
