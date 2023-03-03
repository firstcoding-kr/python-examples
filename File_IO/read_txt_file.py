file_path = "example.txt"

try:
    with open(file_path, "r", encoding="UTF-8") as f:
        data = f.read()
        print("[파일 내용]")
        print(data)

        print("글자수:", len(data))
        print("\"코딩\" 단어 수:", data.count("코딩"), "회")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except PermissionError:
    print(f"파일을 읽을 권한이 없습니다: {file_path}")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
