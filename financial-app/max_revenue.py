x_price_1 = 6 

y_demand_1 = 480
x_price_2 = 7
y_demand_2 = 476

# Solpe and linear equation

slope = (y_demand_2 - y_demand_1)/(x_price_2 - x_price_1)

y_intercept = y_demand_1 - slope*x_price_1

print("y = ", slope, "x + ", y_intercept)