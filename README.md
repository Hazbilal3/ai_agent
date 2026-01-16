
# 🤖 AI Agents Showcase

A curated collection of **production-ready AI agents** built to demonstrate real-world applications of **agentic AI systems** — spanning research, GTM, productivity, wellness, games, and creative automation.

Each folder in this repository is a **self-contained AI agent project** with:
- Its own architecture
- Streamlit or ADK-based UI
- Setup instructions
- Focused use case

This README serves as a **single entry point** to explore, run, and extend every agent in the repository.

---

## 📁 Repository Layout

| Folder | Agent | Primary Use Case | Core Stack |
|------|------|-----------------|------------|
| `pygame_visualizer_agent` | AI 3D PyGame Visualizer | Natural language → PyGame simulations | GPT-4o, DeepSeek, Streamlit |
| `self_evolving_workflow_agent` | EvoAgentX | Self-improving agent workflows | EvoAgentX, Python |
| `chess_duel_agent` | Agent White vs Agent Black | AI vs AI chess battle | AutoGen, Streamlit |
| `news_podcast_automation_agent` | Beifong | News aggregation + podcast automation | agno, Redis, Playwright |
| `tic_tac_toe_battle_agent` | Agent X vs Agent O | LLM vs LLM turn-based game | agno, Streamlit |
| `aqi_analysis_agent` | AQI Analysis Agent | Air quality insights + health advice | Firecrawl, Streamlit |
| `pdf_chat_rag_agent` | Chat with PDF | Lightweight RAG system | LangChain, OpenAI |
| `deep_research_agent` | Deep Research Agent | Automated research reports | Together AI, Composio |
| `email_outreach_agent` | AI Email GTM Agent | Lead research + outreach | Exa, OpenAI |
| `financial_advisor_agent` | Financial Advisor Agent | Personal CFO system | Google ADK, Gemini |
| `hackernews_researcher` | HackerNews Research Team | AI newsroom summarizer | agno, DuckDuckGo |
| `home_renovation_agent` | Home Renovation Planner | Vision-to-renovation AI | Gemini, ADK |
| `mental_wellbeing_agent` | Mental Wellbeing Agent | Emotional support AI swarm | AutoGen |
| `product_launch_agent` | Product Launch Agent | GTM intelligence war room | Firecrawl, agno |
| `speech_trainer_agent` | Speech Trainer | Multimodal speaking coach | Whisper, DeepFace |

---

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hazbilal3/ai_agent.git
   cd ai_agent
````

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   * Each agent has its own `requirements.txt`

   ```bash
   cd <agent_folder>
   pip install -r requirements.txt
   ```

4. **Set API Keys**

   * Most agents require a `.env` file
   * Never commit secrets

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🎮 Featured Agents

---

### ♟️ Chess Duel Agent (`chess_duel_agent`)

Two autonomous AI agents play a complete game of chess under the supervision of a referee agent.

* **Highlights**

  * Move legality enforcement
  * Multi-agent orchestration
  * Live game visualization

* **Run**

  ```bash
  cd chess_duel_agent
  pip install -r requirements.txt
  streamlit run ai_chess_agent.py
  ```

---

### ❌⭕ Tic Tac Toe Battle Agent (`tic_tac_toe_battle_agent`)

A turn-based **LLM vs LLM** game coordinated by a master referee agent.

* **Highlights**

  * Multi-model support (GPT, Claude, Gemini, Groq)
  * Move history with board states
  * Real-time UI

* **Run**

  ```bash
  cd tic_tac_toe_battle_agent
  pip install -r requirements.txt
  streamlit run app.py
  ```

---

### 📄 Chat with PDF Agent (`pdf_chat_rag_agent`)

Upload a PDF and chat with it using a minimal RAG pipeline.

* **Highlights**

  * Lightweight architecture
  * Fast document QA
  * Ideal RAG starter project

* **Run**

  ```bash
  cd pdf_chat_rag_agent
  pip install -r requirements.txt
  streamlit run chat_pdf.py
  ```

---

### 🌍 AQI Analysis Agent (`aqi_analysis_agent`)

Live air-quality monitoring with personalized health recommendations.

* **Highlights**

  * Real-time AQI scraping
  * Health-aware reasoning
  * City-based insights

* **Run**

  ```bash
  cd aqi_analysis_agent
  pip install -r requirements.txt
  streamlit run ai_aqi_analysis_agent_streamlit.py
  ```

---

### 🧠 Deep Research Agent (`deep_research_agent`)

An autonomous analyst that produces structured research reports.

* **Highlights**

  * Question decomposition
  * Multi-source research loops
  * Google Docs export

---

### 💼 AI Email Outreach Agent (`email_outreach_agent`)

End-to-end outbound GTM automation.

* **Highlights**

  * ICP discovery
  * Contact research
  * Personalized cold emails

---

### 🧘 Mental Wellbeing Agent (`mental_wellbeing_agent`)

Multi-agent emotional support system with assessment and follow-ups.

* **Highlights**

  * Swarm-based architecture
  * Empathetic conversations
  * Coping strategy generation

---

### 🎤 Speech Trainer Agent (`speech_trainer_agent`)

Multimodal public speaking coach using video + audio analysis.

* **Highlights**

  * Facial expression scoring
  * Voice delivery feedback
  * Actionable coaching tips

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Agno / AutoGen / Google ADK**
* **OpenAI, Gemini, Claude, Groq**
* **LangChain, Firecrawl, Exa**
* **Whisper, DeepFace, Playwright**

---

## 🚧 Future Plans

* Unified dashboard for all agents
* Shared authentication layer
* CI + automated tests
* Docker support
* Cloud deployment guides

---

## 👤 Author

**Hazbilal**
🔗 GitHub: [https://github.com/Hazbilal3](https://github.com/Hazbilal3)

---

⭐ If you find this repository useful, consider giving it a **star**!


