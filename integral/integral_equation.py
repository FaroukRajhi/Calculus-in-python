import sympy
from sympy import symbols

x,y,c = symbols('x y c')

eq = 1/(x*sympy.log(x))

integral = sympy.integrate(eq)


print(integral)