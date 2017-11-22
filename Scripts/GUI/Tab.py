from tkinter.ttk import *
from tkinter import *

class Tab:
    def __init__(self):
        self.window = Tk()
        self.window.title = ("test")
        # self.notebook = Notebook()

    def style(self):
        button_style = Style()
        button_style.configure("TButton", padding=6, relief="flat", background="#ccc")

    def tab(self):

        notebook = Notebook(self.window)
        tab = Frame(notebook)
        notebook.add(tab, text="UI")
        self.window.mainloop()


if __name__ == '__main__':
    Tab().tab()
