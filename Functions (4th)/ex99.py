# Exercise 99. Next prime number

from ex98 import is_prime

def nextPrime(n):
    next_number = n + 1

    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer: "))
        result = nextPrime(user_input)
        print(f"The first prime number greater than {user_input} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")