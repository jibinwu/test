import requests
def test_login():
    r=requests.post(url='https://cms.mamaqunaer.com/user/login',
                  data={"loginCode":"测试-季彬武","loginPassword":"123456a"},
                                    )

    print('status_code:'+str(r.status_code))
    print(r.url)
    print(r.headers)
    print(r.json())