import fitz  # PyMuPDF

from utils import extract_text_from_pdf, chunk_text, build_prompt


def _make_pdf_bytes(text: str) -> bytes:
    """Helper: build an in-memory single-page PDF containing `text`."""
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text)
    pdf_bytes = doc.tobytes()
    doc.close()
    return pdf_bytes


def test_extract_text_from_pdf_returns_text():
    pdf_bytes = _make_pdf_bytes("Hello DevOps World")
    result = extract_text_from_pdf(pdf_bytes)
    assert "Hello" in result
    assert "DevOps" in result


def test_chunk_text_splits_long_text():
    long_text = "word " * 500  # ~2500 characters
    chunks = chunk_text(long_text, chunk_size=500, chunk_overlap=50)
    assert len(chunks) > 1
    assert all(len(c) <= 550 for c in chunks)  # allow small overlap slack


def test_chunk_text_short_text_single_chunk():
    short_text = "Just one short sentence."
    chunks = chunk_text(short_text, chunk_size=500, chunk_overlap=50)
    assert len(chunks) == 1
    assert chunks[0] == short_text


def test_build_prompt_contains_context_and_question():
    prompt = build_prompt(
        context="Paris is the capital of France.",
        question="What is the capital of France?",
    )
    assert "Paris is the capital of France." in prompt
    assert "What is the capital of France?" in prompt
    assert "I could not find the answer" in prompt
