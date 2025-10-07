from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 4
    llm_model: Optional[str] = None