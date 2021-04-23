import numpy as np 
import time
import sys

size=1000000

l1=range(size)
l2=range(size)

# a1=np.arange(size)
# a2=np.arange(size)

t=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
m=1000
print(f"The result time is {(time.time()-t)*m}")

# t=time.time()
# result=a1+a2
# print(result)
# print(f"The result time is {(time.time()-t)*m}")


