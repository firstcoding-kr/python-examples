import csv

# CSV 파일 읽기 (딕셔너리 형식)
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # 각 행에 대한 반복문
    for row in reader:
        print(row)
