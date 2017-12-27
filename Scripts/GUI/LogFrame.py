from tkinter import scrolledtext
from tkinter.constants import END,BOTH


def log_frame(fg, text):
    """
    输出日志
    :param fg: 字体颜色，error为红色
    :param text: 日志内容
    :return:
    """
    log = scrolledtext.ScrolledText(bg="#C7EFEA", fg=fg)
    log.insert(END, text)
    log.pack(fill=BOTH, expand="yes")
