text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Normalize and split words
words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

common_words = words1 & words2
similarity_percentage = len(common_words) / len(words1 | words2) * 100

print(f"Kopīgie vārdi: {common_words}")
print(f"Sakritības procents: {similarity_percentage:.2f}%")
