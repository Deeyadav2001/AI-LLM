from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


#load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")

#small document

documents = [
    "Artificial intelligence is transforming healthcare",
    "Machine learning improves business decision making",
    "Deep learning is a subset of machine learning",
    "Pizza is one of the most popular fast foods",
    "AI is used in self-driving cars"
]

# Convert documents to embeddings
doc_embeddings = model.encode(documents)

#query
query = "How is AI used in real life?"

# Convert query to embedding
query_embeddings = model.encode([query])

# Compute similarity between query and all documents
scores = cosine_similarity(query_embeddings,doc_embeddings)[0]

# Rank documents by similarity
ranked_results = sorted(
    zip(documents, scores),
    key=lambda x: x[1],
    reverse=True
)

print("Search Query:", query)
print("\nTop Results:\n")

for doc, score in ranked_results:
    print(f"Score: {score:.4f} | Document: {doc}")
