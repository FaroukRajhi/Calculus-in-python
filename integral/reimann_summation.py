'''

f(x) = x²
Range : from x = 0 to 7

'''

dx = 0.0001 # infinitesimal change

start = 0
end = 7

rectangles = int((end -start)/dx)

sum = 0

for a in range(rectangles):
    x = start + dx*a
    y = x**2
    area = y*dx
    sum = sum + area

print(sum)