import httpx
from fastapi import HTTPException
from config import OLLAMA_HOST

client = httpx.AsyncClient(timeout=60.0)

async def get_embeddings(texts, model):
    url = f"{OLLAMA_HOST}/v1/embeddings"
    print("The embedding url is", url)
    resp = await client.post(url, json={"model": model, "input": texts})

    # print("this is resp", resp)
    # print("status code", resp.status_code)
    # print("json data", resp.json())
    data = resp.json()
    import json
    with open("embedding_json.json", 'w') as f:
        json.dump(data, f, indent=4) 
    if resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Embedding error from Ollama")
    return resp.json().get("data", [])

async def generate_response(prompt, model, options=None):
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    if options:
        payload["options"] = options
    print("==================")
    print(url, payload)
    resp = await client.post(url, json=payload)
    if resp.status_code != 200:
        raise HTTPException(status_code=500, detail="Generation error from Ollama")
    return resp.json().get("response", "")



    
        