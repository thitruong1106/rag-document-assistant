from src.loader import load_and_chunk
from src.vector_store import search_chunks, store_chunks
chunks = load_and_chunk("test.txt")
collection = store_chunks(chunks)
results = search_chunks(collection, "What is this document about?")
print(results["documents"])