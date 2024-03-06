# Exercise 141. English cursive

def engCurs(one: dict , number: str):
    result = ""
    if 0 <= int(number) < 1000:
        if len(number) == 1:
            if int(number) in dct:
                result = dct[int(number)]
            else:
                result = "Wrong number."
        elif len(number) == 2:
            if int(number) in dct:
                result = dct[int(number)]
            else:
                first = int(number[0]) * 10
                second = int(number[1])
                result = dct[first] + " " +  dct[second]
        else:
            result = dct[int(number[0])] + " " +  "hundred "
            second = int(number[1]) * 10
            third = int(number[2])
            result += dct[second] + " " + dct[third]
    else:
        result = "Number must be > 0 and < 1000"
    return result

dct = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

number = input("Input number: ")

print(engCurs(dct , number))

