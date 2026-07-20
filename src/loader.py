
from pypdf import PdfReader

def extract_text_from_text(file_path): 
    with open(file_path, 'r', encoding='utf-8') as f: 
        text = f.read() 
    return text 

from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    # strict=False lets pypdf attempt to read slightly damaged PDFs
    reader = PdfReader(file_path, strict=False)
    #current an empty string 
    full_text = ""

    for page in reader.pages:
        # extract_text() can return None, so replace None with empty string instead 
        page_text = page.extract_text() or ""

        full_text += page_text + "\n"

    full_text = full_text.strip()

    if len(full_text) < 10:
        raise ValueError(
            "No readable text was found. "
            "The PDF may be blank, scanned, or corrupted."
        )

    return full_text


def load_document(file_path): 
    try: 
    #read the file path extention 
        if file_path.endswith('.pdf'): 
            return extract_text_from_pdf(file_path)
        else: 
            return extract_text_from_text(file_path)
    except FileNotFoundError as error: 
        print(f"File not found error: {error}")
        return None

def chunk_text(text_file): 
    sentences = text_file.split('.')

    chunk = [] #append chunks here 
    current_sentence = "" #its string, so intialise an empty string first 

    for sentence in sentences: 
        if len(current_sentence) + len(sentence) < 500: 
            current_sentence += sentence + ". "
        else:
            chunk.append(current_sentence)
            #current sentence is equal sentence being looped, because its not being appedn to chunk, we are appending to current 
            current_sentence = sentence + ". "
    chunk.append(current_sentence)
    return chunk 