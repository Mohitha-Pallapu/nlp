from sklearn.linear_model import LogisticRegression

m=LogisticRegression().fit([[0],[1]],[0,1])
s=["AI is powerful","Machine learning improves AI","Football is popular","The match was exciting"]

t=1;print("TOPIC",t,":");print(s[0])
prev=1

for i in range(1,len(s)):
    o=len(set(s[i-1].split())&set(s[i].split()))>0
    if prev and not o and m.predict([[1]])[0]:
        t+=1;print("\nTOPIC",t,":")
    print(s[i]);prev=o
