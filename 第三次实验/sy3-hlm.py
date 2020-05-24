#authored by 19271222-邱烨卿
import jieba
f1=open("红楼梦.txt",encoding='gb18030')
wb=f1.read()
words=jieba.lcut(wb)
dlt_ls=(open("红楼梦屏蔽词语表.txt",encoding='utf-8').readline()).split()
sum={}
for s in words:
    flag=False
    for dltword in dlt_ls:
        if s==dltword:
            flag=True
    if flag:
        continue
    if len(s)==1:
        continue
    else:
        if s=="老太太":
            sum["贾母"]=sum.get("贾母",0)+1
        elif s=="凤姐儿":
            sum["凤姐"]=sum.get("凤姐",0)+1
        else:
            sum[s]=sum.get(s,0)+1
ls=list(sum.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    print("No.{}   {} {}次".format(i+1,ls[i][0],ls[i][1]))
 
