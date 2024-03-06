# Exercise 19. Free fall

from math import sqrt

# V0 = 0

GRAVITY = 9.8

s = float(input("Object release height (meters): "))

v = sqrt(2 * GRAVITY * s)

print(f"The object will reach the ground at a speed of {v:.2f} m/s.")
