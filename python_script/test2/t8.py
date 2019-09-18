f=open(r"C:\Users\user\Desktop\测试文件读取.txt","r")
for i in f.readlines():
    print(i)
f.close()



print('%s %s' % ('Hello', 'world'))

# 简洁版
s1 = 'Hello {}! My name is {}.'.format('World', 'Python猫')
print(s1)


# 对号入座版
s2 = 'Hello {0}! My name is {1}.'.format('World', 'Python猫')
s3 = 'Hello {name1}! My name is {name2}.'.format(name1='World', name2='Python猫')
print(s2)

s_tuple = ('Hello', ' ', 'world')
s_like_tuple = ('Hello' ' ' 'world')

print(s_tuple)

str_1 = 'Hello world！ '
str_2 = 'My name is Python猫.'
print(str_1 + str_2)

str_list = ['Hello', 'world']
str_join1 = ' '.join(str_list)
str_join2 = '-'.join(str_list)


name = 'world'
myname = 'python_cat'
words = f'Hello {name}. My name is {myname}.'
print(words)