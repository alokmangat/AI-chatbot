# 🧠 AI-Chatbot

A **document-aware AI assistant** built with FastAPI, Groq LLM, Google embedding models, and Pinecone vector retrieval — deployed on Render.

This repository provides a scalable RAG (Retrieval-Augmented Generation) backend for answering user questions using uploaded documents and intelligent language models.

---

## 🎓 What is RAG?

**RAG (Retrieval-Augmented Generation)** enhances language models by supplying relevant external context from a knowledge base, preventing hallucinations and improving accuracy, especially for factual or specialized domains like **medicine**.

---

## 🔄 Architecture


User Input
   ↓
Query Embedding → Pinecone Vector DB ← Embedded Chunks ← Chunking ← PDF Loader
   ↓
Retrieved Docs
   ↓
     RAG Chain (Groq + LangChain)
   ↓
LLM-generated Answer


## 🚀 Features

✔ Upload PDF/documents for context retrieval  
✔ Semantic search via vector embeddings  
✔ Uses Groq **llama-4-maverick** for high-quality responses  
✔ Google **text-embedding-004** for embeddings  
✔ FastAPI backend with clean REST endpoints  
✔ Deployable on Render or any cloud provider

---

## 🗂️ Repository Structure

AI-chatbot/
├── server/
│ ├── main.py
│ ├── routes/
│ │ ├── ask_question.py
│ │ └── upload_pdf.py
│ ├── modules/
│ │ ├── llm.py
│ │ └── load_vectorstore.py
│ └── requirements.txt
├── client/ # (optional/frontend if exists)
├── .gitignore
├── README.md
├── env.example



---

## 🛠️ Setup & Development

### 1️⃣ Clone the Repository

bash
git clone https://github.com/alokmangat/AI-chatbot.git
cd AI-chatbot

# Create a Python Virtual Environment

python -m venv venv
venv\Scripts\activate         # Windows
# OR
source venv/bin/activate      # macOS/Linux

# Install Dependencies

cd server
pip install -r requirements.txt

# Setup Environment Variables

cp env.example .env

GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_env

# Local Development

Start your backend with:

uvicorn main:app --reload --host 0.0.0.0 --port 8000

Open the API docs:

👉 http://127.0.0.1:8000/docs

📦 Deployment on Render

Go to https://render.com
 → New Web Service

Connect your GitHub repo

Set Root Directory to: server

Build Command:

pip install -r requirements.txt

Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT

Add environment variables under the Render dashboard:

GROQ_API_KEY
GOOGLE_API_KEY
PINECONE_API_KEY
PINECONE_ENVIRONMENT
