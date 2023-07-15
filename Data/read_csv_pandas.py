import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('data.csv', encoding="utf-8-sig")

# 데이터 확인
print(df)
