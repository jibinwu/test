def ff(a):
    print(a)
    return 1
def bb(ff):
    print(ff)
ff(1)
print(bb(ff(1)))