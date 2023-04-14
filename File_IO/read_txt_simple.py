# 텍스트 파일 읽기
with open("example.txt", mode="r", encoding="UTF-8") as f:
    data = f.read()
    print(data)
