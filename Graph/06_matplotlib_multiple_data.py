import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시 마이너스 폰트깨짐 해결

# (가정) COVID-19 백신 종류별 접종인구
days = [1, 2, 3] # 1일, 2일, 3일

# 단위 만명
az = [2, 4, 8]
pfizer = [5, 1, 3]
moderna = [1, 2, 5]

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='morderna', marker='s', ls='-.')
plt.legend(ncol=3)
#plt.legend(ncol=3)

plt.title('COVID 백신별 접종인구')

plt.show()
