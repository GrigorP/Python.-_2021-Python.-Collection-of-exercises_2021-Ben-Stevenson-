# Exercise 74. Square root

x = float(input("Enter a number to find its square root: "))

guess = x / 2.0

while abs(guess * guess - x) > 1e-12:
    guess = 0.5 * (guess + x / guess)

print(f"The square root of {x} is approximately {guess:.1f}")
