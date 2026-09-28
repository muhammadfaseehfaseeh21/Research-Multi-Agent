import os
import streamlit as st
from crew import build_crew

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Research Multi-Agent Team",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# LIGHT / WHITE PRESENTATION LAYER
# =========================================================

CSS = (
    "<style>"
    ".stApp{background:#f7f9fc;}"
    ".main .block-container{max-width:1450px;padding-top:2rem;padding-bottom:4rem;}"
    "[data-testid='stSidebar']{background:#ffffff;border-right:1px solid #e5eaf2;}"
    ".hero{background:linear-gradient(135deg,#ffffff,#f2f6ff,#f8f3ff);"
    "border:1px solid #dfe7f5;border-radius:26px;padding:2.5rem 2rem;"
    "text-align:center;box-shadow:0 12px 35px rgba(30,55,90,.08);margin-bottom:2rem;}"
    ".hero-title{font-size:clamp(2rem,4vw,3rem);font-weight:800;"
    "color:#2563eb;margin-bottom:.7rem;}"
    ".hero-subtitle{max-width:850px;margin:auto;color:#64748b;"
    "font-size:1rem;line-height:1.7;}"
    ".card{background:#ffffff;border:1px solid #e3e8f0;border-radius:20px;"
    "padding:1.4rem;box-shadow:0 8px 25px rgba(30,55,90,.06);}"
    ".agent-card{min-height:190px;}"
    ".agent-number{display:inline-flex;align-items:center;justify-content:center;"
    "width:30px;height:30px;border-radius:50%;background:#eff6ff;"
    "color:#2563eb;font-weight:800;}"
    ".agent-icon{font-size:2rem;margin-top:.6rem;}"
    ".agent-name{color:#172033;font-size:1.05rem;font-weight:800;margin-top:.4rem;}"
    ".agent-description{color:#64748b;font-size:.88rem;line-height:1.55;margin-top:.4rem;}"
    ".status-card{background:linear-gradient(135deg,#eff6ff,#f5f3ff);"
    "border:1px solid #d7e3f7;border-radius:18px;padding:1.2rem 1.4rem;margin:1rem 0;}"
    ".status-label{color:#64748b;font-size:.72rem;font-weight:800;"
    "text-transform:uppercase;letter-spacing:.12em;}"
    ".status-agent{color:#2563eb;font-size:1.25rem;font-weight:800;margin-top:.3rem;}"
    ".status-description{color:#64748b;font-size:.9rem;margin-top:.25rem;}"
    ".example-box{background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;"
    "padding:1rem;color:#475569;line-height:1.6;}"
    ".workflow{background:#ffffff;border:1px solid #e3e8f0;border-radius:18px;"
    "padding:1rem 1.2rem;margin:1rem 0;box-shadow:0 6px 20px rgba(30,55,90,.04);}"
    ".workflow-step{display:inline-block;margin-right:8px;color:#172033;font-weight:700;}"
    ".footer{text-align:center;color:#94a3b8;font-size:.82rem;margin-top:3rem;"
    "padding-top:1.5rem;border-top:1px solid #e5eaf2;}"
    ".stButton>button{min-height:50px;border-radius:14px!important;font-weight:800!important;}"
    "</style>"
)

st.html(CSS)

# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================

if "report" not in st.session_state:
    st.session_state.report = None

# =========================================================
# HERO
# =========================================================

st.html(
    "<div class='hero'>"
    "<div class='hero-title'>🔬 Research Multi-Agent Team</div>"
    "<div class='hero-subtitle'>"
    "Give your research topic to the team. Four specialized agents "
    "work together to create a structured research report."
    "</div>"
    "</div>"
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("🔬 Research Lab")
    st.caption("Your AI research workspace")

    st.subheader("Agent Team")

    st.markdown("### 🔎 Researcher")
    st.caption("Finds relevant information and evidence.")

    st.markdown("### ✅ Fact Checker")
    st.caption("Checks important claims and evidence.")

    st.markdown("### 📝 Writer")
    st.caption("Drafts structured analysis and insights.")

    st.markdown("### 🎯 Editor")
    st.caption("Refines final report for clarity and style.")

    st.markdown("---")
    api_key_input = st.text_input("GROQ API Key", type="password")
    if api_key_input:
        os.environ["GROQ_API_KEY"] = api_key_input

# =========================================================
# MAIN CONTENT AREA
# =========================================================

topic = st.text_input(
    "Enter Research Topic:",
    placeholder="e.g., Future of Autonomous AI Agents in Healthcare",
)

if st.button("🚀 Start Research Team", type="primary"):
    if not topic.strip():
        st.warning("Please enter a valid research topic.")
    elif not os.getenv("GROQ_API_KEY"):
        st.error("Please enter your GROQ API Key in the sidebar or set it in Streamlit Secrets.")
    else:
        with st.spinner("Multi-Agent team working on your topic..."):
            try:
                crew_instance = build_crew()
                result = crew_instance.kickoff(inputs={"topic": topic})
                st.session_state.report = result.raw if hasattr(result, "raw") else str(result)
                st.success("Research completed successfully!")
            except Exception as e:
                st.error(f"Error during execution: {str(e)}")

if st.session_state.report:
    st.markdown("### 📋 Final Research Report")
    st.markdown(st.session_state.report)
