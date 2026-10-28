import fitz

from langchain_text_splitters import RecursiveCharacterTextSplitter


# --------------------------------------------------
# Extract Text From PDF
# --------------------------------------------------
def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf = fitz.open(
        stream=file_bytes,
        filetype="pdf",
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


# --------------------------------------------------
# Split Text Into Chunks
# --------------------------------------------------
def chunk_text(text: str, chunk_size=500, chunk_overlap=50) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)


# --------------------------------------------------
# Build RAG Prompt
# --------------------------------------------------
def build_prompt(context: str, question: str) -> str:
    prompt = (
        "You are a helpful AI assistant.\n\n"
        "Answer ONLY from the context provided below.\n\n"
        "If the answer is not present in the context,\n"
        "reply exactly:\n\n"
        "I could not find the answer in the uploaded documents.\n\n"
        "Context:\n" + context + "\n\nQuestion:\n" + question + "\n\nAnswer:"
    )
    return prompt


# --------------------------------------------------
# Exam Prep Generator
# --------------------------------------------------
def build_exam_prep_prompt(
    context: str,
    question_count: int = 10,
    difficulty: str = "Medium",
) -> str:
    return f"""
You are an exam preparation assistant.

Generate exactly {question_count} exam questions using ONLY
the information provided in the study context below.

Difficulty: {difficulty}

Requirements:
1. Include both short-answer and long-answer questions.
2. For 10 questions, generate 5 short-answer and 5 long-answer questions.
3. Number all questions from 1 to {question_count}.
4. Provide a clear answer for every question.
5. Base every answer strictly on the supplied context.
6. Do not invent facts or introduce outside knowledge.
7. If the context does not contain enough information,
   state that clearly rather than guessing.
8. Make questions relevant to exam preparation.

Use this format for every question:

Question [number] — [Short Answer / Long Answer]
Question: [Write the question]
Answer: [Write the answer]

Study Context:
{context}

Generate the questions and answers now.
"""
