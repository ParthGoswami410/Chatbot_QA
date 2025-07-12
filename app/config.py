import os

UPLOAD_FOLDER = 'uploaded_docs'
CHUNK_SIZE = 500  
TOP_K = 3         

EMBEDDING_MODEL = 'all-MiniLM-L6-v2'  
VECTOR_DB_PATH = 'vector_store.faiss'
METADATA_STORE_PATH = 'metadata.json'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
