# 📄 Intelligent RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions about their content.

The application extracts text from uploaded PDF files, divides the text into chunks, generates embeddings using Google Gemini, stores the embeddings in ChromaDB, retrieves relevant information, and generates answers using Google Gemini.

This project demonstrates Agile Development, automated testing, Continuous Integration (CI), Docker containerization, and Continuous Deployment (CD).

---

## 🚀 Live Application

The application is deployed on Render:

https://rag-chatbot-agile.onrender.com

---

## ✨ Features

- Upload one or multiple PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate embeddings using Google Gemini
- Store embeddings in ChromaDB
- Perform semantic similarity search
- Ask questions about uploaded documents
- Generate answers using Google Gemini
- Reduce hallucination by using retrieved document context
- Display retrieved document chunks
- Automated testing using Pytest
- Code quality checking using Flake8
- Code formatting using Black
- Continuous Integration using GitHub Actions
- Docker containerization
- Docker image publishing to Docker Hub
- Continuous Deployment using Render

---

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation architecture.

```text
User
  |
  | Upload PDF / Ask Question
  v
Streamlit UI
  |
  v
PDF Ingestion
  |
  +-- Text Extraction
  |
  +-- Text Chunking
  |
  v
Gemini Embeddings
  |
  v
ChromaDB Vector Database
  |
  | Retrieve Relevant Chunks
  v
Gemini LLM
  |
  v
Final Answer
  |
  +-- Retrieved Chunks
```
