n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=len(str(i))
    b.append(a)
print(b.count(min(b)))