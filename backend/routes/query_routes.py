from fastapi import APIRouter
import asyncio
from datetime import datetime, timezone
from backend.database import collection, convos_collection
from backend.config import EMBED_MODEL, LLM_MODEL, TOP_K
from backend.ollama_client import get_embeddings, generate_response
from backend.models.schemas import QueryRequest

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/")
async def query_docs(req: QueryRequest) -> dict:
    """
    get the answer from query
    """
    q = req.query
    query_emb = (await get_embeddings([q], EMBED_MODEL))[0]

    def chroma_query():
        return collection.query(
            query_embedding=[query_emb],
            n_results=req.top_k or TOP_K,
            include=["documents", "metadatas"]
        )
    res = await asyncio.to_thread(chroma_query)
    docs, metas = res["documents"][0], res["metadatas"][0]
    context = "\n\n".join([f"[{m['source']}] {d}" for d, m in zip(docs, metas)])
    prompt = f"Context:\n{context}\n\nQuestions: {q}\n Answer:"

    answer = await generate_response(prompt, req.llm_model or LLM_MODEL)
    await convos_collection.insert_one({"query": q, "answer":answer, "created_at": datetime.now(timezone.utc)})
    return {"answer": answer, "sources": metas}

