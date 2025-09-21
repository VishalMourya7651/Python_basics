from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# 1. Load pre-trained model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set model to evaluation mode
model.eval()

# 2. Provide a prompt
prompt = "The future of AI is"

# 3. Tokenize input text
inputs = tokenizer(prompt, return_tensors="pt")

# 4. Generate text
output = model.generate(
    inputs['input_ids'],
    max_length=50,          # Max length of output
    num_return_sequences=1, # Number of responses
    no_repeat_ngram_size=2, # Avoid repeating same phrase
    temperature=0.7,        # Controls creativity
    top_k=50,               # Sampling only from top 50
    top_p=0.95,             # Nucleus sampling
    do_sample=True          # Enable randomness
)

# 5. Decode and print output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:\n", generated_text)
