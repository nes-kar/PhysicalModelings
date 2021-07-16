import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation
from scipy.integrate import odeint
from matplotlib import cm
from numpy.linalg import norm

a = 20000
b = 0.002
g = 9.81

def SolveSystem(V, t, g, a, b): # https://www.wolframcloud.com/obj/matt68/Published/bouncechaos.nb
	x, Vx, y, Vy = V
	dxdt = [Vx, -a*max(0, x**2 + y**2 - 1)*x - b*Vx]
	dydt = [Vy, -g-a*max(0, x**2 + y**2 - 1)*y - b*Vy]
	return np.array([dxdt, dydt]).flatten() # For any t, returns: [x(t), Vx(t), y(t), Vy(t)]

V1 = [0.001, 0, 0.5, 0] # Initial Conditions: x0, Vx0, y0, Vy0
V2 = [0.0015, 0, 0.5, 0]

t = np.linspace(0, 10, 1000)

sol1 = odeint(SolveSystem, V1, t, args=(g, a, b))
sol2 = odeint(SolveSystem, V2, t, args=(g, a, b))

x1 = sol1[:, 0]
y1 = sol1[:, 2]

x2 = sol2[:, 0]
y2 = sol2[:, 2]

bgColor = "#0D2368"
fig, ax = plt.subplots()
ax = plt.axes(xlim = (-2,2), ylim=(-2,2))
ax.set_aspect("equal")
ax.set_facecolor(bgColor)
sphere = plt.Circle((0, 0), 1.05, fc=ax.get_facecolor(), ec="#92CFDF")
ball1 = plt.Circle((V1[0], V1[2]), 0.05, zorder=10, color="red")
ball2 = plt.Circle((V2[0], V2[2]), 0.05, zorder=10, color="yellow")
path1, = ax.plot([V1[0]], [V1[2]], lw=0.5, color="red", alpha=0.5)
path2, = ax.plot([V2[0]], [V2[2]], lw=0.5, color="yellow", alpha=0.5)


def init():
	ax.add_patch(ball1)
	ax.add_patch(sphere)
	ax.add_patch(ball2)
	return ball1, sphere,ball2
def anim(i):
	ball1.center = (x1[i], y1[i])
	ball2.center = (x2[i], y2[i])
	path1.set_data(x1[:i], y1[:i])
	path2.set_data(x2[:i], y2[:i])
	return ball1, path1, path2, ball2
plt.axis("off")

anim = animation.FuncAnimation(fig, anim, frames=len(t), blit=True, init_func=init)
#anim.save("ballsInSphere.mp4", fps=60, dpi=200, savefig_kwargs=dict(facecolor=bgColor))
plt.show()
