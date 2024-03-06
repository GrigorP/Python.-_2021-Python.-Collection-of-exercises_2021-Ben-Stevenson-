# Exercise 22. Area of a triangle (second)

import math

a = int(input('Input length of the first side: '))
b = int(input('Input length of the second side: '))
c = int(input('Input length of the third side: '))

s = (a + b + c) // 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f'The are of triangle -> {area}')