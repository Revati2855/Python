import numpy as np

arr = np.arange(1, 13)
print("One-dimensional array:")
print(arr)

print("\n2 × 6 Matrix:")
print(arr.reshape(2, 6))

print("\n3 × 4 Matrix:")
print(arr.reshape(3, 4))

print("\n4 × 3 Matrix:")
print(arr.reshape(4, 3))
