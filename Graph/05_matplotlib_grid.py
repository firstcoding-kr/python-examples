import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시 마이너스 폰트깨짐 해결

x = [1,2,3]
y = [2,4,8]

plt.plot(x, y)

plt.title('꺾은선 그래프')

#plt.grid()
#plt.grid(axis='x')
plt.grid(axis='y', color='purple', linestyle='--', linewidth=1)

plt.show()
