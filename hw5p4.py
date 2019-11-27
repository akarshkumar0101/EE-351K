import random


def experiment():
	s=0
	a = random.randint(1,4)#1 to 4
	s+=a
	if(a>3):
		return s
	b = random.randint(1,5)# 1 to 5
	s+=b
	if(b>3):
		return s
	c = random.randint(1,6)# 1 to 6
	s+=c
	print(a)
	print(b)
	print(c)
	print("")
	return s

def averageVal(num):
	s = 0.0
	for x in range(num):
		s+=experiment()
	return s/num


print(averageVal(10000))