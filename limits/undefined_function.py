import sympy

from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

# Putting the equation

eq = x**2 -4

# solving the equation

print("x = ", solve(eq,x))
