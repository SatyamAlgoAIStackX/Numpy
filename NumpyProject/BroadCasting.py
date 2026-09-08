"""
Exercise 4 — Broadcasting & Normalization

Create:

X = np.array([
    [10, 100],
    [20, 200],
    [30, 300],
    [40, 400]
])

Here:

Column 1 = Feature 1
Column 2 = Feature 2
Tasks
Calculate the mean of each feature.
Subtract the mean from every row.
Calculate the standard deviation of each feature.
Perform standardization:
     
     z=x-mue/sigma

Check the mean of your standardized data.

You should get values very close to 0.

"""
import numpy as np
x = np.array([
    [10, 100],
    [20, 200],
    [30, 300],
    [40, 400]
])
#1 Task
Features = np.mean(x,axis=0)
print(Features)

#2 Task
newarr = x-Features # Here broadcasting rule is applied
print(newarr)

#3 Task 
Std_vev=np.std(x,axis=0)
print(Std_vev)

#4 Task
z = (x - np.mean(x))/np.std(x)
print(z)
# And
z = newarr/Std_vev
print(z)



