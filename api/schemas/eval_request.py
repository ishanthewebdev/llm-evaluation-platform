from pydantic import BaseModel
from typing import Optional

class EvalRequest(BaseModel):
    question: str
    answer: str
    context: str
    ground_truth: Optional[str] = None
