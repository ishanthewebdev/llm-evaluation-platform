def compare_runs(baseline_runs:list,new_runs:list):
    """
    Compares two sets of evaluation runs.
    """
    def avg(metric_name,runs):
        values=[
            r["metrices"][metric_name].get("score",0)
            for r in runs
            if metric_name in r["metrices"]

        ]
        return sum(values)/max(len(values),1)
    return {
        "relevance_delta": avg("relevance", new_runs) - avg("relevance", baseline_runs),
        "faithfulness_delta": avg("faithfulness", new_runs) - avg("faithfulness", baseline_runs),
        "hallucination_delta": avg("hallucination", new_runs) - avg("hallucination", baseline_runs),
        "completeness_delta": avg("completeness", new_runs) - avg("completeness", baseline_runs),
    }
