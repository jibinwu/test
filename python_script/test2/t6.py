import  requests,unittest
import json
# url="https://cms.mamaqunaer.com/user/login"
# res=requests.post(url="https://cms.mamaqunaer.com/user/login",data={"loginCode":"测试-季彬武","loginPassword":"123456a","validateCode":""})
# print(res.status_code)
# print(res.text)

# res=requests.get("https://cms.mamaqunaer.com/item/list/5?searchWord=&pageNo=1&pageSize=10",headers={"Cookie":"supplier_mmcc=099f506b978fe07da65a90c489f6609c6768d5a7; auth=NkRFNDEyQkMxQjM2RkQ1MDkyQTM4ODY1NThDNDY3RTQ=; cms_auth=RUMzNTY3ODdCMTlFQzIyQUQ5NTA1RjExOTcyMkZCQjA=","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})
# print(res.text)

print(json.__all__)
res=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京")
print(res.text)
# print('数据类型:',type(json.loads(res.text)))
# print(res.status_code)
if if __name__ == '__main__':
    unittest.main(verbosity=2)