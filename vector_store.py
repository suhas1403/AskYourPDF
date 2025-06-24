import faiss
from sklearn.preprocessing import normalize
import numpy as np

def build_faiss_index(embedded_chunks):
    texts = [text for text, _ in embedded_chunks]
    embeddings = np.array([emb for _, emb in embedded_chunks])
    norm_embeddings = normalize(embeddings, axis=1)
    dim = norm_embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(norm_embeddings)
    return index, texts
