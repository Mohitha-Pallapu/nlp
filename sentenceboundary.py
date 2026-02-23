import re
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
train = "Dr. Smith went home. He met Mr. Rao. It was 5 p.m. He slept."
abbrev = {"dr", "mr", "ms"}
def extract(text):
    X, y, pos = [], [], []
    for i in range(1, len(text)-2):
        if text[i] == '.':
            prev = re.findall(r'\b\w+\b', text[:i])[-1].lower()
            is_pm = text[max(0,i-3):i+1].lower() == "p.m."
            
            feat = {
                "capital_next": text[i+2].isupper(),
                "abbrev": prev in abbrev,
                "pm": is_pm
            }
            
            X.append(feat)
            y.append(1 if feat["capital_next"] and not feat["abbrev"] and not feat["pm"] else 0)
            pos.append(i)
    return X, y, pos

vec = DictVectorizer()
X_train, y_train, _ = extract(train)
model = LogisticRegression().fit(vec.fit_transform(X_train), y_train)
test = "Dr. Rao lives in Mumbai. He works at TCS. He is smart."

X_test, _, positions = extract(test)
X_test_vec = vec.transform(X_test)
pred = [
    1 if f["capital_next"] and not f["abbrev"] and not f["pm"] else 0
    for f in X_test
]
print("\nDetected Sentences:\n")
start = 0
for p, label in zip(positions, pred):
    if label == 1:
        print(test[start:p+1].strip())
        start = p+1

if start < len(test):
    print(test[start:].strip())
# #output: Detected Sentences:

# Dr. Rao lives in Mumbai.
# He works at TCS.
# He is smart.
