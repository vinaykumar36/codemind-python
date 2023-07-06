n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        a.append(sum(l[i:j+1]))
b=max(a)
print(b)