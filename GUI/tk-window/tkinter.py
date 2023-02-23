import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("메시지", "버튼이 클릭되었습니다.")

# 윈도우 생성
window = tk.Tk()

# 윈도우 제목 설정
window.title("버튼 예제")

# 윈도우 크기 설정
window.geometry("200x100")

# 버튼 생성
button = tk.Button(window, text="클릭하세요", command=on_button_click)

# 버튼 배치
button.pack(pady=20)

# 메인 루프 실행
window.mainloop()
