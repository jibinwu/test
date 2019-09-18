class Student(object):
    sum=0
    name='类名'
    age=18

    def __init__(self,name1,age):
        self.name=name1
        self.age=age
        self.__score=0
        print(self.__dict__)
        # print(self.score)
        # if self.score>90:
        #     print('你真厉害！')
        # print(self.name)
        # print(self.__dict__)
        # print(Student.__dict__)
        # print(self.name)
        # print(Student.name)
        # print(self.__class__.name)

    @classmethod
    def cls_function(cls):
        Student.sum+=1
        print(Student.sum)

    # @staticmethod
    # def add(x,y):
    #     print('这是个静态方法')
    #     return '呵呵'

    def marking(self,score):
        if score<0:
            return '呵呵'
        self.score=score
        print(self.name+'同学本次考试分数为：'+str(self.score))
            # score=0
        # self.score=score
        # print(self.score)
        # self.do_homework()


    def do_homework(self):
        print('做作业')
student=Student('jbw',26)
r=student._Student__score
print(r)
# student.marking(90)
# result=student.marking(6)
# print(result)
# student.marking(-3)
# student.add(1,2)
# print(student.name)
# student.cls_function()
# student.do_homework()


