import os

file_name = "text_file.txt"
new_file_name = "new_text_file.txt"

if os.path.exists(file_name):
    os.rename(file_name, new_file_name)
    print(f"{file_name} was renamed to {new_file_name}.")
else:
    print(f"{file_name} does not exist.")
