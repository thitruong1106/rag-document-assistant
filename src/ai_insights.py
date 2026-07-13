from src.vector_store import search_chunks
from anthropic import Anthropic
from dotenv import load_dotenv 
load_dotenv() 

client = Anthropic()

def answer_question(collection, question): 
    #1. Search for the most relevant chunks 
    results = search_chunks(collection, question)

    #2. Get the actual text chunk from result 

    relavent_chunk = results['documents'][0]

    #3. Join the chunk, into one context string 
    context = "\n\n".join(relavent_chunk)

    #4. prompt building 
    prompt = f""" 
    Context: 
    {context}

    Question: 
    {question}
    """

    #Send the prompt to claude for retrival     
    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens=1024, 
        system = "You are a helpful assistant that answers questions using only the provided document context. If the answer is not in the context, say you could not find that information in the documents provided.",
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )

    return response.content[0].text
    