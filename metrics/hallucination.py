# import re

# def hallucination(answer:str,context:str)->dict:
#     """
#     Detects whether the answer contains hallucinated information.
#     """
#     sentences=re.split(r'[.!?]',answer)
#     sentences=[s.strip() for s in sentences if s.strip()]
#     if not sentences:
#         return{'halliucinated':True,"hallucination_ratio":1.0}
#     hallucinated=0

#     for sentence in sentences:
#         if sentence.lower() not in context.lower():
#             hallucinated+=1
#     ratio=hallucinated/len(sentences)

#     return{
#           'hallucinated':ratio>0.3,
#           'hallucination_ratio':round(ratio,2)
#     }        

import re

def hallucination(
    question:str,
    answer: str,
    context: str,
    ground_truth: str
) -> float:
    """
    Hallucination metric.

    Measures how much of the answer is NOT supported
    by context or ground truth.

    Returns:
        float between 0 and 1
        1.0 = no hallucination
        0.0 = completely hallucinated
    """

    # if not answer.strip():
    #     return 0.0

    # if not context.strip() and not ground_truth.strip():
    #     return 0.0

    # # Tokenize answer into words
    # answer_tokens = set(re.findall(r"\w+", answer.lower()))
    # context_tokens = set(re.findall(r"\w+", context.lower()))
    # truth_tokens = set(re.findall(r"\w+", ground_truth.lower()))

    # supported_tokens = context_tokens.union(truth_tokens)

    # unsupported = answer_tokens - supported_tokens

    # if not answer_tokens:
    #     return 0.0

    # hallucination_ratio = len(unsupported) / len(answer_tokens)

    # return round(1 - hallucination_ratio, 3)
    if not answer.strip() or not context.strip():
        return 1.0  # fully hallucinated

    sentences = [s.strip() for s in re.split(r"[.!?]", answer) if s.strip()]
    hallucinated = 0

    for s in sentences:
        keywords = s.lower().split()[:6]
        matches = sum(1 for k in keywords if k in context.lower())

        if matches / len(keywords) < 0.4:
            hallucinated += 1

    return round(hallucinated / len(sentences), 2)
