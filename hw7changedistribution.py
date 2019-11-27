import numpy as np
from random import seed
from random import random


l=5

def f(x):
	y = np.log(1-x)
	y = -y/l
	return y

m=10000

count=0
thresh=0.9

for i in range(m):
	r = random()
	r = f(r)
	if(r<thresh):
		count+=1

print(float(count)/m)

