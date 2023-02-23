import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("메모장")
        self.master.geometry("500x500")
        self.filename = ""
        
        self.text = tk.Text(self.master)
        self.text.pack(expand=True, fill="both")

        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self.master)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="새로 만들기", command=self.new_file)
        filemenu.add_command(label="열기", command=self.open_file)
        filemenu.add_command(label="저장", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="종료", command=self.master.quit)
        menubar.add_cascade(label="파일", menu=filemenu)
        
        self.master.config(menu=menubar)
        
    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.filename = ""
        
    def open_file(self):
        filetypes = [("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
        self.filename = filedialog.askopenfilename(filetypes=filetypes)
        if self.filename:
            with open(self.filename, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())
        
    def save_file(self):
        if not self.filename:
            filetypes = [("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
            self.filename = filedialog.asksaveasfilename(filetypes=filetypes)
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get("1.0", tk.END))
        
def main():
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()

if __name__ == "__main__":
    main()
