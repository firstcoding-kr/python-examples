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

# 데이터프레임 객체 생성
df = pd.DataFrame(data)

# 데이터프레임 출력해보기
print(df)

# 특정 컬럼만 출력: key문자열 전달
print(df['이름'])

# 복수 개의 컬럼 선택 시: 리스트로 key를 전달
print(df[['이름', '키']])

# data 중에서 원하는 컬럼과 순서 지정
df = pd.DataFrame(data, columns=['이름', '학교', '키'])
print(df)

# 인덱스를 별도로 지정 (데이터의 개수와 맞아야한다.)
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df)

# 인덱스 확인
print(df.index)

# 인덱스 이름 지정
df.index.name = '학번'
print(df)

# 인덱스 초기화
# drop=False이면 기존 인덱스는 컬럼으로 이동, inplace=True: 즉시 데이터에 반영
df.reset_index(drop=True, inplace=True)
print(df)

# 원하는 컬럼을 인덱스로
df.set_index('이름', inplace=True)
print(df)

# 인덱스 기준 정렬
df.sort_index(inplace=True)
print(df)
# 역순 정렬
df.sort_index(ascending=False, inplace=True)
print(df)

# value로 정렬 (키 큰 사람)
df.sort_values('키', ascending=False, inplace=True)
print(df)
