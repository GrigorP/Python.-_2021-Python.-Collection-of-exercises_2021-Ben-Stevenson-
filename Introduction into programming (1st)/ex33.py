# Exercise 33. Sorting three numbers

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))
num3 = int(input('Input third number: '))

lst = [num1 , num2 , num3]
lst.sort(reverse=True)

print(lst)