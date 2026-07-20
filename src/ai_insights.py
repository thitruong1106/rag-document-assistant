from src.vector_store import search_chunks
from anthropic import Anthropic
from dotenv import load_dotenv 
load_dotenv() 

client = Anthropic()

def answer_question(collection, question): 
    #1. Search for the most relevant chunks, given the parameter of a colelction, and question 
    try: 
        results = search_chunks(collection, question)
    except Exception as error: 
        raise ValueError(f"Document search failed: {error}")
    try: # Try to Get the full list of chunks 
        relavent_chunk = results['documents'][0]
    except (KeyError, TypeError, IndexError) as error : 
        raise ValueError(f"Invalid search error {error}")
    
    #if no chunks were found 
    if not relavent_chunk: 
        return "I could not find any relevant chunks of information in the document"
    
    #Else Join the chunk, into one context string, because the chunks are seprated 
    context = "\n\n".join(relavent_chunk)

    #4. prompt building 
    prompt = f""" 
    Context: 
    {context}

    Question: 
    {question}
    """
    #try to get a connection 
    try: 
    #Send the prompt to claude for retrival     
        response = client.messages.create(
            model = "claude-sonnet-4-6",
            max_tokens=1024, 
            system = "You are a helpful assistant that answers questions using only the provided document context. If the answer is not in the context, say you could not find that information in the documents provided.",
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
    except Exception as error: 
        raise ValueError(f"Claude API request failed: {error}")

    return response.content[0].text #get response results, open ocntent row 0, and get text 
    