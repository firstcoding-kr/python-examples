import pandas as pd

# csv 파일에서 읽기
df = pd.read_csv('data.csv')
print(df)

# txt 파일에서 읽기
df = pd.read_csv('data.txt', sep='\t', index_col='학번')
print(df)

# 첫 번째 행 무시
df = pd.read_csv('data.csv', skiprows=1)
print(df)

# 무시할 행 지정
df = pd.read_csv('data.csv', skiprows=[2,5,7])
print(df)

# 지정된 행 개수만큼만 가져오기
df = pd.read_csv('data.csv', nrows=4)
print(df)
