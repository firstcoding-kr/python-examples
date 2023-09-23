import socket
# 소켓 참고: https://docs.python.org/ko/3/library/socket.html

# 브로드캐스트 주소 설정
broadcast_address = "255.255.255.255"
port = 9000

# UDP 소켓 생성
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 옵션 설정 (브로드캐스트 전송을 위해 필요)
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    message = input("브로드캐스트할 메시지 입력 (종료하려면 'exit' 입력): ")
    if message == "exit":
        break
    sender_socket.sendto(message.encode(), (broadcast_address, port))

sender_socket.close()
