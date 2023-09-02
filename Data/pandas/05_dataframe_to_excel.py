import pandas as pd
# 이 예제는 pandas 및 openpyxl 모듈 필요 (pip install openpyxl)

# 예시 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'Occupation': ['Engineer', 'Teacher', 'Student', 'Doctor', 'Artist']
}

df = pd.DataFrame(data)

# 데이터프레임을 엑셀 파일로 저장
output_excel_file = "data.xlsx"
df.to_excel(output_excel_file, index=False)

print(f"데이터프레임이 '{output_excel_file}' 파일로 저장되었습니다.")
