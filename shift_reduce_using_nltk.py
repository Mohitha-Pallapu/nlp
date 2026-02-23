import nltk
from nltk import CFG
from nltk.parse import ShiftReduceParser

# Define grammar
g = CFG.fromstring("""
S  -> NP VP
NP -> DT NN
VP -> V NP
DT -> 'the'
NN -> 'boy' | 'ball'
V  -> 'hit'
""")

# Create parser with trace enabled
p = ShiftReduceParser(g, trace=2)

# Input sentence
s = "the boy hit the ball".split()

# Parse (this will print SR actions automatically)
for tree in p.parse(s):
    print("\nFinal Parse Tree:\n")
    tree.pretty_print()
#   #output:Parsing 'the boy hit the ball'
#     [ * the boy hit the ball]
#   S [ 'the' * boy hit the ball]
#   R [ DT * boy hit the ball]
#   S [ DT 'boy' * hit the ball]
#   R [ DT NN * hit the ball]
#   R [ NP * hit the ball]
#   S [ NP 'hit' * the ball]
#   R [ NP V * the ball]
#   S [ NP V 'the' * ball]
#   R [ NP V DT * ball]
#   S [ NP V DT 'ball' * ]
#   R [ NP V DT NN * ]
#   R [ NP V NP * ]
#   R [ NP VP * ]
#   R [ S * ]

# Final Parse Tree:

#              S              
#       _______|___            
#      |           VP         
#      |        ___|___        
#      NP      |       NP     
#   ___|___    |    ___|___    
#  DT      NN  V   DT      NN 
#  |       |   |   |       |   
# the     boy hit the     ball
