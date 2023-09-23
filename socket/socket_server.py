import socket
# 소켓 참고: https://docs.python.org/ko/3/library/socket.html

# 서버 설정
host = "127.0.0.1" # 서버 IP 주소
port = 9090 # 포트 번호

# 소켓 생성 (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 주소와 포트에 바인딩
server_socket.bind((host, port))

# 클라이언트의 연결을 대기
server_socket.listen(5)
print(f"서버가 {host}:{port} 에서 시작되었습니다.")

# 클라이언트 연결을 수락
client_socket, client_address = server_socket.accept()

# 소켓이 연결 된 상태이다.
print(f"{client_address}가 연결되었습니다.")

# 클라이언트로부터 메시지 수신 및 출력
while True:
    data = client_socket.recv(1024).decode() # byte 데이터를 문자열로 수신
    
    if not data:
        continue

    if 'exit' == data: # exit를 수신하면 서버가 종료된다.
        break

    print(f"수신한 메시지: {data}")

# 연결 종료
client_socket.close()
server_socket.close()
