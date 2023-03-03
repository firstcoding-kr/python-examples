import csv

# 입력 파일명과 출력 파일명을 지정합니다.
input_file = 'data.txt'
output_file = 'converted_data.csv'

# 입력 파일을 읽기 모드로 엽니다.
with open(input_file, 'r') as f:
    # csv 모듈의 DictReader 클래스를 사용하여 파일 내용을 딕셔너리 리스트로 읽어옵니다.
    reader = csv.DictReader(f, delimiter=',')
    # 출력 파일을 쓰기 모드로 엽니다.
    with open(output_file, 'w', newline='') as output:
        # csv 모듈의 DictWriter 클래스를 사용하여 딕셔너리 리스트를 CSV 형식으로 변환하여 출력 파일에 씁니다.
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow(row)
