s = input()
a = []
a = s.split(" ")
if a[0]<a[1] and a[1]<a[2]:
    print(a[0]+" "+a[1]+" "+a[2])
if a[0]<a[2] and a[2]<a[1]:
    print(a[0]+" "+a[2]+" "+a[1])
if a[1]<a[2] and a[2]<a[0]:
    print(a[1]+" "+a[2]+" "+a[0])
if a[1]<a[0] and a[0]<a[2]:
    print(a[1]+" "+a[0]+" "+a[2])
if a[2]<a[1] and a[1]<a[0]:
    print(a[2]+" "+a[1]+" "+a[0])
if a[0]<a[1] and a[2]<a[0]:
    print(a[2]+" "+a[0]+" "+a[1])
