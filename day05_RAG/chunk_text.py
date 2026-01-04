from load_pdf import load_pdf_text
import os

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


if __name__ == "__main__":
    print("CHUNKING SCRIPT STARTED")

    PDF_PATH = r"data/Business-Intelligence-notes.pdf"


    pages = load_pdf_text(PDF_PATH)
    print(f"Pages loaded: {len(pages)}")

    all_chunks = []

    for page in pages:
        page_chunks = chunk_text(page)
        all_chunks.extend(page_chunks)

    print(f"Total chunks created: {len(all_chunks)}")

    if all_chunks:
        print("\n--- SAMPLE CHUNK ---\n")
        print(all_chunks[0])
    else:
        print("No chunks created.")