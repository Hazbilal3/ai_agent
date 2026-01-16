
# Financial Advisor Agent 💰
> Personalized Wealth Management using a Multi-Agent AI System

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-Enabled-4285F4.svg)](https://github.com/google/generative-ai-python)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-8E44AD.svg)](https://deepmind.google/technologies/gemini/)

The **Financial Advisor Agent** is a local, multi-agent AI system designed to function like a personal CFO.  
It coordinates specialized agents to analyze spending, optimize savings, and strategically eliminate debt using structured financial reasoning.

This implementation is adapted specifically for the **ai_agent** repository.

---

## 🏗 Architecture

```mermaid
graph TD
    User([User Financial Data]) --> Coordinator[Coordinator Agent]
    Coordinator --> Budget[Budget Analysis Agent]
    Budget --> Savings[Savings Strategy Agent]
    Savings --> Debt[Debt Reduction Agent]
    Debt --> Plan([Comprehensive Financial Plan])

    subgraph Agent_Responsibilities
        Budget -->|Categorize and Audit| B_Out[Spending Insights]
        Savings -->|Allocate and Protect| S_Out[Savings Automation]
        Debt -->|Optimize and Eliminate| D_Out[Debt Payoff Strategy]
    end

    style Coordinator fill:#f9f,stroke:#333,stroke-width:2px
    style Budget fill:#bbf,stroke:#333,stroke-width:2px
    style Savings fill:#bfb,stroke:#333,stroke-width:2px
    style Debt fill:#fbb,stroke:#333,stroke-width:2px
````

---

## ✨ Specialized Agents

### 1. Budget Analysis Agent

* **Role**: Financial Auditor
* **Function**: Processes transaction data (CSV or manual input), categorizes expenses, and detects overspending
* **Output**: Spending breakdown with actionable cost-reduction insights

### 2. Savings Strategy Agent

* **Role**: Financial Planner
* **Function**: Calculates emergency fund targets and allocates surplus income intelligently
* **Output**: Savings automation plan and milestone-based goals

### 3. Debt Reduction Agent

* **Role**: Debt Strategist
* **Function**: Optimizes debt repayment using Avalanche and Snowball methodologies
* **Output**: Payoff timeline and projected interest savings

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* Google API Key (Gemini)

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/financial_advisor_agent
```

---

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#### 3. Configure Environment

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

---

#### 4. Run the Application

```bash
streamlit run financial_advisor_agent.py
```

---

## ⚙️ Configuration

* Upload transaction data or enter values manually
* Adjust financial goals directly from the Streamlit interface
* Review agent recommendations before acting on them

---

## 📁 Suggested Project Structure

```text
financial_advisor_agent/
├── README.md
├── requirements.txt
├── financial_advisor_agent.py
├── agents/
│   ├── coordinator.py
│   ├── budget_agent.py
│   ├── savings_agent.py
│   └── debt_agent.py
├── utils/
│   ├── parsers.py
│   └── calculators.py
```

---

## 🔐 Data Privacy

* All processing happens locally
* Financial data is kept in-memory during runtime only
* No data is stored or logged permanently
* Only anonymized prompts are sent to the LLM for inference

---

## 📝 Best Practices

* Use recent transaction data for better accuracy
* Review recommendations manually before execution
* Combine avalanche and snowball methods based on risk tolerance
* Re-run analysis monthly for updated insights

---

## 📌 Notes

* Designed for personal finance planning and advisory use
* Not a replacement for licensed financial professionals
* Output quality improves with cleaner input data

---

## 🙌 Credits

Inspired by autonomous finance agent architectures
Adapted and maintained for this repository by **Hazbilal3**

