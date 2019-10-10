import math
radius, no_cheese = input().split()

R = int(radius)
C = int(no_cheese)

area_pizza = (math.pi)*(R**2)
area_cheese = (math.pi)*((R-C)**2)

percent_covered =(area_cheese/area_pizza)*100

print(percent_covered)
