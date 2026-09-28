import os

# MONKEY PATCH FOR CREWAI GROQ CACHE ISSUE
import crewai.llm

_original_call = crewai.llm.LLM.call

def patched_call(self, messages, *args, **kwargs):
    if isinstance(messages, list):
        cleaned_messages = []
        for msg in messages:
            if isinstance(msg, dict):
                msg_copy = {k: v for k, v in msg.items() if k != "cache_breakpoint"}
                cleaned_messages.append(msg_copy)
            else:
                cleaned_messages.append(msg)
        messages = cleaned_messages
    return _original_call(self, messages, *args, **kwargs)

crewai.llm.LLM.call = patched_call


from crewai import Agent, Crew, LLM, Process, Task
from researcher import create_researcher
from fact_checker import create_fact_checker
from analyst import create_analyst
from report_writer import create_report_writer
from tools import get_research_tool

# High Quota Model Set Kar Diya Hai
MODEL_NAME = "groq/llama-3.3-70b-versatile"


def create_groq_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.2,
    )
