# Gemini RAG Chatbot — Agile & DevOps Course Project

A PDF-based Retrieval-Augmented Generation (RAG) chatbot built with Streamlit,
LangChain, Google Gemini, and ChromaDB — delivered with a full CI/CD pipeline.

## 1. Architecture

```
User -> Streamlit UI -> PyMuPDF (extract text) -> RecursiveCharacterTextSplitter (chunk)
     -> Gemini Embeddings -> ChromaDB (vector store) -> Retriever (top-k)
     -> Gemini 2.5 Flash (grounded answer) -> Streamlit UI
```

- `utils.py` — pure functions (PDF extraction, chunking, prompt building). No
  Streamlit or network calls, so it can be unit tested in CI.
- `app.py` — Streamlit UI layer, wires `utils.py` to the embedding/LLM/vector
  store.
- `tests/` — pytest suite covering `utils.py`. Runs with no API key needed.

## 2. Local Setup

```bash
git clone <your-repo-url>
cd rag-chatbot-devops
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env            # then paste your GOOGLE_API_KEY into .env
streamlit run app.py
```

Get a free Gemini API key at https://aistudio.google.com/app/apikey.

## 3. Running Tests & Linting Locally

```bash
pytest -v
flake8 . --max-line-length=100
black --check .
```

## 4. Docker

```bash
docker build -t rag-chatbot .
docker run -p 8501:8501 --env-file .env rag-chatbot
```

Visit http://localhost:8501.

## 5. CI/CD Pipeline (`.github/workflows/ci-cd.yml`)

| Stage  | Trigger                     | What it does |
|--------|------------------------------|---------------|
| Lint   | every push / PR              | `flake8` + `black --check` |
| Test   | after lint passes             | `pytest` unit tests, uploads results as an artifact |
| Build  | after tests pass              | `docker build` — verifies the image builds |
| Push   | push to `main` only           | builds & pushes image to Docker Hub, tagged `latest` and `<git-sha>` |
| Deploy | after push                    | calls a deploy webhook (Render/Railway/Streamlit Cloud) |

### Required GitHub repo secrets
Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub account |
| `DOCKERHUB_TOKEN` | Docker Hub access token (not your password) |
| `DEPLOY_WEBHOOK_URL` | Deploy hook URL from your host (optional — remove the `deploy` job if you skip hosting) |

`GOOGLE_API_KEY` is **not** needed in CI because the test suite never calls
the real Gemini API — that's the point of isolating `utils.py`.

## 6. Branching Strategy

- `main` — always deployable. Protected: PRs only, CI must pass.
- `develop` — integration branch for the current sprint.
- `feature/<name>` — one branch per user story, merged into `develop` via PR.

## 7. Agile Artifacts (for course submission)

### Product Backlog / User Stories
| ID | User Story | Priority |
|---|---|---|
| US-1 | As a user, I can upload one or more PDFs so the bot can read their content | High |
| US-2 | As a user, I can ask a natural-language question and get an answer grounded in my documents | High |
| US-3 | As a user, I can see which document chunks were used to answer, so I can verify correctness | Medium |
| US-4 | As a developer, I want CI to lint and test every PR so bugs are caught before merge | High |
| US-5 | As a developer, I want every merge to `main` to auto-build and publish a Docker image | High |
| US-6 | As an operator, I want a one-command way to deploy the latest image | Medium |

### Suggested Sprint Plan (2 sprints)
- **Sprint 1**: US-1, US-2, US-4 (core RAG pipeline + CI skeleton)
- **Sprint 2**: US-3, US-5, US-6 (UX polish + full CD, deployment)

### Definition of Done
- Code merged only via PR with a green CI pipeline (lint + test + build)
- Unit tests added for any new function in `utils.py`
- README updated if setup steps changed
- No secrets committed (`.env` is gitignored)

### Suggested board
Use GitHub Projects (Kanban: Backlog → In Progress → In Review → Done) or
Trello/Jira, one card per user story above, linked to its feature branch/PR.

## 8. Known Limitations / Future Work
- Vector store is in-memory per session (no persistence across restarts) —
  swap in a persistent Chroma path or a hosted vector DB for multi-user use.
- No auth on the Streamlit app — add `streamlit-authenticator` before any
  public deployment.
- No rate-limiting on Gemini calls — add retry/backoff for production use.
