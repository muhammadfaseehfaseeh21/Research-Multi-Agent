import os
import streamlit as st
from crew import build_crew

st.set_page_config(
    page_title="Research Multi-Agent Team",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# WHITE / LIGHT PRESENTATION LAYER
# =========================================================

CSS = (
    "<style>"
    ".stApp{background:#f7f9fc;}"
    ".main .block-container{max-width:1450px;padding-top:2rem;padding-bottom:4rem;}"
    "[data-testid='stSidebar']{background:#fff;border-right:1px solid #e7ebf2;}"
    "[data-testid='stSidebar'] *{color:#172033;}"
    ".hero{padding:2.6rem 3rem;margin-bottom:2rem;background:linear-gradient(135deg,#fff 0%,#f3f7ff 55%,#f7f1ff 100%);border:1px solid #e1e8f5;border-radius:28px;box-shadow:0 12px 35px rgba(30,55,90,.08);text-align:center;}"
    ".hero-title{font-size:clamp(2rem,4vw,3rem);font-weight:800;letter-spacing:-.04em;color:#2563eb;margin-bottom:.8rem;}"
    ".hero-subtitle{max-width:850px;margin:0 auto;color:#64748b;font-size:1.05rem;line-height:1.7;}"
    ".section-title{font-size:1.55rem;font-weight:800;color:#172033;margin-bottom:1rem;}"
    ".settings-card,.agent-card,.status-card,.report-card{background:#fff;border:1px solid #e4e9f2;border-radius:22px;box-shadow:0 8px 25px rgba(30,55,90,.06);}"
    ".settings-card{padding:1.5rem;background:linear-gradient(135deg,#eff6ff,#f5f3ff);}"
    ".settings-title{font-size:1.25rem;font-weight:800;color:#172033;margin-bottom:.8rem;}"
    ".settings-text{color:#64748b;line-height:1.6;font-size:.92rem;}"
    ".agent-card{min-height:175px;padding:1.4rem;transition:transform .2s ease,box-shadow .2s ease;}"
    ".agent-card:hover{transform:translateY(-4px);box-shadow:0 15px 35px rgba(30,55,90,.10);}"
    ".agent-number{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:#eff6ff;color:#2563eb;font-weight:800;font-size:.85rem;margin-bottom:.7rem;}"
    ".agent-icon{font-size:2rem;margin-bottom:.4rem;}"
    ".agent-name{font-size:1.05rem;font-weight:800;color:#172033;margin-bottom:.45rem;}"
    ".agent-description{font-size:.88rem;color:#64748b;line-height:1.55;}"
    ".status-card{padding:1.3rem 1.5rem;background:linear-gradient(135deg,#eff6ff,#f5f3ff);border-color:#d7e3f7;margin:1rem 0;}"
    ".status-label{font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;color:#64748b;font-weight:800;}"
    ".status-agent{margin-top:.3rem;font-size:1.35rem;font-weight:800;color:#2563eb;}"
    ".status-description{margin-top:.25rem;color:#64748b;font-size:.9rem;}"
    ".report-card{padding:1.8rem;margin-top:1.5rem;}"
    ".report-title{font-size:1.55rem;font-weight:800;color:#172033;}"
    "textarea{background:#fff!important;color:#172033!important;border-radius:14px!important;}"
    ".stButton>button{width:100%;min-height:52px;border:none!important;border-radius:15px!important;background:linear-gradient(90deg,#2563eb,#7c3aed)!important;color:#fff!important;font-size:1rem!important;font-weight:800!important;box-shadow:0 10px 25px rgba(79,70,229,.22);}"
    ".stButton>button:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(79,70,229,.28);}"
    ".stDownloadButton>button{border-radius:12px!important;border:1px solid #dbe2ec!important;background:#fff!important;color:#172033!important;font-weight:700!important;}"
    "hr{border-color:#e5eaf2!important;}"
    ".footer{text-align:center;color:#94a3b8;font-size:.82rem;margin-top:3rem;padding-top:1.5rem;border-top:1px solid #e5eaf2;}"
    "</style>"
)

st.html(CSS)

if "report" not in st.session_state:
    st.session_state.report = None

# =========================================================
# HERO
# =========================================================

st.html(
    "<div class='hero'>"
    "<div class='hero-title'>🔬 Research Multi-Agent Team</div>"
    "<div class='hero-subtitle'>"
    "A collaborative AI research workflow powered by CrewAI and Groq. "
    "Specialized agents research, verify, analyze, and transform "
    "information into a structured research report."
    "</div>"
    "</div>"
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.html(
        "<div style='font-size:1.5rem;font-weight:800;color:#172033;"
        "margin-bottom:1.5rem;'>🔬 Research Lab</div>"
    )

    st.html(
        "<div style='font-size:1rem;font-weight:800;color:#172033;"
        "margin-bottom:1rem;'>How it works</div>"
    )

    sidebar_agents = [
        ("1", "🔎", "Researcher", "Finds relevant information."),
        ("2", "✅", "Fact Checker", "Verifies important claims."),
        ("3", "📊", "Analyst", "Extracts research insights."),
        ("4", "📝", "Report Writer", "Creates the final report."),
    ]

    for number, icon, name, description in sidebar_agents:
        st.html(
            f"<div style='padding:.75rem 0;border-bottom:1px solid #edf0f5;'>"
            f"<div style='font-weight:800;color:#172033;'>"
        )
