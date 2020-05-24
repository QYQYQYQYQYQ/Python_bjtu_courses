n = eval(input())
s = input()
a = []
a = s.split(" ")
for t in range(n):
    minnum = 2147483648
    for i in a:
        if eval(i) < minnum:
            minnum = eval(i)
            minnum_ = i
    a.remove(minnum_)
    print(minnum,end=" ")