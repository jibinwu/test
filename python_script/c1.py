# import requests

#1.示例

# url="http://httpbin.org/get"
# data={"name":"jibinwu","age":"24"}
# r=requests.get(url,params=data)
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(r.content)

#2.保存获取到的图片

# r=requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)
# with open(r"C:\favicon.ico","wb") as f:
#     f.write(r.content)

#3.文件上传

# files={"file":open("favicon.ico","rb")}
# r=requests.post("http://httpbin.org/post",files=files)
# print(r.text)
# print(r.content)

#4.Cookies
# r=requests.get("https://www.baidu.com")
# print(r.text)
# print(r.encoding)
# print(r.headers)
# print(r.status_code)
# print(r.url)
# print(r.request)
# print(r.content)
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+"="+value)

#cookies

# headers={'cookie':'tgw_l7_route=116a747939468d99065d12a386ab1c5f; _zap=684fbd57-b6f9-4ab3-b0ca-e927e15011ec;'
#                   ' _xsrf=0LkqjScML7TLZ4NUeKYMQ7YXEjAg9pTK; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569425642; '
#                   'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569425642; d_c0="ANDmTV1XGhCPTtIMlyCRZRkyMj8N_OynvX4=|156'
#                   '9425639"; capsion_ticket="2|1:0|10:1569425639|14:capsion_ticket|44:MzM4MzE3M2FkMGEyNDliYjljNmIyMDlmO'
#                   'GM2ZDdjODE=|d55773f08bfd81fcfb5799ea97c2be46b31aba3df785d4a31c9e18355bf93a5c"; z_c0="2|1:0|10:156942'
#                   '5722|4:z_c0|92:Mi4xdGRtbkNRQUFBQUFBME9aTlhWY2FFQ1lBQUFCZ0FsVk5PdGQ0WGdBTnJ1bWRBX0hNd1hMMWlBcjl5Z2FZZ'
#                   'zZVOGR3|e4fd32ff876790167023a2a0652bf7659b4a3d678dd87509be3f87c5dd2b609b"; unlock_ticket="AFAiH1Bdp'
#                   'A0mAAAAYAJVTUKQi11ojNJjbPI_KF4UP92TTFsbcESurQ=="',
#          'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.38'
#                       '65.90 Safari/537.36',
#
#
#          }
# r=requests.get("https://www.zhihu.com",headers=headers)
# print(r.text)

#session会话维持

# s=requests.session()
# s.get("http://httpbin.org/cookies/set/number/1234567")
# r=s.get("http://httpbin.org/cookies")
# print(r.text)
#
# requests.get("http://httpbin.org/cookies/set/number/1234567")
# r=requests.get("http://httpbin.org/cookies")
# print(r.text)

# r=requests.get("https://www.12306.cn",verify=False )
# print(r.status_code)
import requests
headers={"Cookie":"__mta=88913572.1569430886797.1569431000099.1569431137712.6; _lxsdk_cuid=16d693c9fa74a-0a855b2940eb1"
                  "a-28792744-1c390-16d693c9fa8c8; uuid_n_v=v1; uuid=1AD3A270DFB611E9BE90070FE55B51FA028E43E93F5148B181"
                  "7175DE1B52AEEF; _csrf=1bfebf609aab86dcbfbe3fa3f78c65d6bfc706aa9194707dc384a18034b358c5; _lxsdk=1AD3A"
                  "270DFB611E9BE90070FE55B51FA028E43E93F5148B1817175DE1B52AEEF; _lxsdk_s=16d695ed96d-ec2-0ef-d0b%7C%7C"
                  "12",
         "Host":"maoyan.com",
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.262"
                      "3.221 Safari/537.36 SE 2.X MetaSr 1.0",
         }
r=requests.get("http://maoyan.com/board/4",headers=headers)
print(r.text)





