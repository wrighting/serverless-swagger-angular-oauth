import unittest

from test_example import TestExample

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestExample))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
