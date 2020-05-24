#数学_8 authored by 邱烨卿-19271222
ans = 100
high = 100
for i in range(10):
    high /= 2
    ans += 2 * high
print(high,ans)