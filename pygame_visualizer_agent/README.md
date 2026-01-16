
# 🎮 AI 3D PyGame Visualizer with DeepSeek R1
> **Natural Language → PyGame Code → Live 3D Visualization**

### 🎓 FREE Step-by-Step Tutorial  
👉 https://www.theunwindai.com/p/build-an-ai-3d-pygame-visualizer-with-deepseek-r1  

Learn how to build this system from scratch with detailed explanations, code walkthroughs, and best practices.

---

The **AI 3D PyGame Visualizer Agent** is a multi-agent AI system that converts **natural language descriptions** into executable **PyGame code** and automatically visualizes it in the browser.

It combines:
- **DeepSeek R1** for deep reasoning and code logic
- **OpenAI (GPT-4o)** for clean code extraction
- **Browser automation agents** to run and visualize code on **Trinket.io**
- **Streamlit** for a smooth user interface

This implementation is adapted specifically for the **ai_agent** repository.

---

## ✨ Features

- Generate PyGame code from plain English descriptions
- Deep reasoning and explanation using DeepSeek R1
- Clean, executable code extraction using OpenAI GPT-4o
- Automatic browser-based visualization via Trinket.io
- Streamlit-powered interactive UI
- Multi-agent architecture for:
  - Reasoning
  - Code generation
  - Browser navigation
  - Code execution
  - Visualization

---

## 🧠 How It Works

1. **User Input**  
   The user enters a natural language description of a PyGame or 3D visualization.

2. **Code Reasoning**  
   DeepSeek R1 analyzes the request and produces detailed reasoning along with code logic.

3. **Code Extraction**  
   OpenAI GPT-4o extracts clean, runnable PyGame code from the reasoning output.

4. **Browser Automation**  
   Browser agents:
   - Open Trinket.io
   - Paste the generated code
   - Run the program
   - Display the live visualization

5. **User Interface**  
   Streamlit manages inputs, outputs, logs, and visualization flow.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- DeepSeek API Key
- OpenAI API Key
- Internet access (for Trinket.io visualization)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/pygame_visualizer_agent
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure API Keys

**Linux / macOS**

```bash
export DEEPSEEK_API_KEY="your_deepseek_api_key"
export OPENAI_API_KEY="your_openai_api_key"
```

**Windows PowerShell**

```powershell
setx DEEPSEEK_API_KEY "your_deepseek_api_key"
setx OPENAI_API_KEY "your_openai_api_key"
```

---

### 4️⃣ Run the Application

```bash
streamlit run ai_3dpygame_r1.py
```

---

### 5️⃣ Visualization

* The system will automatically open your browser
* Follow the URL shown in the console output
* Interact with the generated PyGame visualization on Trinket.io

---

## 🧩 Multi-Agent Architecture

### Agents Involved

* **Reasoning Agent (DeepSeek R1)**
  Understands the problem and designs the PyGame logic.

* **Code Extractor Agent (OpenAI GPT-4o)**
  Converts reasoning output into clean, executable PyGame code.

* **Browser Navigation Agent**
  Opens Trinket.io and navigates the UI.

* **Execution Agent**
  Pastes code and runs it in the browser.

* **Visualization Agent**
  Handles rendering and viewing of the output.

---

## 🛠 Tech Stack

* **LLMs**: DeepSeek R1, OpenAI GPT-4o
* **Frontend**: Streamlit
* **Visualization**: PyGame via Trinket.io
* **Automation**: Browser automation agents
* **Language**: Python

---

## 📁 Project Structure

```text
pygame_visualizer_agent/
├── README.md
├── requirements.txt
├── ai_3dpygame_r1.py
├── agents/
│   ├── reasoning_agent.py
│   ├── code_extractor.py
│   ├── browser_navigator.py
│   ├── execution_agent.py
│   └── visualization_agent.py
├── utils/
│   └── helpers.py
```

---

## 📌 Notes

* Designed for experimentation and learning
* Requires active internet for Trinket.io
* Generated code can be copied and run locally
* Complex 3D scenes may take longer to render

---

## 🙌 Credits

Original concept inspired by **awesome-llm-apps**
Adapted and structured for the **ai_agent** repository by **Hazbilal3**
