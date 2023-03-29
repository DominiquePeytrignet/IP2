import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define parameters for the torus
R = 5   # major radius
r = 2   # minor radius
u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]

# Parametric equations for the torus
x = (R + r*np.cos(v)) * np.cos(u)
y = (R + r*np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# Plot the torus
ax.plot_surface(x, y, z, cmap='plasma')

# Set axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Show the plot
plt.show()

