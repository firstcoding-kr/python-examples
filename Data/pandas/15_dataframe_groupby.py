import pandas as pd
# 동일한 값을 가진 것들끼리 합쳐서 통계나 평균 등의 값을 뽑는다. 

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

# 북산고 학생만
print(df.groupby('학교').get_group('북산고'))

# 학교별 계산 가능한 데이터들의 평균값
print(df.groupby('학교').mean(numeric_only=True))

# 각 그룹의 크기 (각 학교별 학생수)
print(df.groupby('학교').size())

# 학교로 그룹화를 한 뒤 능남고에 해당하는 데이터의 수
print(df.groupby('학교').size()['능남고'])

# 각 학교별 키의 평균
print(df.groupby('학교')['키'].mean())

# 학교로 그룹화를 한 뒤 국어, 영어, 수학의 평균
print(df.groupby('학교')[['국어', '영어', '수학']].mean())

df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2] # 학년 컬럼 추가


#학년별 평균 데이터
print(df.groupby('학년').mean(numeric_only=True))

# 학교별, 학년별 평균 데이터
print(df.groupby(['학교', '학년']).mean(numeric_only=True))

# 학년별 그룹에서 키 큰 순으로
print(df.groupby('학년').mean(numeric_only=True).sort_values('키', ascending=False)) 

# 학교별, 학년별 계산 가능한 총합
print(df.groupby(['학교', '학년']).sum())


# 빈 문자열을 NA로 처리
df['SW특기'].apply(lambda s : pd.NA if s == '' else s)

# 학교로 그룹화를 한 뒤에 각 학교별 SW특기 데이터의 수를 구함
print(df.groupby('학교')['SW특기'].count())
print(df.groupby('학교')[['이름', 'SW특기']].count())

# 각 학교별 학년별 학생수
school = df.groupby('학교')
print(school['학년'].value_counts())

# 학교로 그룹화를 한 뒤에 북산고 학생들의 수 데이터를 비율로 구하기
print(school['학년'].value_counts(normalize=True).loc['북산고'])
