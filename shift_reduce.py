from nltk.tree import Tree
grammar = [
("S",["S","+","S"]),
("S",["S","*","S"]),
("S",["id"])
]
input_string = ["id","+","id","+","id","$"]
stack = ["$"]
tree_stack=[]
index = 0
print(f"{'stack':25}{'Input':<25} Action")
def try_reduce():
    global stack, tree_stack
    for lhs,rhs in grammar:
        if stack[-len(rhs):]==rhs:
            #create tree node
            children = tree_stack[-len(rhs):]
            new_tree = Tree(lhs,children)
            
            del stack[-len(rhs):]
            del tree_stack[-len(rhs):]
            
            stack.append(lhs)
            tree_stack.append(new_tree)
            return f"Reduce {lhs} -> {''.join(rhs)}"
    return None
while True:
    print(f"{''.join(stack):<25}{''.join(input_string[index:]):<25}",end="")
    reduction = try_reduce()
    if reduction:
        print(reduction)
        continue
    if input_string[index]!="$":
        stack.append(input_string[index])
        tree_stack.append(Tree(input_string[index],[]))
        print(f"Shift {input_string[index]}")
        index +=1
    else:
        break
if stack==["$","S"] and input_string[index]=="$":
    print("\ninput string accepted")
    print("\nparse tree :")
    print(tree_stack[0])
    tree_stack[0].pretty_print()
else:
    print("\ninput string rejected")
  # output:
# stack                    Input                     Action
# $                        id+id+id$                Shift id
# $id                      +id+id$                  Reduce S -> id
# $S                       +id+id$                  Shift +
# $S+                      id+id$                   Shift id
# $S+id                    +id$                     Reduce S -> id
# $S+S                     +id$                     Reduce S -> S+S
# $S                       +id$                     Shift +
# $S+                      id$                      Shift id
# $S+id                    $                        Reduce S -> id
# $S+S                     $                        Reduce S -> S+S
# $S                       $                        
# input string accepted

# parse tree :
# (S (S (S (id )) (+ ) (S (id ))) (+ ) (S (id )))
#          S         
#       ___|_______   
#      S       |   | 
#   ___|___    |   |  
#  S   |   S   |   S 
#  |   |   |   |   |  
#  id  +   id  +   id
#  |   |   |   |   |  
