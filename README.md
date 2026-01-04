# AI LLM Learning Journey 🚀

This repository documents my **hands-on journey in Artificial Intelligence**, focused on **Large Language Models (LLMs)** and the core systems that power modern AI applications such as **embeddings, semantic search, vector databases, and Retrieval-Augmented Generation (RAG)**.

The purpose of this project is to **build AI systems from scratch with deep understanding**, instead of relying on black-box APIs.  
Each folder represents **working, executable code** developed as part of a structured learning plan.

---

## 🎯 Learning Objectives
- Understand how Large Language Models generate text
- Learn how text meaning is represented using embeddings
- Build semantic search systems using vector similarity
- Implement scalable retrieval using vector databases
- Build document-grounded AI systems using RAG

---

## 🗂️ Repository Structure

```

ai-llm-playground/
|-- README.md
|
|-- .gitignore
|
|-- day01_llm_basics/
|   |-- README.md
│   |-- run_llm.py
|
|-- day02_embeddings/
|   |-- README.md
|   |-- embeddings_demo.py
|
|-- day03_semantic_search/
│   |-- README.md
│   |-- semantic_search.py
|
|-- day04_vector_db/
│   |-- README.md
│   |-- faiss_demo.py
|
|-- day05_rag_pdf/
|   |-- README.md
│   |-- load_pdf.py
│   |-- chunk_text.py
│   |-- embedded_chunks.py
│   |-- rag_retrieval.py

```

Each folder contains:
- Python source code
- A dedicated README explaining:
  - Objective
  - Implementation approach
  - Key concepts learned
  - Outcome

---

## 📘 Progress So Far

### ✅ Day 01 – LLM Basics
**Focus:** Understanding how LLMs generate text  

- Ran a pretrained LLM locally
- Learned token-based text generation
- Compared CPU vs GPU execution
- Verified GPU usage with CUDA

**Key Takeaway:**  
LLMs predict the next token probabilistically; GPUs improve speed, not intelligence.

---

### ✅ Day 02 – Embeddings & Semantic Similarity
**Focus:** Representing text meaning numerically  

- Generated sentence embeddings
- Compared sentences using cosine similarity
- Verified semantic similarity through vector distance

**Key Takeaway:**  
Embeddings capture meaning and are the foundation of modern AI systems.

---

### ✅ Day 03 – Semantic Search
**Focus:** Meaning-based document retrieval  

- Built a semantic search system
- Ranked documents using embedding similarity
- Compared keyword search vs semantic search

**Key Takeaway:**  
Semantic search retrieves information by meaning, not exact words.

---
### ✅ Day 04 – Vector Databases (FAISS)
**Focus:** Scalable vector-based retrieval  

- Earliar --> Text → Embeddings → Similarity → Ranking → (Later) Generation
- Updated --> Text → Tokens → Embeddings → Vector Index (FAISS) → Nearest Vectors → Relevant Context → (Later) LLM Generation

- Generated embeddings for text documents
- Built a FAISS vector index to store embeddings
- Performed fast nearest-neighbor search using FAISS
- Retrieved relevant documents based on semantic similarity
- Compared FAISS-based retrieval with manual similarity search

**Key Learning:**
- Vector databases store embeddings, not raw text
- FAISS enables fast and scalable similarity search
- Indexing is critical for large-scale AI systems
- FAISS is a core retrieval component in RAG pipelines

---

### ✅ Day 05 – PDF-based Retrieval-Augmented Generation (RAG)
**Focus:** Document-grounded question answering  

- Extracted text from a real subject PDF
- Chunked content for semantic retrieval
- Generated embeddings and stored them in FAISS
- Retrieved relevant content for user queries
- Generated accurate answers using an instruction-tuned local LLM

**Key Takeaway:**  
RAG combines retrieval and generation to reduce hallucinations and improve answer reliability.

---

## 🧠 System Architecture (High Level)

PDF → Text → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer



This pipeline reflects how:
- Enterprise AI assistants
- Document Q&A systems
- ChatGPT-with-your-data solutions work internally

---

## ⚙️ Technologies Used
- Python
- Hugging Face Transformers
- sentence-transformers
- FAISS
- PyTorch
- CUDA
- scikit-learn
- FAISS (Facebook AI Similiarity Search)
  
---

## 📌 Why This Repository Exists
This repository is intentionally built as a **learning-first engineering project**.

It demonstrates:
- Strong fundamentals
- System-level thinking
- Progressive AI skill development
- Ability to reason about how AI systems work internally

---

## 🚀 What’s Next
- Improve RAG answer quality
- Add evaluation and tuning
- Build conversational RAG with memory
- Introduce AI agents and tool usage
- Prepare production-ready APIs

---

## 🧾 Summary
> Building modern AI systems from the ground up — from LLM basics to Retrieval-Augmented Generation.
