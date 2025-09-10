import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([[1, 2, 3, 4], [5, 6, 7,]])

print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.seshape (4, 3)

print(newarr)

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

arr1 = np.array([1, 2, 3])
arr2 = np.array ([4, 5, 6])
arrc= np.concatenate((arr1, arr2))
print(arr)