from transformers import pipeline
import torch

device= 0 if torch.cuda.is_available() else -1
print("Using Device:", "GPU" if device == 0 else "CPU")


generator = pipeline("text-generation", model="gpt2", device= device)

prompt = "Today date is "
output = generator(prompt, max_length=50)

print(output[0]["generated_text"])

