# Comparing how fast numpy is...
## List
a = [i for i in range(10000000)]
b = [i for i in range(10000000)]
sum = []

import time
start=time.time()
for k in range(len(a)):
    sum.append(a[k]+b[k])
print(time.time()-start)

 ## Numpy Array
import numpy as np
x = np.arange(10000000)
y = np.arange(10000000)
strt=time.time()
s = x+y
print(time.time()-strt)



