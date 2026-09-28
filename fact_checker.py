from crewai import Agent


def create_fact_checker(llm, research_tool, callback=None):

    return Agent(
        role="Fact Checker",

        goal=(
            "Verify the important claims and information produced by "
            "the researcher. Identify unsupported, outdated, or "
            "questionable claims."
        ),

        backstory=(
            "You are a careful fact-checking specialist. "
            "You compare claims against reliable web sources and "
            "clearly distinguish verified information from uncertainty."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,

        step_callback=callback,
    )
