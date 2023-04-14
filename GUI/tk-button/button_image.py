import tkinter as tk

# 윈도우 생성
window = tk.Tk()

# 이미지 로드
image = tk.PhotoImage(file='pwr.png')

# 버튼 생성
button = tk.Button(window, image=image)

# 버튼 위치 설정
button.pack()

# 윈도우 실행
window.mainloop()
