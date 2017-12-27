from Scripts.GUI.Tab import *
from Scripts.GUI.LogFrame import *
from Scripts.GUI.UploadFile import *

window = Tk()
window.title("test")  # 窗口标题
window.resizable(width=True, height=True)  # 窗口大小可变
tab_style = Style()
tab_style.configure(style="TAB_STYLE", background="#C7EFEA")


def main_page(text):
    Tab().tab()
    UploadFile().page()
    if "err"or "fail"or "exception" in text:
        fg = "red"
    else:
        fg = "green"
    log_frame(fg, text)

    window.mainloop()


main_page("sjdhffkd   fjsiowerorwerwelkfjn v 54321sdf:LL\"W:Eu6ty\"")