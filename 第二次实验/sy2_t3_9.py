n = eval(input())
if n <= 100000:
    print(n * 0.1)
elif n <= 200000:
    print(100000 * 0.1 + (n-100000) * 0.075)
elif n <= 400000:
    print(100000 * 0.1 + (200000 - 100000) * 0.075 + (n - 200000) * 0.05)
elif n <= 600000:
    print(100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (n - 400000) * 0.03)
elif n <= 1000000:
    print(100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + (n - 600000) * 0.015)
else:
    print(100000 * 0.1 + (200000 - 100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + (1000000 - 600000) * 0.015 + (n - 1000000) * 0.01)
