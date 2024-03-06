# Exercise 18. Volume of a cylinder

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius**2 * height

rounded_volume = round(volume, 1)

print(f"The volume of the cylinder is {rounded_volume} cubic units.")