# embeddings/similarity.py

import numpy as np

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.

    INPUT:
        vec1: np.ndarray of shape (d,) or (1, d)
        vec2: np.ndarray of shape (d,) or (1, d)

    OUTPUT:
        float in range [-1, 1]
    """

    # Flatten in case shape is (1, d)
    vec1 = vec1.reshape(-1)
    vec2 = vec2.reshape(-1)

    numerator = np.dot(vec1, vec2)
    denominator = np.linalg.norm(vec1) * np.linalg.norm(vec2)

    if denominator == 0:
        return 0.0

    return float(numerator / denominator)
