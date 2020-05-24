#authored by 邱烨卿-19271222
import random
f1 = open("形容词库.txt","r")
f2 = open("名词库.txt","r")
f3 = open("动词库.txt","r")
t1 = (f1.readline()).split(" ")
t2 = (f2.readline()).split(" ")
t3 = (f3.readline()).split(" ")
num1 = random.randint(0,2)
num2 = random.randint(0,2)
num3 = random.randint(0,2)
num4 = random.randint(0,2)
print(t1[num1]+t2[num2]+t3[num3]+t2[num4])