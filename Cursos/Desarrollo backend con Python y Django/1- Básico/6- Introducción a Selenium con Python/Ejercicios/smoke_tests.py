from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_testing import HomeTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(HomeTests)

smoke_test = TestSuite([search_test, assertions_test])

kwargs = {
  "output":"smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)