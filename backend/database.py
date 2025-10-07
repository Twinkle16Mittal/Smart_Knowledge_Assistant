from motor.motor_asyncio import AsyncIOMotorClient
import cromadb
from cromadb.config import Settings
from backend.config import MONGO_URI, MONGO_DB, CHROMA_PERSIST_DIR


mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client[MONGO_DB]
docs_collection = db["documents"]
convos_collection = db["conversations"]

#chroma_db_impl -> which storage backend to use
#duckdb -> the embedded database engine (like SQLite, but faster for analytics)
#Parquet -> Columnar file format used to store vector efficiently on disk

chroma_client = chroma_db.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=CHROMA_PERSIST_DIR
))
collection = chroma_client.get_or_create_collection(name="documents")

