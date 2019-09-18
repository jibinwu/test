import  csv
# f=open('555.txt','r+',encoding='UTF-8')
# i=f.read()
# f.write('我要学python!')
# print(i)
# f.close()

'''f=open('555.txt','w',encoding='UTF-8')
f.write('你是风儿')
f.close()'''

# f=open('555.txt','r',encoding='UTF-8')
# i=f.readlines()#返回一个列表
# print(i)
# for x in i:
#     print(x.split(',')[1])
# f.close()

# 读取CSV文件
import  csv
file=open('stu_info.csv','r')
csv_file=csv.reader(file)
# csv_file=csv.reader(open('stu_info.csv','r'))
print(csv_file)
for stu in csv_file:
    print(stu[1])


#往CSV文件中添加数据
# import csv
# stu1=['jack',29,'beijing']
# stu2=['bob',30,'shangahi']
# stu3=['kobe',30,'wuhan']
# file=open('stu_info.csv','a')#打开文件
# csv_write=csv.writer(file,dialect='excel')#设定写入模式
# csv_write.writerow(stu1)
# csv_write.writerow(stu2)
# csv_write.writerow(stu3)
# print('Write file over')



