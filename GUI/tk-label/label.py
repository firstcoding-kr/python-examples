import tkinter

window=tkinter.Tk()
window.title("firstcoding")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="파이썬", width=20, height=5, fg="red", bg="skyblue", relief="solid")
label.pack()

def change_label_text():
    label.config(text="Label 글자 바꾸기")

btn = tkinter.Button(window, text="클릭시 Label 텍스트 변경", command=change_label_text)
btn.pack()

window.mainloop()