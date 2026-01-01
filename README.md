# AI LLM Learning Journey 🚀

This repository documents my **hands-on learning journey in Artificial Intelligence**, focusing on **Large Language Models (LLMs)** and the core systems that power modern AI applications such as **semantic search, embeddings, and retrieval-based AI systems**.

The goal of this project is to **build strong fundamentals by implementing concepts step by step**, not just using APIs blindly.  
Each section represents **real working code**, written and understood during a structured learning process.

---

## 🎯 Learning Goals
- Understand how Large Language Models generate text
- Learn how AI represents text meaning using embeddings
- Build semantic search systems based on vector similarity
- Gain practical experience with CPU vs GPU execution
- Create a strong foundation for RAG and AI agents

---

## 🗂️ Repository Structure

```
ai-llm-playground/
├── README.md
├── .gitignore
├── day01_llm_basics/
│   ├── README.md
│   └── run_llm.py
├── day02_embeddings/
│   ├── README.md
│   └── embeddings_demo.py
├── day03_semantic_search/
│   ├── README.md
│   └── semantic_search.py
```

Each folder contains:

- A focused Python implementation
- A dedicated README explaining:
  - Objective
  - Core concept
  - Implementation approach
  - Learning outcome
    
---

## 📘 What Has Been Implemented So Far

### ✅ Day 01 – Large Language Model Basics
**Focus:** Text generation using a pretrained LLM  

- Ran a pretrained GPT-2 model locally
- Understood how LLMs generate text token by token
- Controlled execution on CPU vs GPU using PyTorch
- Verified GPU usage using CUDA and `nvidia-smi`

**Key Learning:**
- LLMs predict the next token based on probability
- Tokens are not the same as words
- GPU improves speed, not intelligence
- Environment setup is critical in AI projects

---

### ✅ Day 02 – Embeddings & Semantic Similarity
**Focus:** Understanding text meaning numerically  

- Generated sentence embeddings using a pretrained embedding model
- Compared sentences using cosine similarity
- Verified that semantically similar sentences score higher

**Key Learning:**
- Embeddings are numerical representations of meaning
- Similar meaning → similar vectors
- Cosine similarity measures semantic closeness
- Embeddings are foundational for search, RAG, and recommendations

---

### ✅ Day 03 – Semantic Search
**Focus:** Meaning-based document retrieval  

- Built a simple semantic search system
- Converted documents and user queries into embeddings
- Ranked documents based on semantic similarity
- Demonstrated difference between keyword search and semantic search

**Key Learning:**
- Semantic search retrieves results by meaning, not keywords
- Vector similarity enables modern AI search systems
- Ranking by relevance is a core component of RAG pipelines

---

## 🧠 Conceptual Flow (Big Picture)

Text → Embeddings → Similarity → Ranking → (Later) Generation


This is the same fundamental pipeline used in:
- ChatGPT-style systems
- Document Q&A tools
- Recommendation engines
- Enterprise AI search platforms

---

## ⚙️ Technologies & Tools Used
- Python 3.11
- Hugging Face Transformers
- sentence-transformers
- PyTorch (CPU & GPU)
- CUDA
- scikit-learn

---

## 📌 Why This Repository Exists
This repository is intentionally designed as a **learning journey**, not a polished product.

It demonstrates:
- Conceptual understanding
- Hands-on implementation
- Progressive skill development
- Ability to explain and reason about AI systems

This approach reflects **real AI engineering practice**, where understanding matters more than copying code.

---

## 🚀 What’s Coming Next
- Vector databases (FAISS)
- Retrieval-Augmented Generation (RAG)
- Combining search + LLMs
- AI agents and tool usage
- API-based deployment practices

---

## 🧾 One-Line Summary
> A structured, hands-on journey building foundational AI systems using LLMs, embeddings, and semantic search.

---
