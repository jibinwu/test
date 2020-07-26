from jhscmall import login
import unittest
case=unittest.TestLoader().loadTestsFromTestCase(login.MyTestCase)
suite=unittest.TestSuite([case])


runner=unittest.TextTestRunner()
runner.run(suite)
