
# Deep Research Agent 🔍
> Automated Multi-Source Research and Reporting Agent

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-purple.svg)](https://github.com/agno-agi/agno)
[![Composio](https://img.shields.io/badge/Composio-Integration-green.svg)](https://composio.ai/)

The **Deep Research Agent** is an advanced multi-agent AI system designed to perform autonomous, end-to-end research on any topic.  
It decomposes complex domains into focused research questions, investigates them using multiple sources, and compiles a professional, consultant-grade report directly into Google Docs.

This version is structured specifically for the **ai_agent** repository.

---

## Architecture

```mermaid
graph TD
    User([User Topic Input]) --> Generator[Question Generator Agent]
    Generator --> Questions[Targeted Research Questions]
    Questions --> Researcher[Research Agent]

    subgraph Deep_Research_Loop
        Researcher --> Tavily[Tavily Web Search]
        Researcher --> Perplexity[Perplexity AI]
        Tavily --> Researcher
        Perplexity --> Researcher
    end

    Researcher --> Compiler[Report Compiler Agent]
    Compiler --> GoogleDocs[Google Docs Output]

    style Generator fill:#f9f,stroke:#333
    style Researcher fill:#bbf,stroke:#333
    style Compiler fill:#bfb,stroke:#333
````

---

## Core Capabilities

* Automated topic scoping into focused research questions
* Multi-source verification using web search and AI answer engines
* Iterative deep analysis loop instead of shallow one-pass searches
* Professional report generation with executive summary and insights
* Direct publishing to Google Docs for sharing and collaboration

---

## Agent Roles

| Agent              | Responsibility                                 |
| ------------------ | ---------------------------------------------- |
| Question Generator | Converts topic into precise research questions |
| Research Agent     | Performs deep multi-source investigation       |
| Report Compiler    | Synthesizes findings into a structured report  |
| Tool Layer         | Google Docs, Tavily, Perplexity                |

---

## Quick Start

### Prerequisites

* Python 3.10+
* Together AI API Key
* Composio API Key

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/deep_research_agent
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Install Composio Tools

```bash
composio add googledocs
composio add perplexityai
```

#### 4. Run the Application

```bash
streamlit run ai_domain_deep_research_agent.py
```

---

## Configuration

* API keys are entered through the Streamlit sidebar
* Enable or disable tools based on research needs
* Adjust research depth according to topic complexity

---

## Suggested Project Structure

```text
deep_research_agent/
├── README.md
├── requirements.txt
├── ai_domain_deep_research_agent.py
├── agents/
│   ├── question_generator.py
│   ├── research_agent.py
│   └── report_compiler.py
├── tools/
│   ├── tavily_search.py
│   ├── perplexity_client.py
│   └── google_docs.py
```

---

## Best Practices

* Keep research questions narrowly scoped
* Confirm findings across multiple sources
* Treat the compiler agent as read-only
* Log intermediate outputs for transparency

---

## Notes

* Designed for research, strategy, and analysis use cases
* Output quality improves with clear initial topic prompts
* Google Docs access must be authorized via Composio

---

## Credits

Inspired by open multi-agent research systems
Adapted and maintained for this repository by **Hazbilal3**

