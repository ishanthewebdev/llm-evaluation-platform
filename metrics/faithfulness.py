import re

def _normalize(text:str) -> str:
    return re.sub(r"\s+"," ",text.lower().strip())

def _split_sentance(text: str)-> list[str]:
    return[s.strip()for s in re.split(r"[.!?]",text) if s.strip()]

def faithfulness_score(answer:str,context:str)->float:
    """
    Checks how much of the answer is supported by the context.
    Returns a score between 0 and 1.
    """
    if not answer or context:
        return 0.0
    
    answer=_normalize(answer)
    context=_normalize(context)
    claims=_split_sentance(answer)
    if not claims:
        return 0.0
    supported=0

    for claim in claims:
        keywords=claim.split()[:5]
        if all(k in context for k in keywords):
            supported+=1
    return supported/len(claims)        

