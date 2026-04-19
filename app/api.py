# uv run uvicorn app.api:app --reload --port 8000
# http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel
from .agents import build_graph

app = FastAPI()
graph = build_graph()


class Query(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "RAG Multi-Agent API running 🚀"}


@app.post("/ask")
def ask(q: Query):
    result = graph.invoke({"query": q.question})
    return {"answer": result["answer"]}