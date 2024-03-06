# Exercise 65. Temperature relationship table

celius = [i for i in range(0 , 101)]
fahrenheit = [round((i * 9 / 5) + 32 , 1) for i in celius]

print(f"Celsius - {celius}.")
print(f"Fahrenheit - {fahrenheit}.")