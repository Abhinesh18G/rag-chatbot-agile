# User Stories

## US01 – Upload Multiple PDFs
**As a user,** I want to upload multiple PDF files so that I can ask questions about their content.

**Acceptance Criteria:**
- User can upload one or more PDF files.
- PDF text is extracted successfully.
- The documents are divided into smaller chunks.

---

## US02 – Ask Questions About Documents
**As a user,** I want to ask questions about the uploaded documents so that I can quickly find relevant information.

**Acceptance Criteria:**
- User can enter a question.
- The system searches the uploaded documents.
- The chatbot generates an answer using the retrieved content.

---

## US03 – Prevent Hallucination
**As a user,** I want the chatbot to answer only from the uploaded documents so that it does not provide unrelated information.

**Acceptance Criteria:**
- The chatbot uses retrieved document chunks as context.
- If the answer is not available in the documents, it should respond:
  "I could not find the answer in the uploaded documents."

---

## US04 – View Retrieved Chunks
**As a user,** I want to see the retrieved document chunks so that I can understand which information was used to generate the answer.

**Acceptance Criteria:**
- Retrieved chunks are displayed after answering.
- The user can inspect the relevant document content.

---

## US05 – Automated Testing
**As a developer,** I want automated tests to run whenever code is pushed so that errors can be detected early.

**Acceptance Criteria:**
- Pytest tests are available.
- GitHub Actions runs the tests automatically.
- The pipeline shows whether the tests passed or failed.

---

## US06 – Code Quality Checking
**As a developer,** I want automated code quality checks so that the project follows coding standards.

**Acceptance Criteria:**
- Flake8 checks the source code.
- Black checks code formatting.
- The CI pipeline fails if quality checks fail.

---

## US07 – Containerized Application
**As a developer,** I want the chatbot to run inside a Docker container so that the application can be deployed consistently.

**Acceptance Criteria:**
- A Dockerfile is provided.
- Docker image can be built successfully.
- The application runs using the Docker image.

---

## US08 – Continuous Deployment
**As a developer,** I want the application to be automatically deployed after a successful build so that the latest version is available online.

**Acceptance Criteria:**
- Docker image is pushed to Docker Hub.
- Deployment is triggered automatically.
- The application is available through the deployed Render URL.
