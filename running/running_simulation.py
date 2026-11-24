import math
import numpy as np
import matplotlib.pyplot as plt


m = 80.0        # mass, kg
c = 0.25        # drag coefficient, kg/m
g = 9.81        # gravitational acceleration, m/s^2
t_end = 20.0    # final time, s

vt = math.sqrt(m * g / c)
print(f"Terminal velocity: {vt:.4f} m/s")