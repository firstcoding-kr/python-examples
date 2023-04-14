import tkinter as tk

# 윈도우 생성
window = tk.Tk()

# 이미지 로드
bg_image = tk.PhotoImage(file='image.png')

# 라벨 생성
bg_label = tk.Label(window, image=bg_image)

# 라벨 위치 설정
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 버튼 생성
btn = tk.Button(bg_label, text='Click me')

# 버튼 위치 설정
btn.place(relx=0.5, rely=0.5, anchor='center')

# 윈도우 실행
window.mainloop()
