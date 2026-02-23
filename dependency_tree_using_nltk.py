from nltk.parse import DependencyGraph

# CoNLL format: Word, POS, Head (index of parent), Relation
conll_data = """
The     DT  2   det
cat     NN  3   nsubj
sat     VBD 0   ROOT
on      IN  3   prep
the     DT  7   det
table   NN  4   pobj
"""

graph = DependencyGraph(conll_data)
tree = graph.tree()
print(tree)
tree.pretty_print()
# #output:(sat (cat The) (on table))
#     sat      
#   ___|____    
# cat       on 
#  |        |   
# The     table
