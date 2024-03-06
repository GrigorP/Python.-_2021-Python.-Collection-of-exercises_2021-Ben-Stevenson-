# Exercise 174. Greatest common divisor

def greatestComDiv(a , b):
    if b == 0:
        return a
    return greatestComDiv(b , a % b)

a = int(input("Input number: "))
while a <= 0:
    print("Number must be positive: ")
    a = int(input("Input number: "))

b = int(input("Input number: "))
while b <= 0:
    print("Number must be positive: ")
    b = int(input("Input number: "))

print(greatestComDiv(a , b))