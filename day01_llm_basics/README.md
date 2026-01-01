## Day 01 – Running a Large Language Model Locally

### Objective
To understand how a pretrained Large Language Model (LLM) generates text and how to run it locally using CPU or GPU.

---

### What I Implemented
- Ran a pretrained GPT-2 model using Hugging Face Transformers
- Configured execution to use GPU (CUDA) when available
- Generated text by providing a prompt and controlling output length

---

### Key Concepts Learned
- LLMs generate text by predicting the **next token**, not by understanding meaning
- Text generation happens **token by token**
- GPU improves execution speed but does not affect model intelligence
- Python version and environment setup are critical in AI projects

---

### Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- CUDA (for GPU acceleration)

---

### Outcome
Successfully ran a local LLM and verified GPU usage using PyTorch and `nvidia-smi`.
