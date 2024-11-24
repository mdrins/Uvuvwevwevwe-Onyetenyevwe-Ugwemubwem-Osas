from gensim.models import KeyedVectors

# Load pretrained word embeddings
model_path = "word2vec.lv.model"  # Piemērs: Gensim Word2Vec modelis
model = KeyedVectors.load(model_path)

words = ["māja", "dzīvoklis", "jūra"]

for word in words:
    vector = model[word]
    print(f"Vektors vārdam '{word}': {vector[:5]}...")

similarity = model.similarity("māja", "dzīvoklis")
print(f"Semantiskā līdzība starp 'māja' un 'dzīvoklis': {similarity:.2f}")
