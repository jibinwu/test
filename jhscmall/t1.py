import  os
import sys
import time
import urllib

# file=r'C:\Users\Administrator\PycharmProjects\test\jhscmall\login.py'
file=r'C:\Users\user\PycharmProjects\test\jhscmall\login.py'
# print(os.path.basename(file))
# print(os.path.dirname(file))
# print(os.path.split(file))

# print(os.path.getatime(file))
# print(os.path.getmtime(file))
# print(os.path.getctime(file))
# print(time.gmtime(os.path.getmtime(file)))

# ll=os.listdir(os.path.dirname(file))
# a=[]
# for i in ll:
#     a.append(i)
#     print(i)
# print(a)
# print(os.path.abspath(__file__))
# ll=os.path.split(os.path.abspath(__file__))
# print(ll)
# print(ll[1])
print(os.listdir(os.path.dirname(file)))
print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.join(os.path.dirname(__file__),'report'))
# print(os.path.basename(__file__))
# curPath=os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# print(os.path.split(curPath))

# print(time.localtime())
# print(time.struct_time(time.localtime()))
# print(os.getcwd())
# print(os.path.dirname(__file__))
# print(sys.platform)
# print(os.path.dirname(__file__))
# print(os.getcwd())
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
