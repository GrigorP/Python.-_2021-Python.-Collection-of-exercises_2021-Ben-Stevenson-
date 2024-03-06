# Exercise 11. Fuel consumption

mpg = float(input("Enter fuel consumption in miles per gallon (MPG): "))

l_per_100km = 235.215 / mpg

print(f"{mpg} MPG is equal to {l_per_100km:.2f} L/100 km in Canadian units.")
