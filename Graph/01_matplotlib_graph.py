import matplotlib.pyplot as plt
# 설치: pip install matplotlib
# 참고: https://matplotlib.org/stable/plot_types/index.html

# 데이터 준비
x = [1, 2, 3, 4, 5]  # x 축 데이터
y = [2, 4, 6, 8, 10]  # y 축 데이터

# 그래프 그리기
plt.plot(x, y)

# 그래프 제목 및 축 레이블 추가
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 보이기
plt.show()
