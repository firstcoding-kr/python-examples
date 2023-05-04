import tkinter
from math import *

window=tkinter.Tk()
window.title("firstcoding")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc(event):
    print(entry.get())
    label.config(text="결과="+str(eval(entry.get())))

entry=tkinter.Entry(window)
entry.bind("<Return>", calc) # 엔터 시 실행할 함수 설정
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()
