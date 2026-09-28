from crewai import Agent


def create_researcher(llm, research_tool, callback=None):

    return Agent(
        role="Senior Researcher",

        goal=(
            "Investigate the user's research topic thoroughly, "
            "find reliable information, identify important evidence, "
            "and collect useful sources."
        ),

        backstory=(
            "You are an experienced research specialist. "
            "You investigate topics carefully instead of relying only "
            "on your existing knowledge. You use web research tools "
            "to find current and relevant information."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,

        step_callback=callback,
    )
