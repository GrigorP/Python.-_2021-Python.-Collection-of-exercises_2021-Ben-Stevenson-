# Exercise 41. Classification of triangles

first_side = int(input('Input here first side of your triangle: '))
second_side = int(input('Input here second side of your triangle: '))
third_side = int(input('Input here third side of your triangle: '))

if first_side == second_side == third_side:
    print('Your triangle Equilateral. ')
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print('Your triangle Isosceles. ')
else:
    print('Your triangle Scalence. ')



