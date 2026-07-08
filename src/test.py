text = "The company reported strong Q3 results with revenue of 2.3 million dollars. Operating costs were reduced by 15 percent compared to the previous quarter. Customer acquisition increased by 22 percent driven by the new marketing campaign. The Sydney office expanded to 45 employees. Employee satisfaction scores reached an all time high of 4.6 out of 5. The board approved a new AI initiative to automate customer support workflows. Initial testing showed a 30 percent reduction in response times. The company plans to roll out the system across all departments by Q1 next year. International expansion into New Zealand is under review. The legal team flagged potential compliance requirements that need to be addressed before launch."

sentences = text.split('. ')

chunks = []
current_chunk = ""

# write your for loop here
for sentence in sentences: 
    if len(current_chunk) + len(sentence) < 500: 
        current_chunk += sentence +  '. '
    else: #over 500 char, so where would the current setnece go 
        #append the first chunk 
        chunks.append(current_chunk)
        #then create new chunk with that current sentence 
        current_chunk = sentence + '. '
#leftover sentence. append to chunks 
chunks.append(current_chunk)

print(chunks)
