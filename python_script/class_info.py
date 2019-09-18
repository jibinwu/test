from xml.dom import minidom

#读取xml元素节点
dom=minidom.parse('test.xml')
root=dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)

#读取xml文本节点
'''dom=minidom.parse('student_info.xml')
root=dom.documentElement
names=root.getElementsByTagName('name')
for i in names :
    print(i.firstChild.data)'''

#读取xml属性节点
dom=minidom.parse('student_info.xml')
root=dom.documentElement
tags=root.getElementsByTagName('login')
for i in tags :
    username=i.getAttribute('username')
    print(username)
    password=i.getAttribute('password')
    print(password)
