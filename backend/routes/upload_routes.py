from fastapi import APIRouter, File, UploadFile, Form, HTTPException
import uuid, asyncio
from datetime import datetime, timezone
from backend.utils import extract_text, chunk_text
from backend.database import docs_collection, collection, chroma_client
from backend.ollama_client import get_embeddings
from backend.config import EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...), owner: str=Form(None)):
    """
    upload file function
    """
    content = await file.read()
    ext = file.filename.split(".")[-1].lower()
    text = await asyncio.to_thread(extract_text, content, ext)
    if not text.strip():
        return HTTPException(status_code=400, detail="No text found")
    doc_id = str(uuid.uuid4())
    chunks = await asyncio.to_thread(chunk_text, text, CHUNK_SIZE, CHUNK_OVERLAP)
    chunks_ids = [f"{doc_id}:{i}" for i in range(len(chunks))]
    metas = [{"doc_id": doc_id, "chunk_index": i, "source": file.filename, 
              "owner": owner} for i in range(len(chunks))]
    embeddings = await get_embeddings(chunks, EMBED_MODEL)

    def add_to_chroma():
        collection.add(ids=chunks_ids, documents=chunks, metadatas=metas, embeddings=embeddings)
        chroma_client.persist()

    await asyncio.to_thread(add_to_chroma)

    await docs_collection.insert_one({
        "_id": doc_id, "file_name": file.filename, "owner": owner, 
        "uploaded_at": datetime.now(timezone.utc), "chunk_count": len(chunks)
    })
    return {"status": "sucess", "doc_id": doc_id, "chunks": len(chunks)}
