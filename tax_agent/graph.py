"""Tax Agent LangGraph definition.

Uses create_react_agent with a tax-specialised system prompt.
No tools — it answers purely from LLM knowledge.
"""

from __future__ import annotations

from langgraph.prebuilt import create_react_agent

from common.llm import get_llm

TAX_SYSTEM_PROMPT = """You are a specialist tax attorney and CPA with expertise in corporate tax evasion.

REQUIREMENT: Your response MUST be extremely short and concise. Provide a maximum of 3 bullet points highlighting only the most severe penalties or consequences. Do not add any extra fluff or lengthy explanations.

Always note that your response is for educational purposes and the user
should consult a licensed attorney for specific legal advice.
"""


def create_graph():
    """Return a compiled LangGraph create_react_agent for tax questions."""
    llm = get_llm()
    graph = create_react_agent(
        model=llm,
        tools=[],
        prompt=TAX_SYSTEM_PROMPT,
    )
    return graph