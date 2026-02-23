import spacy
nlp = spacy.load("en_core_web_sm")
sentence = input("Enter sentence: ")
doc = nlp(sentence)
def print_tree(token, level=0):
    print("   " * level + "|-- " + token.text + " (" + token.dep_ + ")")
    for child in token.children:
        print_tree(child, level + 1)
for token in doc:
    if token.head == token:
        print_tree(token)
