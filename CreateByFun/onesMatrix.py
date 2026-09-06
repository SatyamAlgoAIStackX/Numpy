import numpy as np
# Create matrix having 1 everywhere using dimenstion
arr = np.ones((4,4), dtype=int, order="C")
print(arr)
# We are not giving dtype then by default it is float dtype