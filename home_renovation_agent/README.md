# AI Home Renovation Planner 🏗️
> **Intelligent Design & Visualization using Gemini 2.5**

[![Author](https://img.shields.io/badge/Author-Dan--445-blue.svg)](https://github.com/Dan-445)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google ADK](https://img.shields.io/badge/Google-ADK-blue.svg)](https://github.com/google/adk)
[![Gemini](https://img.shields.io/badge/Model-Gemini%202.5-purple.svg)](https://deepmind.google/technologies/gemini/)

The **AI Home Renovation Planner** is a multimodal agent system that turns photos of your outdated space into fully planned, photorealistic renovation projects. It uses Google's Agent Development Kit (ADK) and the Gemini 2.5 Flash model to analyze room conditions, understand style inspiration, calculate costs, and generate stunning visualizations of the final result.

![Home Renovation UI](home_renovation_ui.png)

## 🏗 Architecture

This agent implements the **Coordinator/Dispatcher Pattern**, routing requests between a quick-response info agent and a sophisticated planning pipeline.

```mermaid
graph TD
    User([User Request: Kitchen Renovation]) --> Coordinator[Coordinator Agent]
    Coordinator -- "General Questions" --> Info[Info Agent]
    Coordinator -- "Refine Rendering" --> Editor[Rendering Editor]
    Coordinator -- "New Project" --> Pipeline[Planning Pipeline]
    
    subgraph "Renovation Pipeline"
    Pipeline --> Assessor[Visual Assessor]
    Assessor -- "Analyze Photos" --> Planner[Design Planner]
    Planner -- "Create Specs" --> Project[Project Coordinator]
    Project -- "Generate Image" --> Rendering([Photorealistic Rendering])
    end
    
    style Coordinator fill:#f9f,stroke:#333
    style Project fill:#bbf,stroke:#333
```

## ✨ Capabilities
- **Visual Intelligence**: Upload a photo of your current room, and the agent "sees" the dimensions, condition, and opportunities.
- **Style Transfer**: Upload a Pinterest inspiration photo, and the agent extracts the aesthetic to apply to your space.
- **Budget-Aware Planning**: Provides realistic cost estimates based on 2024 data for materials and labor.
- **Photorealistic Visualization**: Generates high-fidelity 8K render of your renovated room using Gemini's image generation capabilities.
- **Iterative Design**: Don't like the color? Just say "make the cabinets sage green," and the Rendering Editor updates the visualization.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- **Google API Key** (access to Gemini 2.5 Flash)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dan-445/awesome-llm-apps.git
   cd advanced_ai_agents/multi_agent_apps/home_renovation_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Key**
   ```bash
   export GOOGLE_API_KEY="your_gemini_api_key"
   ```

4. **Launch the Agent** (via ADK Web)
   ```bash
   adk web
   ```

## 💡 How It Works
1. **Assessment**: The `VisualAssessor` scans your room photo: *"It's a 10x12 kitchen with dated oak cabinets."*
2. **Planning**: The `DesignPlanner` creates a spec: *"Replace customized cabinets with white shaker style, add quartz counters. Est cost: $15k."*
3. **Visualization**: The `ProjectCoordinator` synthesizes these specs into a complex prompt for Gemini to generate the "after" photo.

---

**Created by [Dan-445](https://github.com/Dan-445)**
