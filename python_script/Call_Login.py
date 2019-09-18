# num=[]
# for i in range(50):
#     num.append(i)
# print(num)

def build_person(first_name,last_name):
    print(first_name,last_name)
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)