import pandas as pd

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

df = pd.DataFrame(data)

# 1) 전체 데이터 중에서 '영화' 정보만 출력하시오.

# 2) 전체 데이터 중에서 '영화', '평점' 정보를 출력하시오.

# 3) 2015년 이후 개봉한 영화 데이터 중에서 '영화', '개봉 연도' 정보를 출력하시오

# 4) 주어진 계산식을 참고하여 '추천 점수' 컬럼을 추가하시오.
# 추천점수 = (관객수 1761 * 평점 8.88) // 100 = 156

# 5) 전체 데이터를 '개봉 연도' 기준 내림차순으로 정렬하시오.
