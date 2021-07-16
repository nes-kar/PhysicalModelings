import numpy as np 
import matplotlib.pyplot as plt 

modulo = 500
x = 34
phi = 360/modulo

angles = np.radians(np.arange(0, modulo)*phi)

points = np.array([[np.cos(angles)],[np.sin(angles)]])

def draw(x, mod, lim=500):
	for i in range(1,lim):
		p = angles[i % mod] 
		p2 = [(p*x) % mod]
		a = [np.cos(p), np.cos(p2)]
		b = [np.sin(p), np.sin(p2)]
		plt.plot(a, b, "#AB894C" , lw=0.3)

plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(xlim=(-1.2,1.2), ylim=(-1.2,1.2))
ax.set_aspect('equal')
ax.axis("off")
draw(x, modulo)

plt.show()

