start_research = st.button(
    "🚀 Start Multi-Agent Research",
    type="primary",
)

if start_research:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        try:
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
        except Exception:
            st.error(
                "GROQ_API_KEY is missing. Add it to Streamlit Secrets."
            )
            st.stop()

    progress = st.progress(0, text="Preparing your research team...")

    try:
        st.session_state.report = None

        update_status(
            "🔎 Researcher",
            "The research workflow has started."
        )
        progress.progress(20, text="Research team assembled...")

        callbacks = {
            "researcher": lambda output: update_status("🔎 Researcher"),
            "fact_checker": lambda output: update_status("✅ Fact Checker"),
            "analyst": lambda output: update_status("📊 Analyst"),
            "report_writer": lambda output: update_status("📝 Report Writer"),
        }

        try:
            crew = build_crew(callbacks)
        except TypeError:
            crew = build_crew()

        progress.progress(35, text="CrewAI workflow is running...")

        result = crew.kickoff(
            inputs={"topic": topic.strip()}
        )

        progress.progress(
            100,
            text="Research completed successfully!"
        )

        update_status(
            "✨ All agents completed",
            "Your final research report is ready."
        )

        st.session_state.report = str(result)

    except Exception as error:
        progress.empty()
        st.error("Something went wrong while running the CrewAI workflow.")

        with st.expander("Technical error details"):
            st.code(str(error))

# =========================================================
# FINAL REPORT
# =========================================================

if st.session_state.report:
    st.divider()

    st.html(
        "<div class='report-card'>"
        "<div class='report-title'>📄 Final Research Report</div>"
        "</div>"
    )

    st.markdown(st.session_state.report)

    st.download_button(
        "⬇️ Download Research Report",
        data=st.session_state.report,
        file_name="research_report.md",
        mime="text/markdown",
    )

# =========================================================
# FOOTER
# =========================================================

st.html(
    "<div class='footer'>"
    "Research Multi-Agent Team &nbsp;•&nbsp; CrewAI &nbsp;•&nbsp; Groq &nbsp;•&nbsp; Streamlit"
    "</div>"
)
