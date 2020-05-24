yea=eval(input())
tmp=False
if yea%4==0 and yea%100!=0 :
    tmp=True
elif yea%400==0:
    tmp=True
if tmp==True:
    print("是闰年")
else:
    print("不是闰年")
