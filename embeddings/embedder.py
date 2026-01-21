# embeddings/embedder.py

from sentence_transformers import SentenceTransformer
import numpy as np

# Load once (global, efficient)
_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: list[str]) -> np.ndarray:
    """
    Convert a list of texts into embeddings.

    INPUT:
        texts: List[str]

    OUTPUT:
        np.ndarray of shape (len(texts), embedding_dim)
    """
    return _MODEL.encode(
        texts,
        normalize_embeddings=True,
        convert_to_numpy=True
    )

def embed_query(query: str) -> np.ndarray:
    """
    Convert a single query string into an embedding.

    INPUT:
        query: str

    OUTPUT:
        np.ndarray of shape (1, embedding_dim)
    """
    return _MODEL.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True
    )
