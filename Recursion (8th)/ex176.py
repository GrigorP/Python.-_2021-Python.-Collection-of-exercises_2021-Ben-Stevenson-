# Exercise 176. NATO phonetic alphabet

def alphNATO(word: str, dct: dict):
    if word == "":
        return ""
    if word[0].capitalize() in dct:
        return dct[word[0].capitalize()] + alphNATO(word[1:] , dct)
    
dct = {
    "A": "Alpha ",
    "B": "Bravo ",
    "C": "Charlie ",
    "D": "Delta ",
    "E": "Echo ",
    "F": "Foxtrot ",
    "G": "Golf ",
    "H": "Hotel ",
    "I": "India ",
    "J": "Juliet ",
    "K": "Kilo ",
    "L": "Lima ",
    "M": "Mike ",
    "N": "November ",
    "O": "Oscar ",
    "P": "Papa ",
    "Q": "Quebec ",
    "R": "Romeo ",
    "T": "Tango ",
    "U": "Uniform ",
    "V": "Victor ",
    "W": "Whiskey ",
    "X": "Xray ",
    "Y": "Yankee ",
    "Z": "Zulu ",
}

word = input("Input word: ")
print(alphNATO(word , dct))