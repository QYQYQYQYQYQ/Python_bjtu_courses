#排序 authored by 邱烨卿-19271222
ls = []#升序排序数组
ls_ = []#降序排序数组
for i in range(5):
    num = eval(input())
    ls.append(num)
    ls_.append(num)
for i in range(5):
    for j in range(i,5):
        if ls[i] > ls[j] :
            ls[i] , ls[j] = ls[j] , ls[i]
        else :
            ls_[i] , ls_[j] = ls_[j] , ls_[i]
print("升序排序：",end="")
for i in range(5):
    print(ls[i],end=" ")
print("\n降序排序：",end="")
for i in range(5):
    print(ls_[i],end=" " )
print()