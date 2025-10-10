from motor.motor_asyncio import AsyncIOMotorClient
import chromadb
from config import MONGO_URI, MONGO_DB, CHROMA_PERSIST_DIR


mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client[MONGO_DB]
print("=======================================", db)
docs_collection = db["documents"]
convos_collection = db["conversations"]

#chroma_db_impl -> which storage backend to use
#duckdb -> the embedded database engine (like SQLite, but faster for analytics)
#Parquet -> Columnar file format used to store vector efficiently on disk

chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
# get or create collection
collection = chroma_client.get_or_create_collection(name="documents")


