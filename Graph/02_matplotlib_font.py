import matplotlib.pyplot as plt
import matplotlib
# 설치: pip install matplotlib
# 참고: https://matplotlib.org/stable/plot_types/index.html

# 폰트에 대한 전역 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시 마이너스 폰트깨짐 해결

# 각 영역 별 개별적으로 딕셔너리를 지정하여 폰트를 설정할 수 있다.
fontdict = {'family':'Malgun Gothic', 'size':20}

# 데이터 준비
x = [1, 2, 3, 4, 5]  # x 축 데이터
y = [2, 4, 6, 8, 10]  # y 축 데이터

# 그래프 그리기
plt.plot(x, y, label='sample data')
# 범례 보이기
plt.legend(loc='lower right')

# 그래프 제목 및 축 레이블 추가
plt.title('심플 라인 그래프', fontdict=fontdict)
plt.xlabel('X축', fontdict=fontdict, color='red', loc='right') # loc: left center rignt
plt.ylabel('Y축', fontdict=fontdict, color='#0000FF', loc='top') # top, center, bottom

# 축의 간격(수치) 지정
plt.xticks([1,3,5])
plt.yticks([3,6,9,12])

# 그래프 보이기
plt.show()
