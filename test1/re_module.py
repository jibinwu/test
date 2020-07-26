import re
# a='life is short,i use python'
# result=re.match('life(.*)i(.*)python',a)
# print(result.groups())
# print(result.group(0,1,2))

import json
# json的2种数据类型： object（对象） array（数组）
a='[{"name":"jbw","age":18,"flag":false},{"name":"zxy","age":18,"flag":true}]'  # json array
b='{"name":"jbw","age":"18"}'  # json object
# json.loads() 把json字符串转换成python语言的数据结构，叫反序列化
# json.dumps() 序列化
result1=json.loads(a)  # 把json数组转换成python中的列表（list）
result2=json.loads(b)  # 把json对象转换成python中的字典（dict）
print(type(result1),result1)
print(type(result2),result2)



