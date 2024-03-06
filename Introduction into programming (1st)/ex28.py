# Exercise 28. Body mass index

height = int(input('Input your height (centimeter) : '))
weight = int(input('Input your weight (kilogram) : '))

BMI = (weight / (height**2)) * 10000

print(f'Your body mass index (BMI) is - {BMI:.1f} kg/m**2')
