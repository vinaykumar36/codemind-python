n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    b=len(str(i))
    a.append(b)
print(a.count(max(a)))