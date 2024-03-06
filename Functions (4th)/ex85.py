# Exercise 85. Calculate the length of the hypotenuse

from math import sqrt

def hypotenuse(a , b):
    c = sqrt(a**2 + b**2)
    return c

a = int(input("Input first cathetus: "))
b = int(input("Input second cathetus: "))

print(hypotenuse(a , b))