import tkinter

win = tkinter.Tk()

win.geometry("700x400")

# 투명 배경 설정
win.config(bg = '#add123')
win.wm_attributes('-transparentcolor','#add123')
win.attributes('-topmost', 1)

lb = tkinter.Label(text="Hello", font=('맑은 고딕', 60), bg='#add123')
lb.pack()

win.mainloop()
