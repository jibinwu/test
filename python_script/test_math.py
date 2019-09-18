import unittest
from caculator import Math


class TestMath(unittest.TestCase):
         print('test start')

    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)

    def tearDown(self):
        print('test end!')


if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(TestMath('test_add'))
    runer=unittest.TextTestRunner()
    runer.run(suit)