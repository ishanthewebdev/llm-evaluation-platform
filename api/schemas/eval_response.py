from pydantic import BaseModel
from typing import Dict, List
from typing import Dict, List, Optional

class EvalResponse(BaseModel):
    question: str
    answer: str
    ground_truth: Optional[str]
    scores: Dict[str, float]
    verdict: str
    reasons: List[str]
    # run_id: str
    # timestamp: str
    # scores: Dict[str, float]
    # verdict: str
    # reasons: List[str]
