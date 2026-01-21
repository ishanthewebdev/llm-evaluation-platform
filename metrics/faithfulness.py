# import re

# def _normalize(text:str) -> str:
#     return re.sub(r"\s+"," ",text.lower().strip())

# def _split_sentance(text: str)-> list[str]:
#     return[s.strip()for s in re.split(r"[.!?]",text) if s.strip()]

# def faithfulness_score(answer:str,context:str)->float:
#     """
#     Checks how much of the answer is supported by the context.
#     Returns a score between 0 and 1.
#     """
#     if not answer or context:
#         return 0.0
    
#     answer=_normalize(answer)
#     context=_normalize(context)
#     claims=_split_sentance(answer)
#     if not claims:
#         return 0.0
#     supported=0

#     for claim in claims:
#         keywords=claim.split()[:5]
#         if all(k in context for k in keywords):
#             supported+=1
#     return supported/len(claims)        
import re


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def _split_sentence(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]


def faithfulness_score(
    question: str,
    answer: str,
    context: str,
    ground_truth: str | None = None
) -> float:
    """
    Measures how much of the answer is supported by the retrieved context.

    Returns:
        float between 0 and 1
    """

    if not answer or not context:
        return 0.0

    answer = _normalize(answer)
    context = _normalize(context)

    claims = _split_sentence(answer)
    if not claims:
        return 0.0

    supported = 0

    for claim in claims:
        # very simple heuristic: first few keywords must appear in context
        keywords = claim.split()[:5]
        # if all(k in context for k in keywords):
        #     supported += 1
    important = [
    w for w in keywords
    if w not in {"this", "that", "it", "is", "are", "was"}
]

    matches = sum(1 for w in important if w in context)

    if matches / max(len(important), 1) >= 0.5:
     supported += 1
    

    return supported / len(claims)


