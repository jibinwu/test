import pytest
# @pytest.fixture()
# def login():
#     print('登录了') #可以把这个模块抽出来放在conftest文件里，做数据共享

def test_sosuo(login):
    print('case1:登录后才能搜索')

def test_look():
    print('case2:不登录就能看')

def test_cart(login):
    print('case3:登录后才能加入购物车')

if __name__ == '__main__':
    pytest.main(['-s','test_fixture.py'])


