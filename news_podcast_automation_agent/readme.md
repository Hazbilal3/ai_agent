
# 🦉 Beifong: Junk-Free, Personalized Information & Podcast Agent

![image](https://github.com/user-attachments/assets/b2f24f12-6f80-46fa-aa31-ee42e17765b1)

Beifong is an **AI-powered information curation and podcast automation system**.  
It manages **trusted articles and social media sources**, removes noise, and generates **high-quality podcasts** from content you curate.

Beifong handles the **complete pipeline end to end**:
- Data collection
- Content analysis
- Script generation
- Audio and visual production

This version is **adapted and structured for the `ai_agent` repository**.

---

## 🎥 Demos & Resources

▶️ **Demo Video (HD)**  
https://www.canva.com/design/DAGoUfv8ICM/Oj-vJ19AvZYDa2SwJrCWKw/watch

▶️ **YouTube Demo**  
https://youtu.be/dB8FZY3x9EY

🔗 **Technical Blog**  
https://arun477.github.io/posts/beifong_podcast_generator/

---

## 📚 Table of Contents

- [Getting Started](#getting-started)
- [How to Use Beifong](#how-to-use-beifong)
- [Content Processing System](#content-processing-system)
- [AI Agent and Tools](#ai-agent-and-tools)
- [Web Search and Browser Automation](#web-search-and-browser-automation)
- [Social Media Monitoring](#social-media-monitoring)
- [Audio and Voice Generation](#audio-and-voice-generation)
- [Integrations](#integrations)
- [Data Storage and File Management](#data-storage-and-file-management)
- [Deployment and Access Options](#deployment-and-access-options)
- [Cloud Options](#cloud-options)
- [Troubleshooting](#troubleshooting)
- [Updates](#updates)

---

## Getting Started

### System Requirements

- Python 3.11+
- Redis Server
- OpenAI API Key
- ElevenLabs API Key (optional)

---

### Initial Setup and Installation

```bash
# Clone repository
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/news_podcast_automation_agent

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
python -m playwright install
````

#### Optional Demo Bootstrap

```bash
python bootstrap_demo.py
```

---

### Environment Configuration

Create a `.env` file in `news_podcast_automation_agent`:

```env
OPENAI_API_KEY=your_openai_api_key
ELEVENSLAB_API_KEY=your_elevenlabs_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

---

### Starting the Application

Activate the virtual environment in **all terminals**:

```bash
source venv/bin/activate
```

#### Terminal 1: Main Backend

```bash
python main.py
```

#### Terminal 2: Scheduler

```bash
python -m scheduler
```

#### Terminal 3: Workers

```bash
python -m celery_worker
```

Verify Redis:

```bash
redis-cli ping
```

---

## How to Use Beifong

### Usage Modes

1. **Web UI**
   Manage sources, generate podcasts, and explore insights.

2. **API Access**
   Integrate Beifong into custom workflows.

3. **Automated Scheduling**
   Fully hands-off content ingestion and podcast creation.

---

## Content Processing System

### Built-in Processors

* RSS Feed Processor
* URL Content Processor
* AI Content Analyzer
* Vector Embedding Generator
* FAISS Search Indexer
* Podcast Script Generator
* X.com Social Processor
* Facebook Social Processor

---

### Creating Custom Content Processors

#### Step 1: Create Processor

```python
# processors/my_custom_processor.py
def process_custom_task():
    stats = {"processed": 0, "success": 0, "errors": 0}
    return stats
```

#### Step 2: Register Processor

```python
# models/tasks_schemas.py
class TaskType(str, Enum):
    my_custom_processor = "my_custom_processor"
```

#### Step 3: Deploy

Create the task using UI or API.

---

## AI Agent and Tools

### Agent Architecture

Built on the **agno framework**, Beifong supports:

* Semantic and keyword search
* Browser-based research
* Persistent session state
* Multi-step tool orchestration

---

### Adding Custom Tools

```python
def my_custom_tool(agent, param1, param2):
    agent.session_state["key"] = "value"
    return "Processed"
```

Register in `services/celery_tasks.py`.

---

## Web Search and Browser Automation

Powered by **browseruse** with full browser automation:

* Social feeds
* News websites
* Forums
* Logged-in platforms

---

## Social Media Monitoring

### Supported Platforms

* X.com
* Facebook

### Scheduling Best Practices

* Avoid concurrent browser sessions
* Stagger tasks
* Allow buffer time between jobs

---

## Audio and Voice Generation

### Supported TTS Engines

* OpenAI TTS
* ElevenLabs
* Kokoro

New engines can be added via the TTS selector.

---

## Integrations

### Slack Integration

Interact with Beifong inside Slack.

#### Environment Variables

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
```

Run integration:

```bash
python -m integrations.slack.chat
```

---

## Data Storage and File Management

* **Databases**: `databases/`
* **Media Assets**: `podcasts/`

### Storage Management

* S3 mounting via s3fs
* Automated cleanup
* Retention policies

---

## Deployment and Access Options

### Local Network Access

```bash
python main.py --host 0.0.0.0 --port 7000
```

### Remote Access

* SSH port forwarding
* Ngrok tunneling

Authentication layer planned.

---

## Cloud Options

### Beifong Cloud (Coming Soon)

* Hosted service
* More social connectors
* Multi-model support
* Advanced podcast customization
* Authentication and access control

---

## Troubleshooting

### Common Issues

* Kokoro is optional
* FAISS only needed for semantic search
* Browser automation requires Playwright

---

## Updates

🚀 **Original Project**
[https://github.com/arun477/beifong](https://github.com/arun477/beifong)

🛠️ **Adapted for ai_agent Repository**
Maintained and structured by **Hazbilal3**

