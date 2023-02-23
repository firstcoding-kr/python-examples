# list 자료형
'''
 - 값들의 순서를 보장한다.
 - 값의 중복이 가능하므로, 같은 값을 여러 번 사용할 수 있다.
 - 인덱스를 이용하여 원하는 위치에 값을 삽입하거나 삭제할 수 있다.
 - 여러 가지 데이터 타입을 함께 사용할 수 있다.
'''

# 리스트 생성
fruits = ['apple', 'banana', 'kiwi', 'orange']

# 인덱싱
print(fruits[0])    # apple
print(fruits[-1])   # orange

# 슬라이싱
print(fruits[1:3])  # ['banana', 'kiwi']

# 값 추가
fruits.append('grape')
print(fruits)       # ['apple', 'banana', 'kiwi', 'orange', 'grape']

# 값 삭제
fruits.remove('kiwi')
print(fruits)       # ['apple', 'banana', 'orange', 'grape']

# 리스트의 길이
print(len(fruits))  # 4
