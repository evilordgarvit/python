import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
M_bh = 15 * 1.989e30  # mass of Cygnus X-1 in kg
M_star = 20 * 1.989e30  # mass of HD 226868 in kg

# Initial conditions
r_star = np.array([0, 0, 0], dtype=float)  # initial position of the star
v_star = np.array([0, 200000/3.6, 0], dtype=float)  # initial velocity of the star, converting 200000 km/h to m/s
r_bh = np.array([0, 0, 0], dtype=float)  # initial position of the black hole
v_bh = np.array([0, 0, 0], dtype=float)  # initial velocity of the black hole

# Time parameters
dt = 0.01  # time step
t_max = 1000  # maximum simulation time
timesteps = int(t_max / dt)  # number of timesteps

# Simulation
r_star_history = np.zeros((timesteps, 3), dtype=float)  # history of star positions
r_bh_history = np.zeros((timesteps, 3), dtype=float)  # history of black hole positions

for i in range(timesteps):
    # Calculate gravitational force on the star
    r_diff = r_bh - r_star
    distance = np.linalg.norm(r_diff)
    if distance == 0:
        F_gravity = np.zeros(3, dtype=float)  # Avoid division by zero
    else:
        F_gravity = G * M_bh * M_star / distance**3 * r_diff
    
    # Update star's position and velocity using Euler-Cromer method
    v_star += F_gravity / M_star * dt
    r_star += v_star * dt
    
    # Spiral inward
    r_star /= 1.01  # Decrease the distance to simulate spiraling inward
    
    # Save positions
    r_star_history[i] = r_star
    r_bh_history[i] = r_bh

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot star trajectory
ax.plot(r_star_history[:, 0], r_star_history[:, 1], r_star_history[:, 2], label='Star trajectory')

# Plot black hole position
ax.scatter(r_bh_history[-1, 0], r_bh_history[-1, 1], r_bh_history[-1, 2], color='red', label='Black hole position')

ax.set_xlabel('X position (m)')
ax.set_ylabel('Y position (m)')
ax.set_zlabel('Z position (m)')
ax.set_title('Trajectory of Star falling into Black Hole')
ax.legend()

plt.show()
