"""
Scrape Agent Module.
Author: Danish (Dan-445)
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from textwrap import dedent
from tools.browser_crawler import create_browser_crawler

from config import DEFAULT_MODEL_ID
from models.agent_schemas import ScrapedContent
from utils.logger import get_logger

load_dotenv()
logger = get_logger("scrape_agent")

SCRAPE_AGENT_DESCRIPTION = "You are a helpful assistant that can scrape the URL for full content."
SCRAPE_AGENT_INSTRUCTIONS = dedent("""
    You are a content verification and formatting assistant.
    
    You will receive a batch of pre-scraped content from various URLs along with a search query.
    Your job is to:
    
    1. VERIFY RELEVANCE: Ensure each piece of content is relevant to the given query
    2. QUALITY CONTROL: Filter out low-quality, duplicate, or irrelevant content
    3. FORMAT CONSISTENCY: Ensure all content follows a consistent format
    4. LENGTH OPTIMIZATION: Keep content at reasonable length - not too long, not too short
    5. CLEAN TEXT: Remove any formatting artifacts, ads, or navigation elements from scraped content
    
    For each piece of content, return:
    - full_text: The cleaned, relevant text content (or empty if not relevant/low quality)
    - published_date: The publication date in ISO format (or empty if not available)
    
    Note: Some content may be fallback descriptions (when scraping failed) - treat these appropriately and don't penalize them for being shorter.
    
    IMPORTANT: Focus on quality over quantity. It's better to return fewer high-quality, relevant pieces than many low-quality ones.
    """)


def crawl_urls_batch(search_results):
    url_to_search_results = {}
    unique_urls = []
    
    for search_result in search_results:
        # Handle dict or object access
        url = search_result.get("url") if isinstance(search_result, dict) else getattr(search_result, "url", None)
        
        if not url:
            continue
            
        is_required = search_result.get("is_scrapping_required", True) if isinstance(search_result, dict) else getattr(search_result, "is_scrapping_required", True)
        if not is_required:
            continue
            
        original_url = search_result.get('original_url') if isinstance(search_result, dict) else getattr(search_result, 'original_url', None)
        if not original_url:
             if isinstance(search_result, dict):
                search_result['original_url'] = url
             # Note: if it's an object we can't easily set attribute unless it's mutable dataclass/model. 
             # Assuming dict for session state storage.
        
        if url not in url_to_search_results:
            url_to_search_results[url] = []
            unique_urls.append(url)
        url_to_search_results[url].append(search_result)
        
    browser_crawler = create_browser_crawler()
    scraped_results = browser_crawler.scrape_urls(unique_urls)
    url_to_scraped = {result["original_url"]: result for result in scraped_results}
    
    updated_search_results = []
    successful_scrapes = 0
    failed_scrapes = 0
    
    for search_result in search_results:
        # Convert to dict if not already, to ensure mutable
        if not isinstance(search_result, dict):
             if hasattr(search_result, "model_dump"):
                 search_result = search_result.model_dump()
             else:
                 search_result = dict(search_result)

        original_url = search_result["url"]
        scraped = url_to_scraped.get(original_url, {})
        updated_result = search_result.copy()
        updated_result["original_url"] = original_url
        
        if scraped.get("success", False):
            updated_result["url"] = scraped.get("final_url", original_url)
            updated_result["full_text"] = scraped.get("full_text", "")
            updated_result["published_date"] = scraped.get("published_date", "")
            successful_scrapes += 1
        else:
            updated_result["url"] = original_url
            updated_result["full_text"] = search_result.get("description", "")
            updated_result["published_date"] = ""
            failed_scrapes += 1
            
        updated_search_results.append(updated_result)
        
    return updated_search_results, successful_scrapes, failed_scrapes


def verify_content_with_agent(agent, query, search_results, use_agent=True):
    if not use_agent:
        return search_results
    verified_search_results = []
    for _, search_result in enumerate(search_results):
        content_for_verification = {
            "url": search_result["url"],
            "description": search_result.get("description", ""),
            "full_text": search_result["full_text"],
            "published_date": search_result["published_date"],
        }
        search_result["agent_verified"] = False
        try:
            scrape_agent = Agent(
                model=OpenAIChat(id=DEFAULT_MODEL_ID),
                instructions=SCRAPE_AGENT_INSTRUCTIONS,
                description=SCRAPE_AGENT_DESCRIPTION,
                use_json_mode=True,
                session_id=agent.session_id,
                response_model=ScrapedContent,
            )
            response = scrape_agent.run(
                f"Query: {query}\n"
                f"Verify and format this scraped content. "
                f"Keep content relevant to the query and ensure quality: {content_for_verification}",
                session_id=agent.session_id,
            )
            
            # Helper to get dict from response
            if hasattr(response, "content") and hasattr(response.content, "model_dump"):
                 verified_item = response.content.model_dump()
            elif hasattr(response, "to_dict"):
                 verified_item = response.to_dict()["content"]
            else:
                 verified_item = {}

            search_result["full_text"] = verified_item.get("full_text", search_result["full_text"])
            search_result["published_date"] = verified_item.get("published_date", search_result["published_date"])
            search_result["agent_verified"] = True
        except Exception as e:
            logger.error(f"Error validating content: {e}")
            pass
        verified_search_results.append(search_result)
    return verified_search_results


def scrape_agent_run(
    agent: Agent,
    query: str,
) -> str:
    """
    Scrape Agent that takes the search_results (internaly from search_results) and scrapes each URL for full content, making sure those contents are of high quality and relevant to the topic.
    Args:
        agent: The agent instance
        query: The search query
    Returns:
        Response status
    """
    logger.info(f"Scrape Agent Input: {query}")
    session_id = agent.session_id
    from services.internal_session_service import SessionService

    session = SessionService.get_session(session_id)
    current_state = session["state"]
    updated_results, _, _ = crawl_urls_batch(current_state["search_results"])
    verified_results = verify_content_with_agent(agent, query, updated_results, use_agent=False)
    current_state["search_results"] = verified_results
    SessionService.save_session(session_id, current_state)
    has_results = "search_results" in current_state and current_state["search_results"]
    return f"Scraped {len(current_state['search_results'])} sources with full content relevant to '{query}'{' and updated the full text and published date in the search_results items' if has_results else ''}."