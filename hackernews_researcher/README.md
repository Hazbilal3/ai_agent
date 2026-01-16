
# HackerNews Research Team 📰
> Autonomous Multi-Agent Journalism and Technology Trend Analysis

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Models](https://img.shields.io/badge/Models-GPT--4o%20%7C%20Llama%203-green.svg)]()

The **HackerNews Research Team** is a fully autonomous, multi-agent newsroom built to research, verify, and synthesize the latest technology trends from HackerNews.

Instead of relying on a single AI agent, this system mimics a real editorial desk where multiple specialized agents collaborate to reduce hallucinations, improve factual accuracy, and generate high-quality outputs such as reports, summaries, blog posts, and social media content.

This project is structured specifically for the **ai_agent** repository.

---

## 📖 Concept Overview

Single-agent research systems struggle with cognitive overload. Searching, reading, validating, and writing simultaneously often leads to missed context or hallucinated facts.

To solve this, the HackerNews Research Team uses a **team-based architecture**, inspired by real-world journalism workflows.

---

## 🧠 Agent Roles

### 1. The Scout (HackerNews Researcher)
- Scans the HackerNews API
- Identifies trending and high-impact stories
- Collects metadata only, no deep reading

### 2. The Analyst (Article Reader)
- Scrapes full articles using Newspaper4k
- Extracts key arguments, insights, and facts
- Removes noise and boilerplate content

### 3. The Fact Checker (Web Searcher)
- Performs lateral reading using DuckDuckGo
- Validates claims with external sources
- Adds historical and competitive context

### 4. The Editor (Team Lead)
- Orchestrates all agents
- Synthesizes findings into a single coherent output
- Aligns results with the user’s query

---

## 🏗 System Architecture

```mermaid
graph TD
    User([User Query]) --> Team[Team Lead Agent]

    subgraph Newsroom
        Team --> Scout[Scout\nHN Researcher]
        Team --> Analyst[Analyst\nArticle Reader]
        Team --> Checker[Fact Checker\nWeb Searcher]

        Scout --> Team
        Analyst --> Team
        Checker --> Team
    end

    Team --> Output[Final Report or Content]

    style Team fill:#f9f,stroke:#333
    style Scout fill:#bbf,stroke:#333
    style Analyst fill:#dfd,stroke:#333
    style Checker fill:#fdd,stroke:#333
````

---

## ✨ Key Capabilities

* Autonomous discovery of trending HackerNews stories
* Deep article reading and structured extraction
* External validation using web search
* Reduced hallucinations through agent specialization
* Flexible outputs including:

  * News summaries
  * Technical trend analysis
  * Blog posts
  * Social media threads

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* OpenAI API Key for GPT-4o mode
* Ollama installed locally with `llama3` model for offline mode

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/hackernews_researcher
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

#### Option A: Cloud Mode (GPT-4o)

```bash
streamlit run research_agent.py
```

#### Option B: Local Mode (Llama 3 via Ollama)

```bash
streamlit run research_agent_llama3.py
```

---

## 🛠 Tech Stack

* Agent Framework: Agno
* Frontend: Streamlit
* Models: GPT-4o or Llama 3
* Tools:

  * HackerNews API
  * Newspaper4k for article parsing
  * DuckDuckGo for web search

---

## 📁 Project Structure

```text
hackernews_researcher/
├── README.md
├── requirements.txt
├── research_agent.py
├── research_agent_llama3.py
├── agents/
│   ├── team_lead.py
│   ├── hn_researcher.py
│   ├── article_reader.py
│   └── fact_checker.py
├── tools/
│   ├── hackernews_tools.py
│   ├── newspaper_tools.py
│   └── duckduckgo_tools.py
```

---

## 📝 Best Practices

* Keep agent responsibilities strictly separated
* Use the Team Lead as the single output authority
* Prefer local Llama 3 mode for sensitive research
* Re-run analysis frequently for fast-moving topics

---

## 📌 Notes

* Designed for technology research and journalism workflows
* Not intended as a real-time alerting system
* Output quality depends on source freshness and relevance

---

## 🙌 Credits

Inspired by multi-agent newsroom and research systems
Adapted and maintained for this repository by **Hazbilal3**

