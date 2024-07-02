import rebound
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

# Create a rebound simulation
sim = rebound.Simulation()

# Add star
sim.add(m=mass_A)

# Add planet G1
sim.add(m=mass_G1, a=a_G1)

# Add moon F1
sim.add(m=mass_F1, a=a_F1)

# Integrate the simulation
times = np.linspace(0, period_G1, 1000)
positions_A = np.zeros((len(times), 3))
positions_G1 = np.zeros((len(times), 3))
positions_F1 = np.zeros((len(times), 3))
for i, time in enumerate(times):
    sim.integrate(time)
    positions_A[i] = sim.particles[0].xyz
    positions_G1[i] = sim.particles[1].xyz
    positions_F1[i] = sim.particles[2].xyz

# Plot orbits
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions_A[:, 0], positions_A[:, 1], positions_A[:, 2], label='Star A')
ax.plot(positions_G1[:, 0], positions_G1[:, 1], positions_G1[:, 2], label='Planet G1 Orbit')
ax.plot(positions_F1[:, 0], positions_F1[:, 1], positions_F1[:, 2], label='Moon F1 Orbit')
ax.scatter(0, 0, 0, color='yellow')
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
ax.set_title('3D Orbital Simulation using Rebound')
ax.legend()
plt.show()
