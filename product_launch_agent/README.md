
# Product Launch Intelligence Agent 🚀
> **The GTM War Room powered by Multi-Agent AI**

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Data](https://img.shields.io/badge/Data-Firecrawl-orange.svg)](https://www.firecrawl.dev/)

The **Product Launch Intelligence Agent** is an automated **Go-To-Market (GTM) War Room** built using a coordinated team of AI agents.  
Instead of manually researching competitors, tracking market sentiment, and analyzing pricing or traction, this system generates a **comprehensive product launch intelligence report** in minutes.

This implementation is adapted and structured specifically for the **ai_agent** repository.

![Product Launch UI](product_launch_ui.png)

---

## 📖 Concept Overview

Launching a product requires answering three critical questions at once:

1. How should we **position** the product against competitors?
2. What does the **market feel** about similar products?
3. What do the **numbers** say about pricing, traction, and adoption?

This agent mimics a real-world **Product Launch War Room**, where each specialist focuses on one dimension and reports back to a central coordinator.

---

## 🧠 Agent Roles

### 🧭 The Strategist (Product Launch Analyst)
- Analyzes product positioning and differentiation
- Identifies competitor features, pricing, and messaging
- Uses Firecrawl to uncover deep competitive intelligence

### 👂 The Ear (Market Sentiment Specialist)
- Scans social media, forums, and public discussions
- Identifies sentiment trends, objections, and excitement
- Surfaces user language and emotional signals

### 📊 The Scorekeeper (Launch Metrics Specialist)
- Gathers measurable data such as:
  - Pricing tiers
  - Adoption signals
  - Press mentions
- Grounds strategy in factual market data

### 🧠 Team Lead (Orchestrator)
- Coordinates all agents
- Synthesizes findings into a unified GTM report
- Ensures alignment with the user’s query

---

## 🏗 War Room Architecture

```mermaid
graph TD
    User([User Input: Product or Company]) --> UI[Streamlit Interface]
    UI --> Team[Launch Intelligence Team]

    subgraph War_Room
        Team --> Strategist[The Strategist\n(Positioning)]
        Team --> Sentiment[The Ear\n(Market Sentiment)]
        Team --> Metrics[The Scorekeeper\n(Metrics)]

        Strategist -->|Firecrawl| Web[Web Intelligence]
        Sentiment -->|Social Search| Web
        Metrics -->|KPI Search| Web
    end

    Strategist --> Team
    Sentiment --> Team
    Metrics --> Team

    Team --> Report[Unified Launch Intelligence Report]

    style Team fill:#f9f,stroke:#333
    style Strategist fill:#bbf,stroke:#333
    style Sentiment fill:#bfb,stroke:#333
    style Metrics fill:#fbb,stroke:#333
````

---

## ✨ Key Capabilities

* Automated competitor research and positioning analysis
* Real-time market sentiment discovery
* Data-driven pricing and traction insights
* Unified GTM intelligence report generation
* Reduced manual research time from days to minutes

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* OpenAI API Key
* Firecrawl API Key

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/product_launch_agent
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
streamlit run product_launch_intelligence_agent.py
```

---

### 4️⃣ Configure API Keys

Enter your OpenAI and Firecrawl API keys securely in the Streamlit sidebar.

---

## 🛠 Tech Stack

* **Agent Framework**: Agno
* **LLM**: GPT-4o (or compatible model)
* **Web Intelligence**: Firecrawl
* **Frontend**: Streamlit

---

## 📁 Project Structure

```text
product_launch_agent/
├── README.md
├── requirements.txt
├── product_launch_intelligence_agent.py
├── agents/
│   ├── strategist.py
│   ├── sentiment_agent.py
│   └── metrics_agent.py
├── tools/
│   └── firecrawl_client.py
```

---

## 📌 Notes

* Best results come from specific product or company inputs
* Firecrawl significantly improves competitive data quality
* Output is intended for strategy and planning, not financial advice

---

## 🙌 Credits

Inspired by real-world GTM and product launch war rooms
Original concept from multi-agent research systems
Adapted and maintained for this repository by **Hazbilal3**

