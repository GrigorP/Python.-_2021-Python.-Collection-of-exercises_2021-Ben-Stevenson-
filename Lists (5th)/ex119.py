# Exercise 119. Below and above average

number = input("Input number(blank for close): ")
numbers = []

while number:
    if number.isdigit():
        numbers.append(int(number))
    else:
        print("Inpute NUMBER!")
        break
    number = input("Input number(blank for close): ")

average_of_nums = sum(numbers) / len(numbers) 
below_average = [i for i in numbers if i < average_of_nums]
equals_average = [i for i in numbers if i == average_of_nums]
above_average = [i for i in numbers if i > average_of_nums]

print(average_of_nums)
print(below_average)
print(equals_average)
print(above_average)