# AI Speech Trainer Agent 🎙️
> **Multimodal Public Speaking Coach powered by Agno**

[![Author](https://img.shields.io/badge/Author-Danish%20(Dan--445)-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agno](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Multimodal](https://img.shields.io/badge/Analysis-Video%20%2B%20Audio%20%2B%20Text-green.svg)]()

The **AI Speech Trainer** is a multimodal coach that helps you master public speaking. By analyzing your video presentations, it evaluates your facial expressions, voice modulation, and speech content to provide comprehensive, actionable feedback.

## 🏗 Architecture

The system employs a collaborative team of specialized agents, orchestrated by a central Coordinator.

```mermaid
graph TD
    User([User Video Input]) --> App[Streamlit App]
    App --> Coordinator[Coordinator Agent]
    
    subgraph "Multimodal Analysis Team"
    Coordinator --> Facial[Facial Expression Agent]
    Coordinator --> Vocal[Vocal Analysis Agent]
    Coordinator --> Content[Content Agent]
    
    Facial -- "Emotions & Eye Contact" --> Coordinator
    Vocal -- "Pace, Pitch & Fillers" --> Coordinator
    Content -- "Clarity & Structure" --> Coordinator
    end
    
    Coordinator --> Feedback[Feedback Agent]
    Feedback -- "Comprehensive Report" --> App
    
    style Coordinator fill:#f9f,stroke:#333
```

## ✨ Features

- **🙂 Facial Analysis**: Tracks emotions, eye contact, and engagement using OpenCV & DeepFace.
- **🗣️ Vocal Analysis**: Detects speech pace, pitch variations, clarity, and filler words using Whisper & Librosa.
- **📝 Content Evaluation**: Analyzes your speech text for structure, tone, and persuasiveness using GPT-4o/Llama.
- **📊 Comprehensive Scoring**: Provides an aggregated score based on a professional rubric with specific strengths and weaknesses.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **Together AI API Key** (configured in `.env` or UI)
- `ffmpeg` installed on your system (for audio processing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/speech_trainer_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   Create a `.env` file (optional, or enter in UI):
   ```bash
   TOGETHER_API_KEY=your_api_key_here
   ```

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

5. **Usage**
   - Open the Streamlit app in your browser.
   - Upload a short video clip (15-30s recommended for demo).
   - Click "Analyze" and wait for your personalized feedback report.

## 🛠 Tech Stack
- **Frontend**: Streamlit
- **Agent Framework**: Agno
- **AI Models**: Llama-3.3-70B (via Together AI), Faster-Whisper, DeepFace

---

**Created by [Danish (Dan-445)](https://github.com/Dan-445)**