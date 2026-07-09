chunks = [
    "Sydney expansion approved in Q3.",
    "Sydney budget increased.",
    "Melbourne office delayed.",
    "Budget meeting scheduled.",
    "Sydney hiring and budget planning started."
]

def score_chunks(chunks, question): 
    """
    1. take a list of chunks 
    2. take a question with multiple words 
    3. count how man question word appear in each count 
    return a list of dictoinaru, showing each chunk and its score 
    
    """
    result = [] 
    words = question.lower().split() #split each word into its own 

    for chunk in chunks: 
        score = 0 #current counted for word 

        for word in words: 
            if word in chunk.lower(): 
                score += 1 
        
        result.append({
            "chunk": chunk, 
            "score": score
        })
    return results 

        
results = score_chunks(chunks, "Sydney budget")
print(results)