
def aggregate_verdict(
    relevance: dict,
    faithfulness: dict,
    hallucination: dict,
    completeness: dict
) -> dict:
    """
    Aggregates all evaluation metrics into a final verdict.
    """

    reasons = []

    # 1️⃣ Hallucination is fatal
    if hallucination.get("hallucinated", False):
        return {
            "verdict": "FAIL",
            "confidence": 0.0,
            "reasons": ["Answer contains hallucinated information"],
            "metrics": {
                "relevance": relevance,
                "faithfulness": faithfulness,
                "hallucination": hallucination,
                "completeness": completeness
            }
        }

    # 2️⃣ Faithfulness is mandatory
    if not faithfulness.get("supported", True):
        return {
            "verdict": "FAIL",
            "confidence": 0.1,
            "reasons": ["Answer is not supported by context"],
            "metrics": {
                "relevance": relevance,
                "faithfulness": faithfulness,
                "hallucination": hallucination,
                "completeness": completeness
            }
        }

    # 3️⃣ Relevance gate
    if relevance.get("score", 0) < 0.5:
        return {
            "verdict": "FAIL",
            "confidence": 0.2,
            "reasons": ["Answer is not relevant to the question"],
            "metrics": {
                "relevance": relevance,
                "faithfulness": faithfulness,
                "hallucination": hallucination,
                "completeness": completeness
            }
        }

    # 4️⃣ Completeness affects quality, not validity
    if completeness.get("coverage_score", 1.0) < 0.7:
        return {
            "verdict": "PARTIAL",
            "confidence": 0.6,
            "reasons": ["Answer is correct but incomplete"],
            "metrics": {
                "relevance": relevance,
                "faithfulness": faithfulness,
                "hallucination": hallucination,
                "completeness": completeness
            }
        }

    # 5️⃣ Full pass
    return {
        "verdict": "PASS",
        "confidence": 0.9,
        "reasons": ["Answer is relevant, faithful, and complete"],
        "metrics": {
            "relevance": relevance,
            "faithfulness": faithfulness,
            "hallucination": hallucination,
            "completeness": completeness
        }
    }
 