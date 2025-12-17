# AI Agents Showcase

A curated collection of production-ready AI agents that cover research, GTM, personal productivity, wellness, and creative automation use cases. Each folder inside this repo is a self-contained project with its own Streamlit (or ADK) interface, agentic architecture, and setup instructions. This README gathers everything in one place so you can evaluate, run, and extend any agent without hunting for docs.

## Repository Layout

| Folder | Agent | Primary Use Case | Core Stack |
| --- | --- | --- | --- |
| `pygame_visualizer_agent` | AI 3D PyGame Visualizer | Natural-language to PyGame simulations rendered on Trinket | DeepSeek R1, GPT-4o, Streamlit, Browser-use |
| `self_evolving_workflow_agent` | EvoAgentX | Workflow evolution + auto benchmark optimization | EvoAgentX, Python package, Conda |
| `chess_duel_agent` | Agent White vs Agent Black | Multi-agent chess battle in the browser | Autogen, Streamlit, OpenAI |
| `news_podcast_automation_agent` | Beifong | Personalized news pipeline + podcast generator | Python 3.11, Redis, Playwright, agno |
| `tic_tac_toe_battle_agent` | Agent X vs Agent O | Turn-based duel between LLMs | agno, Streamlit, multi-model LLM APIs |
| `aqi_analysis_agent` | AQI Analysis Agent | Live air-quality monitoring + health advice | Streamlit, Firecrawl, OpenAI |
| `pdf_chat_rag_agent` | Chat with PDF | Lightweight RAG chat for documents | Streamlit, OpenAI, LangChain |
| `deep_research_agent` | Deep Research Agent | Automated competitive research reports | Together AI, Composio, Streamlit |
| `email_outreach_agent` | AI Email GTM Outreach Agent | ICP search + multistage outreach writer | Exa, OpenAI, Streamlit |
| `financial_advisor_agent` | Financial Advisor Agent | Multi-agent personal CFO | Google ADK, Gemini 2.5 |
| `hackernews_researcher` | HackerNews Research Team | Newsroom-style summarizer for HN | Streamlit, agno, DuckDuckGo |
| `home_renovation_agent` | Home Renovation Planner | Vision-to-renovation workflows | Google ADK, Gemini 2.5 |
| `mental_wellbeing_agent` | Mental Wellbeing Agent | AutoGen Swarm for emotional support | AG2, Streamlit, OpenAI |
| `product_launch_agent` | Product Launch Intelligence Agent | GTM war room + sentiment digests | agno, Firecrawl, Streamlit |
| `speech_trainer_agent` | Speech Trainer | Multimodal public speaking coach | Streamlit, Together AI, Whisper, DeepFace |

## Quick Start

1. **Install dependencies** – Each folder ships with its own `requirements.txt`. Create a virtual environment per project to avoid dependency conflicts.
2. **Provide API keys** – Most agents rely on `.env` files or Streamlit sidebar inputs (OpenAI, Gemini, Exa, Firecrawl, etc.). Never commit secrets.
3. **Run the UI** – Launch the Streamlit/ADK app as shown in each section below. Most dashboards run on `localhost:8501`.
4. **Bring your data** – Upload PDFs, CSVs, or media files where applicable to see the full workflow in action.

---

## Agent Deep Dives

### 3D PyGame Visualizer Agent (`pygame_visualizer_agent`)

Natural-language prompts become playable PyGame experiments. DeepSeek R1 handles the reasoning trace, GPT-4o extracts clean code, and browser agents publish the sketch to Trinket automatically.

- **Highlights**: Multi-agent browser control, full PyGame code generation, live visualization stream.
- **Stack**: Streamlit UI, DeepSeek Reasoner, GPT-4o, browser-use.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd pygame_visualizer_agent
  pip install -r requirements.txt
  streamlit run ai_3dpygame_r1.py
  ```
- **Mind map**:
![AI 3D PyGame Mind Map](pygame_visualizer_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

### EvoAgentX – Self-Evolving Agent Ecosystem (`self_evolving_workflow_agent`)

A full framework (published May 2025) for generating, executing, and automatically improving agent workflows. Ships with benchmark harnesses (GAIA, HotPotQA, MBPP, MATH) and TextGrad/AFlow/MIPRO optimizers.

- **Highlights**: Automatic workflow graph generation, pluggable evolution algorithms, extensive docs and tutorials.
- **Stack**: Python package, EvoAgentX CLI, optional Conda env, OpenAI-compatible LLM configs.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  pip install git+https://github.com/EvoAgentX/EvoAgentX.git
  # or clone + pip install -e . for local development
  ```
- **Docs**: See `self_evolving_workflow_agent/README.md` for configuration, tutorials, demo videos, and roadmap.

---

### Agent White vs Agent Black (`chess_duel_agent`)

Two Autogen-powered agents play feature-complete chess with a referee agent guarding move legality.

- **Highlights**: Triple-agent orchestration (White, Black, Board Proxy), strict rule enforcement, dynamic analysis feed.
- **Stack**: Autogen, Streamlit, OpenAI (or compatible) models.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd chess_duel_agent
  pip install -r requirements.txt
  streamlit run ai_chess_agent.py
  ```
- **Mind map**:
  ![Chess Agent Mind Map](chess_duel_agent/NotebookLM%20Mind%20Map.png)

---

### Beifong – News + Podcast Agents (`news_podcast_automation_agent`)

Enterprise-grade pipeline that ingests trusted feeds, runs browser automation for social sources, stores data in Redis/FAISS, and assembles narrated podcasts with custom TTS voices.

- **Highlights**: Scheduler-backed feed monitoring, agno-based agent with custom processors, Slack + TTS integrations, optional frontend.
- **Stack**: Python 3.11, Redis, Playwright, agno, ElevenLabs/Kokoro, Slack bot.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd news_podcast_automation_agent/beifong
  python -m venv venv && source venv/bin/activate
  pip install -r requirements.txt
  python -m playwright install
  python main.py  # then scheduler + celery_worker in separate terminals
  ```
- **Mind map**:
![Beifong Mind Map](news_podcast_automation_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

### Agent X vs Agent O (`tic_tac_toe_battle_agent`)

A turn-based battle between two LLMs coordinated by a referee agent. Supports GPT-4o, Gemini, Claude, Groq-hosted models, etc.

- **Highlights**: Multi-model selection, move validation, live board state, move history with board snapshots.
- **Stack**: agno, Streamlit, `.env`-driven API keys.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd tic_tac_toe_battle_agent
  pip install -r requirements.txt
  streamlit run app.py
  ```
- **Mind map**:
  ![Tic Tac Toe Mind Map](tic_tac_toe_battle_agent/NotebookLM%20Mind%20Map.png)

---

### AQI Analysis Agent (`aqi_analysis_agent`)

Scrapes live readings (AQI, PM2.5, CO, weather context) for any city and turns them into medically-aware recommendations.

- **Highlights**: Firecrawl scraping, personalized advice based on conditions/activities, dual-agent pipeline (Analyzer + Health Coach).
- **Stack**: Streamlit, Firecrawl, OpenAI.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd aqi_analysis_agent
  pip install -r requirements.txt
  streamlit run ai_aqi_analysis_agent_streamlit.py
  ```
- **Mind map**:
![AQI Mind Map](aqi_analysis_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

### Chat with PDF Agent (`pdf_chat_rag_agent`)

Minimal 30-line RAG sample: upload a PDF, embed it, and chat using OpenAI (or drop-in replacement) models.

- **Highlights**: Ultra-lightweight architecture, instant doc QA demo, ideal starting point for vertical RAG apps.
- **Stack**: Streamlit, LangChain or equivalent vector store, OpenAI API.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd pdf_chat_rag_agent
  pip install -r requirements.txt
  streamlit run chat_pdf.py
  ```
- **Mind map**:
  ![Chat with PDF Mind Map](pdf_chat_rag_agent/NotebookLM%20Mind%20Map.png)

---

### Deep Research Agent (`deep_research_agent`)

Autonomous analyst that decomposes a topic into targeted questions, runs Tavily + Perplexity loops, and drafts a McKinsey-style report straight into Google Docs.

- **Highlights**: Question generator, multi-source research loop, Composio-powered Google Docs export.
- **Stack**: Streamlit, Together AI, Composio (Tavily, Perplexity, Google Docs).
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd deep_research_agent
  pip install -r requirements.txt
  composio add googledocs
  composio add perplexityai
  streamlit run ai_domain_deep_research_agent.py
  ```
- **Mind map**:
![Deep Research Mind Map](deep_research_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

### AI Email GTM Outreach Agent (`email_outreach_agent`)

Builds entire outbound campaigns: identify companies, surface decision makers, mine Reddit/company sites for personalization, and draft multi-style emails.

- **Highlights**: Parallel prospect + contact research, four tone presets, Exa for neural search, Streamlit UX.
- **Stack**: Streamlit, agno, OpenAI, Exa APIs.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd email_outreach_agent
  pip install -r requirements.txt
  streamlit run ai_email_gtm_outreach_agent.py
  ```
- **Mind map**:
  ![Email Outreach Mind Map](email_outreach_agent/NotebookLM%20Mind%20Map.png)

---

### Financial Advisor Agent (`financial_advisor_agent`)

Acts as a personal CFO with dedicated agents for budgeting, savings automation, and debt destruction using Gemini 2.5 + Google ADK.

- **Highlights**: Coordinator pattern, debt avalanche/snowball simulations, privacy-conscious local processing.
- **Stack**: Google ADK, Gemini 2.5 Flash, Streamlit-like UI (see folder), `.env` with `GOOGLE_API_KEY`.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd financial_advisor_agent
  pip install -r requirements.txt
  streamlit run financial_advisor_agent.py
  ```
- **Mind map**:
  ![Financial Advisor Mind Map](financial_advisor_agent/NotebookLM%20Mind%20Map.png)

---

### HackerNews Research Team (`hackernews_researcher`)

A newsroom-in-a-box: Scout finds trending HN stories, Analyst reads full articles, Fact-Checker validates via DuckDuckGo, and the Editor synthesizes reports.

- **Highlights**: Multi-agent editorial workflow, dual model support (OpenAI or local Llama 3 via Ollama), tactical UI for querying HN.
- **Stack**: Streamlit, agno, HackerNews + Newspaper4k + DuckDuckGo tools.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd hackernews_researcher
  pip install -r requirements.txt
  streamlit run research_agent.py          # GPT-4o version
  # or
  streamlit run research_agent_llama3.py   # local Llama 3 version
  ```
- **Mind map**:
![HackerNews Mind Map](hackernews_researcher/NotebookLM%20Mind%20Map%20%281%29.png)

---

### Home Renovation Planner (`home_renovation_agent`)

Gemini-powered renovation pipeline that inspects your room photo, blends it with inspirational references, estimates budgets, and outputs photorealistic renders.

- **Highlights**: Coordinator/Dispatcher routing, multimodal design planner, iterative rendering editor.
- **Stack**: Google ADK, Gemini 2.5 Flash, ADK Web runtime.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd home_renovation_agent
  pip install -r requirements.txt
  export GOOGLE_API_KEY="your_key"
  adk web
  ```
- **Mind map**:
  ![Home Renovation Mind Map](home_renovation_agent/NotebookLM%20Mind%20Map.png)

---

### Mental Wellbeing Agent (`mental_wellbeing_agent`)

AutoGen Swarm coordinates Assessment, Action, and Follow-up agents to provide empathetic check-ins plus structured coping plans.

- **Highlights**: Swarm pattern hand-offs, long-term plan generation, explicit crisis guidance disclaimers.
- **Stack**: AG2 (AutoGen), Streamlit, OpenAI. `.env` includes `AUTOGEN_USE_DOCKER=0` for local runs.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd mental_wellbeing_agent
  pip install -r requirements.txt
  echo "AUTOGEN_USE_DOCKER=0" > .env
  streamlit run ai_mental_wellbeing_agent.py
  ```
- **Mind map**:
![Mental Wellbeing Mind Map](mental_wellbeing_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

### Product Launch Intelligence Agent (`product_launch_agent`)

Operates like a GTM war room with Strategist, Sentiment Specialist, and Metrics Analyst agents, all feeding a unified launch report.

- **Highlights**: Firecrawl-powered intel gathering, multi-channel sentiment scraping, Streamlit UI for report capture.
- **Stack**: Streamlit, agno, OpenAI, Firecrawl.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd product_launch_agent
  pip install -r requirements.txt
  streamlit run product_launch_intelligence_agent.py
  ```
- **Mind map**:
  ![Product Launch Mind Map](product_launch_agent/NotebookLM%20Mind%20Map.png)

---

### Speech Trainer Agent (`speech_trainer_agent`)

Uploads a rehearsal video and receives multimodal feedback (facial expressiveness, voice delivery, script quality) with actionable coaching tips.

- **Highlights**: Video-to-text extraction, DeepFace-powered expression scoring, Whisper audio stats, consolidated rubric output.
- **Stack**: Streamlit, Together AI (Llama-3.3-70B), Faster-Whisper, DeepFace, ffmpeg.
- **Author**: [Dan-445](https://github.com/Dan-445)
- **Run it**:
  ```bash
  cd speech_trainer_agent
  pip install -r requirements.txt
  streamlit run main.py
  ```
- **Mind map**:
![Speech Trainer Mind Map](speech_trainer_agent/NotebookLM%20Mind%20Map%20%281%29.png)

---

## Next Steps

- **Pick an agent** and run it locally to verify dependencies before consolidating everything under a single GitHub repo named `ai-agents` (or your chosen slug).
- **Standardize env handling** by creating a template `.env.example` per project if you plan to onboard collaborators.
- **Add CI/testing** for agents that are close to production to keep regressions out when new APIs/models arrive.

Happy building! 🚀
