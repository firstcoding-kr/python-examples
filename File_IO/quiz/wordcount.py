with open("text_file.txt", "r") as file:
    word_counts = {}
    for line in file:
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word}: {count}")
