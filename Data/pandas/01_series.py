import pandas as pd

# 기본적인 시리즈 생성 및 인덱스 설정
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']

series_1 = pd.Series(data, index=index)
print(series_1)

# 시리즈 값 선택 및 연산
print(series_1['a'])
print(series_1[2])
print(series_1 + 5)

# 시리즈의 조건 필터링
filtered_series = series_1[series_1 > 30]
print(filtered_series)

# 시리즈 합계, 평균 등 간단한 통계 정보
print("Sum:", series_1.sum())
print("Mean:", series_1.mean())
print("Max:", series_1.max())
print("Min:", series_1.min())

# 시리즈와 딕셔너리 간 변환
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series_2 = pd.Series(data_dict)
print(series_2)

series_to_dict = series_2.to_dict()
print(series_to_dict)
