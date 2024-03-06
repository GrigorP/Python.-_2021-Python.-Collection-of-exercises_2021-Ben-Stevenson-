# Exercise 78. Collatz conjecture

number = int(input("Input number: "))
list_of_numbers = []

while number > 0:
    list_of_numbers.append(number)
    number = int(input("Input number (neg. num for close): "))

if list_of_numbers:
    if list_of_numbers[-1] != 1:
        if list_of_numbers[-1] % 2 == 0:
            list_of_numbers.append(round(number // 2))
        else:
            list_of_numbers.append((number * 3) + 1)

print(list_of_numbers)
