from transformers import pipeline

prompt = "Reiz kādā tālā zemē..."
generator = pipeline("text-generation", model="gpt2")

story = generator(prompt, max_length=500, num_return_sequences=1, truncation=True)

print("Ģenerētais stāsts:")
print(story[0]['generated_text'])
