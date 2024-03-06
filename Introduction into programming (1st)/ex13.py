# Exercise 13. Exchange

TOONIE = 200
LOONIE = 100
QUARTER = 25
DIME = 10
NICKEL = 5

cents = float(input("Enter the amount in cents: "))


print(f"  {cents // TOONIE} two dollar coins")
cents = cents % TOONIE

print(f"  {cents // LOONIE} one dollar coins")
cents = cents % LOONIE

print(f"  {cents // QUARTER} 25-cent coins")
cents = cents % QUARTER

print(f"  {cents // DIME} 10-cent coins")
cents = cents % DIME

print(f"  {cents // NICKEL} 5-cent coins")
cents = cents % NICKEL

print(f"  {cents} центов")
