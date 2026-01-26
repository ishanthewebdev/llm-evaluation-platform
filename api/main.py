from fastapi import FastAPI 
# from api.routes.evaluate import health
from api.routes import evaluate


app = FastAPI(title="LLM Evaluation Service")

# app.include_router(eval_router)
app.include_router(evaluate.router)
@app.get("/")
def health():
    return {"status": "evaluation service running"}
