import numpy as np

A = np.array([[10, 20],
              [30, 40]])

B = np.array([[2, 4],
              [5, 8]])

print("Array A:")
print(A)

print("Array B:")
print(B)

print("Addition:")
print(np.add(A, B))

print("Subtraction:")
print(np.subtract(A, B))

print("Multiplication:")
print(np.multiply(A, B))

print("Division:")
print(np.divide(A, B))

print("Transpose of A:")
print(np.transpose(A))

print("Exponential of A:")
print(np.exp(A))
