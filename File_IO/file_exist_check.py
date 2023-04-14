import os

file_path = "example.txt"

if os.path.exists(file_path):
    print("파일이 존재합니다.")
else:
    print("파일이 존재하지 않습니다.")
