from load_pdf import load_pdf_text
from chunk_text import chunk_text
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

if __name__ == "__main__":
    print("EMBEDDING SCRIPT STARTED")

    PDF_PATH = r"data/Business-Intelligence-notes.pdf"

    pages = load_pdf_text(PDF_PATH)

    all_chunks = []
    for page in pages:
        all_chunks.extend(chunk_text(page))

    print(f"Total chunks to embed: {len(all_chunks)}")

    # Load local embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    embeddings = model.encode(all_chunks, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save FAISS index and chunks
    faiss.write_index(index, "faiss_index.index")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    print("FAISS index and chunks saved successfully")
