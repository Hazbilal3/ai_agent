
# AI Home Renovation Planner 🏗️
> **Intelligent Design & Visualization using Gemini 2.5**

[![Author](https://img.shields.io/badge/Author-Hazbilal3-blue.svg)](https://github.com/Hazbilal3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google ADK](https://img.shields.io/badge/Google-ADK-blue.svg)](https://github.com/google/generative-ai-python)
[![Gemini](https://img.shields.io/badge/Model-Gemini%202.5-purple.svg)](https://deepmind.google/technologies/gemini/)

The **AI Home Renovation Planner** is a multimodal agent system that turns photos of your existing space into fully planned, photorealistic renovation projects.  
It uses Google’s Agent Development Kit (ADK) and the Gemini 2.5 Flash model to analyze room conditions, understand style inspiration, estimate renovation costs, and generate realistic visualizations of the final result.

This implementation is adapted for the **ai_agent** repository.

![Home Renovation UI](home_renovation_ui.png)

---

## 🏗 Architecture

This agent implements the **Coordinator / Dispatcher Pattern**, routing user requests between fast-response agents and a deeper planning pipeline.

```mermaid
graph TD
    User([User Request: Room Renovation]) --> Coordinator[Coordinator Agent]
    Coordinator -- General Questions --> Info[Info Agent]
    Coordinator -- Refine Rendering --> Editor[Rendering Editor]
    Coordinator -- New Project --> Pipeline[Planning Pipeline]

    subgraph Renovation_Pipeline
        Pipeline --> Assessor[Visual Assessor]
        Assessor -- Analyze Photos --> Planner[Design Planner]
        Planner -- Create Specs --> Project[Project Coordinator]
        Project -- Generate Image --> Rendering[Photorealistic Rendering]
    end

    style Coordinator fill:#f9f,stroke:#333
    style Project fill:#bbf,stroke:#333
````

---

## ✨ Capabilities

* **Visual Intelligence**
  Upload a photo of your room and the agent understands layout, condition, lighting, and opportunities.

* **Style Transfer**
  Upload an inspiration image and the agent extracts the aesthetic and applies it to your space.

* **Budget-Aware Planning**
  Generates realistic cost estimates for materials and labor using up-to-date market assumptions.

* **Photorealistic Visualization**
  Produces high-quality renovation renders using Gemini image generation.

* **Iterative Design**
  Refine designs conversationally, such as changing colors, materials, or layout elements.

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* Google API Key with access to Gemini 2.5 Flash

---

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hazbilal3/ai_agent.git
   cd ai_agent/home_renovation_agent
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Key**

   **Linux / macOS**

   ```bash
   export GOOGLE_API_KEY="your_gemini_api_key"
   ```

   **Windows (PowerShell)**

   ```powershell
   setx GOOGLE_API_KEY "your_gemini_api_key"
   ```

4. **Launch the Agent**

   ```bash
   adk web
   ```

---

## 💡 How It Works

1. **Assessment**
   The Visual Assessor analyzes the uploaded room image and identifies dimensions, layout, and condition.

2. **Planning**
   The Design Planner creates renovation specifications including materials, layout changes, and estimated costs.

3. **Visualization**
   The Project Coordinator converts the plan into a detailed prompt for Gemini to generate a renovated image.

4. **Iteration**
   Users can refine the output with natural language instructions until satisfied.

---

## 🛠 Tech Stack

* **Agent Framework**: Google ADK
* **Model**: Gemini 2.5 Flash
* **Frontend**: ADK Web UI
* **Capabilities**: Vision, planning, image generation

---

## 📌 Notes

* Cost estimates are indicative and may vary by region
* Generated designs are conceptual and for planning purposes
* Final construction results may differ from AI-generated visuals

---

## 🙌 Credits

Inspired by multimodal agent-based design systems
Adapted and maintained for this repository by **Hazbilal3**

