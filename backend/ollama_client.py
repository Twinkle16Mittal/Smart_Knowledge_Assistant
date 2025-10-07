import httpx
from fastapi import HTTPException
from backend.config import OLLAMA_HOST

client = httpx.AsyncClient(timeout=60.0)

async def get_embeddings(texts, model):
    url = f"{OLLAMA_HOST}/api/embed"
    resp = await client.post(url, json={"model": model, "input": texts})
    if resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Embedding error from Ollama")
    return resp.json().get("embeddings", [])

async def generate_response(prompt, model, options=None):
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    if options:
        payload["options"] = options
    resp = await client.post(url, json=payload)
    if resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Generation error from Ollama")
    return resp.json().get("response", "")



    
        