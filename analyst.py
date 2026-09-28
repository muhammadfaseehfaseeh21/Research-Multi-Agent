from crewai import Agent


def create_analyst(llm, research_tool, callback=None):

    return Agent(
        role="Research Analyst",

        goal=(
            "Analyze the verified research findings, identify patterns, "
            "connections, important insights, and meaningful conclusions."
        ),

        backstory=(
            "You are a research analyst who turns verified information "
            "into understandable insights. You focus on evidence-based "
            "analysis rather than unsupported assumptions."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,

        step_callback=callback,
    )
