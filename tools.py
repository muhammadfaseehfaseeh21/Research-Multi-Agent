import os
from typing import Type

from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from groq import Groq


class WebResearchInput(BaseModel):
    query: str = Field(
        ...,
        description="The research question or topic that should be searched on the web."
    )


class WebResearchTool(BaseTool):
    name: str = "Web Research Tool"

    description: str = (
        "Searches the live web using Groq's built-in browser search. "
        "Use this tool when you need current information, evidence, "
        "facts, sources, statistics, or recent developments."
    )

    args_schema: Type[BaseModel] = WebResearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "ERROR: GROQ_API_KEY is not configured."

        try:
            client = Groq(api_key=api_key)

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a research web-search assistant. "
                            "Search the web and return useful factual evidence. "
                            "Prefer reliable and authoritative sources. "
                            "Include source names or URLs when available."
                        ),
                    },
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                tools=[
                    {
                        "type": "browser_search"
                    }
                ],
            )

            result = response.choices[0].message.content

            if not result:
                return "The web search returned no readable result."

            return result

        except Exception as e:
            return f"Web research tool error: {str(e)}"


def get_research_tool():
    return WebResearchTool()
