# Exercise 103. Random strong password

from random import choice

def random_password():
    password = ""
    num = choice(range(7 , 11))
    for _ in range(num):
        password += chr(choice(range(33 , 127)))
    return password

count = 1

def checking(password, letters: str, numbers: str , count):
    result = False
    while not result:
        if len(password) >= 8:
            has_number = any(char.isdigit() for char in password)
            has_upper = any(char.isupper() for char in password)
            has_lower = any(char.islower() for char in password)

            if has_number and has_upper and has_lower:
                result = True
            else:
                count += 1
        password = random_password()
            
    return result , count

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = random_password()

print(checking(password , letters , numbers , count))
