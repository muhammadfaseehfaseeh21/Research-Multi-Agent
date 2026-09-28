import os
import streamlit as st

from crew import build_crew


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Research Multi-Agent Team",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* ---------- MAIN BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.18),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(14, 165, 233, 0.15),
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(168, 85, 247, 0.12),
                transparent 30%
            ),
            #07111f;
        color: #f8fafc;
    }

    /* ---------- REMOVE TOP SPACE ---------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* ---------- HERO ---------- */

    .hero {
        padding: 2.5rem;
        border-radius: 28px;
        margin-bottom: 1.5rem;

        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.92),
                rgba(15, 23, 42, 0.78)
            );

        border: 1px solid rgba(148, 163, 184, 0.16);

        box-shadow:
            0 25px 70px rgba(0, 0, 0, 0.35);

        backdrop-filter: blur(18px);
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 0.5rem;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #93c5fd,
                #c4b5fd
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.08rem;
        color: #cbd5e1;
        max-width: 800px;
        line-height: 1.7;
    }

    /* ---------- STATUS ---------- */

    .status-card {
        padding: 1.25rem 1.5rem;
        border-radius: 20px;

        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.90),
                rgba(15, 23, 42, 0.72)
            );

        border: 1px solid rgba(96, 165, 250, 0.22);

        box-shadow:
            0 15px 40px rgba(0, 0, 0, 0.20);
    }

    .status-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: #94a3b8;
    }

    .status-agent {
        font-size: 1.35rem;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 0.25rem;
    }

    /* ---------- AGENT CARDS ---------- */

    .agent-card {
        padding: 1.3rem;
        border-radius: 20px;
        min-height: 150px;

        background:
            linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.88),
                rgba(15, 23, 42, 0.70)
            );

        border: 1px solid rgba(148, 163, 184, 0.14);

        transition: transform 0.2s ease;
    }

    .agent-card:hover {
        transform: translateY(-4px);
    }

    .agent-icon {
        font-size: 2rem;
    }

    .agent-name {
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }

    .agent-description {
        font-size: 0.86rem;
        color: #94a3b8;
        line-height: 1.5;
        margin-top: 0.4rem;
    }

    /* ---------- REPORT ---------- */

    .report-header {
        font-size: 1.7rem;
        font-weight: 750;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0b1220,
                #07111f
            );
        border-right: 1px solid rgba(148, 163, 184, 0.12);
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: none;
        padding: 0.8rem 1rem;

        font-weight: 700;
        font-size: 1rem;

        background:
            linear-gradient(
                90deg,
                #4f46e5,
                #7c3aed
            );

        color: white;

        box-shadow:
            0 10px 30px rgba(79, 70, 229, 0.28);
    }

    .stButton > button:hover {
        border: none;
        color: white;
        transform: translateY(-1px);
    }

    /* ---------- TEXT INPUT ---------- */

    textarea,
    input {
        border-radius: 14px !important;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.82rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(148, 163, 184, 0.10);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "report" not in st.session_state:
    st.session_state.report = None

if "research_running" not in st.session_state:
    st.session_state.research_running = False


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🔬 Research Multi-Agent Team
        </div>

        <div class="hero-subtitle">
            A collaborative AI research workflow powered by
            CrewAI and Groq. Four specialized agents research,
            verify, analyze and transform information into a
            structured research report.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 🔬 Research Lab")

    st.markdown(
        "### How it works"
    )

    st.markdown(
        """
        **1. 🔎 Researcher**  
        Finds relevant information.

        **2. ✅ Fact Checker**  
        Verifies important claims.

        **3. 📊 Analyst**  
        Extracts insights.

        **4. 📝 Report Writer**  
        Creates the final report.
        """
    )

    st.divider()

    st.caption(
        "Powered by CrewAI + Groq"
    )

    st.caption(
        "Model: openai/gpt-oss-120b"
    )


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

left, right = st.columns([2.1, 1])

with left:

    st.markdown("### 🎯 What do you want to research?")

    topic = st.text_area(
        "Research topic",
        placeholder=(
            "Example: The impact of artificial intelligence "
            "on higher education"
        ),
        height=140,
        label_visibility="collapsed",
    )


with right:

    st.markdown("### ⚙️ Research Settings")

    st.info(
        "The team will work sequentially: "
        "Research → Fact Check → Analysis → Report."
    )

    st.caption(
        "The agents can use live web research through Groq's "
        "built-in browser search."
    )


st.write("")


# ---------------------------------------------------------
# AGENT DISPLAY
# ---------------------------------------------------------

st.markdown("### 🤖 Your Research Team")

agent_columns = st.columns(4)

agents_info = [
    (
        "🔎",
        "Researcher",
        "Finds information and evidence."
    ),
    (
        "✅",
        "Fact Checker",
        "Verifies important claims."
    ),
    (
        "📊",
        "Analyst",
        "Turns evidence into insights."
    ),
    (
        "📝",
        "Report Writer",
        "Creates the final report."
    ),
]

for column, (icon, name, description) in zip(
    agent_columns,
    agents_info
):
    with column:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-icon">
                    {icon}
                </div>

                <div class="agent-name">
                    {name}
                </div>

                <div class="agent-description">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


st.write("")


# ---------------------------------------------------------
# CURRENT AGENT STATUS
# ---------------------------------------------------------

status_container = st.empty()


def update_status(agent_name):

    status_container.markdown(
        f"""
        <div class="status-card">

            <div class="status-label">
                CURRENTLY WORKING
            </div>

            <div class="status-agent">
                ⚡ {agent_name}
            </div>

            <div style="color:#94a3b8; margin-top:5px;">
                This agent is currently processing the research.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# CALLBACKS
# ---------------------------------------------------------

def researcher_callback(output):
    update_status("🔎 Researcher")


def fact_checker_callback(output):
    update_status("✅ Fact Checker")


def analyst_callback(output):
    update_status("📊 Research Analyst")


def report_writer_callback(output):
    update_status("📝 Report Writer")


# ---------------------------------------------------------
# START BUTTON
# ---------------------------------------------------------

st.write("")

start = st.button(
    "🚀 Start Multi-Agent Research",
    type="primary",
)


# ---------------------------------------------------------
# RUN CREW
# ---------------------------------------------------------

if start:

    if not topic.strip():
        st.warning(
            "Please enter a research topic first."
        )
        st.stop()

    if not os.getenv("GROQ_API_KEY"):

        try:
            os.environ["GROQ_API_KEY"] = st.secrets[
                "GROQ_API_KEY"
            ]

        except Exception:
            st.error(
                "GROQ_API_KEY is missing. Add it in "
                "Streamlit Secrets."
            )
            st.stop()

    progress = st.progress(
        0,
        text="Preparing your research team..."
    )

    try:

        update_status("🔎 Researcher")

        callbacks = {
            "researcher": researcher_callback,
            "fact_checker": fact_checker_callback,
            "analyst": analyst_callback,
            "report_writer": report_writer_callback,
        }

        crew = build_crew(callbacks)

        progress.progress(
            10,
            text="Research team assembled..."
        )

        result = crew.kickoff(
            inputs={
                "topic": topic
            }
        )

        progress.progress(
            100,
            text="Research completed!"
        )

        update_status("✨ Research complete")

        st.session_state.report = str(result)

    except Exception as e:

        progress.empty()

        st.error(
            f"Something went wrong: {str(e)}"
        )

        st.stop()


# ---------------------------------------------------------
# FINAL REPORT
# ---------------------------------------------------------

if st.session_state.report:

    st.divider()

    st.markdown(
        '<div class="report-header">📄 Final Research Report</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        st.session_state.report
    )

    st.download_button(
        label="⬇️ Download Research Report",
        data=st.session_state.report,
        file_name="research_report.md",
        mime="text/markdown",
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Research Multi-Agent Team · CrewAI · Groq · Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
