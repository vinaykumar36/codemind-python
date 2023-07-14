n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=str(i)
    c=list(a)
    b.append(len(c))
d=0
for i in b:
    if i%2==0:
        d+=1
print(d)