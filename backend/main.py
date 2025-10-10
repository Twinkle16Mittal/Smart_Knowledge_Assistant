from fastapi import FastAPI
from routes import upload_routes, query_routes, doc_routes

app = FastAPI(title="RAG Assistant")
app.include_router(upload_routes.router)
app.include_router(query_routes.router)
app.include_router(doc_routes.router)

@app.get("/health")
def health() -> dict:
    """
    health check of server
    """
    return {"sucess": "OK"}


# uvicorn main:app --reload --host 0.0.0.0 --port 8000