# Deep Research Agent 🔍
> **Automated Multi-Source Research & Reporting**

[![Author](https://img.shields.io/badge/Author-Dan--445-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-purple.svg)](https://github.com/agno-agi/agno)
[![Composio](https://img.shields.io/badge/Composio-Integration-green.svg)](https://composio.ai/)

The **Deep Research Agent** is a sophisticated AI analyst capable of conducting autonomous deep-dives into any topic. It breaks down complex subjects into specific research questions, investigates them using multiple search engines (Tavily, Perplexity), and compiles a professional McKinsey-style report directly into Google Docs.

![Research Agent UI](research_agent_ui.png)

## 🏗 Architecture

```mermaid
graph TD
    User([User Topic: Quantum Computing]) --> Generator[Question Generator Agent]
    Generator -- Qwen 3 --> Questions[5 Targeted Questions]
    Questions --> Researcher[Research Agent]
    
    subgraph "Deep Research Loop"
    Researcher -- Tavily Search --> Web[Web Sources]
    Researcher -- Perplexity AI --> Analysis[Deep Analysis]
    Web --> Researcher
    Analysis --> Researcher
    end
    
    Researcher -- Findings --> Compiler[Report Compiler Agent]
    Compiler -- Google Docs Tool --> Doc([Final Report GDoc])
    
    style Generator fill:#f9f,stroke:#333
    style Researcher fill:#bbf,stroke:#333
    style Compiler fill:#bfb,stroke:#333
```

## ✨ Capabilities
- **Intelligent Scoping**: Automatically breaks broad topics into 5 precise, researchable yes/no questions.
- **Multi-Source Verification**: Cross-references findings from standard web search (Tavily) and AI-driven answer engines (Perplexity).
- **Automated Reporting**: Synthesizes findings into a cohesive narrative (not just a bulleted list) and formats it in a Google Doc.
- **Professional Output**: Produces reports structured with Executive Summaries, Analysis, and Strategic Implications.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **Together AI API Key** (for LLM inference)
- **Composio API Key** (for tool integrations: Google Docs, search)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/deep_research_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Composio Tools**
   ```bash
   composio add googledocs
   composio add perplexityai
   ```

4. **Run the Agent**
   ```bash
   streamlit run ai_domain_deep_research_agent.py
   ```

## 🛠 Configuration
Enter your API keys in the sidebar configuration panel to unlock the agent's full capabilities.

---

**Created by [Dan-445](https://github.com/Dan-445)**
