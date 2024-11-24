from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is sunny day", #so? somali??????
    "This day is sunny",
    "day sunny is today"
]

for text in texts:
    language = detect(text)
    print(f"Teksts: '{text}' -> Valoda: {language}")
