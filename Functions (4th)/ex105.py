# Exercise 105. Arbitrary number systems

def bin2dec(number: str):
    dec_num = int(number , 2)

    return dec_num

number = input("Input binary string(bin-dec): ")

print(bin2dec(number))

def bin2oct(num: str):
    bin_num = int(num , 2)
    oct_num = oct(bin_num)

    return oct_num[2:]

num = input("Input binary string(bin-oct): ")

print(bin2oct(num))

def bin2hex(binary_str):
    decimal_number = int(binary_str, 2)
    hex_number = hex(decimal_number)

    return hex_number[2:]

binary_str = input("Input binary string(bin-hex): ")

print(bin2hex(binary_str))

def dec2bin(dec_number):
    bin_num = bin(dec_number)

    return bin_num[2:]

dec_number = int(input("Input decimal number(dec-bin): "))

print(dec2bin(dec_number))

def dec2oct(dec_num):
    oct_num = oct(dec_num)

    return oct_num[2:]

dec_num = int(input("Input decimal number(dec-oct): "))

print(dec2oct(dec_num))

def dec2hex(decimal_number):
    hex_num = hex(decimal_number)

    return hex_num[2:]

decimal_number = int(input("Input decimal number(dec-hex): "))

print(dec2hex(decimal_number))

def oct2bin(oct_number: str):
    dec_num = int(oct_number , 8)
    bin_num = bin(dec_num)

    return bin_num[2:]

oct_number = input("Input octal number(oct-bin): ")

print(oct2bin(oct_number))

def oct2dec(oct_num: str):
    dec_num = int(oct_num , 8)

    return dec_num

oct_num = input("Input octal number(oct-dec): ")

print(oct2dec(oct_num))


def oct2hex(octal_num: str):
    dec_num = int(octal_num , 8)
    hex_num = hex(dec_num)

    return hex_num[2:]

octal_num = input("Input octal number(oct-hex): ")

print(oct2hex(octal_num))

def hex2bin(hex_number: str):
    dec_num = int(hex_number, 16)
    bin_num = bin(dec_num)

    return bin_num[2:]

hex_number = input("Input hexadecimal number(hex-bin): ")

print(hex2bin(hex_number))

def hex2oct(hexadecimal_num: str):
    dec_num = int(hexadecimal_num, 16)
    oct_num = oct(dec_num)

    return oct_num[2:]

hexadecimal_num = input("Input hexadecimal number(hex-oct): ")

print(hex2oct(hexadecimal_num))

def hex2dec(hex_num: str):
    dec_num = int(hex_num, 16)

    return dec_num

hex_num = input("Input hexadecimal number(hex-dec): ")

print(hex2dec(hex_num))
