# # 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#         print("{1} 说: 我 {0} 岁。" .format (self.name, self.age))
#
#
# # 实例化类
# p = people('runoob', 10, 30)
# p.speak()

# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法


# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


class   Student:
    name="hehe"
    age=""
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print(self.name,self.age)
        # print(Student.name)
        # print(self.__class__.name)
    def homework(self):
        print(self.name,self.age) #在实例方法中访问实例变量
        print(Student.name) #在实例方法中访问类变量第一种形式
        print(self.__class__.name) #在实例方法中访问类变量第二种形式
        return self.name
        # print(Student.name)
stu=Student("张三",18)
print(stu.homework())
print(Student.name)
# print(stu.__dict__)
# print(stu.name)
print(Student.__dict__)
print(dir())

