import socket
# 소켓 참고: https://docs.python.org/ko/3/library/socket.html

# 브로드캐스트 주소 설정
broadcast_address = "0.0.0.0"  # 모든 인터페이스에서 수신
port = 9000

# UDP 소켓 생성
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 바인딩 (브로드캐스트 수신을 위해 필요)
receiver_socket.bind((broadcast_address, port))

print(f"브로드캐스트 수신을 시작합니다. (주소: {broadcast_address}, 포트: {port})")

while True:
    data, address = receiver_socket.recvfrom(1024)
    print(f"수신한 메시지: {data.decode()} (보낸 주소: {address[0]})")
