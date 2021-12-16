# Computational Physics / Giordano : Ex.(4.1)

import matplotlib.pyplot as plt 
from math import *


x, y = 1, 0 # AU unit
vy, vx = 2*pi, 0 # AU / year

dt = 0.002

X = [x]
Y = [y]

t = 0

while t < 1:
	r = sqrt(x**2 + y**2)
	vx += - 4*pi**2 * x*dt / (r**3)
	vy += - 4*pi**2 * y*dt / (r**3)
	x += vx * dt
	y += vy *dt
	X.append(x)
	Y.append(y)
	t += dt
	
plt.plot(X, Y)
plt.gca().set_aspect("equal") # Set aspect ratio to show circles
plt.show()