
# 🎮 Tic Tac Toe Battle Agent (AI vs AI)

An interactive **AI vs AI Tic-Tac-Toe game** where two autonomous agents powered by different Large Language Models (LLMs) compete against each other.

This project is built using the **Agno Agent Framework** for multi-agent coordination and **Streamlit** for the interactive web UI.

---

## 🚀 Project Highlights

This project demonstrates how to:

- Coordinate **multiple AI agents** in a turn-based game
- Use **different LLMs** for each player
- Manage **game state & rule validation**
- Build a **real-time interactive UI** with Streamlit
- Track **move history and board states**
- Compare strategies of different AI models

---

## ✨ Features

- 🤖 AI vs AI gameplay (Agent X vs Agent O)
- 🔁 Turn-based coordination via Master (Referee) Agent
- 🧠 Supports multiple LLM providers
- 📊 Move history with board visualization
- 🎯 Real-time board updates
- 🔄 Reset & replay functionality
- 🧪 Strategy & performance comparison

---

## 🧠 Supported AI Models

- **OpenAI** – GPT-4o, o3-mini  
- **Anthropic** – Claude  
- **Google** – Gemini  
- **Groq** – LLaMA 3  

> You can assign **different models to each player** and observe how they perform against each other.

---

## 🏗️ Architecture Overview

The game uses **three agents**:

### 1️⃣ Master Agent (Referee)
- Controls game flow
- Validates moves
- Maintains board state
- Detects win / draw conditions

### 2️⃣ Player Agent X
- Analyzes board
- Makes strategic moves
- Uses selected AI model

### 3️⃣ Player Agent O
- Responds to opponent moves
- Follows game rules
- Uses a different AI model (optional)

---

## 📦 Project Structure

```bash
tic_tac_toe_battle_agent/
│
├── app.py                  # Streamlit UI & game runner
├── agents/                 # AI agents (Master & Players)
├── utils/                  # Game logic & helpers
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
└── README.md               # Project documentation
````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd tic_tac_toe_battle_agent
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup API Keys

Create a `.env` file in the project root:

```bash
touch .env
```

Add your API keys:

```env
# OpenAI (Required for GPT models)
OPENAI_API_KEY=your_openai_api_key

# Optional Providers
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
```

⚠️ **Note:**

* Only add keys for models you plan to use
* The app will show helpful errors if a key is missing

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open your browser and go to:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🎮 How to Play

1. Select AI models for **Agent X** and **Agent O**
2. Start the game
3. Watch both AI agents compete in real time
4. View:

   * Board updates
   * Move history
   * Game outcome (Win / Draw)

---

## 📊 Game Insights

* Compare decision-making between different LLMs
* Observe strategy patterns
* Analyze move timing & efficiency

---

## 🧪 Use Cases

* Learning **multi-agent AI systems**
* Comparing LLM reasoning abilities
* Autonomous game-playing research
* Streamlit + AI agent integration demo

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Agno Agent Framework**
* **OpenAI / Anthropic / Google / Groq APIs**

---

## 📌 Future Improvements

* Human vs AI mode
* Difficulty levels
* Tournament mode
* Game analytics dashboard
* Reinforcement learning integration

---

## 👤 Author

**Hazbilal**
🔗 GitHub: [https://github.com/Hazbilal3](https://github.com/Hazbilal3)

---

⭐ If you like this project, don't forget to **star the repository**!


