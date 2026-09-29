import os
import json
import urllib.parse
import urllib.request

from crewai import Agent
from crewai import Crew
from crewai import Process
from crewai import Task
from crewai import LLM

from crewai.tools import tool


# =========================================================
# GROQ LLM
# =========================================================

def get_llm():

    api_key = os.getenv(
        "GROQ_API_KEY"
    )

    if not api_key:

        raise ValueError(
            "GROQ_API_KEY is missing."
        )


    return LLM(

        model="openai/gpt-oss-120b",

        api_key=api_key,

        base_url="https://api.groq.com/openai/v1",

        temperature=0.2,
    )


# =========================================================
# WEB RESEARCH TOOL
# =========================================================

@tool("Web Research Tool")
def web_research_tool(query: str) -> str:
    """
    Search Wikipedia for research information.

    Use this tool when you need external information,
    background knowledge, facts, dates, definitions,
    people, organizations or scientific information.
    """

    try:

        encoded_query = urllib.parse.quote(
            query
        )


        url = (
            "https://en.wikipedia.org/w/rest.php/"
            "v1/search/page"
            f"?q={encoded_query}"
            "&limit=5"
        )


        request = urllib.request.Request(

            url,

            headers={
                "User-Agent":
                "ResearchMultiAgentTeam/1.0"
            },
        )


        with urllib.request.urlopen(
            request,
            timeout=15
        ) as response:

            data = json.loads(
                response.read().decode(
                    "utf-8"
                )
            )


        pages = data.get(
            "pages",
            []
        )


        if not pages:

            return (
                "No Wikipedia results were "
                "found for this query."
            )


        results = []


        for page in pages[:5]:

            title = page.get(
                "title",
                ""
            )

            description = page.get(
                "description",
                ""
            )

            excerpt = page.get(
                "excerpt",
                ""
            )


            results.append(

                f"Title: {title}\n"
                f"Description: {description}\n"
                f"Excerpt: {excerpt}\n"
            )


        return "\n---\n".join(
            results
        )


    except Exception as error:

        return (
            "Web research tool error: "
            f"{error}"
        )


# =========================================================
# BUILD CREW
# =========================================================

def build_crew(callbacks=None):

    """
    Build and return the complete Research Multi-Agent Crew.

    callbacks is optional and is supplied by app.py
    to update the Streamlit status area.
    """


    if callbacks is None:

        callbacks = {}


    llm = get_llm()


    # =====================================================
    # AGENT 1 — RESEARCHER
    # =====================================================

    researcher = Agent(

        role="Senior Researcher",

        goal=(
            "Research the given topic carefully and "
            "collect useful, relevant and factual "
            "information."
        ),

        backstory=(
            "You are an experienced research specialist. "
            "You break a topic into important questions, "
            "search for useful evidence and organize the "
            "information clearly for the next agents."
        ),

        tools=[
            web_research_tool
        ],

        llm=llm,

        verbose=True,

        allow_delegation=False,
    )


    # =====================================================
    # AGENT 2 — FACT CHECKER
    # =====================================================

    fact_checker = Agent(

        role="Fact Checker",

        goal=(
            "Review the research produced by the "
            "Researcher, verify important claims and "
            "identify information that needs caution."
        ),

        backstory=(
            "You are a careful fact-checking specialist. "
            "You examine claims, compare them with "
            "available evidence and clearly identify "
            "uncertainty."
        ),

        tools=[
            web_research_tool
        ],

        llm=llm,

        verbose=True,

        allow_delegation=False,
    )


    # =====================================================
    # AGENT 3 — ANALYST
    # =====================================================

    analyst = Agent(

        role="Research Analyst",

        goal=(
            "Analyze the verified research and turn it "
            "into meaningful insights, patterns, "
            "advantages, limitations and conclusions."
        ),

        backstory=(
            "You are an analytical research specialist. "
            "You transform verified information into "
            "clear, logical and useful insights."
        ),

        tools=[
            web_research_tool
        ],

        llm=llm,

        verbose=True,

        allow_delegation=False,
    )


    # =====================================================
    # AGENT 4 — REPORT WRITER
    # =====================================================

    report_writer = Agent(

        role="Professional Research Report Writer",

        goal=(
            "Create a clear, structured and professional "
            "final research report using the work of the "
            "other agents."
        ),

        backstory=(
            "You are an expert research writer. "
            "You combine research, verification and "
            "analysis into a readable final report."
        ),

        tools=[
            web_research_tool
        ],

        llm=llm,

        verbose=True,

        allow_delegation=False,
    )


    # =====================================================
    # TASK 1 — RESEARCH
    # =====================================================

    research_task = Task(

        description=(
            "Research the following topic:\n\n"
            "{topic}\n\n"

            "Use the Web Research Tool to gather "
            "relevant information.\n\n"

            "Cover:\n"
            "1. Background\n"
            "2. Important facts\n"
            "3. Major developments\n"
            "4. Relevant evidence\n"
            "5. Important examples\n\n"

            "Organize the research clearly."
        ),

        expected_output=(
            "A structured research brief containing "
            "important facts, evidence and useful "
            "background information."
        ),

        agent=researcher,

        callback=callbacks.get(
            "researcher"
        ),
    )


    # =====================================================
    # TASK 2 — FACT CHECK
    # =====================================================

    fact_check_task = Task(

        description=(
            "Review the Researcher's work.\n\n"

            "Research topic:\n"
            "{topic}\n\n"

            "Check the important claims using the "
            "Web Research Tool where necessary.\n\n"

            "Identify:\n"
            "1. Well-supported claims\n"
            "2. Claims that require caution\n"
            "3. Conflicting or uncertain information\n"
            "4. Important corrections\n\n"

            "Do not invent facts."
        ),

        expected_output=(
            "A fact-checking summary that identifies "
            "supported claims, uncertain information "
            "and important corrections."
        ),

        agent=fact_checker,

        context=[
            research_task
        ],

        callback=callbacks.get(
            "fact_checker"
        ),
    )


    # =====================================================
    # TASK 3 — ANALYSIS
    # =====================================================

    analysis_task = Task(

        description=(
            "Analyze the research and fact-checking "
            "results for the topic:\n\n"
            "{topic}\n\n"

            "Produce useful analysis covering:\n"
            "1. Main findings\n"
            "2. Important patterns\n"
            "3. Benefits or opportunities\n"
            "4. Risks or limitations\n"
            "5. Practical implications\n"
            "6. Overall insights\n\n"

            "Base the analysis on the available evidence."
        ),

        expected_output=(
            "A structured analytical summary containing "
            "main findings, patterns, implications, "
            "benefits and limitations."
        ),

        agent=analyst,

        context=[
            research_task,
            fact_check_task
        ],

        callback=callbacks.get(
            "analyst"
        ),
    )


    # =====================================================
    # TASK 4 — FINAL REPORT
    # =====================================================

    report_task = Task(

        description=(
            "Write the final research report about:\n\n"
            "{topic}\n\n"

            "Combine the Researcher's findings, "
            "Fact Checker's verification and Analyst's "
            "insights.\n\n"

            "Use this structure:\n\n"

            "# Research Report\n\n"

            "## 1. Introduction\n\n"
            "## 2. Background\n\n"
            "## 3. Key Findings\n\n"
            "## 4. Verified Evidence\n\n"
            "## 5. Analysis\n\n"
            "## 6. Benefits and Opportunities\n\n"
            "## 7. Risks and Limitations\n\n"
            "## 8. Practical Implications\n\n"
            "## 9. Conclusion\n\n"

            "Keep the report factual, clear and "
            "well organized."
        ),

        expected_output=(
            "A professional Markdown research report "
            "with clear headings, factual explanations "
            "and a concise conclusion."
        ),

        agent=report_writer,

        context=[
            research_task,
            fact_check_task,
            analysis_task
        ],

        callback=callbacks.get(
            "report_writer"
        ),
    )


    # =====================================================
    # CREATE CREW
    # =====================================================

    research_crew = Crew(

        agents=[
            researcher,
            fact_checker,
            analyst,
            report_writer,
        ],

        tasks=[
            research_task,
            fact_check_task,
            analysis_task,
            report_task,
        ],

        process=Process.sequential,

        verbose=True,
    )


    return research_crew
