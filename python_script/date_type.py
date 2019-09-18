'''name='jbw'
print('hello,',name)

a='jack'
b="you"
print(f'my name is {a} and {b}')

student=['a','b','c','d']
student.append('e')
print(student)
student.insert(1,'f')
print(student)
student[0]='one'
print(student)
student.pop()
print(student)
student.pop(1)
print(student)'''

'''course=('math','chinese','sport','english')
print(course)
print(course[1:3])
print(course[1])
print(len(course))'''
'''number=(73,32,132,85,18,100)
number[1]=10000
print(number)
print(len(number))
MaxNumber=max(number)
MinNumber=min(number)
print(f'最大值为:{MaxNumber} 最小值为:{MinNumber} ')
print('最大值为:%d'%MaxNumber,'最小值为:%d'%MinNumber)'''
'''test=('a',)
print(test)
'''

#for 循环
'''score=[60,80,95,76,49,100]
for x in score:
    if x>=80:
        print('get A')
    elif 60<=x<=79:
        print('get B')
    else:
        print('get C')'''
'''sum=0
for i in range(1,100):
    if i<100:
        sum+=i
print(sum)'''

#while 循环
'''n=10
while n>0:
    n-=1
    print(n)
print('game is over')'''
#导入第三方库random,生产随机数
'''import  random
anser=random.randint(1,100)
guess=int(input('请输入1到100之间的值:'))
while guess != anser:
    if guess>anser:
        print('亲,你输入的值大了!')
        guess = int(input('请输入1到100之间的值:'))
    if guess<anser:
        print('亲，你输入的值小了!')
        guess = int(input('请输入1到100之间的值:'))
print('你真厉害猜对了!')'''
#自定义函数Max_num()

'''import random
def Max_num(a,b):
    if a>b:
        return  a
    elif a<b:
        return  b
    else:
        return a
one=random.randint(1,100)
print(one)
two=random.randint(1,100)
print(two)
result=Max_num(one,two)
print(result)'''


#定义一个student类
class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print('my name is %s and come from %s'%(name,city))
    def talk(self):
        print('hello,51zxw')


'''try:
    stu='jack'
    print(stu)
except BaseException as msg:
    print(msg)
else:
    print('没有异常')
finally:
    print("the end!")'''

'''try:
    filename=input('请输入文件名称:')
    open('%s.txt'%filename)
except FileNotFoundError:
    print('%s.txt is not found'%filename)'''
'''def division(x,y):
    if y==0:
        raise ZeroDivisionError('Zero is nor allowed!')
    return x/y
try:
    division(8,0)
except BaseException as msg:
    print(msg)'''

