from src.loader import load_document, chunk_text
from src.vector_store import store_chunks
from src.ai_insights import answer_question

file_path = "text.pdf"

try:
    text = load_document(file_path)
except ValueError as error:
    print(f"Document loading failed: {error}")
    raise SystemExit

chunks = chunk_text(text)
db_store = store_chunks(chunks)

user_in = input("What question do you have about this document? ")

answer = answer_question(db_store, user_in)
print(answer)