# Exercise 32. Sum of digits in a number

number = int(input('Input your number: '))
result = 0
for _ in range(number):
    result += number % 10
    number //= 10

print(result)