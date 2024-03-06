# Exercise 177. Roman numerals

def numRoman(romnum: str , dct: dict):
    if romnum == "":
        return 0
    if len(romnum) >= 2:
        if romnum[0].capitalize() + romnum[1].capitalize() in dct:
            return dct[romnum[0].capitalize() + romnum[1].capitalize()] + numRoman(romnum[2:] , dct)
    if romnum[0].capitalize() in dct:
        return dct[romnum[0].capitalize()] + numRoman(romnum[1:] , dct)

dct = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

romnum = input("Input roman num: ")
print(numRoman(romnum , dct))