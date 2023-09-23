import socket
# 소켓 참고: https://docs.python.org/ko/3/library/socket.html

# 서버 설정
host = "127.0.0.1"  # 서버 IP 주소
port = 9090       # 포트 번호

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((host, port))
print(f"서버 {host}:{port} 에 연결되었습니다.")

# 메시지 전송
message = "안녕하세요, 서버!"
client_socket.send(message.encode()) # 문자열을 byte로 변환하여 전송

# 연결 종료
client_socket.close()
