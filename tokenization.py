#Tokenization
text = input("enter text:")
x=0
tokens=[]
for i in range(0,len(text)):
    if text[i]==" ":
        tokens.append(text[x:i])
        x=i+1
    elif i==len(text)-1:
         tokens.append(text[x:i+1])
print(tokens)
