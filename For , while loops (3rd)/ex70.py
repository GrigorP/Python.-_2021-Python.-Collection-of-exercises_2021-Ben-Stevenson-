# Exercise 70: Parity Bits

line = input("Enter 8 bits of information: ")

while line != "":
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        print("It's not 8 bit... Try again.")
    else:
        ones = line.count("1")
        if ones % 2 == 0:
             print("The parity bit must be 0.")
        else:
             print("The parity bit must be 1.")
    line = input("Enter 8 bits of information: ")