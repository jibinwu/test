import random
list1=[1,2,3,4]
# list2=[x*x for x in list1]
# print(list2)

# list2=list(map(lambda x: x*x,list1))
# print(list2)
# f=lambda x: x*x,list1
# for i in f:
#     print(i)
# def A(a,b):
#     return lambda x,y:x*x+y*y
# f=A(1,2)
# print(f)
random.shuffle(list1)
print(list1)