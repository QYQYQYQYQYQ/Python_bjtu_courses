n=input()
nn=[]
nn=n.split()
a=eval(nn[0])
b=eval(nn[1])
c=eval(nn[2])
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)