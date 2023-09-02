import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시 마이너스 폰트깨짐 해결

x = [1,2,3]
y = [2,4,8]

# 그래프 크기, 배경색 지정
plt.figure(figsize=(10, 5), facecolor='lightgray')

plt.plot(x, y, label='범례', color='pink', linewidth=2, marker='o', markersize=10, markeredgecolor='red', markerfacecolor='yellow', linestyle=':')
plt.legend(loc='best') # 범례 표시
# 범례 표시위치 참고: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
# 마커 스타일 참고: https://matplotlib.org/stable/api/markers_api.html
# 라인 스타일 참고: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# 컬러: https://matplotlib.org/stable/gallery/color/named_colors.html
# 투명도 aplha 0~1

plt.title('꺾은선 그래프')

plt.show()
