from evaluation.runner import run_evaluation

question = "What is Retrieval Augmented Generation?"
# answer = "RAG is a technique that combines retrieval from documents with text generation."
answer='''Retrieval Augmented Generation (RAG) is a technique in artificial intelligence that combines document retrieval with language generation.
In RAG, relevant information is first retrieved from external documents or a knowledge base, and this retrieved context is then provided to a language model to generate the final answer.
This approach helps improve factual accuracy, provides up-to-date information, and reduces hallucinations compared to using a language model alone.'''
# context = "Retrieval Augmented Generation (RAG) improves LLMs by grounding answers in retrieved documents."
context='''Retrieval Augmented Generation combines document retrieval
with language generation to improve factual accuracy.'''
ground_truth = "Retrieval Augmented Generation combines document retrieval with language generation to improve factual accuracy."

result = run_evaluation(
    question=question,
    answer=answer,
    context=context,
    ground_truth=ground_truth
)

print(result)
