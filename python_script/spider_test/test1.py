import requests
import re
from bs4 import BeautifulSoup
url='http://www.santostang.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
         'Host':'www.santostang.com'
         }
r=requests.get(url,headers=headers)
print(r.request.headers)
# print(r.text)
'''正则表达式提取标题'''
# result=re.findall(r'<h1 class="post-title"><a href=.*>(.*)</a></h1>',r.text)
# print(result)
# soup=BeautifulSoup('r.text','html.parser')
# print(soup)
# res=soup.find_all("h1",class_="post-title" )
# print(res)














