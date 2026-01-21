def regression_verdict(deltas:dict):
    reasons=[]

    if deltas["hallucnination_delta"]>0:
        reasons.append("hallucination rate increased")

    if deltas["faithfulness_delta"]<-0.05:
        reasons.append("faithfulness dropped significantly")
    if deltas["relevance_delta"]<-0.1:
        reasons.append("Relevance degraded")

    if reasons:
        return{
            "status":"REGRESSION",
            "reasons":reasons
        }
    return{
        "status":"improved",
        "reasons":["all metrics are stable or imporved"]
    }  

def final_verdict(scores: dict) -> dict:
    """
    Produces a final verdict for a SINGLE evaluation run.

    Input:
        scores = {
            "relevance": float,
            "faithfulness": float,
            "hallucination": float,
            "completeness": float
        }

    Output:
        dict with status + explanation
    """

    reasons = []
    if scores["relevance"] < 0.5:
        reasons.append("Answer is weakly related to the question")

    if scores["faithfulness"] < 0.6:
        reasons.append("Answer is not well supported by context")

    if scores["hallucination"] > 0.3:
        reasons.append("Answer contains hallucinated information")

    if scores["completeness"] < 0.6:
        reasons.append("Answer does not fully address the question")

    if reasons:
        return {
            "status": "FAIL",
            "reasons": reasons
        }

    return {
        "status": "PASS",
        "reasons": ["Answer meets all quality criteria"]
    } 
    
    
