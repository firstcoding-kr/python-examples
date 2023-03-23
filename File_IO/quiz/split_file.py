file_name = "text_file.txt"
max_file_size = 1000000 # 1MB

with open(file_name, "r") as input_file:
    part_num = 1
    while True:
        chunk = input_file.read(max_file_size)
        if not chunk:
            break
        part_file_name = f"{file_name}.{part_num}"
        with open(part_file_name, "w") as part_file:
            part_file.write(chunk)
        part_num += 1
