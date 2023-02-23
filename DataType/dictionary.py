# 딕셔너리 생성
my_dict = {'name': 'John', 'age': 30, 'city': 'Seoul'}

# 딕셔너리 출력
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'Seoul'}

# 인덱싱(Indexing)
print(my_dict['name'])  # John

# 값 추가(Add)
my_dict['job'] = 'Developer'
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'Seoul', 'job': 'Developer'}

# 값 변경(Modify)
my_dict['age'] = 35
print(my_dict)  # {'name': 'John', 'age': 35, 'city': 'Seoul', 'job': 'Developer'}

# 값 삭제(Remove)
del my_dict['job']
print(my_dict)  # {'name': 'John', 'age': 35, 'city': 'Seoul'}

# 딕셔너리 내용 비우기(Clear)
my_dict.clear()
print(my_dict)  # {}

# 딕셔너리 삭제
del my_dict
# print(my_dict)  # NameError: name 'my_dict' is not defined
