#porter stremmer algorithm
words=['swimming','played','cats','happily']
def porter(word):
    suffixes=['ing','ed','s','ly']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
stems =[porter(w) for w in words]
print(stems)
