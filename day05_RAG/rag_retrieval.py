import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("faiss_index.index")

# Load stored chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load local LLM
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=180
)

def retrieve_relevant_chunks(query, k=3):
    query_embedding = embed_model.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]

def generate_answer(query):
    retrieved_chunks = retrieve_relevant_chunks(query)

    # Context is used internally ONLY
    context_text = " ".join(retrieved_chunks)

    prompt = f"""
Answer the question strictly based on the information provided.

Question:
{query}

Answer:
"""

    # Inject context silently
    full_prompt = context_text + "\n\n" + prompt

    output = generator(full_prompt)
    answer = output[0]["generated_text"]

    # Clean final answer
    return answer.split("Answer:")[-1].strip()

if __name__ == "__main__":
    question = "What is Business Intelligence?"
    answer = generate_answer(question)

    print("Q:", question)
    print("\nA:", answer)
