import pandas as pd
# 문자열 함수 활용
# 참고 https://pandas.pydata.org/docs/user_guide/text.html#method-summary

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

# 송씨 성을 가진 사람
df_filter = df['이름'].str.startswith('송')
print(df[df_filter])

# 이름에 '태'가 들어가는 사람
df_filter = df['이름'].str.contains('태')
print(df[df_filter])

# 이름에 '태'가 들어가지 않는 사람
print(df[~df_filter])

# SW특기가 Python, Java인 사람
langs = ['Python', 'Java']
df_filter = df['SW특기'].isin(langs)
print(df[df_filter])

# 대소문자 무시
langs = ['python', 'java']
df_filter = df['SW특기'].str.lower().isin(langs)
print(df[df_filter])

# Java가 포함된 문자열
df_filter = df['SW특기'].str.contains('Java', na=False)
print(df[df_filter])

