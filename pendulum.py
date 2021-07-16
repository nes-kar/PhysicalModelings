import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint

def pendulum_approx(y, t, g, l):
	theta, omega = y
	dydt = [omega, -g*theta/l]
	return dydt 

def pendulum_real(y, t, g, l):
	theta, omega = y
	dydt = [omega, -g*np.sin(theta)/l]
	return dydt 

g = 9.8
l = 1

initial_theta = 3*np.pi/7

y0 = [initial_theta, 0.0]

dt = 0.01
t = np.arange(0, 10 + dt, dt)
print(len(t))

sol1 = odeint(pendulum_real, y0, t, args=(g, l))
sol2 = odeint(pendulum_approx, y0, t, args=(g, l))

theta1 = sol1[:, 0]
theta2 = sol2[:, 0]

x1 = l*np.sin(theta1)
y1 = -l*np.cos(theta1)
x2 = l*np.sin(theta2)
y2 = -l*np.cos(theta2)

plt.style.use("dark_background")

fig, ax = plt.subplots()
ax = plt.axes(xlim = (-2,2), ylim=(-2,2))
ax.set_aspect("equal")
line1, = ax.plot([],[], "o-",lw=2, ms=5)
line2, = ax.plot([],[], "o-", lw=2)
degree = ax.text(0.02, 0.95, '', transform=ax.transAxes)


def init():
	line1.set_data([0, l*np.sin(initial_theta)], [0, -np.cos(initial_theta)*l])
	line2.set_data([0, l*np.sin(initial_theta)], [0, -np.cos(initial_theta)*l])
	degree.set_text("")
	return line1, line2, degree

def anim(i):
	line1.set_data([0, x1[i]], [0, y1[i]])
	line2.set_data([0, x2[i]], [0, y2[i]])
	degree.set_text(r"$Phase$ $Angle,$ $\theta$ : {}".format(round(theta1[i] - theta2[i], 2)))
	return line1, line2, degree
plt.axis("off")
anim = animation.FuncAnimation(fig, anim, frames=len(t), blit=True, init_func=init)
anim.save("ApproxVsReal.mp4", fps=60, dpi = 150)
