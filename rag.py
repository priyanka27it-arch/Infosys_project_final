from typing import List, Dict, Optional, Tuple
import os

_documents: List[Dict[str, str]] = []
_chunks: List[str] = []
_chunk_source: List[str] = []
_vector_embeddings = None


def _chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    tokens = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        tokens.append(text[start:end])
        start += chunk_size - overlap
    return tokens


def _get_embedding_model():
    global _vector_embeddings
    # prefer sentence-transformers when present
    try:
        from sentence_transformers import SentenceTransformer

        if _vector_embeddings is None:
            _vector_embeddings = SentenceTransformer("all-MiniLM-L6-v2")
    except Exception:
        _vector_embeddings = None

    return _vector_embeddings


def _embed(texts: List[str]):
    model = _get_embedding_model()
    if model is not None:
        return model.encode(texts).astype("float32")

    # fallback to sklearn TF-IDF vectorizer + cosine similarity (fast enough for trivial examples)
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer

        vectorizer = TfidfVectorizer().fit(texts)
        return vectorizer.transform(texts).toarray().astype("float32")
    except Exception:
        # last resort random embeddings to keep logic running (not production-grade)
        import numpy as np

        return np.random.rand(len(texts), 384).astype("float32")


def _rebuild_index():
    global _chunks, _chunk_source, _vector_embeddings
    _chunks = []
    _chunk_source = []
    for doc in _documents:
        text = doc["content"]
        name = doc["name"]
        for chunk in _chunk_text(text):
            _chunks.append(chunk)
            _chunk_source.append(name)

    if _chunks:
        import numpy as np

        vectors = _embed(_chunks)
        _vector_embeddings = vectors
    else:
        _vector_embeddings = None


def load_document(name: str, content: str):
    """Append a document and re-index chunks."""
    existing = next((d for d in _documents if d["name"] == name), None)
    if existing:
        existing["content"] = content
    else:
        _documents.append({"name": name, "content": content})
    _rebuild_index()


def list_documents() -> List[str]:
    return [doc["name"] for doc in _documents]


def clear_documents():
    global _documents, _chunks, _chunk_source, _vector_embeddings
    _documents = []
    _chunks = []
    _chunk_source = []
    _vector_embeddings = None


def _cosine_sim(a, b):
    import numpy as np

    a_norm = a / (np.linalg.norm(a) + 1e-12)
    b_norm = b / (np.linalg.norm(b, axis=1, keepdims=True) + 1e-12)
    return np.dot(b_norm, a_norm)


def retrieve(query: str, top_k: int = 5) -> List[Tuple[str, str, float]]:
    """Retrieve top-k relevant chunks from indexed docs."""
    if not _chunks or _vector_embeddings is None:
        return []

    query_emb = _embed([query])[0]

    scores = _cosine_sim(query_emb, _vector_embeddings)
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    return [(f"{_chunk_source[i]}", _chunks[i], float(scores[i])) for i in order if scores[i] > 0]


def generate_answer(query: str) -> Dict[str, object]:
    """Run RAG query + mock answer generation."""
    if len(_documents) == 0:
        return {"answer": "No documents uploaded yet. Upload PDF/TXT files first.", "sources": []}

    relevant = retrieve(query, top_k=5)
    if not relevant:
        # fallback to document-level clues
        relevant = [(doc["name"], doc["content"][:250] + "...", 0.0) for doc in _documents[:2]]

    sources = list(dict.fromkeys([r[0] for r in relevant]))
    context_text = "\n\n".join([f"[{r[0]}] {r[1]}" for r in relevant])

    answer_text = (
        "I found relevant information in your documents. "
        "Use the following retrieved context to answer your question:\n\n"
        f"{context_text}\n\n"
        "Final answer:\n"
        f"(RAG response for query: '{query}')"
    )

    # If OpenAI is configured, optionally call real LLM.
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=openai_api_key)
            prompt = (
                "You are a RAG assistant. Answer using only the context below.\n\n"
                f"{context_text}\n\nQuestion: {query}\nAnswer:"
            )
            completion = client.responses.create(model="gpt-4.1-mini", input=prompt)
            llm_text = completion.output_text
            if llm_text:
                answer_text = llm_text
        except Exception:
            pass

    return {"answer": answer_text, "sources": sources}
