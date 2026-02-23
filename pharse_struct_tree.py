#phrase structured tree
#The cat sat on the mat
import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar=CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V PP
PP -> P NP
Det -> 'the' | 'The'
V -> 'sat'
P -> 'on'
N -> 'cat' | 'mat'
""")
parser = ChartParser(grammar)
sentence = "The cat sat on the mat".split()
trees = list(parser.parse(sentence))
if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("sentence not covered by grammar")
# #output: (S
#   (NP (Det The) (N cat))
#   (VP (V sat) (PP (P on) (NP (Det the) (N mat)))))
#              S                     
#       _______|_______               
#      |               VP            
#      |        _______|___           
#      |       |           PP        
#      |       |    _______|___       
#      NP      |   |           NP    
#   ___|___    |   |        ___|___   
# Det      N   V   P      Det      N 
#  |       |   |   |       |       |  
# The     cat sat  on     the     mat
