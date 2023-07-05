n=int(input())
a=[]
b=1
while n:
    d=n%10
    n=n//10
    a.append(d)
    b=d*b
c=sum(a)
if c==b:
    print("Spy Number")
else:
    print("Not Spy Number")