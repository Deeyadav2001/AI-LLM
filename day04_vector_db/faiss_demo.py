from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


sentences = [
    "Artificial Intelligence is transforming industries",
    "Pizza is one of the most popular fast foods",
    "Machine learning enables systems to learn from data",
    "Deep learning is a subset of machine learning"
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings= model.encode(sentences)


dimension =embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


query = "How is AI useful ?"
query_embeddings = model.encode([query])

#top results
k=2
distance, indices = index.search(query_embeddings,k)

for i in indices[0]:
    print(sentences[i])
