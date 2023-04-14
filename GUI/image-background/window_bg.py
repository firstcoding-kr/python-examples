import tkinter as tk

# 윈도우 생성
window = tk.Tk()

# 이미지 로드
image = tk.PhotoImage(file='image.png')

# 캔버스 생성
canvas = tk.Canvas(window, width=image.width(), height=image.height())
canvas.create_image(0, 0, anchor='nw', image=image)

# 버튼 생성
button = tk.Button(canvas, text='Click me')

# 버튼 위치 설정
canvas.create_window(100, 100, anchor='nw', window=button)

# 캔버스 위치 설정
canvas.pack()

# 윈도우 실행
window.mainloop()
