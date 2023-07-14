def prime(n):
    if n==1:
        return 0
    elif n==2:
        return 0
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return 1
    return 0

c=int(input())
l=list(map(int,input().split()))

a=[]
b=[]
for n in l:
    if prime(n):
        a.append(n)
    else:
        b.append(n)
c=1
d=1
for i in a:
    c=c*i
for i in b:
    d=d*i
print(abs(c-d))