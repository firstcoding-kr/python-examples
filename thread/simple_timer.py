import threading
import keyboard

is_running = True

def on_key_press(event):
    global is_running

    print(f'Key {event.name} pressed.')
    if event.name == 'esc':
        is_running = False

def start_timer():
    print("Timer 실행 (esc 누르면 종료됩니다.)")

    if is_running:
        timer = threading.Timer(1, start_timer)
        timer.start()
 
if __name__ == '__main__':
    keyboard.on_press(on_key_press)
    start_timer()
