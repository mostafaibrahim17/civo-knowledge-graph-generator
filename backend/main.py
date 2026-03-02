import os
import json
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Environment variables
RELAXAI_API_KEY = os.getenv("RELAXAI_API_KEY")
RELAXAI_API_URL = os.getenv(
    "RELAXAI_API_URL",
    "https://api.relax.ai/v1/chat/completions"
)
if not RELAXAI_API_KEY:
    raise RuntimeError("RELAXAI_API_KEY is missing.")

# FastAPI setup
app = FastAPI(title="Knowledge Graph Backend (JSON-Safe)")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models setup
class GraphifyRequest(BaseModel):
    text: str

class Node(BaseModel):
    id: str
    type: str

class Edge(BaseModel):
    source: str
    target: str
    relation: str

class GraphifyResponse(BaseModel):
    nodes: list[Node]
    edges: list[Edge]

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Hard JSON-only prompt builder
@app.post("/graphify", response_model=GraphifyResponse)
async def graphify(payload: GraphifyRequest):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")
    prompt = build_prompt(payload.text)
    body = {
        "model": "Llama-4-Maverick-17B-128E",
        "messages": [
            {"role": "system", "content": "Return ONLY JSON following the given structure."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0,
        "max_tokens": 300
    }
    # Call relaxAI
    try:
        async with httpx.AsyncClient(timeout=40.0) as client:
            response = await client.post(
                RELAXAI_API_URL,
                json=body,
                headers={"Authorization": f"Bearer {RELAXAI_API_KEY}"}
            )
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"relaxAI unreachable: {str(e)}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    # Extract model content
    content = response.json()["choices"][0]["message"]["content"]
    content = clean_model_output(content)
    # JSON parsing attempts
    data = None
    try:
        data = try_parse_json_strict(content)
    except Exception:
        data = try_parse_json_fallback(content)
    # Guaranteed safe output
    nodes = [Node(**n) for n in data.get("nodes", []) if "id" in n and "type" in n]
    edges = [Edge(**e) for e in data.get("edges", []) if "source" in e and "target" in e]
    return GraphifyResponse(nodes=nodes, edges=edges)

# Helper functions
# ... (Include all helper functions here) ...
