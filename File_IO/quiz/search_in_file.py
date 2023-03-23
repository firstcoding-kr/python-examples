file_name = "text_file.txt"
search_string = "python"

with open(file_name, "r") as file:
    for line_num, line in enumerate(file, start=1):
        if search_string in line:
            print(f"Found '{search_string}' on line {line_num}: {line.strip()}")
