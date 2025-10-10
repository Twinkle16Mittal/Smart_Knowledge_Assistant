from fastapi import APIRouter
from database import docs_collection

router = APIRouter(prefix="/docs", tags=["Docs"])

@router.get("/")
async def list_docs(limit: int = 20)-> dict:
    """
    list all the docs
    """
    cursor = docs_collection.find().sort("uploaded_at", -1).limit(limit)
    docs = []
    print("Hi i a the cursor", cursor)
    async for d in cursor:
        print("the value of d", d)
        d["_id"] = str(d["_id"])
        docs.append(d)
    return {"documents": docs}
