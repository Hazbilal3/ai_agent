"""
Podcast Script Agent Module.
Author: Danish (Dan-445)
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from typing import List
from dotenv import load_dotenv
from textwrap import dedent
from datetime import datetime

from config import DEFAULT_MODEL_ID
from models.agent_schemas import PodcastScript
from utils.logger import get_logger

load_dotenv()
logger = get_logger("script_agent")

PODCAST_AGENT_DESCRIPTION = "You are a helpful assistant that can generate engaging podcast scripts for the given sources."
PODCAST_AGENT_INSTRUCTIONS = dedent("""
    You are a helpful assistant that can generate engaging podcast scripts for the given source content and query.
    For given content, create an engaging podcast script that should be at least 15 minutes worth of content and your allowed enhance the script beyond given sources if you know something additional info will be interesting to the discussion or not enough conents available.
    You use the provided sources to ground your podcast script generation process. Keep it engaging and interesting.
    
    IMPORTANT: Generate the entire script in the provided language. basically only text field needs to be in requested language,
    
    CONTENT GUIDELINES [THIS IS EXAMPLE YOU CAN CHANGE THE GUIDELINES ANYWAY BASED ON THE QUERY OR TOPIC DISCUSSED]:
    - Provide insightful analysis that helps the audience understand the significance
    - Include discussions on potential implications and broader context of each story
    - Explain complex concepts in an accessible but thorough manner
    - Make connections between current and relevant historical developments when applicable
    - Provide comparisons and contrasts with similar stories or trends when relevant
    
    PERSONALITY NOTES [THIS IS EXAMPLE YOU CAN CHANGE THE PERSONALITY OF ALEX AND MORGAN ANYWAY BASED ON THE QUERY OR TOPIC DISCUSSED]:
    - Alex is more analytical and fact-focused
    * Should reference specific details and data points
    * Should explain complex topics clearly
    * Should identify key implications of stories
    - Morgan is more focused on human impact, social context, and practical applications
    * Should analyze broader implications
    * Should consider ethical implications and real-world applications
    - Include natural, conversational banter and smooth transitions between topics
    - Each article discussion should go beyond the basic summary to provide valuable insights
    - Maintain a conversational but informed tone that would appeal to a general audience
    
    IMPORTNAT:
        - MAKE SURE PODCAST SCRIPS ARE AT LEAST 15 MINUTES LONG WHICH MEANS YOU NEED TO HAVE DETAILED DISCUSSIONS OFFCOURSE KEEP IT INTERESTING AND ENGAGING.
    """)


def format_search_results_for_podcast(
    search_results: List[dict],
) -> tuple[str, List[str]]:
    created_at = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    structured_content = []
    structured_content.append(f"PODCAST CREATION: {created_at}\n")
    sources = []
    
    if not search_results:
        return "", []

    for idx, search_result in enumerate(search_results):
        try:
            # Handle possible object instead of dict
            if hasattr(search_result, "get"):
                 confirmed = search_result.get("confirmed", False)
                 url = search_result.get("url")
                 title = search_result.get("title")
                 full_text = search_result.get("full_text")
                 description = search_result.get("description", "")
            else:
                 # Assume dataclass/pydantic
                 confirmed = getattr(search_result, "confirmed", False)
                 url = getattr(search_result, "url", "")
                 title = getattr(search_result, "title", "")
                 full_text = getattr(search_result, "full_text", "")
                 description = getattr(search_result, "description", "")

            if confirmed:
                sources.append(url)
                structured_content.append(
                    f"""
                                        SOURCE {idx + 1}:
                                        Title: {title}
                                        URL: {url}
                                        Content: {full_text or description}
                                        ---END OF SOURCE {idx + 1}---
                                        """.strip()
                )
        except Exception as e:
            logger.error(f"Error processing search result: {e}")
            
    content_texts = "\n\n".join(structured_content)
    return content_texts, sources


def podcast_script_agent_run(
    agent: Agent,
    query: str,
    language_name: str,
) -> str:
    """
    Podcast Script Agent that takes the search_results (internally from search_results) and creates a podcast script for the given query and language.

    Args:
        agent: The agent instance
        query: The search query
        language_name: The language the podcast script should be.
    Returns:
        Response status
    """
    from services.internal_session_service import SessionService
    session_id = agent.session_id
    session = SessionService.get_session(session_id)
    session_state = session["state"]
    
    logger.info(f"Podcast Script Agent Input: {query}")
    content_texts, sources = format_search_results_for_podcast(session_state.get("search_results", []))
    if not content_texts:
        return "No confirmed sources found to generate podcast script."

    podcast_script_agent = Agent(
        model=OpenAIChat(id=DEFAULT_MODEL_ID),
        instructions=PODCAST_AGENT_INSTRUCTIONS,
        description=PODCAST_AGENT_DESCRIPTION,
        use_json_mode=True,
        response_model=PodcastScript,
        session_id=agent.session_id,
    )
    
    response = podcast_script_agent.run(
        f"query: {query}\n language_name: {language_name}\n content_texts: {content_texts}\n, IMPORTANT: texts should be in {language_name} language.",
        session_id=agent.session_id,
    )
    
    response_dict = response.to_dict()
    # Extract content from response
    if "content" in response_dict:
        script_content = response_dict["content"]
        # If it's still an object (Pydantic model), dump it
        if hasattr(script_content, "model_dump"):
            script_content = script_content.model_dump()
            
        script_content["sources"] = sources
        session_state["generated_script"] = script_content
    else:
        logger.error("Failed to extract content from script agent response")
        
    session_state['stage'] = 'script'
    SessionService.save_session(session_id, session_state)

    if not session_state.get("generated_script") or not session_state["generated_script"].get("sections"):
        return "Failed to generate podcast script."
        
    return f"Generated podcast script for '{query}' with {len(sources)} confirmed sources."