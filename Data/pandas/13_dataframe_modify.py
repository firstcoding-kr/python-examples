import pandas as pd
# DataFrame 데이터 수정 예제

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

# 특정 컬럼(열) 데이터 수정 (북산고 -> 상북고로 수정)
df['학교'].replace({'북산고':'상북고'}, inplace=True)
print(df)

# SW특기 열의 데이터를 모두 대문자로
df['SW특기'] = df['SW특기'].str.upper()
print(df)

# 일괄적으로 문자열 연결 (xx고 -> xx고등학교로)
df['학교'] = df['학교'] + '등학교'
print(df)

# 새로운 열에 기존 열의 값을 계산하여 넣기
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

# 총합이 400점이 넘는 학생만 Pass 처리
df['결과'] = 'Fail' # 결과 열을 추가하고 Fail로 초기화
df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터의 결과를 Pass로 업데이트
print(df)

# 컬럼(열) 삭제
df.drop(columns=['총합'], inplace=True) # 총합 열 삭제
print(df)  

# 여러 컬럼 삭제 
# (inplace=False(기본값) 이면 원본을 변경하지 않고 수정본의 복사된 값이 리턴된다)
print(df.drop(columns=['국어', '영어', '수학']))

# 특정 Row(행) 삭제
print(df.drop(index="4번"))

# 수학 점수가 80미만인 학생 삭제
print( df.drop(index=df[df['수학'] < 80].index) )

# Row 추가
df.loc['9번'] = ['이정환', '해남고등학교', 184, 85, 80, 90, 90, 87, 'Java', 'Pass']
print(df)

# Cell 수정
# 4번 학생의 SW특기 입력
df.loc['4번', 'SW특기'] = 'Python'
print(df)

# 5번 학생의 학교, SW특기 수정
df.loc['5번', ['학교', 'SW특기']] = ['능남고등학교', 'C']
print(df)

# 컬럼(열) 순서 변경
cols = list(df.columns) # 컬럼을 파이썬 리스트로 가져오기
df = df[[cols[-1]] + cols[0:-1]] # list 슬라이싱 조합으로 원하는 순서를 만들고 df인덱싱
print(df)

# 컬럼 이름을 변경
cols = list(df.columns) # 컬럼을 파이썬 리스트로 가져와서
cols[0] = "Result" # 원하는대로 수정한 후
df.columns = list(cols) # DataFrame 컬럼을 재지정
print(df)
