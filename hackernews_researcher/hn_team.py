"""
HackerNews Agent Team Logic.
Author: Danish (Dan-445)
"""
import logging
from typing import Optional, Literal

from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools

from config import DEFAULT_OPENAI_MODEL, DEFAULT_OLLAMA_MODEL

logger = logging.getLogger(__name__)

def get_model(provider: Literal["OpenAI", "Ollama"], api_key: Optional[str] = None, model_id: Optional[str] = None):
    """Factory to get the requested Model instance."""
    if provider == "OpenAI":
        mid = model_id or DEFAULT_OPENAI_MODEL
        if not api_key:
            raise ValueError("OpenAI API Key is required for OpenAI models.")
        return OpenAIChat(id=mid, api_key=api_key)
    
    elif provider == "Ollama":
        mid = model_id or DEFAULT_OLLAMA_MODEL
        # Ollama is local, usually no key needed unless proxied.
        return Ollama(id=mid)
    
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def create_hackernews_team(
    provider: Literal["OpenAI", "Ollama"] = "OpenAI",
    api_key: Optional[str] = None,
    model_id: Optional[str] = None
) -> Team:
    """
    Creates the HackerNews Research Team with the specified backend.
    
    Args:
        provider: "OpenAI" or "Ollama"
        api_key: OpenAI API Key (if provider is OpenAI)
        model_id: Optional model override
        
    Returns:
        Agno Team instance
    """
    logger.info(f"Creating HackerNews Team with provider: {provider}")
    
    # We use the same model config for all agents in the team for consistency,
    # but technically they could vary.
    
    # 1. HackerNews Researcher
    hn_researcher = Agent(
        name="HackerNews Researcher",
        model=get_model(provider, api_key, model_id),
        role="Gets top stories from hackernews.",
        tools=[HackerNewsTools()],
    )

    # 2. Web Searcher
    web_searcher = Agent(
        name="Web Searcher",
        model=get_model(provider, api_key, model_id),
        role="Searches the web for information on a topic",
        tools=[DuckDuckGoTools()],
        add_datetime_to_context=True,
    )

    # 3. Article Reader
    article_reader = Agent(
        name="Article Reader",
        model=get_model(provider, api_key, model_id),
        role="Reads articles from URLs.",
        tools=[Newspaper4kTools()],
    )

    # 4. Team Lead
    hackernews_team = Team(
        name="HackerNews Team",
        model=get_model(provider, api_key, model_id),
        members=[hn_researcher, web_searcher, article_reader],
        instructions=[
            "First, search hackernews for what the user is asking about.",
            "Then, ask the article reader to read the links for the stories to get more information.",
            "Important: you must provide the article reader with the links to read.",
            "Then, ask the web searcher to search for each story to get more information.",
            "Finally, provide a thoughtful and engaging summary.",
        ],
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
    )
    
    return hackernews_team
