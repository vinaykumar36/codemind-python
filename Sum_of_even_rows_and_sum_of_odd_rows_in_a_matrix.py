r,c=map(int,input().split())
a=0
b=0
for i in range(r):
    l=list(map(int,input().split()))
    if i%2==0:
        a+=sum(l)
    else:
        b+=sum(l)
print(a,b)