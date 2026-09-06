import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9],[22,3,4]]) # This is 2D array 
# Here we are using reshaping method to reshape 
arr = a.reshape(2,6)
arr1 = a.reshape(6,2)
print(arr, arr1) 
# actually it is used for reshaping the array provided it must be row*column is equal to total number of elements