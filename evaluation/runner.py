# evaluation/runner.py

from rag_app.services.rag_service import RAGService

from metrics.relevance import relevance_score
from metrics.faithfulness import faithfulness_score
from metrics.hallucination import hallucination_score
from metrics.completeness import completeness_score

from evaluation.verdict import final_verdict


def run_evaluation(
    question: str,
    ground_truth: str,
    session_id: str
) -> dict:
    """
    Runs full evaluation pipeline on a single question.

    INPUT:
        question (str)        -> user question
        ground_truth (str)    -> expected correct answer
        session_id (str)      -> identifies uploaded PDFs

    OUTPUT:
        dict with scores + final verdict
    """

    # 1️⃣ Call RAG system
    rag = RAGService()
    answer, context = rag.ask_with_context(question, session_id)

    # 2️⃣ Run metrics (pure evaluation, no side effects)
    scores = {
        "relevance": relevance_score(
            question=question,
            answer=answer,
            context=context,
            ground_truth=ground_truth
        ),

        "faithfulness": faithfulness_score(
            question=question,
            answer=answer,
            context=context,
            ground_truth=ground_truth
        ),

        "hallucination": hallucination_score(
            question=question,
            answer=answer,
            context=context,
            ground_truth=ground_truth
        ),

        "completeness": completeness_score(
            question=question,
            answer=answer,
            context=context,
            ground_truth=ground_truth
        ),
    }

    # 3️⃣ Aggregate scores into final verdict
    verdict = final_verdict(scores)

    # 4️⃣ Return structured evaluation result
    return {
        "question": question,
        "answer": answer,
        "ground_truth": ground_truth,
        "scores": scores,
        "verdict": verdict
    }
