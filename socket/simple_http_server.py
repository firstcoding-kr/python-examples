import socket

def create_response(status_code, content):
    response = f"HTTP/1.1 {status_code}\r\n"
    response += "Content-Type: text/html\r\n"
    response += f"Content-Length: {len(content)}\r\n"
    response += "\r\n"
    response += content
    return response

# 서버 설정
host = "127.0.0.1"  # 서버 IP 주소
port = 80 # HTTP 포트 번호

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 주소와 포트에 바인딩
server_socket.bind((host, port))

# 클라이언트의 연결을 대기 (동시 연결수 = 5)
server_socket.listen(5)
print(f"서버가 {host}:{port} 에서 시작되었습니다.")

while True:
    # 클라이언트 연결을 수락
    client_socket, client_address = server_socket.accept()
    print(f"{client_address}가 연결되었습니다.")

    # 클라이언트로부터 HTTP 요청 수신
    request = client_socket.recv(1024).decode()

    # HTTP 응답 생성
    if request:
        response_content = "<html><body><h1>Hello, World!</h1></body></html>"
        response = create_response("200 OK", response_content)
        client_socket.send(response.encode())

    # 클라이언트 연결 종료
    client_socket.close()
