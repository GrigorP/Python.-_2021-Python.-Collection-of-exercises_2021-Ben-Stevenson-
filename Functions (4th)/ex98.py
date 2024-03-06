# Exercise 98. Prime number?

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer: "))
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")