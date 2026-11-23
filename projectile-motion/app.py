import numpy as np
import matplotlib.pyplot as plt
import math


v0 = 20 # Initial velocity (m/s)

angle = 45 # Launch angle (degrees)

g = 9.81 # Gravity (m/s²) m = mass

'''

Convert degrees to radians


'''

theta = math.radians(angle)


# Velocity Components

vx = v0 * math.cos(theta) # horizontal velocity

vy = v0 * math.sin(theta) # Vertical velocity


print("Horizontal velocity:", round(vx, 2), "m/s")
print("Initial vertical velocity:", round(vy, 2), "m/s")


# Flight time calculation


flight_time = (2 * vy) / g


max_height = (vy ** 2 ) / ( 2 * g)


# Horizontal range calculate


horizontal_range = vx * flight_time



print("Flight time:", round(flight_time, 2), "seconds")
print("Maximum height:", round(max_height, 2), "meters")
print("Horizontal range:", round(horizontal_range, 2), "meters")


#  projectile motion Simulation

# Generate time values
t = np.linspace(0, flight_time, 100)

# Horizontal position
x = vx * t

# Vertical position
y = vy * t - 0.5 * g * t**2

# -----------------------------
# 7. Plot trajectory
# -----------------------------

plt.figure(figsize=(10, 6))

plt.plot(x, y, label="Projectile trajectory")

plt.scatter(0, 0, label="Launch point")
plt.scatter(horizontal_range, 0, label="Landing point")

plt.axhline(0, color="black", linewidth=0.8)

plt.title("Projectile Motion Simulation")
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical height (m)")

plt.grid(True)
plt.legend()

plt.show()

