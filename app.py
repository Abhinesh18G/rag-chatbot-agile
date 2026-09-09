import os

import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import Chroma

from utils import (
    extract_text_from_pdf,
    chunk_text,
    build_prompt,
)


# --------------------------------------------------
# Load API Key
# --------------------------------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Intelligent RAG Document Chatbot",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Intelligent RAG Document Chatbot")
st.write("Upload one or more PDF documents and ask questions.")


# --------------------------------------------------
# Check API Key
# --------------------------------------------------
if not GOOGLE_API_KEY:
    st.error(
        "GOOGLE_API_KEY not found. " "Set it in a .env file or environment variable."
    )
    st.stop()


# --------------------------------------------------
# Gemini Embedding Model
# --------------------------------------------------
@st.cache_resource
def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001", google_api_key=GOOGLE_API_KEY
    )


# --------------------------------------------------
# Gemini Chat Model
# --------------------------------------------------
@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0,
        google_api_key=GOOGLE_API_KEY,
    )


embedding_model = get_embedding_model()
llm = get_llm()


# --------------------------------------------------
# Session State
# --------------------------------------------------
if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "processed_files" not in st.session_state:
    st.session_state.processed_files = None


# --------------------------------------------------
# Upload PDF Files
# --------------------------------------------------
uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True,
)


# --------------------------------------------------
# Process PDF Files
# --------------------------------------------------
if uploaded_files:

    file_signature = tuple((file.name, file.size) for file in uploaded_files)

    if file_signature != st.session_state.processed_files:

        all_chunks = []

        with st.spinner("Reading and processing PDF documents..."):

            for uploaded_file in uploaded_files:

                st.info(f"Reading {uploaded_file.name}")

                file_bytes = uploaded_file.read()

                text = extract_text_from_pdf(file_bytes)

                if not text.strip():
                    st.warning(f"No readable text found in " f"{uploaded_file.name}")
                    continue

                chunks = chunk_text(text)

                all_chunks.extend(chunks)

        if not all_chunks:
            st.error("No readable text was found " "in the uploaded PDF files.")
            st.stop()

        st.success(f"Successfully processed " f"{len(uploaded_files)} PDF file(s).")

        st.info(f"Total Chunks: {len(all_chunks)}")

        # --------------------------------------------------
        # Create Chroma Vector Database
        # --------------------------------------------------
        with st.spinner("Generating embeddings..."):

            vector_db = Chroma.from_texts(
                texts=all_chunks,
                embedding=embedding_model,
            )

        st.success("Embeddings generated successfully! ✅")

        # --------------------------------------------------
        # Create Retriever
        # --------------------------------------------------
        st.session_state.retriever = vector_db.as_retriever(search_kwargs={"k": 3})

        st.session_state.processed_files = file_signature

        st.success("Documents are ready for questions! 🎉")


# --------------------------------------------------
# Question and Answer Section
# --------------------------------------------------
if st.session_state.retriever:

    st.divider()

    st.subheader("💬 Ask a Question")

    question = st.text_input("Ask a question about your documents:")

    if question:

        with st.spinner("Searching documents and generating answer..."):

            docs = st.session_state.retriever.invoke(question)

            context = "\n\n".join(doc.page_content for doc in docs)

            prompt = build_prompt(
                context,
                question,
            )

            response = llm.invoke(prompt)

        # --------------------------------------------------
        # Display Answer
        # --------------------------------------------------
        st.subheader("🤖 Answer")

        st.write(response.content)

        # --------------------------------------------------
        # Display Retrieved Chunks
        # --------------------------------------------------
        with st.expander("📚 Retrieved Chunks"):

            for i, doc in enumerate(
                docs,
                start=1,
            ):

                st.markdown(f"### Chunk {i}")

                st.write(doc.page_content)

                st.divider()
