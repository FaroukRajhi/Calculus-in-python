import sympy
from sympy import symbols

x,y = symbols('x y')


# The equation

expression = sympy.exp(x)*(2*x**2+3)
derivative = sympy.diff(expression,x)


print("derivative:")
derivative
