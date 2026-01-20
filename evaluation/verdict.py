def regression_verdict(deltas:dict):
    reasons=[]

    if deltas["hallucninatio_delta"]>0:
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