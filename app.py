"""
=====================================================================
 HARINI PRIYA KARTHIKEYAN — IBCP PORTFOLIO (Streamlit)
=====================================================================
 A production-ready, responsive, glassmorphism portfolio app.

 Stack : Python · Streamlit · Plotly · Pandas · Pillow · Components
 Run   : streamlit run app.py
 Deploy: GitHub + Streamlit Community Cloud

 Architecture
 ------------
   1. Configuration & constants
   2. Theme system (light / dark)
   3. CSS loader
   4. Reusable UI helpers
   5. Page renderers (one function per section)
   6. Sidebar navigation + router
=====================================================================
"""

from __future__ import annotations

import base64
import time
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------
# 1. CONFIGURATION & CONSTANTS
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Harini Priya Karthikeyan · IBCP Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
CSS_FILE = ASSETS_DIR / "style.css"
PROFILE_IMG = ASSETS_DIR / "profile.jpg"

# ---- Core palette (used by Plotly charts & components) ----
PALETTE = {
    "primary": "#2F80ED",
    "purple": "#8B5CF6",
    "pink": "#EC4899",
    "dark": "#1F2937",
    "muted": "#6B7280",
    "light": "#E5E7EB",
    "bg": "#F5F7FA",
}
GRAD_TRI = "linear-gradient(120deg,#2F80ED,#8B5CF6,#EC4899)"

# ---- Student profile ----
STUDENT = {
    "name": "Harini Priya Karthikeyan",
    "short": "Harini Priya K.",
    "grade": "Grade 12",
    "programme": "International Baccalaureate Career-related Programme (IBCP)",
    "crs": "Artificial Intelligence",
    "school": "Jain Vidyalaya IB World School",
    "goal": "B.Tech Computer Science with specialization in Artificial Intelligence and Machine Learning",
    "quote": "Rooted in tradition, growing in knowledge.",
    "email": "harini.karthikeyan@example.com",
    "linkedin": "https://linkedin.com/in/your-profile",
    "github": "https://github.com/your-username",
}

# ---- Sidebar navigation ----
NAV_ITEMS = [
    ("🏠", "Home"),
    ("👩", "About Me"),
    ("🌍", "IBCP Core"),
    ("📚", "DP Subjects"),
    ("🤖", "Artificial Intelligence"),
    ("🎨", "Beyond Academics"),
    ("🏆", "Certificates"),
    ("🎯", "Future Goals"),
    ("📞", "Contact"),
]

# ---- Reusable content data ----
STRENGTHS = [
    ("🧩", "Critical Thinking", "Analysing problems from multiple angles before acting."),
    ("🛠️", "Problem Solving", "Turning challenges into structured, working solutions."),
    ("🎨", "Creativity", "Bringing original ideas into design and code."),
    ("🔥", "Persistence", "Iterating until something genuinely works."),
    ("🔄", "Adaptability", "Learning new tools quickly and adjusting to change."),
    ("🤝", "Collaboration", "Working with others to reach shared goals."),
]

JOURNEY = [
    ("Grade 10", "Foundations", "Built strong academic fundamentals and discovered a passion for technology and problem solving."),
    ("Grade 11", "IBCP Begins", "Joined the IBCP, chose Artificial Intelligence as my career-related study, and started building real projects."),
    ("Grade 12", "Deepening Expertise", "Advanced my programming skills, completed the Reflective Project, and grew a portfolio of AI applications."),
    ("Future University", "B.Tech CS (AI & ML)", "Pursue Computer Science with a specialization in Artificial Intelligence and Machine Learning."),
]

LO_CARDS = [
    ("LO1", "Personal Development", "Understanding my strengths, weaknesses and how I learn best.", "Evidence: personal reflection journal, goal-setting worksheet.", "I grew more self-aware and confident as a learner."),
    ("LO2", "Interpersonal Skills", "Collaborating effectively and valuing others' contributions.", "Evidence: team project roles, peer feedback notes.", "I learned that great outcomes come from listening."),
    ("LO3", "Thinking Processes", "Applying critical and creative thinking to real problems.", "Evidence: project design documents, problem logs.", "I now break big problems into small, testable steps."),
    ("LO4", "Communication", "Expressing ideas clearly in writing, speech and visuals.", "Evidence: presentations, project documentation, portfolio.", "I communicate technical ideas to non-technical audiences."),
    ("LO5", "Applied Ethics", "Making responsible, ethical decisions with integrity.", "Evidence: Reflective Project ethics section.", "I design technology with people and fairness in mind."),
]

DP_SUBJECTS = [
    {
        "icon": "📐", "name": "Mathematics: Analysis & Approaches", "level": "HL", "cls": "blue",
        "overview": "A rigorous course in algebra, functions, calculus and proof that develops strong analytical and mathematical reasoning.",
        "topics": ["Calculus", "Algebra", "Proof", "Statistics", "Modelling"],
        "ia": "A mathematical modelling investigation applying calculus and statistics to a real-world scenario.",
        "reflection": "Mathematics sharpened my logic and precision — skills I use daily when designing algorithms and analysing data.",
    },
    {
        "icon": "⚛️", "name": "Physics", "level": "HL", "cls": "purple",
        "overview": "The study of matter, energy and the laws of nature, from mechanics and electricity to modern physics.",
        "topics": ["Mechanics", "Electricity & Magnetism", "Waves", "Thermal Physics", "Modern Physics"],
        "ia": "Effect of rate of change of magnetic flux through a solenoid on induced electromotive force.",
        "reflection": "Physics taught me to question, experiment and verify — a scientific mindset that supports reliable AI systems.",
    },
    {
        "icon": "🧪", "name": "Chemistry", "level": "SL", "cls": "pink",
        "overview": "The study of substances, their properties and reactions, connecting atomic structure to real-world materials.",
        "topics": ["Stoichiometry", "Atomic Structure", "Kinetics", "Organic Chemistry", "Energetics"],
        "ia": "Effect of ferric nitrate concentration on the initial rate of oxidation of iodide ions.",
        "reflection": "Chemistry developed my attention to detail and experimental discipline — essential for accurate, data-driven work.",
    },
    {
        "icon": "📖", "name": "English B", "level": "SL", "cls": "teal",
        "overview": "Language acquisition focused on communication, cultural understanding and effective expression across text types.",
        "topics": ["Identities", "Human Ingenuity", "Social Organization", "Sharing the Planet"],
        "ia": "An individual oral presentation connecting a cultural topic to personal experience and global context.",
        "reflection": "English B strengthened my ability to communicate ideas clearly — vital for documenting and presenting technical work.",
    },
]

AI_SKILLS = [
    ("🐍", "Python", 88), ("📊", "Streamlit", 84), ("🗄️", "SQLite", 74),
    ("🌐", "HTML", 78), ("🧩", "Problem Solving", 92), ("🎨", "UI Design", 80),
    ("📈", "Data Analysis", 76), ("🚀", "Project Development", 85),
]

PROJECTS = [
    {
        "name": "WaterBuddy", "icon": "💧", "cls": "", "cat": "AI Hydration Tracker",
        "desc": "An AI-based hydration tracking application that helps users build healthy drinking habits.",
        "features": ["Age-based hydration goals", "Water intake tracking", "Daily challenges", "Achievement badges", "Analytics dashboard"],
        "tech": ["Python", "Streamlit", "SQLite", "Plotly"],
        "outcomes": "Learned how to model personalised goals, persist user data and visualise progress.",
        "highlight": "Adapts targets to the user's age and activity for genuinely useful guidance.",
    },
    {
        "name": "MedTimer", "icon": "⏰", "cls": "m2", "cat": "Medicine Reminder App",
        "desc": "A medicine reminder application that helps users take medication on time, every time.",
        "features": ["Customisable schedules", "Timely reminders", "Dose history", "Simple accessible UI"],
        "tech": ["Python", "Streamlit", "SQLite"],
        "outcomes": "Learned scheduling logic, state management and designing for accessibility.",
        "highlight": "Reliability-first design for a health-critical use case.",
    },
    {
        "name": "SmartFarm AI", "icon": "🌱", "cls": "m3", "cat": "Agricultural Assistant",
        "desc": "An AI-powered agricultural assistant that supports smarter farming decisions.",
        "features": ["Crop recommendations", "Soil & weather insights", "Data-driven guidance", "Clean dashboard"],
        "tech": ["Python", "Streamlit", "Pandas", "Data Analysis"],
        "outcomes": "Learned to clean, analyse and present real-world data for practical decisions.",
        "highlight": "Connects data science to a socially meaningful problem — food security.",
    },
    {
        "name": "SafeFall AI", "icon": "🛡️", "cls": "m4", "cat": "Fall Detection System",
        "desc": "A human fall detection application designed to improve safety and rapid response for at-risk individuals.",
        "features": ["Real-time detection", "Instant alerts", "Designed for elderly care", "Monitoring view"],
        "tech": ["Python", "Computer Vision", "AI"],
        "outcomes": "Learned applied computer vision and designing for safety-critical reliability.",
        "highlight": "Uses AI to protect people — technology with direct human impact.",
    },
    {
        "name": "StockSense Pro", "icon": "📈", "cls": "m5", "cat": "Market Analytics App",
        "desc": "A stock market analytics dashboard that turns raw market data into clear, actionable insight.",
        "features": ["Interactive charts", "Trend analysis", "Key metrics", "Modern dashboard"],
        "tech": ["Python", "Streamlit", "Pandas", "Plotly"],
        "outcomes": "Learned financial data handling, time-series visualisation and dashboard UX.",
        "highlight": "Transforms complex market data into decisions anyone can understand.",
    },
]

BEYOND = [
    ("💻", "Technology Exploration", "Constantly exploring new tools, frameworks and AI concepts through self-driven learning and hands-on experimentation.", "blue"),
    ("🗣️", "Language Learning", "Building communication skills across languages, deepening cultural understanding and the ability to connect with diverse people.", "purple"),
    ("🎨", "Creative Design", "Expressing ideas through design and visual creativity — from embroidery patterns to clean, modern user interfaces.", "pink"),
    ("💃", "Classical Dance Experience", "Training in classical dance built discipline, focus and stage confidence that carry into every challenge I take on.", "teal"),
    ("🌱", "Personal Development", "Actively working on resilience, time management and self-awareness to become a well-rounded learner and future professional.", "blue"),
]

CERTIFICATES = [
    ("🎓", "Academic Achievement", "Outstanding Academic Performance", "Recognised for consistent excellence across Diploma Programme subjects."),
    ("🐍", "Certification", "Python Programming Certification", "Completed structured training in Python fundamentals and applications."),
    ("🤖", "Workshop", "Introduction to Artificial Intelligence", "Hands-on workshop covering core AI concepts and real-world applications."),
    ("💧", "Technology Project", "WaterBuddy — AI Hydration Tracker", "Designed and built a complete AI-based hydration tracking application."),
    ("🏅", "Competition", "Science & Innovation Competition", "Participated with a technology-driven project addressing a real-world problem."),
    ("🏆", "Award", "Best Project Presentation", "Awarded for clarity, creativity and impact in a project presentation."),
    ("🎨", "Workshop", "UI/UX Design Fundamentals", "Learned the principles of user-centred design and modern interface layout."),
    ("📊", "Certification", "Data Analysis with Python", "Certified in analysing and visualising data using Python libraries."),
    ("📐", "Academic Achievement", "Mathematics Excellence Award", "Recognised for strong analytical and problem-solving ability in Mathematics."),
    ("🛡️", "Technology Project", "SafeFall AI — Fall Detection System", "Developed a human fall detection system to support safety and rapid response."),
    ("🧠", "Competition", "Coding Challenge Participation", "Solved algorithmic problems under time constraints in a coding competition."),
    ("🌟", "Award", "Community Engagement Recognition", "Honoured for leadership and impact in the Life Skills embroidery project."),
]

FUTURE_STEPS = [
    ("Step 01", "My Journey", "From a curious student to a builder of AI projects — blending rigorous academics with real, hands-on technology."),
    ("Step 02", "Lessons Learned", "Consistency beats perfection, feedback is a gift, and every failed attempt is a step closer to a working solution."),
    ("Step 03", "Challenges Overcome", "Balancing demanding HL subjects with ambitious projects taught me time management, resilience and when to ask for help."),
    ("Step 04", "Skills Developed", "Programming, data analysis, UI design and project management — plus the soft skills to communicate and collaborate."),
    ("Step 05", "Future Aspirations", "Pursue a B.Tech in Computer Science (AI & ML) and build technology that genuinely helps people."),
]

CAREER_PATH = ["School", "IBCP", "Computer Science", "AI & ML", "Software Engineer", "Future Innovation"]


# ---------------------------------------------------------------------
# 2. THEME SYSTEM
# ---------------------------------------------------------------------
def get_theme() -> bool:
    """Return True if dark mode is active (stored in session state)."""
    return st.session_state.get("dark_mode", False)


def theme_vars(dark: bool) -> str:
    """Return a :root override block for the selected theme."""
    if dark:
        return """
        :root {
          --bg:#0f1420; --bg-2:#0b0f18;
          --dark:#e8ecf3; --muted:#a9b2c3; --muted-soft:#7c8698;
          --light-gray:#2a3242;
          --card:#151b28;
          --glass:rgba(28,34,48,0.62);
          --glass-strong:rgba(24,30,43,0.82);
          --glass-border:rgba(255,255,255,0.09);
          --soft:rgba(47,128,237,0.16);
          --shadow-sm:0 4px 14px rgba(0,0,0,0.35);
          --shadow-md:0 12px 34px rgba(0,0,0,0.45);
          --shadow-lg:0 24px 60px rgba(0,0,0,0.55);
        }
        .stApp { background:
            radial-gradient(42rem 42rem at 12% 6%, rgba(47,128,237,.20), transparent 60%),
            radial-gradient(38rem 38rem at 90% 12%, rgba(139,92,246,.20), transparent 60%),
            radial-gradient(40rem 40rem at 72% 96%, rgba(236,72,153,.16), transparent 60%),
            linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%); }
        """
    return ""  # light theme uses the defaults in style.css


# ---------------------------------------------------------------------
# 3. CSS LOADER
# ---------------------------------------------------------------------
def load_css(dark: bool) -> None:
    """Inject the external stylesheet + theme variable overrides."""
    css = CSS_FILE.read_text(encoding="utf-8") if CSS_FILE.exists() else ""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.markdown(f"<style>{theme_vars(dark)}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------------------
# 4. REUSABLE UI HELPERS
# ---------------------------------------------------------------------
def html(markup: str) -> None:
    """Render raw HTML."""
    st.markdown(markup, unsafe_allow_html=True)


def img_to_b64(path: Path) -> str:
    """Base64-encode an image for inline HTML use."""
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        return ""


def section_header(eyebrow: str, title: str, subtitle: str = "") -> None:
    """Standard section heading with eyebrow, gradient title and subtitle."""
    sub = f'<p class="section-sub">{subtitle}</p>' if subtitle else ""
    html(
        f'<span class="eyebrow">{eyebrow}</span>'
        f'<h2 class="section-title">{title}</h2>'
        f'{sub}'
    )


def divider() -> None:
    html('<div class="divider"></div>')


def glass_card(title: str, body: str, accent: str = "", icon: str = "") -> str:
    """Return HTML for a glass card."""
    accent_cls = f"accent-{accent}" if accent else ""
    icon_html = f'<div class="chip {accent or "blue"}">{icon}</div>' if icon else ""
    return f'<div class="card {accent_cls}">{icon_html}<h4>{title}</h4>{body}</div>'


def animated_counters(items: list[dict], height: int = 160) -> None:
    """
    Render animated count-up statistics inside an isolated component.

    Each item: {"icon": str, "value": int, "label": str, "suffix": str}
    """
    cards = ""
    for it in items:
        suffix = it.get("suffix", "")
        cards += (
            f'<div class="ac-card">'
            f'<div class="ac-ic">{it["icon"]}</div>'
            f'<div class="ac-num" data-target="{it["value"]}" data-suffix="{suffix}">0{suffix}</div>'
            f'<div class="ac-lbl">{it["label"]}</div>'
            f'</div>'
        )

    component_html = f"""
    <html><head><style>
      * {{ box-sizing: border-box; font-family: 'Inter', system-ui, sans-serif; }}
      body {{ margin: 0; background: transparent; }}
      .ac-row {{ display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; }}
      .ac-card {{ flex: 1 1 150px; min-width: 130px; text-align: center;
        padding: 18px 12px; border-radius: 18px;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(255,255,255,0.85);
        box-shadow: 0 12px 34px rgba(31,41,55,0.09); }}
      .ac-ic {{ font-size: 24px; line-height: 1; }}
      .ac-num {{ font-family: 'Poppins', sans-serif; font-weight: 800; font-size: 32px;
        line-height: 1.15; margin-top: 4px;
        background: linear-gradient(135deg,#2F80ED,#EC4899);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent; }}
      .ac-lbl {{ font-size: 12.5px; color: #6B7280; font-weight: 600; margin-top: 2px; }}
    </style></head><body>
      <div class="ac-row">{cards}</div>
      <script>
        document.querySelectorAll('.ac-num').forEach(function (el) {{
          var target = parseInt(el.getAttribute('data-target'), 10) || 0;
          var suffix = el.getAttribute('data-suffix') || '';
          var dur = 1600, start = null;
          function step(ts) {{
            if (!start) start = ts;
            var p = Math.min((ts - start) / dur, 1);
            var e = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(e * target) + suffix;
            if (p < 1) requestAnimationFrame(step);
            else el.textContent = target + suffix;
          }}
          requestAnimationFrame(step);
        }});
      </script>
    </body></html>
    """
    components.html(component_html, height=height, scrolling=False)


def skill_bar(name: str, pct: int, color: str = "linear-gradient(90deg,#2F80ED,#8B5CF6)") -> str:
    """Return HTML for a single animated skill bar."""
    return (
        f'<div class="skill-row">'
        f'<div class="skill-top"><span>{name}</span><span class="pct">{pct}%</span></div>'
        f'<div class="skill-track"><div class="skill-fill" style="width:{pct}%;background:{color}"></div></div>'
        f'</div>'
    )


def timeline(items: list[tuple], prefix: str = "") -> str:
    """Return HTML for a vertical timeline. items = [(title, body), ...]"""
    rows = ""
    for i, (title, body) in enumerate(items):
        step = f'<div class="tl-step">{prefix} {i + 1:02d}</div>' if prefix else ""
        rows += f'<div class="tl-item"><div class="tl-card">{step}<h4>{title}</h4><p>{body}</p></div></div>'
    return f'<div class="timeline">{rows}</div>'


def badge_list(items: list[str]) -> str:
    """Return HTML for a row of hover badges."""
    inner = "".join(f'<span class="badge">{b}</span>' for b in items)
    return f'<div class="badge-wrap">{inner}</div>'


def placeholder_gallery(labels: list[str], icon: str = "🖼️") -> str:
    """Return HTML for photo-gallery placeholders."""
    boxes = "".join(
        f'<div class="ph-box"><div><div class="em">{icon}</div>{lbl}</div></div>' for lbl in labels
    )
    return f'<div class="gallery">{boxes}</div>'


def project_card(p: dict) -> str:
    """Return HTML for a premium project card."""
    feats = "".join(f"<li>{f}</li>" for f in p["features"])
    tech = "".join(f'<span class="tech">{t}</span>' for t in p["tech"])
    return f"""
    <div class="project">
      <div class="media {p['cls']}">
        <span class="em">{p['icon']}</span>
        <span class="ph">SCREENSHOT</span>
      </div>
      <div class="body">
        <div class="cat">{p['cat']}</div>
        <h4>{p['name']}</h4>
        <p class="desc">{p['desc']}</p>
        <ul class="feat">{feats}</ul>
        <div class="tech-wrap">{tech}</div>
        <p class="desc" style="font-size:.84rem;"><b>Learning outcome:</b> {p['outcomes']}</p>
        <p class="desc" style="font-size:.84rem;"><b>Highlight:</b> {p['highlight']}</p>
        <div class="proj-links">
          <a class="btn-link primary" href="{STUDENT['github']}" target="_blank">⌨ GitHub</a>
          <a class="btn-link ghost" href="#contact" target="_self">▶ Live Demo</a>
        </div>
      </div>
    </div>
    """


def cert_card(icon: str, cat: str, title: str, desc: str) -> str:
    """Return HTML for a certificate card."""
    return (
        f'<div class="cert"><div class="top"><div class="ic">{icon}</div>'
        f'<div class="cat">{cat}</div></div>'
        f'<h4>{title}</h4><p>{desc}</p>'
        f'<div class="meta">📌 Portfolio entry</div></div>'
    )


def plotly_theme(fig, dark: bool, height: int = 380):
    """Apply a transparent, palette-matched theme to a Plotly figure."""
    text = "#E8ECF3" if dark else "#1F2937"
    grid = "rgba(255,255,255,0.08)" if dark else "rgba(31,41,55,0.08)"
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=text, size=13),
        margin=dict(l=20, r=20, t=48, b=20),
        height=height,
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(gridcolor=grid, zerolinecolor=grid)
    fig.update_yaxes(gridcolor=grid, zerolinecolor=grid)
    return fig


def footer() -> None:
    html(
        '<div class="footer">'
        f'<div class="brand">HP <span class="gradient-text">Portfolio</span></div>'
        f'<div class="line">© {time.strftime("%Y")} {STUDENT["name"]} · IBCP · Artificial Intelligence</div>'
        f'<div class="line">“{STUDENT["quote"]}”</div>'
        '</div>'
    )


# ---------------------------------------------------------------------
# 5. PAGE RENDERERS
# ---------------------------------------------------------------------
def page_home() -> None:
    # --- Hero banner with floating shapes ---
    html(f"""
    <div class="hero">
      <div class="hero-shape s1"></div>
      <div class="hero-shape s2"></div>
      <div class="hero-shape s3"></div>
      <div class="hero-shape s4"></div>
      <div class="hero-content">
        <span class="hero-badge">✦ International Baccalaureate Career-related Programme</span>
        <h1>{STUDENT['name']}</h1>
        <div class="sub">IBCP Student &nbsp;|&nbsp; Artificial Intelligence</div>
        <p class="desc">
          Welcome to my portfolio. This website showcases my academic journey, personal growth,
          achievements, projects, and experiences throughout the International Baccalaureate
          Career-related Programme.
        </p>
        <p class="quote">“{STUDENT['quote']}”</p>
      </div>
    </div>
    """)

    # --- Call-to-action buttons ---
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("🚀 Explore Portfolio", use_container_width=True, type="primary"):
            st.session_state["nav"] = "About Me"
            st.rerun()
    with c2:
        if st.button("🤖 View Projects", use_container_width=True):
            st.session_state["nav"] = "Artificial Intelligence"
            st.rerun()

    # --- Animated statistics ---
    divider()
    section_header("✦ Snapshot", "At a <span class='gradient-text'>Glance</span>")
    animated_counters([
        {"icon": "🎓", "value": 12, "label": "Grade Level", "suffix": ""},
        {"icon": "🤖", "value": 1, "label": "AI Career-related Study", "suffix": ""},
        {"icon": "🚀", "value": 5, "label": "Projects Built", "suffix": "+"},
        {"icon": "🌟", "value": 100, "label": "IBCP Learner", "suffix": "%"},
    ])

    # --- Quick highlights ---
    divider()
    section_header("✦ Highlights", "What Defines <span class='gradient-text'>My Journey</span>")
    col1, col2, col3 = st.columns(3)
    with col1:
        html(glass_card("Academic Rigour", "Balancing HL Mathematics and Physics with a career-related study in Artificial Intelligence.", "blue", "📚"))
    with col2:
        html(glass_card("Real Projects", "Five working applications — from hydration tracking to fall detection — built end-to-end.", "purple", "🛠️"))
    with col3:
        html(glass_card("Growth Mindset", "A reflective learner who values feedback, ethics and continuous improvement.", "pink", "🌱"))


def page_about() -> None:
    section_header("✦ About Me", "A Student <span class='gradient-text'>Building with Intelligence</span>",
                   "Curious, driven and grounded — here is the person behind the projects.")

    left, right = st.columns([1, 1.6], gap="large")

    # --- Profile card ---
    with left:
        b64 = img_to_b64(PROFILE_IMG)
        img_tag = f'<img src="data:image/jpeg;base64,{b64}" alt="Profile photo">' if b64 else ""
        html(f"""
        <div class="glass" style="text-align:center;">
          <div style="width:130px;height:130px;margin:0 auto .8rem;border-radius:50%;overflow:hidden;
                      box-shadow:var(--glow-purple);">{img_tag}</div>
          <h3 style="margin:.2rem 0;">{STUDENT['name']}</h3>
          <p style="color:var(--primary);font-weight:600;margin:0 0 1rem;">IBCP Student · Artificial Intelligence</p>
          <div style="text-align:left;font-size:.9rem;color:var(--muted);">
            <p style="margin:.3rem 0;"><b>🎓 Programme:</b> {STUDENT['programme']}</p>
            <p style="margin:.3rem 0;"><b>🤖 CRS:</b> {STUDENT['crs']}</p>
            <p style="margin:.3rem 0;"><b>🏫 School:</b> {STUDENT['school']}</p>
            <p style="margin:.3rem 0;"><b>🚀 Goal:</b> {STUDENT['goal']}</p>
          </div>
        </div>
        """)

    # --- Introduction, aspirations, values ---
    with right:
        html(glass_card(
            "Introduction",
            "<p>I am a Grade 12 IBCP student at Jain Vidyalaya IB World School, specialising in "
            "Artificial Intelligence. I love turning ideas into working software and using technology "
            "to solve problems that matter to real people.</p>",
            "blue", "👋"))
        html(glass_card(
            "Academic Background",
            "<p>My academic journey combines the rigour of Higher Level Mathematics and Physics with "
            "the practical, project-based focus of the IBCP core and my AI career-related study.</p>",
            "purple", "📚"))
        html(glass_card(
            "Career Aspirations",
            f"<p>{STUDENT['goal']}. I aim to become an AI engineer who designs ethical, accessible and "
            "impactful solutions.</p>",
            "pink", "🚀"))
        html(glass_card(
            "Personal Values",
            "<p>Integrity, curiosity and empathy. I believe technology should be built responsibly and "
            "with the people who use it in mind.</p>",
            "blue", "💎"))

    # --- Strengths ---
    divider()
    section_header("✦ Strengths", "My Core <span class='gradient-text'>Strengths</span>")
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(STRENGTHS):
        with cols[i % 3]:
            html(glass_card(title, f"<p>{desc}</p>", "", icon))

    # --- Journey timeline ---
    divider()
    section_header("✦ Journey", "Academic <span class='gradient-text'>Timeline</span>")
    tl = timeline([(f"{stage} — {label}", body) for stage, label, body in JOURNEY])
    html(tl)


def page_ibcp_core() -> None:
    section_header("✦ IBCP Core", "The <span class='gradient-text'>Four Pillars</span> of My Programme",
                   "The IBCP core develops the skills, values and perspectives that connect my subjects with my AI career-related study.")

    # ---- 1. Language and Cultural Studies ----
    html('<div class="glass">')
    html('<div class="chip blue">🌍</div><h3>Language and Cultural Studies</h3>')
    st.markdown("##### Overview")
    st.write("This component develops intercultural understanding and communication skills. I explored "
             "how language shapes identity and how cultural awareness strengthens collaboration in a "
             "globally connected world.")
    a, b = st.columns(2)
    with a:
        st.markdown("##### Skills Developed")
        st.markdown("- Confident communication across cultures\n- Empathy and respect for diversity\n- "
                    "Adapting language to context")
    with b:
        st.markdown("##### Research & Cultural Understanding")
        st.markdown("- Studied cultural expressions and traditions\n- Compared communication norms\n- "
                    "Connected culture to technology design")
    st.markdown("##### Communication Growth & Reflection")
    st.info("Studying language and culture taught me that technology must be designed for people from "
            "all backgrounds. Clear communication is just as important as technical skill when building AI.")
    html('</div>')

    divider()

    # ---- 2. Reflective Project ----
    html('<div class="glass">')
    html('<div class="chip purple">📝</div><h3>Reflective Project</h3>')
    html('<div class="card accent-purple"><h4>Research Question</h4>'
         '<p>Should the use of Artificial Intelligence in education be limited even if it provides '
         'significant benefits to students?</p></div>')
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("##### Background")
        st.write("AI tools are rapidly entering classrooms, offering personalised learning while raising "
                 "questions about integrity, equity and privacy.")
        st.markdown("##### Stakeholders")
        st.markdown("- Students and teachers\n- School leadership & policymakers\n- AI developers")
        st.markdown("##### Benefits")
        st.markdown("- Personalised learning\n- Instant feedback\n- Wider access to support")
    with c2:
        st.markdown("##### Concerns")
        st.markdown("- Academic integrity\n- Over-reliance on tools\n- Data privacy\n- Unequal access")
        st.markdown("##### Ethical Analysis")
        st.write("A balanced approach is needed: clear guidelines, teacher training and ethical frameworks "
                 "that protect students while unlocking AI's benefits.")
        st.markdown("##### Key Findings")
        st.write("AI should be guided, not banned — regulated use maximises benefit and minimises harm.")
    st.markdown("##### Personal Reflection")
    st.success("This project strengthened my research, analysis and ethical reasoning. It shaped my belief "
               "that responsible AI is about balance — maximising benefit while protecting people.")
    html('</div>')

    divider()

    # ---- 3. Personal and Professional Skills (LO1-LO5) ----
    html('<div class="glass">')
    html('<div class="chip pink">💼</div><h3>Personal and Professional Skills</h3>')
    lo_html = "".join(
        f'<div class="lo c{i+1}"><span class="n">{n}</span><span class="t">{t}</span></div>'
        for i, (n, t, _d, _e, _r) in enumerate(LO_CARDS)
    )
    html(f'<div class="lo-grid">{lo_html}</div>')
    for n, t, desc, evidence, reflection in LO_CARDS:
        with st.expander(f"{n} · {t}"):
            st.markdown(f"**Description:** {desc}")
            st.markdown(f"**Evidence (placeholder):** {evidence}")
            st.markdown(f"**Reflection (placeholder):** {reflection}")
    html('</div>')

    divider()

    # ---- 4. Community Engagement ----
    html('<div class="glass">')
    html('<div class="chip teal">🧵</div><h3>Community Engagement</h3>')
    html('<div class="card accent-blue"><h4>Project: Life Skills – Embroidery Design</h4>'
         '<p>Empowering community members with a practical, creative life skill that supports '
         'self-expression, patience and potential income generation.</p></div>')
    e1, e2 = st.columns(2)
    with e1:
        st.markdown("##### Objectives")
        st.markdown("- Teach a practical creative skill\n- Build confidence\n- Encourage lifelong learning")
        st.markdown("##### Planning")
        st.markdown("- Researched beginner patterns\n- Prepared materials & samples\n- Organised tiered sessions")
    with e2:
        st.markdown("##### Activities")
        st.write("Hands-on workshops teaching basic stitches, colour selection and design layout, guiding "
                 "participants from simple patterns to their own creative pieces.")
        st.markdown("##### Impact")
        st.write("Participants gained a new skill and confidence, strengthening community bonds.")
    st.markdown("##### Skills Developed & Reflection")
    st.info("This experience taught me leadership, patience and the value of giving back. Small, "
            "consistent efforts can create meaningful change in a community.")
    st.markdown("##### Photo Gallery (placeholders)")
    html(placeholder_gallery(["Session 1", "Materials", "Participants", "Final Pieces"], "🧵"))
    html('</div>')


def page_dp_subjects() -> None:
    section_header("✦ DP Subjects", "Diploma Programme <span class='gradient-text'>Subjects</span>",
                   "A rigorous academic foundation in mathematics and the sciences, balanced with language and communication.")

    for subj in DP_SUBJECTS:
        html('<div class="glass">')
        html(f'<div class="chip {subj["cls"]}">{subj["icon"]}</div>'
             f'<h3>{subj["name"]} <span class="badge" style="font-size:.7rem;">{subj["level"]}</span></h3>')
        s1, s2 = st.columns(2)
        with s1:
            st.markdown("##### Overview")
            st.write(subj["overview"])
            st.markdown("##### " + ("Topics Studied" if subj["name"] != "Mathematics: Analysis & Approaches" else "Skills Developed"))
            st.markdown("\n".join(f"- {t}" for t in subj["topics"]))
        with s2:
            st.markdown("##### Internal Assessment")
            html(f'<div class="card accent-purple"><p>{subj["ia"]}</p></div>')
            st.markdown("##### Reflection")
            st.write(subj["reflection"])
        html('</div>')
        divider()


def page_ai() -> None:
    section_header("✦ Career-related Study", "Artificial <span class='gradient-text'>Intelligence</span>",
                   "My career-related study — where curiosity becomes code and ideas become working solutions.")

    # --- Introduction ---
    html('<div class="glass" style="text-align:center;">')
    html('<div class="chip purple" style="margin:0 auto .8rem;">🤖</div>')
    html('<p style="font-family:var(--font-head);font-weight:500;font-size:1.15rem;max-width:760px;margin:0 auto;">'
         'Artificial Intelligence has allowed me to develop programming skills, problem-solving abilities, '
         'and practical technology solutions through real-world projects.</p>')
    html('</div>')

    divider()

    # --- Why AI ---
    section_header("✦ Motivation", "Why <span class='gradient-text'>AI</span>?")
    w1, w2, w3 = st.columns(3)
    with w1:
        html(glass_card("Impact at Scale", "AI can help millions of people at once — from healthcare to agriculture.", "blue", "🌍"))
    with w2:
        html(glass_card("Creative Problem Solving", "It blends logic and creativity, letting me design genuinely useful tools.", "purple", "💡"))
    with w3:
        html(glass_card("Future-Ready", "AI is shaping every industry, and I want to help build it responsibly.", "pink", "🚀"))

    divider()

    # --- Skills: badges + bars + radar ---
    section_header("✦ Skills", "Skills <span class='gradient-text'>Developed</span>")
    html(badge_list([f"{ic} {n}" for ic, n, _ in AI_SKILLS]))

    s_left, s_right = st.columns([1.1, 1], gap="large")
    with s_left:
        st.markdown("##### Proficiency")
        bars = "".join(skill_bar(n, pct) for _ic, n, pct in AI_SKILLS)
        html(bars)
    with s_right:
        st.markdown("##### Skill Radar")
        cats = [n for _ic, n, _ in AI_SKILLS]
        vals = [p for _ic, _n, p in AI_SKILLS]
        fig = go.Figure(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=cats + [cats[0]],
            fill="toself",
            line=dict(color=PALETTE["purple"], width=2),
            fillcolor="rgba(139,92,246,0.28)",
            name="Proficiency",
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(120,130,150,0.25)"),
                angularaxis=dict(gridcolor="rgba(120,130,150,0.25)"),
            ),
            showlegend=False,
        )
        plotly_theme(fig, get_theme(), height=380)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    divider()

    # --- Project showcase ---
    section_header("✦ Portfolio", "Project <span class='gradient-text'>Showcase</span>",
                   "Five projects built to solve real problems with practical AI and software.")
    for i in range(0, len(PROJECTS), 2):
        cols = st.columns(2, gap="large")
        for j, col in enumerate(cols):
            if i + j < len(PROJECTS):
                with col:
                    html(project_card(PROJECTS[i + j]))


def page_beyond() -> None:
    section_header("✦ Beyond Academics", "Life <span class='gradient-text'>Beyond the Classroom</span>",
                   "Growth happens outside textbooks too — through creativity, culture and curiosity.")

    for i in range(0, len(BEYOND), 2):
        cols = st.columns(2, gap="large")
        for j, col in enumerate(cols):
            if i + j < len(BEYOND):
                icon, title, desc, cls = BEYOND[i + j]
                with col:
                    html(glass_card(title, f"<p>{desc}</p>", cls, icon))

    divider()
    section_header("✦ Values", "Values &amp; <span class='gradient-text'>Interests</span>")
    html(badge_list(["Integrity", "Curiosity", "Empathy", "Discipline", "Creativity",
                     "Collaboration", "Lifelong Learning", "Cultural Awareness"]))


def page_certificates() -> None:
    section_header("✦ Certificates &amp; Achievements", "Milestones &amp; <span class='gradient-text'>Recognition</span>",
                   "A growing record of learning, participation and accomplishment.")

    # --- Animated statistics ---
    animated_counters([
        {"icon": "🚀", "value": 5, "label": "Projects Completed", "suffix": "+"},
        {"icon": "📜", "value": 12, "label": "Certificates Earned", "suffix": "+"},
        {"icon": "🧠", "value": 8, "label": "Skills Learned", "suffix": "+"},
        {"icon": "🏆", "value": 6, "label": "Academic Achievements", "suffix": "+"},
    ])

    divider()

    # --- Achievement dashboard (Plotly) ---
    section_header("✦ Dashboard", "Achievement <span class='gradient-text'>Dashboard</span>")
    df = pd.DataFrame({
        "Category": ["Academic", "Certifications", "Workshops", "Competitions", "Projects", "Awards"],
        "Count": [6, 2, 2, 2, 5, 2],
    })
    d1, d2 = st.columns([1.3, 1], gap="large")
    with d1:
        fig = px.bar(df, x="Category", y="Count", text="Count",
                     color="Category",
                     color_discrete_sequence=[PALETTE["primary"], PALETTE["purple"], PALETTE["pink"],
                                              "#22c55e", "#f59e0b", "#06b6d4"])
        fig.update_traces(textposition="outside", marker_line_width=0)
        fig.update_layout(showlegend=False, title="Achievements by Category")
        plotly_theme(fig, get_theme(), height=360)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    with d2:
        fig2 = px.pie(df, names="Category", values="Count", hole=0.55,
                      color_discrete_sequence=[PALETTE["primary"], PALETTE["purple"], PALETTE["pink"],
                                               "#22c55e", "#f59e0b", "#06b6d4"])
        fig2.update_layout(title="Distribution")
        plotly_theme(fig2, get_theme(), height=360)
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    divider()

    # --- Certificate gallery with category filter ---
    section_header("✦ Gallery", "Certificate <span class='gradient-text'>Gallery</span>")
    categories = ["All"] + sorted({c[1] for c in CERTIFICATES})
    chosen = st.selectbox("Filter by category", categories, index=0)
    filtered = CERTIFICATES if chosen == "All" else [c for c in CERTIFICATES if c[1] == chosen]
    for i in range(0, len(filtered), 3):
        cols = st.columns(3, gap="medium")
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                with col:
                    html(cert_card(*filtered[i + j]))

    divider()
    st.markdown("##### Upload future certificates (placeholders)")
    st.file_uploader("Drop a certificate image (PDF/JPG/PNG) to add it to the gallery", type=["pdf", "jpg", "jpeg", "png"])
    html(placeholder_gallery(["Certificate 1", "Certificate 2", "Certificate 3"], "📜"))


def page_future() -> None:
    section_header("✦ Future Goals", "My <span class='gradient-text'>Roadmap</span> Forward",
                   "Where I have been, what I have learned, and where I am heading next.")

    html(timeline([(f"{step} — {title}", body) for step, title, body in FUTURE_STEPS]))

    divider()

    # --- Career pathway ---
    section_header("✦ Pathway", "Career <span class='gradient-text'>Pathway</span>")
    chips = " → ".join(f'<span class="badge">{c}</span>' for c in CAREER_PATH)
    html(f'<div style="text-align:center;line-height:2.6;">{chips}</div>')

    divider()

    # --- Vision statement ---
    html('<div class="glass" style="text-align:center;">')
    html('<div class="chip purple" style="margin:0 auto .8rem;">🌏</div>')
    html('<h3>Vision Statement</h3>')
    html('<p style="font-family:var(--font-head);font-weight:500;font-size:1.1rem;max-width:720px;margin:0 auto;">'
         '“To grow from a student who learns technology into a professional who shapes it — building '
         'intelligent, responsible solutions that make a real difference in the world.”</p>')
    html('</div>')

    divider()

    # --- Progress indicators ---
    section_header("✦ Progress", "Journey <span class='gradient-text'>Progress</span>")
    p1, p2 = st.columns(2, gap="large")
    with p1:
        st.markdown("##### Academic")
        html(skill_bar("IBCP Core Components", 90, "linear-gradient(90deg,#2F80ED,#8B5CF6)"))
        html(skill_bar("Diploma Programme Subjects", 85, "linear-gradient(90deg,#8B5CF6,#EC4899)"))
    with p2:
        st.markdown("##### Career-related")
        html(skill_bar("AI Projects Portfolio", 80, "linear-gradient(90deg,#2F80ED,#EC4899)"))
        html(skill_bar("University Preparation", 70, "linear-gradient(90deg,#22c55e,#2F80ED)"))


def page_contact() -> None:
    section_header("✦ Contact", "Let's <span class='gradient-text'>Connect</span>",
                   "Thank you for visiting my portfolio. I'm always open to learning opportunities, collaborations and conversations about AI.")

    c1, c2 = st.columns([1.2, 1], gap="large")
    with c1:
        html(glass_card("Contact Details",
                        f"<p><b>👤 Name:</b> {STUDENT['name']}</p>"
                        f"<p><b>🏫 School:</b> {STUDENT['school']}</p>"
                        f"<p><b>🎓 Programme:</b> {STUDENT['programme']}</p>"
                        f"<p><b>✉️ Email:</b> {STUDENT['email']}</p>",
                        "blue", "📇"))
        html(glass_card("Portfolio Links",
                        f'<p><a href="{STUDENT["linkedin"]}" target="_blank">🔗 LinkedIn (placeholder)</a></p>'
                        f'<p><a href="{STUDENT["github"]}" target="_blank">⌨ GitHub (placeholder)</a></p>'
                        f'<p><a href="#home" target="_self">🌐 Portfolio Home</a></p>',
                        "purple", "🔗"))
    with c2:
        html('<div class="glass" style="text-align:center;">')
        html('<div class="chip pink" style="margin:0 auto .8rem;">💌</div>')
        html('<h3>Thank You</h3>')
        html('<p style="color:var(--muted);">Thank you for taking the time to explore my portfolio. '
             'I would love to hear from you — whether it\'s about AI, a project idea, or an opportunity '
             'to learn and grow.</p>')
        html(f'<p style="font-family:var(--font-head);font-style:italic;color:var(--primary);">“{STUDENT["quote"]}”</p>')
        html('</div>')

    divider()
    st.markdown("##### Send a message (placeholder form)")
    with st.form("contact_form", clear_on_submit=True):
        fc1, fc2 = st.columns(2)
        with fc1:
            st.text_input("Your name")
        with fc2:
            st.text_input("Your email")
        st.text_area("Message")
        st.form_submit_button("Send Message ✉️", type="primary")


# ---------------------------------------------------------------------
# 6. SIDEBAR NAVIGATION + ROUTER
# ---------------------------------------------------------------------
def render_sidebar() -> str:
    """Render the branded sidebar with navigation and theme toggle."""
    with st.sidebar:
        # Brand logo
        html('<div class="side-logo"><div class="mark">HP</div>'
             '<div class="txt">HP Portfolio<small>IBCP · AI</small></div></div>')

        # Mini profile
        b64 = img_to_b64(PROFILE_IMG)
        img_tag = f'<img src="data:image/jpeg;base64,{b64}" alt="Profile">' if b64 else ""
        html(f'<div class="side-profile">{img_tag}'
             f'<div class="n">{STUDENT["short"]}</div>'
             f'<div class="r">IBCP · Artificial Intelligence</div></div>')

        # Navigation (radio styled as nav pills)
        labels = [name for _icon, name in NAV_ITEMS]
        icons = {name: icon for icon, name in NAV_ITEMS}
        choice = st.radio(
            "Navigation",
            labels,
            format_func=lambda x: f"{icons[x]}  {x}",
            label_visibility="collapsed",
            key="nav",
        )

        st.markdown("---")

        # Theme toggle
        st.toggle("🌙 Dark mode", key="dark_mode")

        st.markdown(
            '<p style="font-size:.74rem;color:var(--muted-soft);text-align:center;margin-top:1rem;">'
            'Built with Streamlit · Plotly · Pandas</p>',
            unsafe_allow_html=True,
        )
    return choice


def show_splash() -> None:
    """Brief branded loading animation on first load."""
    if st.session_state.get("_splash_done"):
        return
    ph = st.empty()
    ph.markdown(
        '<div style="position:fixed;inset:0;z-index:9999;display:grid;place-items:center;'
        'background:linear-gradient(135deg,#2F80ED,#8B5CF6,#EC4899);">'
        '<div style="text-align:center;color:#fff;">'
        '<div style="font-family:Poppins,sans-serif;font-weight:800;font-size:2rem;">HP Portfolio</div>'
        '<div style="width:44px;height:44px;margin:1rem auto 0;border:4px solid rgba(255,255,255,.35);'
        'border-top-color:#fff;border-radius:50%;animation:spin 0.9s linear infinite;"></div>'
        '<style>@keyframes spin{to{transform:rotate(360deg);}}</style>'
        '</div></div>',
        unsafe_allow_html=True,
    )
    time.sleep(0.9)
    ph.empty()
    st.session_state["_splash_done"] = True


PAGES = {
    "Home": page_home,
    "About Me": page_about,
    "IBCP Core": page_ibcp_core,
    "DP Subjects": page_dp_subjects,
    "Artificial Intelligence": page_ai,
    "Beyond Academics": page_beyond,
    "Certificates": page_certificates,
    "Future Goals": page_future,
    "Contact": page_contact,
}


def main() -> None:
    """Application entry point."""
    show_splash()
    page = render_sidebar()
    load_css(get_theme())

    # Render the selected page
    PAGES.get(page, page_home)()
    footer()


if __name__ == "__main__":
    main()
