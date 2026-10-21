import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title("Bar Plot")

plt.subplot(2, 2, 4)
plt.hist(y, bins=5)
plt.title("Histogram")

plt.tight_layout()
plt.show()