
# AI Speech Trainer Agent 🎙️
> **Multimodal Public Speaking Coach powered by Agno**

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Agno-purple.svg)](https://github.com/agno-agi/agno)
[![Multimodal](https://img.shields.io/badge/Analysis-Video%20%2B%20Audio%20%2B%20Text-green.svg)]()

The **AI Speech Trainer Agent** is a multimodal public speaking coach designed to help you improve your **delivery, confidence, and clarity**.

By analyzing uploaded **video presentations**, the system evaluates:
- Facial expressions and eye contact
- Voice modulation, pace, and filler words
- Speech content, structure, and persuasion

It then generates a **professional, actionable feedback report**, similar to what a human speech coach would provide.

This README is structured specifically for the **ai_agent** repository.

---

## 🏗 Architecture

The system follows a **Coordinator-based Multi-Agent Architecture**, where each agent specializes in a single modality and reports back to a central orchestrator.

```mermaid
graph TD
    User([User Video Input]) --> UI[Streamlit App]
    UI --> Coordinator[Coordinator Agent]

    subgraph Multimodal_Analysis_Team
        Coordinator --> Facial[Facial Expression Agent]
        Coordinator --> Vocal[Vocal Analysis Agent]
        Coordinator --> Content[Content Analysis Agent]

        Facial -->|Emotions & Eye Contact| Coordinator
        Vocal -->|Pace, Pitch & Fillers| Coordinator
        Content -->|Clarity & Structure| Coordinator
    end

    Coordinator --> Feedback[Feedback Agent]
    Feedback -->|Comprehensive Report| UI

    style Coordinator fill:#f9f,stroke:#333
````

---

## ✨ Features

### 🙂 Facial Expression Analysis

* Tracks facial emotions and engagement
* Evaluates eye contact consistency
* Powered by OpenCV and DeepFace

### 🗣️ Vocal Analysis

* Measures speech pace and pauses
* Detects pitch variation and monotony
* Identifies filler words such as “um”, “uh”, and “you know”
* Uses Faster-Whisper and Librosa

### 📝 Content Evaluation

* Analyzes clarity, structure, and flow
* Evaluates tone, confidence, and persuasiveness
* Uses large language models for semantic analysis

### 📊 Comprehensive Scoring

* Aggregated score using a professional rubric
* Clear strengths, weaknesses, and improvement tips
* Actionable guidance you can apply immediately

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* Together AI API Key
* `ffmpeg` installed and available in system PATH

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/speech_trainer_agent
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment

Create a `.env` file (optional) or enter the key directly in the UI:

```env
TOGETHER_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```bash
streamlit run main.py
```

---

### 5️⃣ How to Use

1. Open the Streamlit app in your browser
2. Upload a short video clip (15–30 seconds recommended)
3. Click **Analyze**
4. Wait for multimodal analysis to complete
5. Review your personalized feedback report

---

## 🛠 Tech Stack

* **Frontend**: Streamlit
* **Agent Framework**: Agno
* **LLMs**: Llama-3.3-70B (via Together AI)
* **Speech Processing**: Faster-Whisper, Librosa
* **Vision Analysis**: OpenCV, DeepFace
* **Language**: Python

---

## 📁 Project Structure

```text
speech_trainer_agent/
├── README.md
├── requirements.txt
├── main.py
├── agents/
│   ├── coordinator.py
│   ├── facial_agent.py
│   ├── vocal_agent.py
│   ├── content_agent.py
│   └── feedback_agent.py
├── utils/
│   ├── video_utils.py
│   └── audio_utils.py
```

---

## 📌 Notes

* Short videos process faster and give more accurate feedback
* Clear lighting and audio significantly improve results
* Designed for **training and coaching purposes only**
* Not intended for medical or psychological diagnosis

---

## 🙌 Credits

Inspired by multimodal AI coaching systems
Adapted and maintained for the **ai_agent** repository by **Hazbilal3**

