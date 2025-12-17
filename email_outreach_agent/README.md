# AI Email GTM Outreach Agent 📧
> **Autonomous Multi-Agent Sales Development**

[![Author](https://img.shields.io/badge/Author-Dan--445-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-purple.svg)](https://github.com/agno-agi/agno)
[![Exa](https://img.shields.io/badge/Exa-Neural%20Search-green.svg)](https://exa.ai/)

The **Email GTM Outreach Agent** is an autonomous sales team in a box. It doesn't just write emails; it finds target companies, identifies key decision makers, researches them deeply (using their website and Reddit presence), and writes highly personalized, relevant outreach that converts.

![Email Outreach UI](email_outreach_ui.png)

## 🏗 Architecture

```mermaid
graph TD
    User([User Input: Target ICP & Offering]) --> Company[Company Finder Agent]
    Company -- Exa Search --> Companies[List of 1-10 Target Companies]
    Companies --> Contact[Contact Finder Agent]
    Companies --> Research[Research Agent]
    
    subgraph "Parallel Discovery"
    Contact -- Exa Search --> Contacts[Decision Makers]
    Research -- Web & Reddit --> Insights[Personalization Points]
    end
    
    Contacts & Insights --> Writer[Email Writer Agent]
    Writer -- GPT-4o --> Emails([Drafted Outreach Emails])
    
    style Company fill:#f9f,stroke:#333
    style Writer fill:#bbf,stroke:#333
```

## ✨ Capabilities
- **Autonomous Prospecting**: Finds companies fitting your ICP (Ideal Customer Profile) without manual lists.
- **Deep Research**: Scrapes company websites and Reddit discussions to find specific pain points or news.
- **Decision Maker Identification**: Locates founders, sales leads, and marketing heads automatically.
- **Style-Adapted Writing**: Drafts emails in multiple styles:
  - *Professional*: Formal and respectful.
  - *Casual*: Low-friction and friendly.
  - *Cold*: Direct, hook-focused.
  - *Consultative*: Insight-led and value-first.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **OpenAI API Key** (for reasoning and writing)
- **Exa API Key** (for reliable company & contact search)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/email_outreach_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run ai_email_gtm_outreach_agent.py
   ```

## 🛠 Configuration
Enter your keys in the sidebar. Select your target count (1-10) and one of the 4 writing styles to begin.

---

**Created by [Dan-445](https://github.com/Dan-445)**
