import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
earth_mass = 5.972e24  # kg

# Masses
mass_A = 40000 * earth_mass  # Earth masses
mass_G1 = 1.25 * earth_mass  # Earth masses
mass_F1 = 0.15 * earth_mass  # Earth masses

# Orbital periods (in seconds)
period_G1 = 70 * 24 * 3600  # 70 days converted to seconds
period_F1 = 7 * 24 * 3600   # 7 days converted to seconds

# Calculate semi-major axes
a_G1 = ((G * mass_A * (period_G1 ** 2)) / (4 * np.pi ** 2)) ** (1/3)
a_F1 = ((G * mass_G1 * (period_F1 ** 2)) / (4 * np.pi ** 2)) ** (1/3)

# Inclination angles (in radians)
inclination_G1 = np.radians(30)  # Assume 30 degrees for planet G1
inclination_F1 = np.radians(60)  # Assume 60 degrees for moon F1

# Generate time array
t = np.linspace(0, period_G1, 1000)

# Calculate angles for planet and moon orbits
theta_G1 = 2 * np.pi * t / period_G1
theta_F1 = 2 * np.pi * t / period_F1

# Calculate positions in xy-plane
x_G1 = a_G1 * np.cos(theta_G1)
y_G1 = a_G1 * np.sin(theta_G1)

x_F1 = x_G1 + a_F1 * np.cos(theta_F1)
y_F1 = y_G1 + a_F1 * np.sin(theta_F1)

# Calculate positions in z-direction
z_G1 = np.zeros_like(x_G1)
z_F1 = a_F1 * np.sin(inclination_F1) * np.sin(theta_F1)

# Plot orbits
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_G1, y_G1, z_G1, label='Planet G1 Orbit')
ax.plot(x_F1, y_F1, z_F1, label='Moon F1 Orbit')
ax.scatter(0, 0, 0, color='yellow', label='Star A')
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
ax.set_title('3D Orbital Simulation')
ax.legend()
plt.show()
