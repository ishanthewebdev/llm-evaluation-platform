from embeddings.embedder import embed_query,embed_texts
from embeddings.similarity import cosine_simlarity

def relevance_score(question:str,answer:str)->float:
    """
    Measures how relevant the answer is to the question.
    Returns a score between 0 and 1.
    """
    if not question or answer:
        return 0.0
    
    q_emb=embed_query(question)
    a_emb=embed_texts([answer])[0]
    score=cosine_simlarity(q_emb,a_emb)
    score=max(0.0,min(1.0,float(score)))
    return score
