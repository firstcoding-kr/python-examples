#튜플(Tuple) 예제

# --- 생성방법 ---

# 튜플 생성 방법 1
my_tuple = (1, 2, 3)

# 튜플 생성 방법 2
my_tuple = 1, 2, 3

# 튜플 생성 방법 3
my_tuple = tuple([1, 2, 3])

# --- 기본예제 ---

# 과일 정보를 담은 튜플 생성
fruit_tuple = ("사과", "바나나", "딸기", "오렌지")

# 튜플의 원소 출력
for fruit in fruit_tuple:
    print(fruit)

# --- 예제2 ---

# 국가와 수도 정보를 담은 튜플 생성
country_capital = (("한국", "서울"), ("미국", "워싱턴 D.C."), ("일본", "도쿄"), ("중국", "베이징"))

# 튜플의 원소 출력
for country, capital in country_capital:
    print(f"{country}의 수도는 {capital}입니다.")

country_capital[0][1] = "수도를 바꾸자" # 튜플은 값을 수정할 수 없으므로 에러가 발생한다.
