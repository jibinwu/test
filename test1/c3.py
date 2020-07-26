class My:
    name = 'jbw'
    age = 18

    def add(self, x, y):
        self.name=My.name
        self.age=My.age
        summ = x + y
        sss=x-y
        return summ,sss
# a = My()
# b = a.add(1, 2)
# print(b)
# print(a.age)
# print(a.name)

class Student:
    def __init__(self):
        print('我是构造函数哦')
        return 'aa'
        # return None

    def do_homework(self):
        print('我能做作业哦')
# A=Student()
# a=A.__init__()
# print(a)

# 模板
class Person:
    name='这是类的名字'
    age=0
# 类变量、实例变量

    def __init__(self,name,age):
        # 构造函数
        # 初始化对象的属性
        self.name=name
        self.__age=age
        # print(name)
        # print(age)

    # 行为与特征
    def __work(self):
        pass
jbw=Person('季彬武',18)
jbw.__age=33
jbw.name='lilei'
print(jbw.name)
print(jbw.__age)
print(jbw.__dict__)
# zxy=Person('朱晓英',18)
# print(jbw.name)
# print(zxy.name)
# print(Person.name)


# print(dir())
# print(jbw.__dict__)

