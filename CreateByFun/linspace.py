# This is important method in numpy python 
"""
By using linspace we are generating floating number  between
two Number
--- Syntax for linspace are as---
np.linspace(start,stop,num,endpoint,retstep,dtype)
num-- Number of sample to generate
endpoint-- It store bool value , if true it include stop value otherwise not and default True
retstep-- It also store Bool value, But if it is true return tuple(sample,step--step between cosecutive two number)
"""
import numpy as np
arr = np.linspace(2,3,retstep=True) # Default it generate 50 numbers
print(arr)
arr1 = np.linspace(4,6,10,endpoint=False,retstep=True)
print(arr1)