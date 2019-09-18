import  sys
print(sys.argv)
class Math(object):
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self):
        return self.a+self.b
num=Math(1,2)
result=num.add()
print(result)
print(dir(Math))


