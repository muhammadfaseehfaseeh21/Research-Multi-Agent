import os

# =========================================================
# MONKEY PATCH: Fix CrewAI cache_breakpoint issue for Groq
# =========================================================
import crewai.llm

_original_call = crewai.llm.LLM.call

def patched_call(self, messages, *args, **kwargs):
    if isinstance(messages, list):
        cleaned_messages = []
        for msg in messages:
            if isinstance(msg, dict):
                # Copy dict and remove cache_breakpoint key
                msg_copy = {k: v for k, v in msg.items() if k != "cache_breakpoint"}
                cleaned_messages.append(msg_copy)
            else:
                cleaned_messages.append(msg)
        messages = cleaned_messages
    return _original_call(self, messages, *args, **kwargs)

crewai.llm.LLM.call = patched_call
# =========================================================

from crewai import Agent, Crew, LLM, Process, Task

from researcher import create_researcher
from fact_checker import create_fact_checker
from analyst import create_analyst
from report_writer import create_report_writer
from tools import get_research_tool


MODEL_NAME = "groq/openai/gpt-oss-120b"

def create_groq_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model=MODEL_NAME,
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.2,
    )


def build_crew(callbacks=None):
    if callbacks is None:
        callbacks = {}

    llm = create_groq_llm()
    research_tool = get_research_tool()

    researcher = create_researcher(
        llm,
        research_tool,
        callbacks.get("researcher"),
    )

    fact_checker = create_fact_checker(
        llm,
        research_tool,
        callbacks.get("fact_checker"),
    )

    analyst = create_analyst(
        llm,
        research_tool,
        callbacks.get("analyst"),
    )

    report_writer = create_report_writer(
        llm,
        research_tool,
        callbacks.get("report_writer"),
    )

    research_task = Task(
        description="""
        Research the following topic thoroughly:

        {topic}

        Use the Web Research Tool to gather current and relevant
        information.

        Find:
        - Important facts
        - Key concepts
        - Recent developments
        - Relevant evidence
        - Reliable sources

        Return organized research notes for the fact checker.
        """,
        expected_output="""
        A detailed research brief containing:
        1. Main findings
        2. Important facts
        3. Evidence
        4. Recent information
        5. Source names or URLs
        """,
        agent=researcher,
    )

    fact_check_task = Task(
        description="""
        Carefully fact-check the research produced by the Researcher for the topic: {topic}.

        Use the provided context from the research task and the Web Research Tool to verify important claims.

        For each important claim:
        - Determine whether it is supported
        - Identify conflicting information if relevant
        - Remove or flag unsupported claims
        - Prefer reliable sources

        Return a verified research brief.
        """,
        expected_output="""
        A fact-checked research brief containing:
        - Verified claims
        - Claims needing caution
        - Important corrections
        - Supporting sources
        """,
        agent=fact_checker,
        context=[research_task],
    )

    analysis_task = Task(
        description="""
        Analyze the verified research for the topic: {topic}.

        Review the fact-checked findings provided in the context and identify:
        - Major findings
        - Important patterns
        - Relationships between ideas
        - Practical implications
        - Areas of uncertainty
        - Key insights

        Keep the analysis evidence-based.
        """,
        expected_output="""
        A structured analytical brief containing:
        1. Major findings
        2. Key insights
        3. Patterns and relationships
        4. Implications
        5. Important limitations
        """,
        agent=analyst,
        context=[fact_check_task],
    )

    report_task = Task(
        description="""
        Write the final research report on: {topic}

        Use the verified research and analysis provided in the context to create a professional report with:

        # Research Report

        ## Executive Summary

        ## Introduction

        ## Key Findings

        ## Evidence and Analysis

        ## Important Insights

        ## Limitations

        ## Conclusion

        ## Sources

        Do not invent sources.
        Do not present unsupported claims as facts.
        Keep the report clear and readable.
        """,
        expected_output="""
        A polished research report containing:
        - Executive Summary
        - Introduction
        - Key Findings
        - Evidence and Analysis
        - Important Insights
        - Limitations
        - Conclusion
        - Sources
        """,
        agent=report_writer,
        context=[fact_check_task, analysis_task],
    )

    crew = Crew(
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

    return crew
