import numpy as np 
import matplotlib.pyplot as plt 
from statistics import mean

steps = 1000
iterations = 500

def step(n):
	if n > 0.5:
		return 1
	else:
		return -1 

def walk(x):
	for i in range(1, x.size):
		x[i] = x[i-1] + step(np.random.random(1))
	return x


xfinal = []
yfinal = []
distance = []

for i in range(iterations):
	x = walk(np.zeros(steps))
	y = walk(np.zeros(steps))
	xfinal.append(x[-1])
	yfinal.append(y[-1])
	distance.append(np.sqrt(x[-1]**2+y[-1]**2))
distance2 = [x**2 for x in distance]

plt.scatter(xfinal, yfinal)
plt.axis("equal")
plt.grid()
plt.show()




