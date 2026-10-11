import numpy as np

arr = np.array([10, 20, 30, 40])

labels = np.array(['A', 'B', 'C', 'D'])

print("Array:", arr)
print("Character Labels:", labels)

for i in range(len(arr)):
    print(labels[i], "=", arr[i])
