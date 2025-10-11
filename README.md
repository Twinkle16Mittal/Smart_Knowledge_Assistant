# 🧠 Smart Knowledge Assistant

An **AI-powered document understanding system** that lets you **upload PDFs**, automatically **embed and index** their content, and then **chat with your documents** using **Ollama LLMs** (like LLaMA 3.2 or Gemma3).  

Built using **FastAPI**, **Streamlit**, **ChromaDB**, and **Ollama** — it’s your personal knowledge assistant for local/private document intelligence.

---

##  Features

- 📄 Upload and parse documents (PDF, TXT, DOCX, etc.)
- 🔍 Automatically chunk and embed text using Ollama embedding models  
- 🧩 Store embeddings locally using ChromaDB for fast semantic search
- 💬 Query and chat with your documents using LLMs (e.g., `llama3.2:3b`)
- 🧱 Modular backend with FastAPI, separate Streamlit frontend
- 🐳 Easy local or containerized setup with Docker Compose

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| LLM Backend | [Ollama](https://ollama.ai) |
| API Server | FastAPI |
| Vector Database | ChromaDB |
| Frontend UI | Streamlit |
| Database | MongoDB |
| Containerization | Docker Compose |

---

## 🧠 Environment Setup

    ### 1. Clone the Repository

    ```bash
    git clone https://github.com/Twinkle16Mittal/Smart_Knowledge_Assistant.git
    cd Smart_Knowledge_Assistant