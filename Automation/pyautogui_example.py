import pyautogui

# PyAutoGUI를 사용하면 Python 스크립트가 마우스와 키보드를 제어하여
# 다른 응용 프로그램과의 상호 작용을 자동화할 수 있다.

# 래퍼런스: https://pyautogui.readthedocs.io/en/latest/

# 주 모니터의 스크린 사이즈(해상도) 구하기
screenWidth, screenHeight = pyautogui.size()

# 마우스 커서의 현재 좌표 구하기
currentMouseX, currentMouseY = pyautogui.position()

# 마우스 포인터 이동
pyautogui.moveTo(100, 150)

# 마우스 클릭
pyautogui.click()

# 마우스 특정 위치 클릭
pyautogui.click(100, 200)

# 마우스 포인터 이동
pyautogui.move(400, 0)

# 더블 클릭
pyautogui.doubleClick()

# 특정 시간동안 정해진 위치로 마우스 이동
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  

# 키보드 입력
pyautogui.write('Hello world!', interval=0.25)

# ESC키 누르기 / 모든 키 이름은 pyautogui.KEY_NAMES 참조
pyautogui.press('esc')

with pyautogui.hold('shift'):  # Shift 키 누른 상태
        pyautogui.press(['left', 'left', 'left', 'left'])  # 왼쪽 방향키 4번 누름
# Shift 키는 자동으로 해제됨

# Ctrl-C 단축키 누르기
pyautogui.hotkey('ctrl', 'c') 

# 메시지 띄우기
pyautogui.alert('This is the message to display.')
