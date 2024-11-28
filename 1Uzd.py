from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# Normalize text
words = text.lower().split()
word_counts = Counter(words)

print("Vārdu biežums:")
print(word_counts)
