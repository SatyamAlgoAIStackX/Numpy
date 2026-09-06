import numpy as np
# Create zeros matrix by numpy method zeros 
# Zeros(shape, dtype, order) ->> This is the way of writing zeros method
arr = np.zeros((3,3)) # 1st method
print(arr)
arr1 = np.zeros((2,6), dtype=int, order='F') # 2nd method 
print(arr1)
arr2 = np.zeros((2,6), dtype=int, order='C') 
print(arr2)