from fastapi import APIRouter
from api.schemas.eval_request import EvalRequest
from api.schemas.eval_response import EvalResponse
from evaluation.runner import run_evaluation

router = APIRouter()

# @router.post("/evaluate", response_model=EvalResponse)
# def evaluate(req: EvalRequest):
#     result = run_evaluation(
#         req.question,
#         req.answer,
#         req.context

#     )

#     print("\n=== EVALUATION RESULT ===")
#     print(result)

#     return result
# def evaluate(req: EvalRequest):
#     result = run_evaluation(
#         question=req.question,
#         answer=req.answer,
#         context=req.context,
#         ground_truth=req.ground_truth
#     )
#     return result
@router.post("/evaluate", response_model=EvalResponse)
def evaluate(req: EvalRequest):
    result = run_evaluation(
    question=req.question,
    answer=req.answer,
    context=req.context,
    ground_truth=req.ground_truth
) 
    print("\n=== EVALUATION RESULT ===")
    print(result)

    return result

    