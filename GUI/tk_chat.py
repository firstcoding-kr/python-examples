# tkinter 채팅 프로그램 화면 만들기 예제
import tkinter
import tkinter.messagebox
import tkinter.simpledialog

def on_send(e=None):
    msg = text_input.get()
    text_input.delete(0, 'end')
    if not msg:
        tkinter.messagebox.showinfo('메시지를 입력해주세요.', '메시지를 입력해주세요.')
        return

    msg = f'{nickname}: {msg}'
    listbox.insert('end', msg)

    # 소켓 전송 코드 짜기
    
# 윈도우 창 만들기
w = tkinter.Tk()

# 창을 닫을때 실행할 함수
#w.protocol('WM_DELETE_WINDOW', on_closing)

# 창을 화면 중앙에 위치시키기
width, height = 500, 700
x = (w.winfo_screenwidth() // 2) - (width // 2)
y = (w.winfo_screenheight() // 2) - (height // 2)
w.geometry(f'{width}x{height}+{x}+{y}')

w.resizable(False, False) # 크기변경 안되게 
w.title('채팅 프로그램') # 창 제목

listbox = tkinter.Listbox(w, height=24, font=('맑은 고딕', 14))
listbox.pack(fill='both', padx=5, pady=(5, 0))

#입력창
input_group = tkinter.Frame(w)
text_input = tkinter.Entry(input_group, font=('맑은 고딕', 16), width=33)
text_input.bind('<Return>', on_send)
text_input.pack(side='left')

send_btn = tkinter.Button(input_group, text='전송하기', command=on_send, font=('맑은 고딕', 11))
send_btn.pack(side='left', padx=(10, 0))
input_group.pack(side='bottom', pady=20)

# 처음 켤 때 닉네임 입력 받음
nickname = tkinter.simpledialog.askstring('닉네임 입력', '닉네임을 입력해주세요.')
if not nickname: nickname = '익명'
#w.wm_attributes("-topmost", 1) # 창 맨 위로 오게 설정
w.focus_force() # 채팅창으로 포커스 이동
text_input.focus() # 채팅 입력창으로 포커스 이동

w.mainloop()
