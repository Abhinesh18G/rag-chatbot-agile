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
