import os

file_name = "text_file.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} was deleted.")
else:
    print(f"{file_name} does not exist.")
