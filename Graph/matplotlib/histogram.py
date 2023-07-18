import matplotlib.pyplot as plt

data = [1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 10]

plt.hist(data, bins=5)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
