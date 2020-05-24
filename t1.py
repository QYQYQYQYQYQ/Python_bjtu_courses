n = eval(input())
cnt1 = 0
cnt2 = 0
summ = 0
cnt = 0
while n != 0:
    if n > 0:
        cnt1+=1
    if n < 0:
        cnt2+=1
    summ+=n
    cnt+=1
    n=eval(input())
print(summ/cnt)
print(cnt1)
print(cnt2)