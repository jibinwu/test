import requests
import chardet
from  bs4 import  BeautifulSoup

# str_utf8=str.encode('utf-8')
# str1=str_utf8.decode('utf-8')
# print(str1,type(str1))


# str_utf=str.encode('utf-8')
# str1=str_utf.decode('utf-8').encode('gbk')
# print(str1,type(str1))
'''处理网页编码不是utf-8'''
# url='http://w3school.com.cn/'
# r=requests.get(url)
# r.encoding='gb2312'
# soup=BeautifulSoup(r.text,'html.parser')
# title=soup.find('div',id='d1').h2.text
# print(title)


# url='http://www.sina.com.cn/'
# r=requests.get(url)
# after_gzip=r.content
# print('解压后的字符串编码为：',chardet.detect(after_gzip))
# str=after_gzip.decode('utf-8')
# print(str)

# with open(r'C:\Users\user\Desktop\gbk.txt','r') as f:
#     r=f.read()
#     print(r)
#
# with open(r'C:\Users\user\Desktop\utf-8.txt','r',encoding='UTF-8') as f:
#     r=f.read()
#     print(r)
# print("5//3')