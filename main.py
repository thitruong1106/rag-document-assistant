from src.loader import load_and_chunk
from src.vector_store import store_chunks
from src.ai_insights import answer_question

chunks = load_and_chunk("test.txt")
collection = store_chunks(chunks)

answer = answer_question(collection, "What were the Q3 results?")
print(answer)