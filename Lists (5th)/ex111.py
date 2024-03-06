# Exercise 111. Reverse order

num = int(input("Input number(0 for close): "))
numbers = []

while num:
    numbers.append(num)
    num = int(input("Input number(0 for close): "))

print(sorted(numbers , reverse=True))