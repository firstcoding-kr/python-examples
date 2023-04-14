import tkinter
import tkinter.font

class CounterWindow:
    def __init__(self):
        self.window=tkinter.Tk()
        self.window.title("firstcoding")
        self.window.geometry("640x400+100+100")
        self.window.resizable(False, False)
        self.count=0

        font = tkinter.font.Font(size=80, family='맑은 고딕', weight='bold')
        self.label = tkinter.Label(self.window, text="0", font=font)
        self.label.pack(pady=50)

        self.add_button("업", self.count_up)
        self.add_button("다운", self.count_down)
        self.add_button("리셋", self.reset_count)
        self.add_button("새창", self.new_window)

    def new_window(self):
        w =  CounterWindow()
        w.show()

    def count_up(self):
        self.count +=1
        self.label.config(text=str(self.count))

    def count_down(self):
        if self.count > 0:
            self.count -= 1
        self.label.config(text=str(self.count))

    def reset_count(self):
        self.count = 0
        self.label.config(text = self.count)

    def add_button(self, text, cmd):
        button = tkinter.Button(self.window, text=text, overrelief="solid", width=15, command=cmd)
        button.pack(side="left", padx=10, anchor="center", expand=True)

    def show(self):
        self.window.mainloop()

w = CounterWindow()
w.show()
