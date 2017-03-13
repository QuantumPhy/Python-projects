import math
import numpy as np
def fibon_direkt(n):
	fi=(1+math.sqrt(5))/2
	return math.floor(math.pow(fi,n)/math.sqrt(5)+1/2)

print(fibon_direkt(35))

A=np.array([[1,2],[3,4]])
print(A)