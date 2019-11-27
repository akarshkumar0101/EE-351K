import numpy as np


r = np.random.normal(size = 10000)

rsqr = r ** 2

rcube = r ** 3
rfour = r ** 4

print(np.average(rcube))
print(np.average(rfour))


#print(r)

