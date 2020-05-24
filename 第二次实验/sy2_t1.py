#字符串处理 authored by 邱烨卿-19271222
s = input()
n=eval(input())
letter=[]
Letter=[]
num=[]
for i in range(26):
    letter.append(0)
    Letter.append(0)
for i in range(10):
    num.append(0)
sum_letter = 0
sum_space = 0
sum_other = 0
sum_num=0
for i in s:
    if i >= 'a' and i <= 'z' :
        sum_letter += 1
        letter[ord(i)-ord('a')] += 1
    elif i >= 'A' and i <= 'Z':
        sum_letter += 1
        Letter[ord(i)-ord('A')] += 1
    elif i == ' ':
        sum_space += 1
    elif i >= '0' and i <= '9':
        sum_num += 1
        num[ord(i)-ord('0')]+=1
    else:
        sum_other += 1
print(sum_letter,sum_space,sum_space,sum_other)
for i in range(26):
    if(letter[i] != 0):
        print(chr(ord('a')+i)+'出现了{}次'.format(letter[i]))
for i in range(26):
    if(Letter[i] != 0):
        print(chr(ord('A')+i)+'出现了{}次'.format(Letter[i]))
for i in range(10):
    if(num[i] != 0):
        print(chr(ord('0')+i)+'出现了{}次'.format(num[i]))
print("出现两次的字母有:",end="")
for i in range(26):
    if letter[i] == 2 :
        print(chr(ord('a')+i),end="")
    if Letter[i] == 2 :
        print(chr(ord('A')+i),end="")
print()
print("出现{}次的数字有:".format(n),end="")
for i in range(10):
    if num[i] == n:
        print(i,end="")
print()