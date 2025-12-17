"""
Shared data models for Beifong Agents.
Author: Danish (Dan-445)
"""
from typing import List, Optional
from pydantic import BaseModel, Field

# --- Search Agent Models ---

class ReturnItem(BaseModel):
    url: str = Field(..., description="The URL of the search result")
    title: str = Field(..., description="The title of the search result")
    description: str = Field(..., description="A brief description or summary of the search result content")
    source_name: str = Field(
        ...,
        description="The name/type of the source (e.g., 'wikipedia', 'general', or any reputable source tag)",
    )
    tool_used: str = Field(
        ...,
        description="The tools used to generate the search results, unknown if not used or not applicable",
    )
    published_date: str = Field(
        ...,
        description="The published date of the content in ISO format, if not available keep it empty",
    )
    is_scrapping_required: bool = Field(
        ...,
        description="Set to True if the content need scraping, False otherwise, default keep it True if not sure",
    )

class SearchResults(BaseModel):
    items: List[ReturnItem] = Field(..., description="A list of search result items")


# --- Scrape Agent Models ---

class ScrapedContent(BaseModel):
    url: str = Field(..., description="The URL of the search result")
    description: str = Field(description="The description of the search result")
    full_text: str = Field(
        ...,
        description="The full text of the given source URL, if not available or not applicable keep it empty",
    )
    published_date: str = Field(
        ...,
        description="The published date of the content in ISO format, if not available keep it empty",
    )


# --- Podcast Script Agent Models ---

class Dialog(BaseModel):
    speaker: str = Field(..., description="The speaker name (SHOULD BE 'ALEX' OR 'MORGAN')")
    text: str = Field(
        ...,
        description="The spoken text content for this speaker based on the requested language, default is English",
    )

class Section(BaseModel):
    type: str = Field(..., description="The section type (intro, headlines, article, outro)")
    title: Optional[str] = Field(None, description="Optional title for the section (required for article type)")
    dialog: List[Dialog] = Field(..., description="List of dialog exchanges between speakers")

class PodcastScript(BaseModel):
    title: str = Field(..., description="The podcast episode title with date")
    sections: List[Section] = Field(..., description="List of podcast sections (intro, headlines, articles, outro)")
