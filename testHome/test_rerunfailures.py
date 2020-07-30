import pytest
import random
def add(x,y):
    return x+y

#pytest -v -s --reruns 3 --reruns-delay 1 test_rerunfailures.py  失败用例重跑
def test_muti_assert():
    assert add(1,2) == random.randint(3,10)



