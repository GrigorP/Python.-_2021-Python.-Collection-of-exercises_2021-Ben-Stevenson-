# Exercise 81. Binary number to decimal

number = input("Input binary number: ")
length = []

for i in range(0 , len(number)):
    length += [i]

to_decimal = 0
for i in number:
    i = int(i)
    to_decimal += i * (2**length[-1])
    length.remove(length[-1])

print(to_decimal)