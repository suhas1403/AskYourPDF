from sentence_transformers import SentenceTransformer
import numpy as np

def embed_chunks(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return list(zip(texts, embeddings))
