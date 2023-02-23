import timeit

# 리스트와 집합에 10,000개의 무작위 값 추가
my_list = [i for i in range(10000)]
my_set = set(my_list)

# timeit 모듈의 timeit() 함수를 이용하여 두 자료형에서 값을 검색하는 데 걸리는 시간을 측정
# 리스트에서 값 검색
list_time = timeit.timeit(stmt='9999 in my_list', globals=globals(), number=10000)

# 집합에서 값 검색
set_time = timeit.timeit(stmt='9999 in my_set', globals=globals(), number=10000)

# 검색 결과 출력
print(f'List search time: {list_time}')
print(f'Set search time: {set_time}')

#집합 자료형은 해시 테이블을 이용하여 빠른 검색을 지원하기 때문에 리스트 자료형보다 검색 속도가 빠르다. 
