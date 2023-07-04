n=int(input())
a=[]
b=[]
while n:
    d=n%10
    n=n//10
    a.append(d)
for i in a:
    if i not in b:
        b.append(i)
if a==b:
    print("Unique Number")
else:
    print("Not Unique Number")
    
