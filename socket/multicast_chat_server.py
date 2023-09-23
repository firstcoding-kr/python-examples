import socket
import struct

# 멀티캐스트 그룹 정보 설정
MULTICAST_GROUP = '239.0.0.1'
MULTICAST_PORT = 5000

# 서버 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', MULTICAST_PORT))

# 멀티캐스트 그룹에 가입
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("멀티캐스트 채팅 서버 시작. 대기 중...")

while True:
    message, address = server_socket.recvfrom(1024)
    print(f"수신된 메시지: {message.decode()}")

    if message == 'kill':
        break

server_socket.close()
