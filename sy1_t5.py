# authored by 邱烨卿-19271222
from bs4 import BeautifulSoup
import requests
my_web=requests.get('https://qyqyqyqyqyq.top')
# 创建requests对象my_web
file = open('myweb.html','wb')
for line in my_web.iter_content():
    file.write(line)
file.close()
# 将网站的源代码写入myweb.html并保存在本地
web = open('myweb.html','r').read()
#print(web)
soup = BeautifulSoup(web,"html.parser")
#将本地的html文件读取并转化为beautifulsoup对象soup
lis = soup.find_all('img')
urllist=[]
for i in range(len(lis)):
    print(lis[i].attrs['src'])
#输出所有img标签中的链接，即博客主页中所有图片的链接
'''
这个程序是爬取我自己的个人博客主页https://qyqyqyqyqyq.top
图片地址，并且输出在终端之中，也欢迎老师拜访我的博客
'''