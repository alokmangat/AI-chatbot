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



