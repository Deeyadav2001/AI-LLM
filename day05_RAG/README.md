## Day 05 – PDF-based Retrieval-Augmented Generation (RAG)

### Objective
To build an end-to-end Retrieval-Augmented Generation (RAG) system that answers user questions using knowledge extracted from a real PDF document.

---

### What I Built
- Loaded and extracted text from a subject PDF
- Split the content into meaningful text chunks
- Converted chunks into vector embeddings using a local transformer model
- Stored embeddings in a FAISS vector database
- Retrieved relevant chunks for a user query
- Generated accurate, grounded answers using an instruction-tuned local LLM

---

### System Flow
PDF → Text → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer


---

### Key Concepts Learned
- Retrieval-Augmented Generation (RAG) reduces hallucination by grounding LLM answers in external data
- Chunking strategy directly impacts retrieval and answer quality
- Vector databases enable fast semantic search at scale
- Instruction-tuned models are required for reliable question answering
- Retrieval happens internally; users see only clean answers

---

### Technologies Used
- Python
- pypdf
- sentence-transformers
- FAISS
- Hugging Face Transformers (FLAN-T5)

---

### Outcome
Built a working PDF-based AI assistant capable of answering questions accurately using document-grounded knowledge instead of memorized or hallucinated responses.