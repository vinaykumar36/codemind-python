n=int(input())
a=str(n)
b=a[::-1]
c=int(b)
e=[]
g=[]
j=1
while c:
    d=c%10
    c=c//10
    e.append(d)
for i in e:
    f=i**j
    g.append(f)
    j+=1
if sum(g)==n:
    print("True")
else:
    print("False")