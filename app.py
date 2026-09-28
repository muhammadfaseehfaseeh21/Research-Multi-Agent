update_status(
    "⏳ Waiting to start",
    "Enter your topic and start the research workflow.",
)

# =========================================================
# START RESEARCH
# =========================================================

start_research = st.button(
    "🚀 Start Multi-Agent Research",
    type="primary",
    use_container_width=True,
)

if start_research:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    if not os.getenv("GROQ_API_KEY"):
        try:
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
        except Exception:
            st.error("GROQ_API_KEY is missing. Add it in Streamlit Secrets.")
            st.stop()

    progress = st.progress(0, text="Preparing your research team...")

    try:
        st.session_state.report = None

        update_status(
            "🔎 Researcher",
            "Starting research on your topic...",
        )
        progress.progress(20, text="Research team assembled...")

        callbacks = {
            "researcher": lambda output: update_status(
                "🔎 Researcher",
                "Finding relevant information...",
            ),
            "fact_checker": lambda output: update_status(
                "✅ Fact Checker",
                "Checking important claims...",
            ),
            "analyst": lambda output: update_status(
                "📊 Analyst",
                "Analyzing verified information...",
            ),
            "report_writer": lambda output: update_status(
                "📝 Report Writer",
                "Preparing the final report...",
            ),
        }

        try:
            crew = build_crew(callbacks)
        except TypeError:
            crew = build_crew()

        progress.progress(35, text="CrewAI agents are working...")

        result = crew.kickoff(
            inputs={"topic": topic.strip()}
        )

        progress.progress(100, text="Research completed!")

        update_status(
            "✨ All Agents Completed",
            "Your research report is ready.",
        )

        st.session_state.report = str(result)
        st.success("Research completed successfully!")

    except Exception as error:
        progress.empty()
        st.error("The research workflow could not be completed.")
        with st.expander("Technical error details"):
            st.code(str(error))

# =========================================================
# FINAL REPORT
# =========================================================

if st.session_state.report:
    st.divider()
    st.subheader("📄 Final Research Report")
    st.markdown(st.session_state.report)

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
    "<div class='footer'>"
    "Research Multi-Agent Team • CrewAI • Groq • Streamlit"
    "</div>"
)

