import HTMLTestRunner
from Scripts.TestCases.UI.TestSuites.TestSuites import *


def file_name():
    dir = report_dir()
    file_name = dir + "\\" + time_temp() + ".html"
    return file_name


def html():
    file = open(file_name(), "wb")
    suites = TestSuites().test_suites()
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file,
        title='本周测试报告',
        # description='This demonstrates the report output by HTMLTestRunner.'
    )

    runner.run(suites)
    file.close()


if __name__ == '__main__':
    html()
