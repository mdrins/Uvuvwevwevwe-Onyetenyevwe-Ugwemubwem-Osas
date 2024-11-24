from transformers import pipeline

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

sentiment_analyzer = pipeline("sentiment-analysis")

for sentence in sentences:
    result = sentiment_analyzer(sentence)[0]
    print(f"Teikums: '{sentence}' -> Noskaņojums: {result['label']}, Skala: {result['score']:.2f}")
