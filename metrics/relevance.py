# from embeddings.embedder import embed_query,embed_texts
# from embeddings.similarity import cosine_similarity

# def relevance_score(question:str,answer:str)->float:
#     """
#     Measures how relevant the answer is to the question.
#     Returns a score between 0 and 1.
#     """
#     if not question or answer:
#         return 0.0
    
#     q_emb=embed_query(question)
#     a_emb=embed_texts([answer])[0]
#     score=cosine_similarity(q_emb,a_emb)
#     score=max(0.0,min(1.0,float(score)))
#     return score
from embeddings.embedder import embed_query, embed_texts
from embeddings.similarity import cosine_similarity


def relevance_score(
    question: str,
    answer: str,
    context: str | None = None,
    ground_truth: str | None = None
) -> float:
    """
    Measures how relevant the answer is to the question.

    Returns:
        float between 0 and 1
    """

    if not question or not answer:
        return 0.0

    # Embed question and answer
    q_emb = embed_query(question)
    a_emb = embed_texts([answer])[0]

    # Compute cosine similarity
    score = cosine_similarity(q_emb, a_emb)

    # Clamp to [0, 1]
    score = max(0.0, min(1.0, float(score)))

    return score
