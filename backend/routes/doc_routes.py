from fastapi import APIRouter
from backend.database import docs_collection

router = APIRouter(prefix="/docs", tags=["Docs"])

@router.get("/")
async def list_docs(limit: int = 20)-> dict:
    """
    list all the docs
    """
    cursor = docs_collection.find().sort("uploaded_at", -1).limit(limit)
    docs = []
    async for d in cursor:
        d["_id"] = str(d["_id"])
        docs.append(d)
    return {"documents": docs}
