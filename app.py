import os
import streamlit as st

from crew import build_crew


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Research Multi-Agent Team",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM LIGHT THEME
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL APP
       ===================================================== */

    .stApp {
        background: #f7f9fc;
        color: #172033;
    }

    .main {
        background: #f7f9fc;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e7ebf2;
    }

    [data-testid="stSidebar"] * {
        color: #172033;
    }


    /* =====================================================
       HERO SECTION
       ===================================================== */

    .hero {
        padding: 2.6rem 3rem;
        margin-bottom: 2rem;

        background:
            linear-gradient(
                135deg,
                #ffffff 0%,
                #f3f7ff 55%,
                #f7f1ff 100%
            );

        border: 1px solid #e1e8f5;
        border-radius: 28px;

        box-shadow:
            0 12px 35px rgba(30, 55, 90, 0.08);

        text-align: center;
    }


    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -0.04em;

        background:
            linear-gradient(
                90deg,
                #2563eb,
                #7c3aed
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 0.8rem;
    }


    .hero-subtitle {
        max-width: 850px;
        margin: 0 auto;

        color: #64748b;

        font-size: 1.05rem;
        line-height: 1.7;
    }


    /* =====================================================
       SECTION HEADINGS
       ===================================================== */

    .section-title {
        font-size: 1.55rem;
        font-weight: 750;

        color: #172033;

        margin-bottom: 1rem;
    }


    /* =====================================================
       INPUT CARD
       ===================================================== */

    .input-card {
        background: #ffffff;

        border: 1px solid #e4e9f2;

        border-radius: 22px;

        padding: 1.5rem;

        box-shadow:
            0 8px 25px rgba(30, 55, 90, 0.06);
    }


    /* =====================================================
       SETTINGS CARD
       ===================================================== */

    .settings-card {
        background:
            linear-gradient(
                135deg,
                #eff6ff,
                #f5f3ff
            );

        border: 1px solid #dce6f8;

        border-radius: 22px;

        padding: 1.5rem;

        box-shadow:
            0 8px 25px rgba(30, 55, 90, 0.05);
    }


    .settings-title {
        font-size: 1.25rem;
        font-weight: 750;

        color: #172033;

        margin-bottom: 0.8rem;
    }


    .settings-text {
        color: #64748b;

        line-height: 1.6;

        font-size: 0.92rem;
    }


    /* =====================================================
       AGENT CARDS
       ===================================================== */

    .agent-card {
        min-height: 175px;

        padding: 1.4rem;

        background: #ffffff;

        border-radius: 20px;

        border: 1px solid #e5eaf2;

        box-shadow:
            0 8px 25px rgba(30, 55, 90, 0.06);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .agent-card:hover {
        transform: translateY(-4px);

        box-shadow:
            0 15px 35px rgba(30, 55, 90, 0.10);
    }


    .agent-number {
        display: inline-flex;

        align-items: center;
        justify-content: center;

        width: 30px;
        height: 30px;

        border-radius: 50%;

        background: #eff6ff;

        color: #2563eb;

        font-weight: 700;

        font-size: 0.85rem;

        margin-bottom: 0.7rem;
    }


    .agent-icon {
        font-size: 2rem;

        margin-bottom: 0.4rem;
    }


    .agent-name {
        font-size: 1.05rem;

        font-weight: 750;

        color: #172033;

        margin-bottom: 0.45rem;
    }


    .agent-description {
        font-size: 0.88rem;

        color: #64748b;

        line-height: 1.55;
    }


    /* =====================================================
       CURRENT AGENT STATUS
       ===================================================== */

    .status-card {
        padding: 1.3rem 1.5rem;

        background:
            linear-gradient(
                135deg,
                #eff6ff,
                #f5f3ff
            );

        border: 1px solid #d7e3f7;

        border-radius: 20px;

        box-shadow:
            0 8px 25px rgba(30, 55, 90, 0.06);
    }


    .status-label {
        font-size: 0.72rem;

        text-transform: uppercase;

        letter-spacing: 0.14em;

        color: #64748b;

        font-weight: 700;
    }


    .status-agent {
        margin-top: 0.3rem;

        font-size: 1.35rem;

        font-weight: 800;

        color: #2563eb;
    }


    .status-description {
        margin-top: 0.25rem;

        color: #64748b;

        font-size: 0.9rem;
    }


    /* =====================================================
       REPORT SECTION
       ===================================================== */

    .report-card {
        background: #ffffff;

        border: 1px solid #e4e9f2;

        border-radius: 22px;

        padding: 1.8rem;

        box-shadow:
            0 10px 30px rgba(30, 55, 90, 0.07);
    }


    .report-title {
        font-size: 1.55rem;

        font-weight: 800;

        color: #172033;

        margin-bottom: 1rem;
    }


    /* =====================================================
       START BUTTON
       ===================================================== */

    .stButton > button {
        width: 100%;

        min-height: 52px;

        border: none !important;

        border-radius: 15px !important;

        background:
            linear-gradient(
                90deg,
                #2563eb,
                #7c3aed
            ) !important;

        color: white !important;

        font-size: 1rem !important;

        font-weight: 750 !important;

        box-shadow:
            0 10px 25px rgba(79, 70, 229, 0.22);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 14px 30px rgba(79, 70, 229, 0.28);
    }


    /* =====================================================
       TEXT AREA
       ===================================================== */

    textarea {
        background: #ffffff !important;

        color: #172033 !important;

        border: 1px solid #dbe2ec !important;

        border-radius: 14px !important;
    }


    textarea:focus {
        border: 1px solid #6366f1 !important;

        box-shadow:
            0 0 0 2px rgba(99, 102, 241, 0.12) !important;
    }


    /* =====================================================
       DOWNLOAD BUTTON
       ===================================================== */

    .stDownloadButton > button {
        border-radius: 12px;

        border: 1px solid #dbe2ec;

        background: #ffffff;

        color: #172033;

        font-weight: 650;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: #e5eaf2 !important;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;

        color: #94a3b8;

        font-size: 0.82rem;

        margin-top: 3rem;

        padding-top: 1.5rem;

        border-top: 1px solid #e5eaf2;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "report" not in st.session_state:
    st.session_state.report = None


# =========================================================
# HERO
# =========================================================

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


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:1.5rem;
            font-weight:800;
            color:#172033;
            margin-bottom:1.5rem;
        ">
            🔬 Research Lab
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            font-size:1rem;
            font-weight:750;
            color:#172033;
            margin-bottom:1rem;
        ">
            How it works
        </div>
        """,
        unsafe_allow_html=True,
    )

    sidebar_agents = [
        ("1", "🔎", "Researcher", "Finds relevant information."),
        ("2", "✅", "Fact Checker", "Verifies important claims."),
        ("3", "📊", "Analyst", "Extracts research insights."),
        ("4", "📝", "Report Writer", "Creates the final report."),
    ]

    for number, icon, name, description in sidebar_agents:

        st.markdown(
            f"""
            <div style="
                padding:0.75rem 0;
                border-bottom:1px solid #edf0f5;
            ">

                <div style="
                    font-weight:750;
                    color:#172033;
                ">
                    <span style="
                        color:#2563eb;
                        margin-right:6px;
                    ">
                        {number}.
                    </span>

                    {icon} {name}
                </div>

                <div style="
                    color:#64748b;
                    font-size:0.82rem;
                    margin-top:4px;
                    margin-left:24px;
                ">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            border-top:1px solid #e5eaf2;
            padding-top:1rem;
            color:#94a3b8;
            font-size:0.8rem;
        ">
            Powered by CrewAI + Groq<br><br>
            Model: openai/gpt-oss-120b
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# RESEARCH INPUT
# =========================================================

left_column, right_column = st.columns(
    [2.1, 1],
    gap="large"
)


with left_column:

    st.markdown(
        """
        <div class="section-title">
            🎯 What do you want to research?
        </div>
        """,
        unsafe_allow_html=True,
    )

    topic = st.text_area(
        "Research Topic",
        placeholder=(
            "Example: The impact of artificial intelligence "
            "on higher education"
        ),
        height=150,
        label_visibility="collapsed",
    )


with right_column:

    st.markdown(
        """
        <div class="settings-card">

            <div class="settings-title">
                ⚙️ Research Settings
            </div>

            <div class="settings-text">

                <b>Sequential workflow</b><br><br>

                🔎 Research<br>
                ↓<br>
                ✅ Fact Check<br>
                ↓<br>
                📊 Analysis<br>
                ↓<br>
                📝 Final Report

                <br><br>

                🌐 Agents can use live web research
                through Groq's browser search.

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("")


# =========================================================
# RESEARCH TEAM
# =========================================================

st.markdown(
    """
    <div class="section-title">
        🤖 Your Research Team
    </div>
    """,
    unsafe_allow_html=True,
)


agent_columns = st.columns(
    4,
    gap="medium"
)


agents = [
    (
        "1",
        "🔎",
        "Researcher",
        "Finds information and evidence from relevant sources."
    ),
    (
        "2",
        "✅",
        "Fact Checker",
        "Verifies important claims and identifies uncertainty."
    ),
    (
        "3",
        "📊",
        "Analyst",
        "Turns verified evidence into meaningful insights."
    ),
    (
        "4",
        "📝",
        "Report Writer",
        "Transforms the research into a professional report."
    ),
]


for column, agent in zip(agent_columns, agents):

    number, icon, name, description = agent

    with column:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-number">
                    {number}
                </div>

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


# =========================================================
# CURRENT AGENT STATUS
# =========================================================

status_container = st.empty()


def update_status(agent_name):

    status_container.markdown(
        f"""
        <div class="status-card">

            <div class="status-label">
                Currently Working
            </div>

            <div class="status-agent">
                ⚡ {agent_name}
            </div>

            <div class="status-description">
                This agent is currently processing the research.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# AGENT CALLBACKS
# =========================================================

def researcher_callback(output):
    update_status("🔎 Researcher")


def fact_checker_callback(output):
    update_status("✅ Fact Checker")


def analyst_callback(output):
    update_status("📊 Research Analyst")


def report_writer_callback(output):
    update_status("📝 Report Writer")


# =========================================================
# START RESEARCH BUTTON
# =========================================================

st.write("")

start_research = st.button(
    "🚀 Start Multi-Agent Research",
    type="primary",
)


# =========================================================
# RUN CREW
# =========================================================

if start_research:

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

        st.stop()


    # -----------------------------------------------------
    # LOAD GROQ API KEY
    # -----------------------------------------------------

    if not os.getenv("GROQ_API_KEY"):

        try:

            os.environ["GROQ_API_KEY"] = st.secrets[
                "GROQ_API_KEY"
            ]

        except Exception:

            st.error(
                "GROQ_API_KEY is missing. "
                "Please add it in Streamlit Secrets."
            )

            st.stop()


    # -----------------------------------------------------
    # PROGRESS
    # -----------------------------------------------------

    progress = st.progress(
        0,
        text="Preparing your research team..."
    )


    try:

        # ---------------------------------------------
        # INITIAL STATUS
        # ---------------------------------------------

        update_status("🔎 Researcher")


        # ---------------------------------------------
        # CALLBACKS
        # ---------------------------------------------

        callbacks = {
            "researcher": researcher_callback,
            "fact_checker": fact_checker_callback,
            "analyst": analyst_callback,
            "report_writer": report_writer_callback,
        }


        # ---------------------------------------------
        # BUILD CREW
        # ---------------------------------------------

        crew = build_crew(callbacks)


        progress.progress(
            10,
            text="Research team assembled..."
        )


        # ---------------------------------------------
        # RUN CREW
        # ---------------------------------------------

        result = crew.kickoff(
            inputs={
                "topic": topic
            }
        )


        # ---------------------------------------------
        # COMPLETE
        # ---------------------------------------------

        progress.progress(
            100,
            text="Research completed successfully!"
        )


        update_status(
            "✨ All agents completed the research"
        )


        st.session_state.report = str(result)


    except Exception as error:

        progress.empty()

        st.error(
            f"Something went wrong: {error}"
        )

        st.stop()


# =========================================================
# FINAL REPORT
# =========================================================

if st.session_state.report:

    st.divider()

    st.markdown(
        """
        <div class="report-card">

            <div class="report-title">
                📄 Final Research Report
            </div>

        </div>
        """,
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


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Research Multi-Agent Team
        &nbsp;•&nbsp;
        CrewAI
        &nbsp;•&nbsp;
        Groq
        &nbsp;•&nbsp;
        Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
