import csv

# 데이터 준비
data = [
    ['이름', '나이', '성별'],
    ['John', 25, '남성'],
    ['Lisa', 30, '여성'],
    ['Michael', 35, '남성']
]

# CSV 파일 쓰기
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
