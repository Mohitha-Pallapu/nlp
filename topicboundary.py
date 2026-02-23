import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
train_sentences = [
    "Machine learning is a part of AI.",
    "It uses data for training models.",
    "Neural networks are powerful models.",
    
    "Mumbai is a city in India.",
    "It is famous for Bollywood.",
    "Tourism is growing in Mumbai."
]
pair_labels = [0, 0, 1, 0, 0]  
def create_pairs(sentences):
    pairs = []
    for i in range(len(sentences)-1):
        pairs.append(sentences[i] + " " + sentences[i+1])
    return pairs

train_pairs = create_pairs(train_sentences)
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X_train = vectorizer.fit_transform(train_pairs)
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, pair_labels)
test_sentences = [
    "Deep learning is a subset of ML.",
    "It uses neural networks.",
    
    "Chennai is another big city in India.",
    "It has beautiful beaches."
]

test_pairs = create_pairs(test_sentences)
X_test = vectorizer.transform(test_pairs)

predictions = model.predict(X_test)

print("Topic Boundary Detection:\n")

print(test_sentences[0])
print("Topic Boundary\n")   # First sentence always boundary

for i in range(len(predictions)):
    print(test_sentences[i+1])
    print("Topic Boundary\n" if predictions[i] == 1 else "Same Topic\n")
#   output:
# Topic Boundary Detection:

# Deep learning is a subset of ML.
# Topic Boundary

# It uses neural networks.
# Same Topic

# Chennai is another big city in India.
# Topic Boundary

# It has beautiful beaches.
# Same Topic
