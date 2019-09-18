# =1
# print(dir())
# a
from functools import  reduce
list=[1,2,3,4]
f=reduce(lambda x,y:x+y,list)
print(f)
print(__package__)