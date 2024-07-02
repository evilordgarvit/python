import math

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)

# Masses
mass_A = 40000  # Earth masses
mass_G1 = 1.25  # Earth masses
mass_F1 = 0.15  # Earth masses

# Orbital periods (in seconds)
period_G1 = 70 * 24 * 3600  # 70 days converted to seconds
period_F1 = 7 * 24 * 3600   # 7 days converted to seconds

# Calculate semi-major axes
a_G1 = ((G * mass_A * (period_G1 ** 2)) / (4 * math.pi ** 2)) ** (1/3)
a_F1 = ((G * mass_G1 * (period_F1 ** 2)) / (4 * math.pi ** 2)) ** (1/3)

# Print semi-major axes
print("Semi-major axis of G1's orbit around A:", a_G1, "meters")
print("Semi-major axis of F1's orbit around G1:", a_F1, "meters")

