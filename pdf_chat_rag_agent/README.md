
# 📄 Chat with PDF (RAG-based PDF Q&A Agent)

### 🎓 FREE Step-by-Step Tutorial
👉 https://www.theunwindai.com/p/build-an-llm-app-with-rag-using-llama-3-2-running-locally  

Learn how to build this project from scratch with clear explanations, minimal code, and best practices.

---

The **Chat with PDF Agent** is a simple yet powerful LLM application that lets you **upload a PDF and ask questions about its content**.  
It uses **Retrieval Augmented Generation (RAG)** to ensure that answers are grounded in the actual document instead of hallucinated responses.

This version is adapted and structured specifically for the **ai_agent** repository.

---

## ✨ Features

- Upload a PDF document
- Ask natural language questions about the PDF
- Accurate, context-aware answers using RAG
- Lightweight implementation with minimal code
- Interactive Streamlit user interface

---

## 🧠 How It Works

1. User uploads a PDF file  
2. Text is extracted from the PDF  
3. Text is split into smaller chunks  
4. Embeddings are generated for each chunk  
5. Relevant chunks are retrieved based on the question  
6. The LLM generates an answer using only retrieved context  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API Key or any compatible LLM provider

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hazbilal3/ai_agent.git
cd ai_agent/pdf_chat_rag_agent
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure API Key

**Linux or macOS**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows PowerShell**

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

---

### 4️⃣ Run the Application

```bash
streamlit run chat_pdf.py
```

---

## 🎥 Interactive Application Demo

👉 Demo recording
[https://github.com/Shubhamsaboo/awesome-llm-apps/assets/31396011/12bdfc11-c877-4fc7-9e70-63f21d2eb977](https://github.com/Shubhamsaboo/awesome-llm-apps/assets/31396011/12bdfc11-c877-4fc7-9e70-63f21d2eb977)

---

## 📁 Project Structure

```text
pdf_chat_rag_agent/
├── README.md
├── requirements.txt
├── chat_pdf.py
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   └── retriever.py
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* OpenAI or compatible LLM
* Embeddings and vector search
* Retrieval Augmented Generation (RAG)

---

## 📌 Notes

* Best results with text-based PDFs
* Scanned PDFs may require OCR
* Large PDFs may take longer to process
* LLM provider can be swapped easily
* Answers are limited strictly to PDF content

---

## 🙌 Credits

Original inspiration from **awesome-llm-apps**
Adapted and maintained for this repository by **Hazbilal3**

