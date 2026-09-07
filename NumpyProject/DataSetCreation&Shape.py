"""
Exercise 1 — Dataset Creation & Shape

Create a NumPy array representing 5 students and 3 features:

Hours studied
Attendance %
Previous score

Example data:
import numpy as np

X = np.array([
    [2, 75, 60],
    [4, 80, 65],
    [5, 85, 72],
    [7, 90, 85],
    [8, 95, 90]
])
Tasks
Find the shape of X.
Find the number of rows and columns separately.
Extract the first student.
Extract the Hours studied column.
Extract the last two students.
Extract the first two features of every student.

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
print("Shape: ",np.shape(x))
#2 TasK
x_rows, x_colm = np.shape(x)
print("Rows: ",x_rows)
print("colm: ",x_colm)

#3 Task
print("First student: ",x[0])
 #4 Task
print("Hours studied colums: ",x[:,1])

#5 Task
print("last two student details: ",x[3:])

#6 task
print("First two features Of Every student: ",x[:,1:3])
