# Exercise 67. Find the perimeter of a polygon

from math import sqrt

perimeter = 0

first_x = float(input("Введите первую координату X: "))
first_y = float(input("Введите первую координату Y: "))

prev_x = first_x
prev_y = first_y

line = input("Enter the following X coordinate (Enter to end entry): ")

while line != "":
    x = float(line)
    y = float(input("Enter the next Y coordinate: "))

    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

    prev_x = x
    prev_y = y

    line = input("Enter the following X coordinate (Enter to end entry): ")

dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)

perimeter = perimeter + dist

print(f"The perimeter of the polygon is {perimeter}")