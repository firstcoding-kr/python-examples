import socket, threading

# 멀티캐스트 그룹 정보 설정
MULTICAST_GROUP = '239.0.0.2'
MULTICAST_PORT = 5000

# 클라이언트 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  # 타임아웃 설정

# 멀티캐스트 그룹에 가입
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind(('', MULTICAST_PORT))
mreq = socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0')
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# 사용자 이름 입력
user_name = input("사용자 이름 입력: ")

# 메시지 수신 함수
def receive_messages():
    while True:
        try:
            message, address = client_socket.recvfrom(1024)
            sender_name, actual_message = message.decode().split(':', 1)
            if sender_name != user_name: # 자신이 보낸 메시지는 표시하지 않는다.
                print(f"{sender_name}: {actual_message}")
        except socket.timeout:
            pass

# 메시지 발송 함수
def send_messages():
    while True:
        message = input()
        client_socket.sendto(f"{user_name}:{message}".encode(), (MULTICAST_GROUP, MULTICAST_PORT))

# 별도의 스레드에서 메시지 수신을 처리
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# 메시지 발송은 메인 스레드에서 처리
send_messages()

# 스레드 종료 대기
receive_thread.join()
client_socket.close()
