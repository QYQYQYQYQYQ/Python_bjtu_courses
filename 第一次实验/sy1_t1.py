#authored by 邱烨卿-19271222
f1 = open("text1.txt",'r')
t1 = f1.read()
print(t1)
f1.seek(0)
t2 = f1.readline()
while t2 != "":
    print(t2,end="")
    t2 = f1.readline()
f1.seek(0)
t3 = f1.readline()

print("\n"+t3.replace("Python","java"),end="")
while t3 != "":
    t3 = f1.readline()
    print(t3.replace("Python","java"),end="")