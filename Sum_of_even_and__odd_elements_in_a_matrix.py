r,c=map(int,input().split())
a,b=0,0
for i in range(r):
    l=list(map(int,input().split()))
    for i in l:
        if i%2==0:
            a+=i
        else:
            b+=i
print(a,b)        
            