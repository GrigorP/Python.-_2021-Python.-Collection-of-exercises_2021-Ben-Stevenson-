# Exercise 100. Random password

from random import choice

def random_password():
    password = ""
    num = choice(range(7 , 11))
    for _ in range(num):
        password += chr(choice(range(33 , 127)))
    return password


if __name__ == "__main__":
    print(random_password())