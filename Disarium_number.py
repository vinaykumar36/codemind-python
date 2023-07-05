n=int(input())
a=str(n)
b=a[::-1]
c=int(b)
i=1
f=[]
while c:
    d=c%10
    c=c//10
    e=d**i 
    i+=1
    f.append(e)
if sum(f)==n:
    print("True")
else:
    print("False")
