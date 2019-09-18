import csv
# a=['d1','d2','d3','d4']
with open(r'C:\Users\user\Desktop\est.csv','r',encoding='utf-8') as f:
    # res=csv.writer(f)
    # res.writerow(a)
    res=csv.reader(f)
    for x in res:
        print(x)




