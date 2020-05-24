#数学_7 authored by 邱烨卿-19271222
i1 = 2
i2 = 3
j1 = 1
j2 = 2
ans = i1 / j1 + i2 / j2
for i in range(3,21):
    i3 = i1 + i2
    j3 = j1 + j2
    ans += i3 / j3
    i1 = i2
    j1 = j2
    i2 = i3
    j2 = j3
print(ans)