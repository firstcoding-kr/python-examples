with open("file1.txt", "r") as file1:
    with open("file2.txt", "r") as file2:
        for line_num, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1 != line2:
                print(f"Difference found on line {line_num}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
