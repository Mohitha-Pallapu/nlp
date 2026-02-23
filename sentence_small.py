from sklearn.linear_model import LogisticRegression

m=LogisticRegression().fit([[1],[0]],[1,0])
t="Wow! Is this working? Yes it is.".split()
o=[t[0]]

for i in range(1,len(t)):
    if t[i-1][-1] in ".!?" and m.predict([[t[i][0].isupper()]])[0]:
        o.append(t[i])
    else:
        o[-1]+=" "+t[i]

print(o)
