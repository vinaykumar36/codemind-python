n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=i*i
    b.append(a)
b.sort()
print(*b)
    