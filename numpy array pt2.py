import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

arr1 = np.array([1, 2, 3])
arr2 = np.array ([4, 5, 6])
arrc= np.concatenate((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 4, 4,])
x = np.where(arr==4)

print(x)

from numpy import random

x = random.randint(100)

print(x)