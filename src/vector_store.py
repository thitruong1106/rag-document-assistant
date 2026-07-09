"""
Storing chunks in ChromaDB and searching them 
"""

"""
Function 1 

Take a list of chunks, (output from load_chunk)
Create a chromaDB collection and add all the chunks to it 
return the collection so you can search it later 

Each chun
"""

import chromadb

def store_chunks(chunks):
    # create client (local, not cloud)
    # create collection
    # generate ids
    # add chunks with ids
    # return collection

    #create a database 
    client = chromadb.Client() 

    #create collection (table)
    collection = client.create_collection("my_first_documents")
    
    #generate id 
    ids = [f"chunks_{i}" for i in range(len(chunks))]

    #add chunks 
    collection.add(
        documents=chunks, 
        ids=ids
    )

    return collection
def search_chunks(collection, question):
    # query the collection with the question
    # return top 3 results
    results = collection.query(
        query_texts=[question], 
        n_results = 3
    )
    return results 
