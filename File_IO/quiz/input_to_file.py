with open("text_file.txt", "w") as file:
    while True:
        user_input = input("파일에 저장할 내용을 입력해주세요. (exit 입력 시 종료): ")
        if user_input == "exit":
            break
        file.write(user_input + "\n")
