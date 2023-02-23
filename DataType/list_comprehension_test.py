import time

test_size = 1000000

# 리스트 컴프리헨션으로 1부터 1000000 수 중에서 짝수를 선택
start_time = time.time()
even_numbers = [num for num in range(1, test_size) if num % 2 == 0]
end_time = time.time()
print("List comprehension took {:.10f} seconds".format(end_time - start_time))

# 일반적인 for문으로 1부터 1000000까지의 수 중에서 짝수를 선택
start_time = time.time()
even_numbers = []
for num in range(1, test_size):
    if num % 2 == 0:
        even_numbers.append(num)
end_time = time.time()
print("For loop took {:.10f} seconds".format(end_time - start_time))
