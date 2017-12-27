import subprocess
from Scripts.Public.Path import *


def report_name():
    """
    获取最新生成的文件
    :return: 文件名（绝对路径）
    """
    report_dir = Path().report_dir()  # 文件所在目录
    # command = "dir " + report_dir + "\*.pdf /B"
    command = "dir " + report_dir + "\*.html /B"

    ls = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    report_name = ls.communicate()[0].decode().split("\r\n")[-2]
    return report_name


def last_file():
    report_dir = Path().report_dir()  # 文件所在目录
    last_pdf = report_dir + "\\" + report_name()
    return last_pdf




