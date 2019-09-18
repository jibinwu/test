from  time import  ctime,sleep
import threading
#定义说和写的方法
def talk(content,loop):
    for i in range(loop):
        print('start talk :%s %s'%(content,ctime()))
        sleep(2)
def write(content,loop):
    for i in range(loop):
        print('start write :%s %s'%(content,ctime()))
        sleep(3)

#定义和加载说和写的线程
threads=[]
t1=threading.Thread(target=talk,args=('hello,kobe!',2))
threads.append(t1)

t2=threading.Thread(target=write,args=('life is short,you need python!',3))
threads.append(t2)


#执行多线程
if __name__=='__main__' :
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all thread is end! %s'%ctime())

