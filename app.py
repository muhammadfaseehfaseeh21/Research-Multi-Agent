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
# LIGHT / WHITE UI
# =========================================================

CSS = """
<style>

.stApp {
    background: #f7f9fc;
    color: #172033;
}

.main .block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5eaf2;
}

/* Hero */

.hero {
    background: linear-gradient(
        135deg,
        #ffffff,
        #f2f6ff,
        #f8f3ff
    );

    border: 1px solid #dfe7f5;
    border-radius: 26px;

    padding: 2.5rem 2rem;

    text-align: center;

    box-shadow:
        0 12px 35px rgba(30,55,90,0.08);

    margin-bottom: 2rem;
}

.hero-title {
    font-size: clamp(2rem,4vw,3rem);
    font-weight: 800;
    color: #2563eb;
    margin-bottom: 0.7rem;
}

.hero-subtitle {
    max-width: 850px;
    margin: auto;

    color: #64748b;

    font-size: 1rem;
    line-height: 1.7;
}


/* Cards */

.card {
    background: #ffffff;

    border: 1px solid #e3e8f0;

    border-radius: 20px;

    padding: 1.4rem;

    box-shadow:
        0 8px 25px rgba(30,55,90,0.06);
}

.agent-card {
    min-height: 190px;
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

    font-weight: 800;
}

.agent-icon {
    font-size: 2rem;
    margin-top: 0.6rem;
}

.agent-name {
    color: #172033;

    font-size: 1.05rem;

    font-weight: 800;

    margin-top: 0.4rem;
}

.agent-description {
    color: #64748b;

    font-size: 0.88rem;

    line-height: 1.55;

    margin-top: 0.4rem;
}


/* Status */

.status-card {
    background: linear-gradient(
        135deg,
        #eff6ff,
        #f5f3ff
    );

    border: 1px solid #d7e3f7;

    border-radius: 18px;

    padding: 1.2rem 1.4rem;

    margin: 1rem 0;
}

.status-label {
    color: #64748b;

    font-size: 0.72rem;

    font-weight: 800;

    text-transform: uppercase;

    letter-spacing: 0.12em;
}

.status-agent {
    color: #2563eb;

    font-size: 1.25rem;

    font-weight: 800;

    margin-top: 0.3rem;
}

.status-description {
    color: #64748b;

    font-size: 0.9rem;

    margin-top: 0.25rem;
}


/* Example */

.example-box {
    background: #f8fafc;

    border: 1px solid #e2e8f0;

    border-radius: 14px;

    padding: 1rem;

    color: #475569;

    line-height: 1.6;
}


/* Workflow */

.workflow {
    background: #ffffff;

    border: 1px solid #e3e8f0;

    border-radius: 18px;

    padding: 1rem 1.2rem;

    margin: 1rem 0;

    box-shadow:
        0 6px 20px rgba(30,55,90,0.04);
}

.workflow-step {
    display: inline-block;

    margin-right: 8px;

    color: #172033;

    font-weight: 700;
}


/* Button */

.stButton > button {
    min-height: 52px;

    border-radius: 14px !important;

    font-weight: 800 !important;
}


/* Footer */

.footer {
    text-align: center;

    color: #94a3b8;

    font-size: 0.82rem;

    margin-top: 3rem;

    padding-top: 1.5rem;

    border-top: 1px solid #e5eaf2;
}

</style>
"""

st.html(CSS)


# =========================================================
# SESSION STATE
# =========================================================

if "report" not in st.session_state:
    st.session_state.report = None


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title">
            🔬 Research Multi-Agent Team
        </div>

        <div class="hero-subtitle">
            Give your research topic to the team.
            Four specialized AI agents work together
            to research, verify, analyze and create
            a structured research report.
        </div>

    </div>
    """
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🔬 Research Lab")

    st.caption(
        "Your AI research workspace"
    )

    st.subheader("Agent Team")

    st.markdown("### 🔎 Researcher")
    st.caption(
        "Finds relevant information and evidence."
    )

    st.markdown("### ✅ Fact Checker")
    st.caption(
        "Checks important claims and evidence."
    )

    st.markdown("### 📊 Analyst")
    st.caption(
        "Analyzes the verified information."
    )

    st.markdown("### 📝 Report Writer")
    st.caption(
        "Creates the final structured report."
    )

    st.divider()

    st.caption(
        "Powered by CrewAI + Groq"
    )

    st.caption(
        "Model: openai/gpt-oss-120b"
    )


# =========================================================
# TOPIC INPUT
# =========================================================

st.subheader(
    "🎯 What do you want to research?"
)

topic = st.text_area(
    "Research topic",

    placeholder=(
        "Example: Impact of Artificial Intelligence "
        "on Higher Education\n\n"

        "Other examples:\n"
        "• Benefits and risks of AI in healthcare\n"
        "• Future of renewable energy\n"
        "• Cybersecurity challenges in 2026"
    ),

    height=160,

    label_visibility="collapsed",
)


st.html(
    """
    <div class="example-box">

        <b>💡 How to use the app</b>
        <br><br>

        Enter your research topic and click
        <b>Start Multi-Agent Research</b>.

        <br><br>

        The agents will automatically work in this order:

        <br><br>

        🔎 Research →
        ✅ Fact Check →
        📊 Analysis →
        📝 Final Report

    </div>
    """
)


# =========================================================
# WORKFLOW
# =========================================================

st.subheader(
    "🔄 Research Workflow"
)

st.html(
    """
    <div class="workflow">

        <span class="workflow-step">
            🔎 Research
        </span>

        →

        <span class="workflow-step">
            ✅ Fact Check
        </span>

        →

        <span class="workflow-step">
            📊 Analysis
        </span>

        →

        <span class="workflow-step">
            📝 Report
        </span>

    </div>
    """
)


# =========================================================
# AGENT CARDS
# =========================================================

st.subheader(
    "🤖 Your Research Team"
)

agents = [

    (
        "1",
        "🔎",
        "Researcher",
        "Finds information and evidence related to your topic."
    ),

    (
        "2",
        "✅",
        "Fact Checker",
        "Reviews important claims and checks reliability."
    ),

    (
        "3",
        "📊",
        "Analyst",
        "Turns verified information into useful insights."
    ),

    (
        "4",
        "📝",
        "Report Writer",
        "Combines the work into a structured report."
    ),
]


columns = st.columns(4)


for column, agent in zip(
    columns,
    agents
):

    number, icon, name, description = agent

    with column:

        st.html(
            "<div class='card agent-card'>"

            f"<div class='agent-number'>"
            f"{number}"
            f"</div>"

            f"<div class='agent-icon'>"
            f"{icon}"
            f"</div>"

            f"<div class='agent-name'>"
            f"{name}"
            f"</div>"

            f"<div class='agent-description'>"
            f"{description}"
            f"</div>"

            "</div>"
        )


# =========================================================
# STATUS
# =========================================================

status_placeholder = st.empty()


def update_status(
    agent_name,
    description
):

    status_placeholder.html(

        "<div class='status-card'>"

        "<div class='status-label'>"
        "CURRENTLY WORKING"
        "</div>"

        f"<div class='status-agent'>"
        f"⚡ {agent_name}"
        f"</div>"

        f"<div class='status-description'>"
        f"{description}"
        f"</div>"

        "</div>"
    )


update_status(
    "⏳ Waiting to start",
    "Enter a research topic and start the workflow."
)


# =========================================================
# START BUTTON
# =========================================================

start_research = st.button(
    "🚀 Start Multi-Agent Research",

    type="primary",

    use_container_width=True,
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
    # GET GROQ API KEY
    # -----------------------------------------------------

    api_key = os.getenv(
        "GROQ_API_KEY"
    )


    if not api_key:

        try:

            api_key = st.secrets[
                "GROQ_API_KEY"
            ]

            os.environ[
                "GROQ_API_KEY"
            ] = api_key

        except Exception:

            st.error(
                "GROQ_API_KEY is missing. "
                "Please add it to Streamlit Secrets."
            )

            st.stop()


    progress = st.progress(
        0,
        text="Preparing your research team..."
    )


    try:

        st.session_state.report = None


        # -------------------------------------------------
        # RESEARCHER
        # -------------------------------------------------

        update_status(
            "🔎 Researcher",
            "Searching for relevant information..."
        )

        progress.progress(
            20,
            text="Researcher is working..."
        )


        # -------------------------------------------------
        # BUILD CREW
        # -------------------------------------------------

        crew = build_crew(
            callbacks={
                "researcher": lambda output:
                    update_status(
                        "🔎 Researcher",
                        "Finding information and evidence..."
                    ),

                "fact_checker": lambda output:
                    update_status(
                        "✅ Fact Checker",
                        "Checking important claims..."
                    ),

                "analyst": lambda output:
                    update_status(
                        "📊 Analyst",
                        "Analyzing verified information..."
                    ),

                "report_writer": lambda output:
                    update_status(
                        "📝 Report Writer",
                        "Preparing the final research report..."
                    ),
            }
        )


        progress.progress(
            35,
            text="CrewAI team assembled..."
        )


        # -------------------------------------------------
        # RUN CREW
        # -------------------------------------------------

        update_status(
            "🤖 Research Team",
            "The agents are working together..."
        )

        progress.progress(
            50,
            text="Agents are processing your research..."
        )


        result = crew.kickoff(
            inputs={
                "topic": topic.strip()
            }
        )


        # -------------------------------------------------
        # COMPLETE
        # -------------------------------------------------

        progress.progress(
            100,
            text="Research completed successfully!"
        )


        update_status(
            "✨ All Agents Completed",
            "Your final research report is ready."
        )


        st.session_state.report = str(
            result
        )


        st.success(
            "Research completed successfully!"
        )


    except Exception as error:

        progress.empty()

        st.error(
            "The CrewAI workflow could not be completed."
        )

        with st.expander(
            "Technical error details"
        ):

            st.code(
                str(error)
            )


# =========================================================
# FINAL REPORT
# =========================================================

if st.session_state.report:

    st.divider()

    st.subheader(
        "📄 Final Research Report"
    )

    st.markdown(
        st.session_state.report
    )


    st.download_button(

        label="⬇️ Download Research Report",

        data=st.session_state.report,

        file_name="research_report.md",

        mime="text/markdown",

        use_container_width=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="footer">
        Research Multi-Agent Team
        • CrewAI
        • Groq
        • Streamlit
    </div>
    """
)
