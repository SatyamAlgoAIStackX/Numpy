"""
Exercise 2 — Statistics of Features

Use the same X.

Tasks

Calculate:

Average hours studied.
Average attendance.
Average previous score.
Maximum value of each feature
Minimum value of each feature.
Standard deviation of each feature.
"""
import numpy as np

x = np.array([
    [2, 75, 60],
    [4, 80, 65],
    [5, 85, 72],
    [7, 90, 85],
    [8, 95, 90]
])
#1 Task
avg= np.mean(x[:,0])
print('Average hours studied: ',avg)

#2 Task
avg= np.mean(x[:,1])
print('Average attendance: ',avg)

#3 Task
avg= np.mean(x[:,2])
print('Average previous marks: ',avg)

#4 Task
maX = np.max(x,axis=0)
print("Maximum value of each feature: ",maX)

#5 Task
miN= np.min(x,axis=0)
print("Minimum value of each feature: ",miN)

#6 Task
stdv= np.std(x,axis=0)
print("standard Deviation of each features: ",stdv)





