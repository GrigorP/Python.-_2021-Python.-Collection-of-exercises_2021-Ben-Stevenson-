# Exercise 101. Random license plate

from random import choice

def rand_plate(len_plate , letters , numbers):
    result = ""
    if len_plate == 6:
        while len(result) != 3:
            result += choice(letters)
        while len(result) != 6:
            result += choice(numbers)
    elif len_plate == 7:
        while len(result) != 4:
            result += choice(letters)
        while len(result) != 7:
            result += choice(numbers)
    return result

len_plate = choice(range(6 , 8))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

print(rand_plate(len_plate , letters , numbers))