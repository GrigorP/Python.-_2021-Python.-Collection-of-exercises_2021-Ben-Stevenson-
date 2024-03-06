# Exercise 79. Greatest common divisor

n = int(input("Input number: "))
m = int(input("Input number: "))

if n > m:
    d = m
else:
    d = n

while n % d != 0 or m % d != 0:
    d -= 1

print(d)