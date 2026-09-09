# 📄 Gemini RAG Chatbot – Agile Development & DevOps

A Retrieval-Augmented Generation (RAG) chatbot built using **Streamlit, Google Gemini, LangChain and ChromaDB**.

The application allows users to upload PDF documents and ask questions about their content. The system retrieves relevant document chunks using vector similarity search and uses Gemini to generate answers based only on the retrieved context.

The project also demonstrates **Agile Development, automated testing, Continuous Integration (CI), Docker containerization and Continuous Deployment (CD).**

---

## 🚀 Live Application

The application is deployed on Render:

https://rag-chatbot-agile.onrender.com

---

## ✨ Features

- 📄 Upload one or multiple PDF files
- 🔍 Extract text from PDF documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate vector embeddings using Gemini
- 🗄️ Store and search document embeddings using ChromaDB
- 💬 Ask questions about uploaded documents
- 🤖 Generate answers using Google Gemini
- 🛡️ Reduce hallucination by answering only from retrieved context
- 📚 Display retrieved document chunks
- 🧪 Automated testing using Pytest
- 🔎 Code quality checking using Flake8
- 🖤 Code formatting using Black
- ⚙️ Automated CI using GitHub Actions
- 🐳 Docker containerization
- 📦 Docker image publishing to Docker Hub
- ☁️ Deployment using Render
- 🔄 Automated deployment using GitHub Actions

---

# 🏗️ System Architecture

The system follows a Retrieval-Augmented Generation architecture.

```text
User
  │
  ├── Upload PDF
  │
  ▼
Streamlit UI
  │
  ▼
PDF Ingestion
  │
  ├── Text Extraction
  └── Text Chunking
  │
  ▼
Gemini Embeddings
  │
  ▼
ChromaDB
  │
  └── Vector Similarity Search
          │
          ▼
    Relevant Chunks
          │
          ▼
    Gemini LLM
          │
          ▼
       Answer
          │
          ▼
Retrieved Chunks + Answer
