# Exercise 104. Hexadecimal and decimals

def hex2int(symbol: str, dct: dict):
    result = ""
    if symbol != "10":
        if len(symbol) == 1:
            if symbol.isdigit():
                symbol = int(symbol)
                result = symbol
            else:
                if symbol.isalpha():
                    if symbol in dct:
                        result = dct[symbol]
                    else:
                        result = "Wrong Symbol."
        else:
            result = "Need only ONE symbol."
    else:
        result = "You need to input 'A' (A = 10)"

    return result

symbol = input("Input here a symbol(in Hexadecimal , 0-9 , A-F): ")

dct = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

print(hex2int(symbol , dct))    
        

def int2hex(number: str , dct):
    result = ""
    reversed_dict = {value: key for key, value in dct.items()}
    if number.isdigit():
        number = int(number)
        if number <= 15:
            if 0 <= number <= 9:
                result = number
            else:
                if number in reversed_dict:
                    result = reversed_dict[number]
        else:
            result = "Number need to be <= 15"

    return result

number = input("Input here number(0-15): ")

print(int2hex(number , dct))

