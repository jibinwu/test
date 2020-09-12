import requests
import pytest
import json
def test_login():
    r=requests.post(url='https://cms.mamaqunaer.com/user/login',
                    data={"loginCode":"测试-季彬武","loginPassword":"123456a",},
                    # proxies={'https':'127.0.0.1:8888'},
                    verify=False)

    # print('status_code:'+str(r.status_code))
    # print(r.url)
    # print(r.headers)
    print(type(r.json()))
    print(r.headers['Set-Cookie'])
    print(r.cookies)
    return  r.headers['Set-Cookie']

def test_get():
    url='https://cms.mamaqunaer.com/shop/list'
    cookies=test_login()
    headers={'Host':'cms.mamaqunaer.com',
             # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
             'Cookie':cookies,
             }
    r=requests.get(url=url,
                   headers=headers,
                   params={'searchWord':'15058321650'},
                   # proxies={'https':'https://127.0.0.1:8888'},
                   verify=False)
    # print(r.text)
    print(r.json())
    # print(json.dumps(r.json()))
    # print(r.encoding)
    # print(r.status_code)
    # print(r.raise_for_status())
    # print(r.url)
    # print(r.headers['Content-Type'])
    print(r.content)

'''
默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
可以使用响应对象的 history 方法来追踪重定向。
如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理
'''
@pytest.mark.webtest
def test_history():
    r=requests.head('http://cms.mamaqunaer.com',allow_redirects=True)
    print(r.url,r.status_code,r.history)

# def test_timeout():
#     url='https://cms.mamaqunaer.com/order/list'
#     headers={'Host':'cms.mamaqunaer.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
#             ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#              'Cookie': 'cms_auth=MjMzQTU1MTYzRUVGQjY1NjZDQjBGNDRCNzY0NEZGMUE='}
#     r=requests.get(url=url,headers=headers,timeout=5,proxies={'https':'127.0.0.1:8888'},verify=False)#本地开启charles，requests库发起的请求被charles拦截
#     if r.status_code==requests.codes.ok:
#         print(r.headers['Content-Type'])
#         print(r.json().keys())