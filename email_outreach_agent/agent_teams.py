"""
Core Agent Teams Logic for Email Outreach.
Author: Danish (Dan-445)
"""
import json
import logging
from typing import Any, Dict, List, Optional
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

logger = logging.getLogger(__name__)

def create_company_finder_agent(model_id: str = "gpt-4o") -> Agent:
    """Creates the agent responsible for finding companies matching criteria."""
    exa_tools = ExaTools(category="company")
    db = SqliteDb(db_file="tmp/gtm_outreach.db")
    return Agent(
        model=OpenAIChat(id=model_id),
        tools=[exa_tools],
        db=db,
        enable_user_memories=True,
        add_history_to_context=True,
        num_history_runs=6,
        session_id="gtm_outreach_company_finder",
        debug_mode=True,
        instructions=[
            "You are CompanyFinderAgent. Use ExaTools to search the web for companies that match the targeting criteria.",
            "Return ONLY valid JSON with key 'companies' as a list; respect the requested limit provided in the user prompt.",
            "Each item must have: name, website, why_fit (1-2 lines).",
        ],
    )

def create_contact_finder_agent(model_id: str = "gpt-4o") -> Agent:
    """Creates the agent responsible for finding decision maker contacts."""
    exa_tools = ExaTools()
    db = SqliteDb(db_file="tmp/gtm_outreach.db")
    return Agent(
        model=OpenAIChat(id=model_id),
        tools=[exa_tools],
        db=db,
        enable_user_memories=True,
        add_history_to_context=True,
        num_history_runs=6,
        session_id="gtm_outreach_contact_finder",
        debug_mode=True,
        instructions=[
            "You are ContactFinderAgent. Use ExaTools to find 1-2 relevant decision makers per company and their emails if available.",
            "Prioritize roles from Founder's Office, GTM (Marketing/Growth), Sales leadership, Partnerships/Business Development, and Product Marketing.",
            "Search queries can include patterns like '<Company> email format', 'contact', 'team', 'leadership', and role titles.",
            "If direct emails are not found, infer likely email using common formats (e.g., first.last@domain), but mark inferred=true.",
            "Return ONLY valid JSON with key 'companies' as a list; each has: name, contacts: [{full_name, title, email, inferred}]",
        ],
    )

def get_email_style_instruction(style_key: str) -> str:
    styles = {
        "Professional": "Style: Professional. Clear, respectful, and businesslike. Short paragraphs; no slang.",
        "Casual": "Style: Casual. Friendly, approachable, first-name basis. No slang or emojis; keep it human.",
        "Cold": "Style: Cold email. Strong hook in opening 2 lines, tight value proposition, minimal fluff, strong CTA.",
        "Consultative": "Style: Consultative. Insight-led, frames observed problems and tailored solution hypotheses; soft CTA.",
    }
    return styles.get(style_key, styles["Professional"])

def create_email_writer_agent(style_key: str = "Professional", model_id: str = "gpt-4o") -> Agent:
    """Creates the agent responsible for drafting personalized emails."""
    db = SqliteDb(db_file="tmp/gtm_outreach.db")
    style_instruction = get_email_style_instruction(style_key)
    return Agent(
        model=OpenAIChat(id=model_id),
        tools=[],
        db=db,
        enable_user_memories=True,
        add_history_to_context=True,
        num_history_runs=6,
        session_id="gtm_outreach_email_writer",
        debug_mode=False,
        instructions=[
            "You are EmailWriterAgent. Write concise, personalized B2B outreach emails.",
            style_instruction,
            "Return ONLY valid JSON with key 'emails' as a list of items: {company, contact, subject, body}.",
            "Length: 120-160 words. Include 1-2 lines of strong personalization referencing research insights (company website and Reddit findings).",
            "CTA: suggest a short intro call; include sender company name and calendar link if provided.",
        ],
    )

def create_research_agent(model_id: str = "gpt-4o") -> Agent:
    """Agent to gather interesting insights from company websites and Reddit."""
    # Note: Using gpt-4o as default instead of gpt-5 to be safe, unless user has access. 
    # The original code had gpt-5, but that's likely a placeholders or restricted. 
    # I will stick to gpt-4o for broad compatibility or allow override.
    exa_tools = ExaTools()
    db = SqliteDb(db_file="tmp/gtm_outreach.db")
    return Agent(
        model=OpenAIChat(id=model_id),
        tools=[exa_tools],
        db=db,
        enable_user_memories=True,
        add_history_to_context=True,
        num_history_runs=6,
        session_id="gtm_outreach_researcher",
        debug_mode=True,
        instructions=[
            "You are ResearchAgent. For each company, collect concise, valuable insights from:",
            "1) Their official website (about, blog, product pages)",
            "2) Reddit discussions (site:reddit.com mentions)",
            "Summarize 2-4 interesting, non-generic points per company that a human would bring up in an email to show genuine effort.",
            "Return ONLY valid JSON with key 'companies' as a list; each has: name, insights: [strings].",
        ],
    )

def extract_json_or_raise(text: str) -> Dict[str, Any]:
    """Extract JSON from a model response. Assumes the response is pure JSON."""
    try:
        if "```json" in text:
             text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
             text = text.split("```")[1].split("```")[0].strip()
             
        return json.loads(text)
    except Exception as e:
        # Try to locate a JSON block if extra text snuck in
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            candidate = text[start : end + 1]
            return json.loads(candidate)
        raise ValueError(f"Failed to parse JSON: {e}\nResponse was:\n{text}")

def run_company_finder(agent: Agent, target_desc: str, offering_desc: str, max_companies: int) -> List[Dict[str, str]]:
    prompt = (
        f"Find exactly {max_companies} companies that are a strong B2B fit given the user inputs.\n"
        f"Targeting: {target_desc}\n"
        f"Offering: {offering_desc}\n"
        "For each, provide: name, website, why_fit (1-2 lines)."
    )
    resp: RunOutput = agent.run(prompt)
    data = extract_json_or_raise(str(resp.content))
    companies = data.get("companies", [])
    return companies[: max(1, min(max_companies, 10))]

def run_contact_finder(agent: Agent, companies: List[Dict[str, str]], target_desc: str, offering_desc: str) -> List[Dict[str, Any]]:
    prompt = (
        "For each company below, find 2-3 relevant decision makers and emails (if available). Ensure at least 2 per company when possible, and cap at 3.\n"
        "If not available, infer likely email and mark inferred=true.\n"
        f"Targeting: {target_desc}\nOffering: {offering_desc}\n"
        f"Companies JSON: {json.dumps(companies, ensure_ascii=False)}\n"
        "Return JSON: {companies: [{name, contacts: [{full_name, title, email, inferred}]}]}"
    )
    resp: RunOutput = agent.run(prompt)
    data = extract_json_or_raise(str(resp.content))
    return data.get("companies", [])

def run_research(agent: Agent, companies: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    prompt = (
        "For each company, gather 2-4 interesting insights from their website and Reddit that would help personalize outreach.\n"
        f"Companies JSON: {json.dumps(companies, ensure_ascii=False)}\n"
        "Return JSON: {companies: [{name, insights: [string, ...]}]}"
    )
    resp: RunOutput = agent.run(prompt)
    data = extract_json_or_raise(str(resp.content))
    return data.get("companies", [])

def run_email_writer(agent: Agent, contacts_data: List[Dict[str, Any]], research_data: List[Dict[str, Any]], offering_desc: str, sender_name: str, sender_company: str, calendar_link: Optional[str]) -> List[Dict[str, str]]:
    prompt = (
        "Write personalized outreach emails for the following contacts.\n"
        f"Sender: {sender_name} at {sender_company}.\n"
        f"Offering: {offering_desc}.\n"
        f"Calendar link: {calendar_link or 'N/A'}.\n"
        f"Contacts JSON: {json.dumps(contacts_data, ensure_ascii=False)}\n"
        f"Research JSON: {json.dumps(research_data, ensure_ascii=False)}\n"
        "Return JSON with key 'emails' as a list of {company, contact, subject, body}."
    )
    resp: RunOutput = agent.run(prompt)
    data = extract_json_or_raise(str(resp.content))
    return data.get("emails", [])
