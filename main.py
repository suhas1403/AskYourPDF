from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import os
import shutil

from pdf_utils import extract_text_from_pdf, chunk_text
from embedder import embed_chunks
from vector_store import build_faiss_index
from query_engine import answer_query
from local_llm import load_llm, generate_answer

app = FastAPI()

# Global state
INDEX = None
TEXTS = None
MODEL = load_llm()

UPLOAD_DIR = "uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global INDEX, TEXTS
    pdf_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embedded_chunks = embed_chunks(chunks)
    INDEX, TEXTS = build_faiss_index(embedded_chunks)

    return {"message": "PDF processed and indexed successfully"}

@app.post("/ask")
async def ask_question(question: str = Form(...)):
    if INDEX is None or TEXTS is None:
        return JSONResponse({"error": "No PDF uploaded yet"}, status_code=400)

    relevant_chunks = answer_query(question, INDEX, TEXTS)
    answer = generate_answer(MODEL, question, relevant_chunks)

    return {"answer": answer}


