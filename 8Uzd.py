import spacy

# Ielādē latviešu valodas modeli
try:
    nlp = spacy.load("lv_core_news_sm")
except OSError:
    print("Latviešu valodas modelis nav instalēts. Lūdzu, instalējiet to ar komandu:")
    print("python -m spacy download lv_core_news_sm")
    exit()

# Teksts ievadei
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Apstrādā tekstu
doc = nlp(text)

# Izdrukā identificētās vienības
print("Atpazītās īpašās vienības:")
for ent in doc.ents:
    if ent.label_ in ["PER", "ORG"]:  # PER - personvārdi, ORG - organizācijas
        print(f"{ent.text} -> {ent.label_}")
