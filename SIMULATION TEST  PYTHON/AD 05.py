import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
c = 299792458     # speed of light (m/s)
M = 1.989e30      # mass of the black hole (kg)
RS = 2 * G * M / c**2  # Schwarzschild radius

# Grid parameters
size = 10 * RS  # size of the grid (meters)
num_points = 100  # number of grid points
x = np.linspace(-size, size, num_points)
y = np.linspace(-size, size, num_points)
X, Y = np.meshgrid(x, y)

# Function to calculate gravitational field
def gravitational_field(x, y):
    r = np.sqrt(x**2 + y**2)
    if r < RS:
        return np.array([0, 0])
    else:
        return -G * M / r**3 * np.array([x, y])

# Function to update plot
def update(frame):
    ax.clear()
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Calculate gravitational field at each point
    Gx, Gy = np.zeros_like(X), np.zeros_like(Y)
    for i in range(num_points):
        for j in range(num_points):
            G_vec = gravitational_field(X[i,j], Y[i,j])
            Gx[i,j], Gy[i,j] = G_vec[0], G_vec[1]

    # Plot the gravitational field
    ax.streamplot(x, y, Gx, Gy, color='black', linewidth=1)

    # Plot the black hole
    ax.add_patch(plt.Circle((0, 0), RS, color='black'))

# Initialize plot
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), interval=100)
plt.show()
