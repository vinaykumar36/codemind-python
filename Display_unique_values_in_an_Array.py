n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in l:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
for i in a:
    if i not in b:
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)
