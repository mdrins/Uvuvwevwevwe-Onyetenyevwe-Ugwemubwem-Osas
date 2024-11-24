from transformers import pipeline

texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-lv-en")

for text in texts:
    translation = translator(text)[0]['translation_text']
    print(f"Teksts: '{text}' -> Tulkojums: '{translation}'")
