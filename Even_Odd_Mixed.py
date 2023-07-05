n=int(input())
c=[]
a=[]
b=[]
while n:
    d=n%10
    n=n//10
    c.append(d)
    if d%2==0:
        a.append(d)
    else:
        b.append(d)
if c==a:
    print("Even")
elif c==b:
    print("Odd")
else:
    print("Mixed")