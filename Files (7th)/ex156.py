# Exercise 156. Sum of numbers

file_name = input("Input file name: ")
file = open(file_name, "r")

total = 0
lines = file.read().strip()

for line in lines:
    if line.isdigit():
        total += int(line)

print(total)
file.close()
