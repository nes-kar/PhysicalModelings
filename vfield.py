import numpy as np
import matplotlib.pyplot as plt 


coords = np.linspace(-5,5,50)

k = 8.987*10**9
q = 1

X, Y = np.meshgrid(coords, coords)
R = np.sqrt(X**2+Y**2)


dX = k*q*X/R**3
dY = k*q*Y/R**3



length = np.sqrt(dX**2 + dY**2)

fig = plt.subplots()
ax = plt.axes()

plt.set_cmap("coolwarm")
ax.streamplot(X, Y, dX, dY, cmap="coolwarm")
plt.show()