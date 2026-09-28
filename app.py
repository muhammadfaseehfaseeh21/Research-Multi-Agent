import os
from crewai import Agent, Crew, Process, Task, LLM

# Model configuration using CrewAI LLM wrapper
groq_llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

def build_crew(topic: str):
    # Example Researcher Agent
    researcher = Agent(
        role="Researcher",
        goal=f"Research deeply about {topic}",
        backstory="Expert researcher extracting factual details.",
        verbose=True,
        llm=groq_llm
    )

    # Example Fact Checker Agent
    fact_checker = Agent(
        role="Fact Checker",
        goal="Verify claims and ensure accuracy",
        backstory="Critical fact checker validating all claims.",
        verbose=True,
        llm=groq_llm
    )

    # Example Writer Agent
    writer = Agent(
        role="Writer",
        goal="Write structured research analysis",
        backstory="Skilled writer drafting detailed reports.",
        verbose=True,
        llm=groq_llm
    )

    # Example Editor Agent
    editor = Agent(
        role="Editor",
        goal="Refine and format the final report",
        backstory="Meticulous editor polishing final content.",
        verbose=True,
        llm=groq_llm
    )

    # Example Tasks
    task_research = Task(
        description=f"Conduct thorough research on {topic}.",
        expected_output="Detailed key findings and data points.",
        agent=researcher
    )

    task_check = Task(
        description="Verify facts and references in the research findings.",
        expected_output="Verified facts list.",
        agent=fact_checker
    )

    task_write = Task(
        description="Draft a full report based on verified findings.",
        expected_output="Comprehensive structured report draft.",
        agent=writer
    )

    task_edit = Task(
        description="Edit and polish the final report.",
        expected_output="Polished Markdown research report.",
        agent=editor
    )

    return Crew(
        agents=[researcher, fact_checker, writer, editor],
        tasks=[task_research, task_check, task_write, task_edit],
        process=Process.sequential
    )
