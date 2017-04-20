import unittest
import test_login2

suite=unittest.TestSuite()

# 测试
suite.addTest(test_login2.TestLogin("test_null"))
suite.addTest(test_login2.TestLogin("pawd_null"))
suite.addTest(test_login2.TestLogin("user_null"))
suite.addTest(test_login2.TestLogin("error"))

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)
