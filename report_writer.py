from crewai import Agent


def create_report_writer(llm, research_tool, callback=None):

    return Agent(
        role="Research Report Writer",

        goal=(
            "Create a professional, well-structured research report "
            "using the research, fact-checking, and analysis produced "
            "by the other agents."
        ),

        backstory=(
            "You are an expert research writer. You transform complex "
            "research material into clear, organized and readable reports. "
            "You never invent sources or unsupported facts."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,

        step_callback=callback,
    )
