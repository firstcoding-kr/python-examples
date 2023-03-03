# 리스트 컴프리헨션을 활용하여 홀수만 출력
odd_numbers = [num for num in range(1, 11) if num % 2 != 0]

print(odd_numbers)

# 리스트 컴프리헨션을 사용하지 않은 코드
odd_numbers = []
for num in range(1, 11):
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)
