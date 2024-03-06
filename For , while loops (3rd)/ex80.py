# Exercise 80. Prime factors

n = int(input("Input number (graeater than 2): "))
prime_factors = []

factor = 2

while factor <= n:
    if n % factor == 0:
        prime_factors.append(factor)
        n = round(n // factor)
    else:
        factor += 1

print(f"Prime factors - {prime_factors}")