from tkinter.ttk import *
from tkinter import *


def tab_ui_fun(notebook):
    text = Text(notebook, width=60, heigh=2)
    text.pack(side="left")
    button = Button(notebook, text="选择文件")
    button.pack(side='right')


def tab():
    """
    选项卡
    :return:
    """
    notebook = Notebook(heigh=300)
    tab_ui = Frame(notebook)
    tab_api = Frame(notebook)
    notebook.add(tab_ui, text="   UI   ")
    tab_ui_fun(tab_ui)
    notebook.add(tab_api, text="   API   ")
    notebook.pack(fill=BOTH, expand="yes")


def tab_api():
        pass
