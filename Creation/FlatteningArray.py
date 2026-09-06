import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9],[22,3,4]]) # This is 2D array 
# By using reshape method we are flattening the array
arr= a.reshape(-1)
print(arr)