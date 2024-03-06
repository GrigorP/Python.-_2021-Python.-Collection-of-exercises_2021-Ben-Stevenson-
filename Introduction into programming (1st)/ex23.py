# Exercise 23. Area of a regular polygon

import math

s = int(input('Input the length of side: '))
n = int(input('Input the quantity of the sides: '))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of polygon -> {area:.4f}")