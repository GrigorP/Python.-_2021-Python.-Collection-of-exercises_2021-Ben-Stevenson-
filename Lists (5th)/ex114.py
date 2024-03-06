# Exercise 114. Negative, positive and zeros

num = input("Input here number(blank for close): ")
positive_numbers = []
negative_numbers = []
zeros = []

while num:
    num = int(num)
    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)
    else:
        zeros.append(num)
    num = input("Input here number(blank for close): ")

all_numbers = negative_numbers + zeros + positive_numbers
print(all_numbers)