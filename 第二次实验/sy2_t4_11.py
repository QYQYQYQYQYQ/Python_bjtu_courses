#绘图_11 authored by 19271222-邱烨卿
n = eval(input())
for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
print("--------分割线--------",end="")
nn = n // 2 + 1
for i in range(nn):
    print(" ",end="")
    for j in range(nn-1-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()
for i in range(nn):
    print("* ",end="")
print()
for i in range(nn):
    print(" ",end="")
    for j in range(i):
        print(" ",end="")
    for j in range(nn-1-i):
        print("* ",end="")
    print()

