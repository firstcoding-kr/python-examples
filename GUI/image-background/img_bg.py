import tkinter as tk
from PIL import ImageTk, Image

# ImageTk와 Image는 PIL (Python Imaging Library) 패키지를 활용하므로 다음과 같이 설치한다.
# 설치: pip install Pillow

# tkinter 윈도우 생성
window = tk.Tk()

# 이미지 로드
image = Image.open("image.jpg")
# png 사용 시 다음과 같이 간단하게 사용할 수 있으나 
# jpg및 resize등의 재처리가 필요하다면 PIL패키지 활용
# img = tk.PhotoImage(file='image.png')

# 이미지 크기 조정
image = image.resize((200, 200), Image.ANTIALIAS)

# 이미지 객체 생성
img = ImageTk.PhotoImage(image)

# 레이블에 이미지 추가
label = tk.Label(window, image=img)

# 레이블 위치 설정
label.pack()

# tkinter 윈도우 실행
window.mainloop()
