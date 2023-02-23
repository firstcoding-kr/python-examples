'''
집합(Set)
 - 중복된 값을 허용하지 않는다.
 - 값의 순서를 보장하지 않는다.
 - 인덱싱이나 슬라이싱이 불가능.
 - 합집합, 교집합, 차집합 등 다양한 집합 연산을 지원.
'''

# 집합 생성
fruits = {'apple', 'banana', 'kiwi', 'orange'}
print(fruits)       # {'kiwi', 'banana', 'orange', 'apple'}

# 값 추가
fruits.add('grape')
print(fruits)       # {'kiwi', 'grape', 'banana', 'orange', 'apple'}

# 값 제거
fruits.remove('kiwi')
print(fruits)       # {'grape', 'banana', 'orange', 'apple'}

# 합집합 연산
fruits1 = {'apple', 'banana', 'kiwi', 'orange'}
fruits2 = {'banana', 'kiwi', 'strawberry'}
union_fruits = fruits1.union(fruits2)
print(union_fruits)  # {'banana', 'apple', 'kiwi', 'orange', 'strawberry'}

# 교집합 연산
intersection_fruits = fruits1.intersection(fruits2)
print(intersection_fruits)  # {'kiwi', 'banana'}

# 차집합 연산
difference_fruits = fruits1.difference(fruits2)
print(difference_fruits)    # {'apple', 'orange'}

# 부분집합 연산
print(fruits2.issubset(fruits1))  # False
print(fruits2.issubset(union_fruits))  # True
