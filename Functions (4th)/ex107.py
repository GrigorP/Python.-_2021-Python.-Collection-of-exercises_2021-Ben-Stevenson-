# Exercise 107. Maximum reduction of fractions

def max_red_of_fract(n , m):
    if n > m:
        d = m
    else:
        d = n

    while n % d != 0 or m % d != 0:
        d -= 1

    n //= d
    m //= d
    return n , m

n = int(input("Input number: "))
m = int(input("Input number: "))

print(max_red_of_fract(n , m))