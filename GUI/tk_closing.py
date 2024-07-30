# Tk 창을 닫을 때 처리
import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
