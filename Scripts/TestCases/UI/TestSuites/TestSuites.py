from Scripts.TestCases.UI.Index.LaunchApp import *
from Scripts.TestCases.UI.Install.Install import *


class TestSuites:
    def test_suites(self):
        test_suites = unittest.TestSuite()
        # 按执行顺序添加
        test_suites.addTest(unittest.makeSuite(Install))
        test_suites.addTest(unittest.makeSuite(LaunchApp))

        return test_suites


if __name__ == '__main__':
    unittest.main()