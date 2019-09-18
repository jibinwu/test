import requests
import time
import random
r=requests.get('http://www.santostang.com/',proxies=)
# print(r.request.headers)

# t=time.ctime()
# t2=time.time()
# t3=time.asctime()
# t4=time.localtime()
#
# print(t,)
# print(t2)
# print(t3)
# print(t4)
starttime=time.time()
t=random.randint(1,5)+random.random()
time.sleep(t)
endtime=time.time()
print(endtime-starttime)


