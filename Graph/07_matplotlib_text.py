import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시 마이너스 폰트깨짐 해결

x = [1,2,3]
y = [2,4,8]

plt.plot(x, y, marker='o')

# 그래프에 텍스트 찍어보기
plt.text(2, 2, 'Text', color='green')

# 마커 위치에 텍스트 찍기
for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.2, txt, ha='center', color='red')

# ha = 수평정렬
# y에 0.2를 더한 이유는 보기 좋도록 offset을 이동시킨 것

plt.title('꺾은선 그래프')

plt.show()
