from tkinter.ttk import *
from tkinter import *


def progress(self):
    """
    用例执行进度
    :return:
    """
    progress_bar = Progressbar(lenth=200, mode="indeterminate")
    bar = Frame(progress_bar)
    progress_bar.grid()
