import fitz
import re
from langchain.text_splitter import CharacterTextSplitter

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        text = re.sub(r'\n{2,}', '\n', text)
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        full_text += text.strip() + "\n"
    return full_text

def chunk_text(text):
    splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
    return splitter.create_documents([text])

# chunked_doc = chunk_text(text)
# for i, chunk in enumerate(chunked_doc):
#     print(f"Chunk {i + 1}: {len(chunk.page_content)} characters")
