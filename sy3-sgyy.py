#authored by 19271222-邱烨卿
import jieba
f1 = open("三国演义.txt",encoding='utf-8')
wb = f1.read()
words = jieba.lcut(wb)
delete_ls=(open("三国演义屏蔽词语表.txt",encoding='utf-8').readline()).split()
#干扰词的屏蔽列表
sum={}
#统计单词出现次数的字典类型
for s in words:
    flag=False
    for dltwd in delete_ls:
        if s==dltwd:
            flag=True
    if flag:
        continue
    if len(s)<=1:
        continue
    else:#某些特殊词语的重定向与统计
        if s=="玄德曰" or s=="玄德":
            sum["曹操"]=sum.get("曹操",0)+1
        elif s=="孔明曰":
            sum["孔明"]=sum.get("孔明",0)+1
        elif s=="云长" or s=="关公":
            sum["关羽"]=sum.get("关羽",0)+1
        elif s=="都督":
            sum["周瑜"]=sum.get("周瑜",0)+1
        else:
            sum[s]=sum.get(s,0)+1
ls=list(sum.items())
ls.sort(key=lambda x:x[1],reverse=True)#以ls列表的1号元素作为关键字进行从大到小的排序
for i in range(10):
    print("No.{}   {} {}次".format(i+1,ls[i][0],ls[i][1]))
 