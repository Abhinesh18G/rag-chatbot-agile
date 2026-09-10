# 📄 Gemini RAG Chatbot – Agile Development & DevOps

A Retrieval-Augmented Generation (RAG) chatbot developed using Streamlit, Google Gemini, LangChain, and ChromaDB.

The application allows users to upload PDF documents and ask questions about their content. The system retrieves relevant document chunks using vector similarity search and generates answers using Google Gemini.

This project also demonstrates Agile development, automated testing, Continuous Integration (CI), Docker containerization, and Continuous Deployment (CD).

---

## 🚀 Live Application

The chatbot is deployed on Render:

https://rag-chatbot-agile.onrender.com

---

## ✨ Features

- Upload one or multiple PDF files
- Extract text from PDF documents
- Split documents into smaller chunks
- Generate vector embeddings using Gemini
- Store embeddings using ChromaDB
- Perform semantic similarity search
- Ask questions about uploaded documents
- Generate answers using Google Gemini
- Reduce hallucination using retrieved document context
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

### RAG Flow

## Architecture Diagram

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
---
### 🔄 RAG Workflow
1. PDF Upload
The user uploads one or more PDF documents through the Streamlit interface.
2. Text Extraction
Text is extracted from the uploaded PDF files using PyMuPDF.
3. Text Chunking
The extracted text is divided into smaller chunks for efficient retrieval.
4. Embedding Generation
Gemini converts the text chunks into numerical vector representations.
5. Vector Storage
The generated embeddings are stored in ChromaDB.
6. Question
The user enters a question related to the uploaded documents.
7. Similarity Search
ChromaDB searches for the most relevant document chunks.
8. Answer Generation
The retrieved chunks are passed as context to Gemini.
Gemini generates the answer using the retrieved information.
9. Retrieved Chunks
The application displays the retrieved chunks so that the user can inspect the information used for the answer.
---
## 🛠️ Technologies Used
Technology
Purpose
Python
Application development
Streamlit
Web user interface
LangChain
RAG integration
Google Gemini
Embeddings and LLM
ChromaDB
Vector database
PyMuPDF
PDF text extraction
Pytest
Automated testing
Flake8
Code quality
Black
Code formatting
Git
Version control
GitHub
Source code management
GitHub Actions
CI/CD automation
Docker
Containerization
Docker Hub
Docker image registry
Render
Cloud deployment
---
## 🤖 Gemini Models
Embedding Model
gemini-embedding-001
Used to convert document chunks into vector embeddings.
Chat Model
gemini-3.6-flash
Used to generate answers from the retrieved document context.
---
## 📁 Project Structure
rag-chatbot-agile/
│
├── app.py
├── utils.py
├── test_utils.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
└── docs/
    ├── user-stories.md
    ├── backlog.md
    ├── scrum-board.md
    ├── sprint-review.md
    ├── retrospectives.md
    ├── architecture.png
    └── cicd.png
The .env file is used for the Gemini API key and must not be committed to GitHub.
---
## ⚙️ Local Setup
1. Clone the Repository
git clone https://github.com/Abhinesh18G/rag-chatbot-agile.git
Go to the project directory:
cd rag-chatbot-agile
2. Create Virtual Environment
python -m venv venv
Activate the environment on Windows:
venv\Scripts\activate
3. Install Dependencies
Install the application dependencies:
pip install -r requirements.txt
Install development and testing dependencies:
pip install -r requirements-dev.txt
---
## 🔑 API Key Configuration
Create a .env file in the project root.
GOOGLE_API_KEY=your_gemini_api_key
Replace your_gemini_api_key with your Google Gemini API key.
The API key should never be hard-coded or committed to GitHub.
---
## ▶️ Run the Application
Start the Streamlit application:
streamlit run app.py
The application will open in the browser.
Upload a PDF and ask a question related to its content.
---
## 🧪 Testing
The project uses Pytest for automated testing.
Run:
pytest -v
The tests verify important application functionality
---
## 🔎 Code Quality
Flake8 is used for code quality checking.
Run:
flake8 . --max-line-length=100 --exclude=.venv,venv
---
## 🖤 Code Formatting
Black is used to maintain consistent Python formatting.
Format the source code:
black app.py utils.py
Check formatting:
black --check .
---
## 🐳 Docker
The application is containerized using Docker.
Build the Docker image:
docker build -t rag-chatbot .
The Streamlit application runs on port:
8501
The Docker image is published to Docker Hub through the CI/CD pipeline.
---
## 🔁 CI/CD Pipeline
GitHub Actions is used to automate Continuous Integration and Continuous Deployment.
The pipeline follows this process:
Developer
    |
    v
GitHub Push
    |
    v
GitHub Actions
    |
    +-- Flake8
    |
    +-- Black Check
    |
    +-- Pytest
    |
    +-- Docker Build
    |
    v
Docker Hub
    |
    v
Render
    |
    v
Live RAG Chatbot
---
## 🔧 Continuous Integration
The CI pipeline automatically performs:
Checkout source code
Setup Python environment
Install dependencies
Run Flake8
Check Black formatting
Run Pytest
Build the Docker image
The pipeline runs automatically when code is pushed or a pull request is created for the configured branches.
---
## 📦 Docker Image Publishing
After successful CI checks, the Docker image is built and pushed to Docker Hub.
The image is tagged using:
latest
and the GitHub commit SHA.
---
## ☁️ Continuous Deployment
The application is deployed using Render.
The deployment flow is:
GitHub
   |
   v
GitHub Actions
   |
   v
Docker Build
   |
   v
Docker Hub
   |
   v
Render Deploy Hook
   |
   v
Live Application
A successful push to the main branch triggers the deployment process.
---
## 🏃 Agile Development
The project follows an Agile development approach using three sprints.
Sprint 1 – RAG Chatbot Development
Tasks included:
PDF upload
PDF text extraction
Text chunking
Gemini embeddings
ChromaDB integration
Question answering
Retrieved chunk display
Sprint 2 – Testing and Continuous Integration
Tasks included:
Pytest
Flake8
Black
GitHub repository
GitHub Actions
Automated Docker build
Sprint 3 – Deployment and Continuous Delivery
Tasks included:
Docker containerization
Docker Hub
Render deployment
Deploy webhook
Automated deployment
---
## 📋 Agile Documentation
Detailed Agile documentation is available in the docs folder.
User Stories
View User Stories
Product & Sprint Backlog
View Backlog
Scrum Board
View Scrum Board
Sprint Reviews
View Sprint Reviews
Sprint Retrospectives
View Retrospectives
---
## 🔐 Security
The Gemini API key is stored as an environment variable.
It is not hard-coded in the source code.
The .env file is excluded from Git using .gitignore.
For cloud deployment, the API key is configured securely using environment variables.
---
## 📊 Project Status
Component
Status
RAG Chatbot
✅ Completed
PDF Upload
✅ Completed
PDF Text Extraction
✅ Completed
Text Chunking
✅ Completed
Gemini Embeddings
✅ Completed
ChromaDB
✅ Completed
Gemini LLM
✅ Completed
Retrieved Chunks
✅ Completed
Pytest
✅ Completed
Flake8
✅ Completed
Black
✅ Completed
GitHub Actions CI
✅ Completed
Docker Build
✅ Completed
Docker Hub Push
✅ Completed
Render Deployment
✅ Completed
Automatic Deployment
✅ Completed
Agile Documentation
✅ Completed
---
##🌐 Live Demo
Gemini RAG Chatbot:
https://rag-chatbot-agile.onrender.com⁠�
---
##👨‍💻 Project Information
Project: Gemini RAG Chatbot
Course: Agile Development Process & DevOps
Frontend: Streamlit
Programming Language: Python
AI Model: Google Gemini
Embedding Model: gemini-embedding-001
Vector Database: ChromaDB
Testing: Pytest
CI/CD: GitHub Actions
Containerization: Docker
Container Registry: Docker Hub
Deployment: Render
---
