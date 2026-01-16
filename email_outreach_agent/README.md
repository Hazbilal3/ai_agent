
# AI Email GTM Outreach Agent 📧
> Autonomous Multi-Agent Sales Development and Cold Outreach

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Agno-Agent%20Framework-purple.svg)](https://github.com/agno-agi/agno)
[![Exa](https://img.shields.io/badge/Exa-Neural%20Search-green.svg)](https://exa.ai/)

The **AI Email GTM Outreach Agent** is a fully autonomous multi-agent system for outbound sales and go-to-market outreach.  
It discovers target companies, identifies key decision makers, performs deep research, and generates highly personalized cold emails designed to convert.

This version is adapted for the **ai_agent** repository.

---

## Architecture

```mermaid
graph TD
    User([User Input: ICP and Offer]) --> Company[Company Finder Agent]
    Company -->|Exa Search| Companies[Target Companies]
    Companies --> Contact[Contact Finder Agent]
    Companies --> Research[Research Agent]

    subgraph Parallel_Discovery
        Contact -->|Exa Search| Contacts[Decision Makers]
        Research -->|Web and Reddit| Insights[Personalization Insights]
    end

    Contacts --> Writer[Email Writer Agent]
    Insights --> Writer
    Writer --> Emails[Personalized Outreach Emails]

    style Company fill:#f9f,stroke:#333
    style Writer fill:#bbf,stroke:#333
````

---

## Core Capabilities

* Autonomous prospecting without manual lead lists
* Automatic discovery of founders and GTM decision makers
* Deep research using company websites and Reddit discussions
* Highly personalized cold email generation
* Multiple outreach writing styles:

  * Professional
  * Casual
  * Cold
  * Consultative

---

## Agent Roles

| Agent          | Responsibility                    |
| -------------- | --------------------------------- |
| Company Finder | Identifies ICP-matching companies |
| Contact Finder | Finds decision makers             |
| Research Agent | Gathers personalization insights  |
| Email Writer   | Writes outreach emails            |

---

## Quick Start

### Prerequisites

* Python 3.10+
* OpenAI API Key
* Exa API Key

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/email_outreach_agent
```

---

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#### 3. Run the Application

```bash
streamlit run ai_email_gtm_outreach_agent.py
```

---

## Configuration

* Enter API keys in the Streamlit sidebar
* Select number of target companies (1 to 10)
* Choose preferred outreach writing style
* Define ICP and offering clearly for best results

---

## Suggested Project Structure

```text
email_outreach_agent/
├── README.md
├── requirements.txt
├── ai_email_gtm_outreach_agent.py
├── agents/
│   ├── company_finder.py
│   ├── contact_finder.py
│   ├── research_agent.py
│   └── email_writer.py
├── tools/
│   ├── exa_search.py
│   ├── web_scraper.py
│   └── reddit_analyzer.py
```

---

## Best Practices

* Use narrow and clear ICP definitions
* Review generated emails before bulk usage
* Prefer consultative style for high-ticket offers
* Enrich prompts for better personalization

---

## Notes

* Designed for founders, SDRs, and GTM teams
* Email quality improves with better research signals
* Exa API access is required for discovery

---

## Credits

Inspired by autonomous GTM and sales agent systems
Adapted and maintained for this repository by **Hazbilal3**

