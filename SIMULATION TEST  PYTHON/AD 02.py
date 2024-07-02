import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
earth_mass = 5.972e24  # kg

# Masses
mass_A = 333060 * earth_mass  # Earth masses
mass_G1 = 1 * earth_mass  # Earth masses
mass_F1 = 0.0123031469 * earth_mass  # Earth masses

# Orbital periods (in seconds)
period_G1 = 365.25 * 24 * 3600  # 70 days converted to seconds
period_F1 = 27.3 * 24 * 3600   # 7 days converted to seconds

# Calculate semi-major axes
a_G1 = ((G * mass_A * (period_G1 ** 2)) / (4 * np.pi ** 2)) ** (1/3)
a_F1 = ((G * mass_G1 * (period_F1 ** 2)) / (4 * np.pi ** 2)) ** (1/3)

# Generate time array
t = np.linspace(0, period_G1, 1000)

# Calculate angles for planet and moon orbits
theta_G1 = 2 * np.pi * t / period_G1
theta_F1 = 2 * np.pi * t / period_F1

# Calculate positions
x_G1 = a_G1 * np.cos(theta_G1)
y_G1 = a_G1 * np.sin(theta_G1)

x_F1 = x_G1 + a_F1 * np.cos(theta_F1)
y_F1 = y_G1 + a_F1 * np.sin(theta_F1)

# Plot orbits
plt.figure(figsize=(8, 8))
plt.plot(x_G1, y_G1, label='Planet G1 Orbit')
plt.plot(x_F1, y_F1, label='Moon F1 Orbit')
plt.scatter(0, 0, color='yellow', label='Star A')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Orbital Simulation')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()
