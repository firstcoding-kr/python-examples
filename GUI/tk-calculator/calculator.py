import tkinter as tk

# 계산 함수
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# 버튼 클릭 함수
def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + symbol)

# 윈도우 창 만들기
window = tk.Tk()
window.title("간단한 계산기")

# 결과 표시 창 만들기
display = tk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# 숫자 버튼 만들기
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3)
]

for symbol, row, column in buttons:
    button = tk.Button(window, text=symbol, width=5, height=2, command=lambda symbol=symbol: button_click(symbol))
    button.grid(row=row, column=column, padx=5, pady=5)

# 계산 버튼 만들기
equal_button = tk.Button(window, text="=", width=5, height=2, command=calculate)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# 윈도우 창 실행
window.mainloop()
