import numpy as np 
from matplotlib import animation
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

xs = []
ys = []

fig = plt.figure()
ax = plt.axes(xlim=(-2,2), ylim=(-2,2))
ax.set_aspect('equal')
sun = plt.Circle((0, 0), 0.1, color="yellow")
earth = plt.Circle((0, 1), 0.03, color="cyan")
venus = plt.Circle((0, 0.723), 0.03, color="orange")
line, = ax.plot([], [], lw=0.1, color="white", alpha=0.65) 

def init():
	earth.center = (0,1)
	sun.center = (0, 0)
	venus.center = (0, 0.723)
	line.set_data([], [])
	ax.add_patch(earth)
	ax.add_patch(sun)
	ax.add_patch(venus)
	return earth, sun, venus, line
def animate(i):
	t = 0.05 * i
	omega1 = 1
	omega2 = 35/30
	x1 = np.sin(t*omega1)
	y1 = np.cos(t*omega1)
	earth.center = (x1, y1)
	x2 = 0.723*np.sin(t*omega2)
	y2 = 0.723*np.cos(t*omega2)
	venus.center = (x2, y2)
	xs.append([x1, x2])
	ys.append([y1, y2])
	line.set_data(xs, ys)
	return earth, sun, venus, line
plt.axis("off")
anim = animation.FuncAnimation(fig, animate, init_func=init,
	blit=True, interval=10)

plt.show()