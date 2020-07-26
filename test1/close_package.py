def outer():
    a=1
    b=2
    def inner(x):
        return a+b+x
    return inner

result=outer()
print(result(2))
print(result.__closure__)
print(result.__closure__[0].cell_contents)
for i in result.__closure__:
    print(i.cell_contents)


# def f1():
#     a=10
#     def f2():
#         a=20
#         print(a)
#     f2()
# f=f1()
# print(f.__closure__)






