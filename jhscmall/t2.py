# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("测试前装备")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("测试结束")
#
#     def test_01(self):
#         print("第一个")
#
#     def test_02(self):
#         print("第二个")
#
#     def test_03(self):
#         print("第三个")
#
#
#
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
import unittest
from HtmlTestRunner import HTMLTestRunner
import time
import os

class TestMethod(unittest.TestCase):  # 定义一个类，继承自unittest.TestCase
    # 每次执行用例前执行setUp()，可以在这里做一些初始化的工作
    @classmethod
    def setUpClass(cls):
        print('setUp\n')

    @classmethod
    def tearDownClass(cls):
        print('tearDown')

    def test001(self):  # unittest中的用例必须以test开头
        print('test001')

    # @unittest.skip('test002')
    def test002(self):
        print('test002')

    def test003(self):
        print('test003')



if __name__ == '__main__':
    '''第一种方法'''
    # suite=unittest.TestSuite()
    # suite.addTest(TestMethod('test001'))
    # suite.addTest(TestMethod('test002'))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)

    '''第二种方法'''
    # suite=unittest.TestSuite()
    # case=unittest.TestLoader().loadTestsFromTestCase(TestMethod)
    # suite.addTest(case)
    # runner=unittest.TextTestRunner()
    # runner.run(suite)

report='C:/Users/Administrator/PycharmProjects/test/jhscmall/testresult.html'
fp=open(report,'wb',)
suite = unittest.TestSuite()
case = unittest.TestLoader().loadTestsFromTestCase(TestMethod)
# discover=unittest.defaultTestLoader.discover() 这个方法其实是最厉害的查找测试用例的方法
suite.addTest(case)
suite.addTest(TestMethod('test001'))
runner = HTMLTestRunner(stream=fp, report_title='接口测试报告', descriptions='测试结果如下：')
runner.run(suite)
fp.close()


# report_path=os.path.join(os.path.dirname(__file__),'report')
# now=time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())
# filename=report_path+'/'+now+'_result.html'
#suite = unittest.TestSuite()
#case = unittest.TestLoader().loadTestsFromTestCase(TestMethod)
#suite.addTest(case)
#with open(filename,'wb',) as f:
#     runner = HTMLTestRunner.HTMLTestRunner(
#          stream=f,
#          title='接口测试报告',
#          description='测试结果如下：')
#     runner.run(suite)
