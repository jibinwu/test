import requests
import pytest
import json
def test_login():
    r=requests.post(url='https://cms.mamaqunaer.com/user/login',
                    data={"loginCode":"测试-季彬武","loginPassword":"123456a",},
                    proxies={'https':'127.0.0.1:8888'},
                    verify=False)

    # print('status_code:'+str(r.status_code))
    # print(r.url)
    # print(r.headers)
    print(type(r.json()))
    print(r.headers['Set-Cookie'])
    print(r.cookies)