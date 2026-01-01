from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model= SentenceTransformer("all-MiniLM-L6-v2")

sentence=[
    "Artificial intelligence is changing the world",
    "AI is transforming industries",
    "I love eating pizza"
    ]

embeddings = model.encode(sentence)

similiarity= cosine_similarity(embeddings)

for i, s in enumerate(sentence):\
    print(i,s)

print("\n Cosine Similiarity Matrix")
print(similiarity)
