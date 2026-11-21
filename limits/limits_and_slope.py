import matplotlib.pyplot as plt
import numpy as np

'''
equation : f(x) = x²

'''

x_value = 1
y_value = x_value**2

h = 0.2 # infinidesimal change in x axis

y_value_2 = (x_value + h)**2

zoom = 20
xmin = x_value - zoom
xmax = x_value + zoom
ymin = y_value - zoom
ymax = y_value + zoom


x = np.linspace(xmin,xmax, 100)
y = x**2

slope = (y_value_2 - y_value)/h

print("Slope = ",slope)

plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot(x, y)
plt.plot([x_value],[y_value],'ro')
plt.plot([x_value + h],[y_value_2],'ro')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y=x^2")
plt.show()