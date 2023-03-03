
# for문을 활용한 리스트 탐색 및 합계 구하기
numbers = [1, 2, 3, 4, 5]
sum = 0

for num in numbers:
    sum += num

print("숫자들의 합:", sum)

print("-" * 20)

start = 1
end = 10 # range함수는 end 미만의 수까지 생성된다.
step = 2 # step을 2로 하면 시작부터 2씩 증가한다.
for num in range(start, end, step):
    print(num)

print("-" * 20)

# for문을 활용한 딕셔너리 탐색
person = {"name": "Alice", "age": 25, "gender": "female"}

for key, value in person.items():
    print(key, ":", value)
