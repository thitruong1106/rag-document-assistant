
def load_and_chunk(file): 
    with open(file, 'r', encoding='utf-8') as f: 
        text_file = f.read() 
        sentences = text_file.split('.')
        
        chunk = [] 
        current_sentence = "" 

        for sentence in sentences: 
            #Check if current sentence we are processing + current_sentence is under 500 char 
            if len(current_sentence) + len(sentence) < 500: 
                #if under 500 len, then add the sentence being loop to current sentence 
                current_sentence += sentence + ". "
            else: #if its over 500 char then, append to chunk 
                chunk.append(current_sentence)
                #Then what do we do we the current sentence being looped, but doesnt fit in ? 
                current_sentence = sentence + '. '
        chunk.append(current_sentence)
        return chunk

print(load_and_chunk('test.txt'))        