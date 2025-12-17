# HackerNews Research Team 📰
> **Autonomous Multi-Agent Journalism & Analysis**

[![Author](https://img.shields.io/badge/Author-Dan--445-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Models](https://img.shields.io/badge/Models-GPT--4o%20%7C%20Llama%203-green.svg)]()

The **HackerNews Research Team** is not just a scraper; it's an **autonomous newsroom**. A team of three specialized PC agents collaborates to uncover, read, verify, and synthesize the latest tech trends from HackerNews into comprehensive reports, blog posts, or social content.

![HackerNews Team UI](hackernews_team_ui.png)

## 📖 The Architecture Story

When building a research assistant, the biggest challenge is **cognitive load**. A single agent trying to search, read, comparing sources, and writing often hallucinates or misses details.

To solve this, we implemented a **Team-based Architecture** inspired by a real-world editorial desk:

1.  **The Scout (HackerNews Researcher)**: This agent lives on the front lines. Its only job is to sift through the noise of the HackerNews API, identifying trending stories and extracting raw metadata. It doesn't read articles; it finds leads.
2.  **The Analyst (Article Reader)**: Once a lead is identified, the Analyst takes over. It uses `Newspaper4k` to scrape, parse, and "read" the deep content of the target URLs. It separates signal from noise, extracting core arguments and facts.
3.  **The Fact-Checker (Web Searcher)**: Internal sources aren't enough. The Fact-Checker uses DuckDuckGo to lateral-read, finding external context, previous coverage, and related discussions to validate the story's significance.
4.  **The Editor (Team Lead)**: Finally, the Team Lead synthesizes these three distinct streams of information. It acts as the orchestrator, ensuring the final output answers the user's specific query—whether that's "Summarize the top AI news" or "Write a blog post about the latest Rust framework."

### 🧠 System Flowchart

```mermaid
graph TD
    User([User Query]) --> Team[HackerNews Team Lead]
    
    subgraph "The Newsroom"
    Team -- "1. Find Trends" --> HN[The Scout\n(HN Researcher)]
    Team -- "2. Read Content" --> Reader[The Analyst\n(Article Reader)]
    Team -- "3. Verify/Expand" --> Web[The Fact-Checker\n(Web Searcher)]
    
    HN -- "Top Stories List" --> Team
    Reader -- "Extracted Content" --> Team
    Web -- "Context & Validation" --> Team
    end
    
    Team -- "Synthesized Report" --> Report([Final Output])
    
    style Team fill:#f9f,stroke:#333
    style HN fill:#bbf,stroke:#333
    style Reader fill:#dfd,stroke:#333
    style Web fill:#fdd,stroke:#333
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **OpenAI API Key** (for `research_agent.py`)
- **Ollama** running locally with `llama3` (for `research_agent_llama3.py`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/hackernews_researcher
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   
   **Option A: GPT-4o Version (Cloud)**
   ```bash
   streamlit run research_agent.py
   ```
   
   **Option B: Llama 3 Version (Local Privacy)**
   ```bash
   streamlit run research_agent_llama3.py
   ```

## 🛠 Tech Stack
- **Framework**: Agno (formerly Phidata)
- **Frontend**: Streamlit
- **Tools**:
  - `HackerNewsTools`: API interaction
  - `Newspaper4kTools`: Article parsing
  - `DuckDuckGoTools`: Web search

---

**Created by [Dan-445](https://github.com/Dan-445)**
