import socket

# 멀티캐스트 그룹 정보 설정
MULTICAST_GROUP = '239.0.0.1'
MULTICAST_PORT = 5000

# 클라이언트 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  # 타임아웃 설정

while True:
    message = input("메시지 입력 (끝내려면 'exit' 입력): ")
    if message.lower() == 'exit':
        break
    client_socket.sendto(message.encode(), (MULTICAST_GROUP, MULTICAST_PORT))

client_socket.close()
