
# ♜ Chess Duel Agent  
**Multi-Agent Chess Game using Streamlit + LLM Agents**

A Streamlit-based chess application where **two AI agents** play chess against each other while a **Board Proxy (Validator Agent)** enforces legal moves, manages turns, and controls the game state.

This project lives inside the `aqi_analysis_agent` repository under the `chess_duel_agent` directory.

---

## 🚀 Features

### Multi-Agent Architecture
- **White Agent**: Strategic decision maker  
- **Black Agent**: Tactical opponent  
- **Board Proxy Agent**: Validates moves, enforces rules, updates board state  

### Safety & Validation
- Illegal move prevention  
- Turn-based enforcement  
- Centralized board state management  
- Game-over detection (checkmate, stalemate, draw if implemented)

### Gameplay Intelligence
- Position-aware decision making  
- Tactical captures and defense  
- Adaptive strategy based on board state  

---

## 🛠 Tech Stack
- Python 3.10+
- Streamlit
- AutoGen
- python-chess
- OpenAI API or compatible LLM provider

---

## 📂 Project Location

```text
aqi_analysis_agent/
 └── chess_duel_agent/
     ├── README.md
     ├── requirements.txt
     ├── ai_chess_agent.py
     ├── agents/
     │   ├── white_agent.py
     │   ├── black_agent.py
     │   └── board_proxy.py
     └── utils/
         └── chess_helpers.py
````

Structure may vary slightly based on your implementation.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hazbilal3/aqi_analysis_agent.git
cd aqi_analysis_agent/chess_duel_agent
```

---

### 2️⃣ Create Virtual Environment (Recommended)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Mac / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure API Key

**Windows**

```bash
setx OPENAI_API_KEY "YOUR_API_KEY"
```

**Mac / Linux**

```bash
export OPENAI_API_KEY="YOUR_API_KEY"
```

If using a different provider, configure the environment variables required by your setup.

---

## ▶️ Run the Application

```bash
streamlit run ai_chess_agent.py
```

If your entry file has a different name (for example `app.py`), replace it accordingly.

---

## 🧠 How the System Works

1. Streamlit initializes the UI and chess board
2. White agent generates a move
3. Board Proxy validates the move
4. If valid, the move is applied and turn switches
5. Black agent generates a move
6. Cycle continues until game completion

---

## 📝 Best Practices

* Use **UCI move format** (`e2e4`) for best validation
* Keep model temperature low for move consistency
* Log FEN after each move for debugging
* Let only the Board Proxy update the board

---

## 📌 Notes

* The Board Proxy must be the single source of truth
* Never let agents modify the board directly
* Always validate moves using `python-chess`

---

## 🙌 Credits

Inspired by multi-agent chess systems and adapted specifically for this repository and folder structure.


```
```
