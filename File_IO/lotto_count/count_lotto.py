
lotto = [] # 각 회차별 당첨 번호 리스트가 리스트로 저장된다 (2차원 리스트)

# 당첨 이력 파일에서부터 데이터를 한 줄씩 리스트로 읽어온다.
f = open('lotto.txt', 'r')
lines = f.readlines()
f.close()

for l in lines:
    n_removed = l.replace('\n','') # 줄바꿈 \n을 없앤다
    splitted = n_removed.split('\t') # 탭 기준으로 잘라서 리스트로
    lotto.append(splitted) # 만들어진 한 회차 리스트를 lotto 리스트에 추가

# 초기화된 로또번호 집계 딕셔너리
sum_dict = {}
for i in range(1, 46):
    sum_dict[i] = 0

# 각 번호별 당첨 번호 출현 수를 집계한다.
for game in lotto:
    for game_number in game:
        sum_dict[int(game_number)] += 1

# 출현 횟수를 중복을 제거하고 정렬한다. (set으로 변환하면 중복 제거됨)
sorted_count = sorted(set(sum_dict.values()), reverse=True)

# 출현 횟수에 해당하는 번호를 찾아 출력한다.
for cnt in sorted_count:
    print(f'{cnt}번 나온 번호:', end=' ')
    for (num_key, counted_value) in sum_dict.items():
        if counted_value == cnt:
            print(f'{num_key}', end=' ')
    print('')
