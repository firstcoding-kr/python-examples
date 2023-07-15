import pandas as pd

# 데이터 준비
data = {
    '이름': ['John', 'Lisa', 'Michael'],
    '나이': [25, 30, 35],
    '성별': ['남성', '여성', '남성']
}

# DataFrame 생성
df = pd.DataFrame(data)

# CSV 파일 저장
df.to_csv('data.csv', index=False, encoding="utf-8-sig")
