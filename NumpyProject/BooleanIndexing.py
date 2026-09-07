"""
Exercise 3 — Boolean Indexing & where()

Create:

scores = np.array([45, 67, 82, 39, 91, 56, 74, 30])
Tasks
Find all scores greater than 60.
Find all scores between 50 and 80.
Count how many scores are greater than 60.
Replace scores below 40 with 0.
Create a new array where:
score ≥ 50 → 1
score < 50 → 0

"""
import numpy as np
scores = np.array([45, 67, 82, 39, 91, 56, 74, 30])

#1 Task
arr=scores[scores>60]
print(arr)

#2 Task
ar=scores[(scores>50) & (scores<80)]

print(ar)

#3 Task
print(len(arr))

#4 Task
arr1=np.where(scores<40,0,scores)
print(arr1)
#5 Task

arr2=np.where(scores>=50,1,0)
print(arr2)
