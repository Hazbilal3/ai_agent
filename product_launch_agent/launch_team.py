"""
Product Launch Team Logic.
Author: Danish (Dan-445)
"""
from typing import Optional
from textwrap import dedent
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.firecrawl import FirecrawlTools
from agno.run.agent import RunOutput

def create_product_team(openai_key: str, firecrawl_key: str) -> Optional[Team]:
    """Creates the Product Intelligence Team with the given keys."""
    if not openai_key or not firecrawl_key:
        return None

    # Agent 1: Competitor Launch Analyst
    launch_analyst = Agent(
        name="Product Launch Analyst",
        description=dedent("""
            You are a senior Go-To-Market strategist who evaluates competitor product launches with a critical, evidence-driven lens.
            Your objective is to uncover:
            • How the product is positioned in the market
            • Which launch tactics drove success (strengths)
            • Where execution fell short (weaknesses)
            • Actionable learnings competitors can leverage
            Always cite observable signals (messaging, pricing actions, channel mix, timing, engagement metrics). Maintain a crisp, executive tone and focus on strategic value.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """),
        model=OpenAIChat(id="gpt-4o", api_key=openai_key),
        tools=[FirecrawlTools(api_key=firecrawl_key, search=True, crawl=True, poll_interval=10)],
        debug_mode=True,
        markdown=True,
        exponential_backoff=True,
        delay_between_retries=2,
    )
    
    # Agent 2: Market Sentiment Specialist
    sentiment_analyst = Agent(
        name="Market Sentiment Specialist",
        description=dedent("""
            You are a market research expert specializing in sentiment analysis and consumer perception tracking.
            Your expertise includes:
            • Analyzing social media sentiment and customer feedback
            • Identifying positive and negative sentiment drivers
            • Tracking brand perception trends across platforms
            • Monitoring customer satisfaction and review patterns
            • Providing actionable insights on market reception
            Focus on extracting sentiment signals from social platforms, review sites, forums, and customer feedback channels.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """),
        model=OpenAIChat(id="gpt-4o", api_key=openai_key),
        tools=[FirecrawlTools(api_key=firecrawl_key, search=True, crawl=True, poll_interval=10)],
        debug_mode=True,
        markdown=True,
        exponential_backoff=True,
        delay_between_retries=2,
    )
    
    # Agent 3: Launch Metrics Specialist
    metrics_analyst = Agent(
        name="Launch Metrics Specialist", 
        description=dedent("""
            You are a product launch performance analyst who specializes in tracking and analyzing launch KPIs.
            Your focus areas include:
            • User adoption and engagement metrics
            • Revenue and business performance indicators
            • Market penetration and growth rates
            • Press coverage and media attention analysis
            • Social media traction and viral coefficient tracking
            • Competitive market share analysis
            Always provide quantitative insights with context and benchmark against industry standards when possible.
            IMPORTANT: Conclude your report with a 'Sources:' section, listing all URLs of websites you crawled or searched for this analysis.
        """),
        model=OpenAIChat(id="gpt-4o", api_key=openai_key),
        tools=[FirecrawlTools(api_key=firecrawl_key, search=True, crawl=True, poll_interval=10)],
        debug_mode=True,
        markdown=True,
        exponential_backoff=True,
        delay_between_retries=2,
    )

    # Create the coordinated team
    return Team(
        name="Product Intelligence Team",
        model=OpenAIChat(id="gpt-4o", api_key=openai_key),
        members=[launch_analyst, sentiment_analyst, metrics_analyst],
        instructions=[
            "Coordinate the analysis based on the user's request type:",
            "1. For competitor analysis: Use the Product Launch Analyst to evaluate positioning, strengths, weaknesses, and strategic insights",
            "2. For market sentiment: Use the Market Sentiment Specialist to analyze social media sentiment, customer feedback, and brand perception",
            "3. For launch metrics: Use the Launch Metrics Specialist to track KPIs, adoption rates, press coverage, and performance indicators",
            "Always provide evidence-based insights with specific examples and data points",
            "Structure responses with clear sections and actionable recommendations",
            "Include sources section with all URLs crawled or searched"
        ],
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
    )


# Helper to craft competitor-focused launch report for product managers
def expand_competitor_report(team: Team, bullet_text: str, competitor: str) -> str:
    prompt = (
        f"Transform the insight bullets below into a professional launch review for product managers analysing {competitor}.\n\n"
        f"Produce well-structured **Markdown** with a mix of tables, call-outs and concise bullet points — avoid long paragraphs.\n\n"
        f"=== FORMAT SPECIFICATION ===\n"
        f"# {competitor} – Launch Review\n\n"
        f"## 1. Market & Product Positioning\n"
        f"• Bullet point summary of how the product is positioned (max 6 bullets).\n\n"
        f"## 2. Launch Strengths\n"
        f"| Strength | Evidence / Rationale |\n|---|---|\n| … | … | (add 4-6 rows)\n\n"
        f"## 3. Launch Weaknesses\n"
        f"| Weakness | Evidence / Rationale |\n|---|---|\n| … | … | (add 4-6 rows)\n\n"
        f"## 4. Strategic Takeaways for Competitors\n"
        f"1. … (max 5 numbered recommendations)\n\n"
        f"=== SOURCE BULLETS ===\n{bullet_text}\n\n"
        f"Guidelines:\n"
        f"• Populate the tables with specific points derived from the bullets.\n"
        f"• Only include rows that contain meaningful data; omit any blank entries."
    )
    resp: RunOutput = team.run(prompt)
    return resp.content if hasattr(resp, "content") else str(resp)


# Helper to craft market sentiment report
def expand_sentiment_report(team: Team, bullet_text: str, product: str) -> str:
    prompt = (
        f"Use the tagged bullets below to create a concise market-sentiment brief for **{product}**.\n\n"
        f"### Positive Sentiment\n"
        f"• List each positive point as a separate bullet (max 6).\n\n"
        f"### Negative Sentiment\n"
        f"• List each negative point as a separate bullet (max 6).\n\n"
        f"### Overall Summary\n"
        f"Provide a short paragraph (≤120 words) summarising the overall sentiment balance and key drivers.\n\n"
        f"Tagged Bullets:\n{bullet_text}"
    )
    resp: RunOutput = team.run(prompt)
    return resp.content if hasattr(resp, "content") else str(resp)


# Helper to craft launch metrics report
def expand_metrics_report(team: Team, bullet_text: str, launch: str) -> str:
    prompt = (
        f"Convert the KPI bullets below into a launch-performance snapshot for **{launch}** suitable for an executive dashboard.\n\n"
        f"## Key Performance Indicators\n"
        f"| Metric | Value / Detail | Source |\n"
        f"|---|---|---|\n"
        f"| … | … | … |  (include one row per KPI)\n\n"
        f"## Qualitative Signals\n"
        f"• Bullet list of notable qualitative insights (max 5).\n\n"
        f"## Summary & Implications\n"
        f"Brief paragraph (≤120 words) highlighting what the metrics imply about launch success and next steps.\n\n"
        f"KPI Bullets:\n{bullet_text}"
    )
    resp: RunOutput = team.run(prompt)
    return resp.content if hasattr(resp, "content") else str(resp)
