import numpy as np, matplotlib.pyplot as plt
coords = np.linspace(-2, 2, 101)
X, Y = np.meshgrid(coords[::5], coords[::5]) # Coarse grid for vector field
R = np.sqrt(X**2 + Y**2)
Z = np.exp(-R**2)

ds = coords[5] - coords[0] # Coarse grid spacing
dX, dY = np.gradient(Z, ds) # Calculate gradient.

plt.quiver(X, Y, dX.transpose(), dY.transpose(), scale=25, cmap='hot')
plt.show()