import  random

ll=[]
# result=random.randrange(1,3)#不包括3
for i in range(10):
    result=random.randint(1,1000)#包括3
    ll.append(result)
ll.sort(reverse=True)
sorted(ll)
print(ll)