#local RAG
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = open("data/docs.txt").read().split("\n")
embeddings = model.encode(docs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))


def retrieve(query, k=3):
    q_emb = model.encode([query])
    distances, indices = index.search(np.array(q_emb), k)
    return [docs[i] for i in indices[0]]