import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.fill_between(x, y, color='skyblue', alpha=0.7)
plt.plot(x, y, color='darkblue')
plt.title("Area Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()