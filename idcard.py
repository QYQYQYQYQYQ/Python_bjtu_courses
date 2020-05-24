s = input()
cnt = 1
for i in s:
    if (cnt>=7 and cnt <=14):
        print("*",end="")
    else:
        print(i,end="")
    cnt+=1
