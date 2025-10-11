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

- Clone the Repository
    - git clone https://github.com/Twinkle16Mittal/Smart_Knowledge_Assistant.git
    - cd Smart_Knowledge_Assistant

- Create and Activate a Virtual Environment
    - python3 -m venv venv
    - source venv/bin/activate

- Install Dependencies
    - pip install -r requirements.txt

- Setup Environment Variables (Create a .env file in the root folder:)
    - OLLAMA_HOST=http://localhost:11434
    - MONGO_URI=mongodb://localhost:27017
    - EMBED_MODEL=nomic-embed-text:latest
    - CHAT_MODEL=llama3.2:3b
    - CHROMA_DB_DIR=./chroma_db

---

## ▶️ Running the Application

- Start Ollama Server
    - ollama serve
    - curl http://localhost:11434/v1/models

- Run the Backend (FastAPI)
    - cd backend
    - uvicorn main:app --reload
    - API Available at http://localhost:8000
    - for docs http://localhost:8000/docs

- Run the Frontend (Streamlit)
    - cd streamlit_app
    - streamlit run app.py
    - http://localhost:8501

- Run with Docker
    - docker compose up --build

---

## 🧩 Example Flow
- Go to the Streamlit UI

- Upload a PDF file (e.g., Food Menu.pdf)

- It’s automatically chunked → embedded via nomic-embed-text

- Indexed in ChromaDB

- Ask questions like:
    - What’s for dinner on Wednesday?

---

## 📘 API Reference
- POST /upload/
    - Upload and embed documents.
- POST /query/
    - Ask a question and get a contextual LLM response.
- GET /docs/
    - List all uploaded documents and metadata.

---

## 👩‍💻 Author
- Twinkle Mittal
- 💼 AI Developer | Data Science Enthusiast
- 📧 mtwinkle013@gmail.com

---