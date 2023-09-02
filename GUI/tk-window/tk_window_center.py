import tkinter

tk = tkinter.Tk()

w = 600 # 창 가로크기
h = 300 # 창 세로크기

# 창을 화면 중앙에 띄울 x, y 좌표를 구한다.
x = int((tk.winfo_screenwidth() / 2) - (w/2))
y = int((tk.winfo_screenheight() / 2) - (h/2))

tk.geometry(f'{w}x{h}+{x}+{y}')
tk.mainloop()
