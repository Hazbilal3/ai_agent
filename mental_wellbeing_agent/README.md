
# AI Mental Wellbeing Agent 🧠
> **Compassionate AI Support Team powered by AutoGen Swarm**

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AG2](https://img.shields.io/badge/Framework-AG2%20(AutoGen)-blue.svg)](https://github.com/ag2ai/ag2)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)

The **AI Mental Wellbeing Agent** is a compassionate, multi-agent mental health support system designed to provide personalized emotional guidance and structured wellbeing planning.

Built using **AG2 (formerly AutoGen)** and a **Swarm Architecture**, this system coordinates multiple specialized agents to assess emotional states, provide immediate coping strategies, and design long-term mental wellness plans.

This implementation is structured specifically for the **ai_agent** repository.

---

## 🏗 Architecture

The application follows the **Swarm Pattern**, where agents dynamically hand off tasks to one another to provide continuous and holistic support.

```mermaid
graph TD
    User([User Input: Emotional State]) --> Swarm[AutoGen Swarm Router]
    Swarm -->|Analyze| Assessment[Assessment Agent]
    Swarm -->|Act| Action[Action Agent]
    Swarm -->|Plan| Followup[Follow-up Agent]

    subgraph Swarm_Coordination_Cycle
        Assessment -->|Situation Analyzed| Action
        Action -->|Coping Plan Created| Followup
        Followup -->|Long-term Strategy Set| Assessment
    end

    style Swarm fill:#f9f,stroke:#333
    style Assessment fill:#bbf,stroke:#333
    style Action fill:#bfb,stroke:#333
    style Followup fill:#fbf,stroke:#333
````

---

## ✨ Specialized Agent Team

### 🧠 Assessment Agent

* Acts as an empathy-first listener
* Analyzes emotional tone and patterns
* Validates feelings without judgment
* Identifies stressors and emotional risk signals

### 🎯 Action Agent

* Focuses on immediate coping and grounding strategies
* Suggests evidence-based techniques
* Recommends external resources when needed

### 🔄 Follow-up Agent

* Designs long-term wellbeing strategies
* Builds habit-based mental health routines
* Creates relapse prevention and recovery plans

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* OpenAI API Key (for reasoning, empathy, and language understanding)

---

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hazbilal3/ai_agent.git
   cd ai_agent/mental_wellbeing_agent
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   Create a `.env` file to disable Docker usage for local execution:

   ```bash
   AUTOGEN_USE_DOCKER=0
   ```

4. **Run the Application**

   ```bash
   streamlit run ai_mental_wellbeing_agent.py
   ```

---

## 🛠 Tech Stack

* **Framework**: AG2 (AutoGen)
* **Architecture**: Swarm Pattern
* **Frontend**: Streamlit
* **LLM Provider**: OpenAI

---

## ⚠️ Important Notice

This tool is intended for **emotional support and guidance only**.
It is **not a replacement** for licensed medical or mental health professionals.

### If you are in crisis:

* Call **988** (Mental Health Crisis Hotline)
* Call **911** (Emergency Services)
* Visit the nearest emergency room immediately

---

## 📌 Notes

* Designed for supportive conversations and wellbeing planning
* No personal data is stored permanently
* Output quality improves with honest and detailed user input

---

## 🙌 Credits

Inspired by multi-agent therapeutic support systems
Adapted and maintained for this repository by **Hazbilal3**
