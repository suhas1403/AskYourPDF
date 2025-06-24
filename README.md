# 🔍 Local PDF Q&A Chatbot using RAG + Mistral 7B

This project is a private, offline chatbot that answers questions based on PDF documents using **RAG (Retrieval-Augmented Generation)** and a locally-run **Mistral 7B** language model. No external APIs or internet access required!

---

## 🚀 Features

- Upload any PDF file (research paper, project report, documentation, etc.)
- Ask questions and get context-aware answers from the document
- Uses **FAISS** for semantic search and **Mistral 7B** via `llama-cpp-python` for local LLM inference
- Frontend built with **Streamlit**
- Backend served using \*\*FastAPI`

---

## 🧠 Tech Stack

- `FastAPI` – for serving the API
- `Streamlit` – for the frontend UI
- `PyMuPDF (fitz)` – to parse PDF files
- `sentence-transformers` – for embeddings
- `FAISS` – for vector search
- `llama-cpp-python` – for running Mistral 7B locally

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/suhas1403/AskYourPDF.git
cd cd AskYourPDF
```

### 2. Install Dependencies

Make sure you're using Python 3.10+ and ideally create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

(or)

```conda
conda create --name yourenvname python=yourpythonversion(3.10+) #in conda env
conda activate yourenvname
pip install -r requirements.txt
```

### 3. Download Mistral 7B GGUF Model

Download the Mistral 7B Instruct model in `.gguf` format from [TheBloke on Hugging Face](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF). Place the `.gguf` file inside a `models/` directory in the project root:

```
AskYourPDF/
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

Update the model path in `local_llm.py` if needed.

### 4. Run the FastAPI Server

```bash
python main.py (or) python -m uvicorn main:app --reload
```

This will start the backend API at `http://127.0.0.1:8000`.

### 5. Run the Streamlit Frontend

```bash
streamlit run app.py
```

The frontend should open automatically in your browser. If not, visit [http://localhost:8501](http://localhost:8501).

---

## 🧪 API Endpoints

### `POST /upload_pdf`

Upload a PDF file.

**Form Data:**

- `file`: PDF file

### `POST /ask`

Ask a question related to the uploaded PDF.

**Form Data:**

- `question`: Your question

---

## 📝 Project Structure

```
.
├── app.py                # Streamlit frontend
├── main.py               # FastAPI backend
├── pdf_utils.py          # PDF parsing & chunking
├── embedder.py           # Embedding generation
├── vector_store.py       # FAISS index handling
├── query_engine.py       # Semantic search
├── local_llm.py          # Local model inference
├── requirements.txt
└── models/               # GGUF model file goes here
```

---

## 🙌 Acknowledgements

- [Mistral 7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- [TheBloke's GGUF Models](https://huggingface.co/TheBloke)
- [sentence-transformers](https://www.sbert.net/)
- [FAISS by Facebook AI](https://github.com/facebookresearch/faiss)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

---

## 🗨️ Want to Contribute or Collaborate?

Feel free to fork, suggest improvements, or reach out if you want to collaborate on enhancements like:

- Multi-PDF support
- Citations in answers
- Better chunking and context handling
- UI polishing

---

## 🔐 Privacy First

This project runs entirely locally. No data is sent to the cloud. Your documents and questions stay on your machine.

---

## 📸 Demo

![PDF Q&A Chatbot Screenshot](assets/screenshot.png)
