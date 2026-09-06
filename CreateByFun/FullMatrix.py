import numpy as np
# Here we are creating matrix with any other number like 3,5 ,80 ...
'''
way of writing full method in numpy python
np.full(shape,number,dtype,order)

'''
arr = np.full((3,3), 7, dtype=int, order='C')
print(arr)