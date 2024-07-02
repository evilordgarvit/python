import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
c = 299792458     # speed of light (m/s)
M = 1.989e30      # mass of the black hole (kg)
RS = 2 * G * M / c**2  # Schwarzschild radius

# Function to calculate Schwarzschild metric components
def schwarzschild_metric(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    gtt = np.where(r < RS, 0, 1 - RS / r)
    return gtt, x, y, z

# Create a grid
size = 20  # size of the grid (meters)
num_points = 100  # number of grid points
x = np.linspace(-size, size, num_points)
y = np.linspace(-size, size, num_points)
z = np.linspace(-size, size, num_points)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate Schwarzschild metric components
GTT, X, Y, Z = schwarzschild_metric(X, Y, Z)

# Plot the curvature of space-time with grid lines
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the space-time fabric as a grid sheet
for i in range(num_points):
    ax.plot(X[:, i, 0], Y[:, i, 0], Z[:, i, 0], color='lightgray', alpha=0.2)
    ax.plot(X[i, :, 0], Y[i, :, 0], Z[i, :, 0], color='lightgray', alpha=0.2)

# Plot the curvature of space-time as color map
surf = ax.scatter(X, Y, Z, c=GTT.flatten(), cmap='viridis', s=2)

# Plot the black hole as a point
ax.scatter(0, 0, 0, color='black', s=100)

# Add a color bar
cbar = fig.colorbar(surf)
cbar.set_label('Curvature')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Space-Time Fabric and Curvature around a Black Hole')

plt.show()
