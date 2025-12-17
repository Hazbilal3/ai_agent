# Product Launch Intelligence Agent 🚀
> **The GTM War Room powered by Multi-Agent AI**

[![Author](https://img.shields.io/badge/Author-Dan--445-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Firecrawl](https://img.shields.io/badge/Data-Firecrawl-orange.svg)](https://www.firecrawl.dev/)

The **Product Launch Intelligence Agent** is your automated Go-To-Market (GTM) War Room. Instead of manually scouring the web, checking Reddit sentiment, and hunting for competitor pricing, this system deploys a coordinated team of three specialized PC agents to build a comprehensive launch strategy report in minutes.

![Product Launch UI](product_launch_ui.png)

## 📖 The Architecture Story

Launch days are chaotic. You need strategy, public perception, and hard data all at once. We designed this agent team to mimic the structure of a high-functioning **Product "War Room"**:

1.  **The Strategist (Product Launch Analyst)**: This agent thinks big picture. It looks at *positioning*—how does your product stack up against the competition's latest moves? It uses Firecrawl to find deep competitive intel that Google searches often miss.
2.  **The Ear (Market Sentiment Specialist)**: While the strategist looks at features, The Ear listens to the *people*. It scans social channels, forums, and reviews to understand the emotional landscape—are people excited, skeptical, or indifferent?
3.  **The Scorekeeper (Launch Metrics Specialist)**: This agent deals in cold, hard facts. Adoption numbers, press mentions, pricing tiers. It ensures your strategy is grounded in data, not just vibes.

### 🧠 War Room Flowchart

```mermaid
graph TD
    User([User Query: Company/Product]) --> Platform[Streamlit Interface]
    Platform --> Team[Launch Intelligence Team]
    
    subgraph "The War Room"
    Team -- "Strategy & Positioning" --> Analyst[The Strategist\n(Launch Analyst)]
    Team -- "Public Perception" --> Sentiment[The Ear\n(Sentiment Specialist)]
    Team -- "Performance Data" --> Metrics[The Scorekeeper\n(Metrics Specialist)]
    
    Analyst -- "Firecrawl Search" --> Web[Web Data]
    Sentiment -- "Social Search" --> Web
    Metrics -- "KPI Search" --> Web
    end
    
    Analyst & Sentiment & Metrics --> Team
    Team --> Report([Unified Launch Report])
    
    style Team fill:#f9f,stroke:#333
    style Analyst fill:#bbf,stroke:#333
    style Sentiment fill:#bfb,stroke:#333
    style Metrics fill:#fbb,stroke:#333
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **OpenAI API Key** (for strategic reasoning)
- **Firecrawl API Key** (for deep web scraping)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/product_launch_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run product_launch_intelligence_agent.py
   ```

4. **Enter Keys**: Input your API keys in the secure sidebar.

## 🛠 Tech Stack
- **Framework**: Agno
- **Search Engine**: Firecrawl
- **UI**: Streamlit
- **Model**: GPT-4o

---

**Created by [Dan-445](https://github.com/Dan-445)**
