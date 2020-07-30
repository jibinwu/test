import pytest

'''
pytest.ini文件定义了mark标签属性，所以在执行脚本时不会报warning信息
pytest -s -v test_mark.py -m "not iostest"
pytest -s -v -x test_mark.py 用例执行错误就停止
pytest -s -v --maxfail=2 test_mark.py 用例执行错误累积2次就停止
pytest -s -v --reruns 3 test_mark.py 自动重跑3次失败的测试用例
pytest -s -v --html=report.html --self-contained-html 需要先装pytest-html,运行后生成可视化的报告，然后通过浏览器打开
pytest -s -v --alluredir=./result/ && allure serve ./result/ 在测试执行期间收集结果；测试完成后查看实际报告，在线看报告；
  
'''
@pytest.mark.webtest
def test_web():
    # print('这是web的测试用例')
    assert 1==1

@pytest.mark.apptest
def test_app():
    # print('这是APP的测试用例')
    assert 1==2

@pytest.mark.androidtest
def test_android():
    # print('这是安卓的测试用例')
    assert 2==3

@pytest.mark.iostest
def test_ios():
    # print('这是ios的测试用例')
    assert 3==3