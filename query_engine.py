from embedder import embed_chunks
from langchain.text_splitter import CharacterTextSplitter
import numpy as np
from sklearn.preprocessing import normalize

def answer_query(query, index, texts, k=3):
    splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([query])
    embedded = embed_chunks(chunks)
    query_embedding = np.array([emb for _, emb in embedded])
    query_embedding = normalize(query_embedding, axis=1)
    D, I = index.search(query_embedding, k)
    return [texts[i] for i in I[0]]
