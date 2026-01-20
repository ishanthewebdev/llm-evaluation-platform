import uuid
import json
from datetime import datetime
from pathlib import Path

RUNS_DIR=Path("storage/runs")
RUNS_DIR.mkdir(parents=True,exist_ok=True)

def log_evaluation(run_data:dict):
     """
    Appends a single evaluation run to a JSONL file.
    """
     run_data["run_id"]=str(uuid.uuid4())
     run_data["timestamp"]=datetime.utcnow().isoformat()

     file_path=RUNS_DIR/f"run_{datetime.utcnow().date()}.jsonl"

     with open(file_path,"a",encoding="utf-8") as f:
          f.write(json.dumps(run_data)+"\n")
          
