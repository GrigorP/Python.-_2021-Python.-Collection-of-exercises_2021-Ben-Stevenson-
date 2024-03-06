# Exercise 51. Roots of a quadratic function

from math import sqrt

a = int(input('Input first number: '))
b = int(input('Input second number: '))
c = int(input('Input third number: '))


if a != 0:
    D = (b**2) - (4 * a * c)
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(f'x1 - {x1}\nx2 - {x2}')
    elif D == 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        print(f'x1 - {x1}')
    else:
        print('There are no real roots.')
else:
    print('a - needs to be nonzero.')

