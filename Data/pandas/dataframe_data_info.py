import pandas as pd
# 이 예제는 pandas 및 openpyxl 모듈 필요 (pip install openpyxl)

# 예시 데이터 생성
data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
df.index.name = '학번'

# 계산 가능한 데이터에 대해 컬럼 별로 
# 개수, 평균, 표준편차, 최소/최댓값 등의 정보를 보여준다.
print(df.describe())

# 데이터가 많을 경우 일부분만 가져오기
# 처음 5개의 데이터 (df.head(7): 처음 7개)
print(df.head())

# 마지막 5개의 데이터
print(df.tail())

# 값을 배열로 가져오기
print(df.values)

print(df.index)
print(df.columns)

# row와 colum의 개수
print(df.shape)

# 단일 컬럼에 대한 분석 (시리즈 처럼 취급된다.)
print(df['키'].describe())
print('평균', df['키'].mean())
print('키큰사람 3명 데이터\n', df['키'].nlargest(3))
print(df['학교'].unique())
