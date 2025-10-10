from fastapi import APIRouter, File, UploadFile, Form, HTTPException
import uuid, asyncio
from datetime import datetime, timezone
from utils import extract_text, chunk_text
from database import docs_collection, collection
from ollama_client import get_embeddings
from config import EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...), owner: str = Form(None)):
    content = await file.read()
    ext = file.filename.split(".")[-1].lower()
    text = await asyncio.to_thread(extract_text, content, ext)
    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found")

    doc_id = str(uuid.uuid4())
    chunks = await asyncio.to_thread(chunk_text, text, CHUNK_SIZE, CHUNK_OVERLAP)
    # print("I am the chunk", chunks)
    chunks_ids = [f"{doc_id}:{i}" for i in range(len(chunks))]
    metas = [
        {"doc_id": doc_id, "chunk_index": i, "source": file.filename, "owner": owner}
        for i in range(len(chunks))
    ]
    # print("What is metas", metas)
    # print("Embed Model is", EMBED_MODEL)
    embeddings = await get_embeddings(chunks, EMBED_MODEL)
    all_embeddings = []
    all_embeddings.append(embeddings[0]["embedding"])
    print("The chunk is", chunks)
    print("The length is", len(chunks), len(all_embeddings))
    # print("I am the embeddings", embeddings)

    def add_to_chroma():
        collection.add(ids=chunks_ids, documents=chunks, metadatas=metas, embeddings=all_embeddings)
    await asyncio.to_thread(add_to_chroma)

    await docs_collection.insert_one({
        "_id": doc_id,
        "file_name": file.filename,
        "owner": owner,
        "uploaded_at": datetime.now(timezone.utc),
        "chunk_count": len(chunks)
    })

    return {"status": "success", "doc_id": doc_id, "chunks": len(chunks)}

